# AI Code Cartographer Skill

The **AI Code Cartographer** is a specialized skill for exhaustively parsing a codebase to create a high-level call stack and structural graph (JSON) for Neo4j. It relies entirely on the AI's ability to analyze and relationship-map code without external tools.

## Core Capabilities
1.  **Exhaustive Scanning**: Traverses the entire directory and maintains a state of processed/pending files and FOLDERS.
2.  **Structural Extraction**: Identifies `Module`, `File`, `Class`, `Constructor`, `Method`, `Function`, `Procedure`, `Enum`, `Interface`, `Override`, and `Inheritance`.
3.  **Relationship Mapping**: Detects `CALLS`, `DEFINES`, `INHERITS`, `IMPLEMENTS`, and `OVERRIDES` links.
4.  **Symbol Resolution**: Cross-references symbols across files to build a complete application "map".
5.  **Project Hierarchy Mapping**: Maps the physical directory tree to a logical Neo4j graph using `Folder` and `File` nodes.
6. **External Reference Capture**: Identifies and extracts calls to external libraries (e.g., `org.springframework.*`) as external method nodes to provide full context of the code's dependencies.
7. **Advanced Edge Case Resolution**: Explicitly handles method overloading, anonymous classes, lambdas, generics, and multiple class definitions per file to ensure zero data loss in the structural map.

## Operational Protocol

### 1. Initial Setup
Run the `init_project.py` script to scan the workspace and generate `results/project_tree.json` and `results/status.json`.
- `status.json` tracks the exhaustive completion of every file.
- `project_tree.json` tracks the folder hierarchy.

### 2. Recursive Parsing Loop
The AI MUST follow this cycle:
1.  **Identify**: Find the next batch of `NOT_STARTED` files in `status.json`. **Recommended batch size: 5-10 files per iteration** to ensure exhaustive analysis and handle context limits.
2.  **Analyze (Standard vs. Large)**:
    *   **Standard (<2k lines)**: Extract all structural elements, parameters, types, and calls in a single pass.
    *   **Large (>=2k lines)**: Switch to **Contextual Chunking Protocol**. Parse in 1,500-line segments with 200-line overlaps until the end-of-file. Maintain cross-chunk state for class and method scopes.
3.  **Register**: Update `symbol_table.json` with new definitions and external references.
4.  **Validate**: Verify that 100% of the file's visible symbols were caught, including edge cases like anonymous types and overloaded methods. Edge Case Audit: Ensure no ID collisions between overloads or classes in same file.
5.  **Integrate**: Append extracted nodes and edges to `graph.json`.
6.  **Update**: Mark files as `COMPLETED` in `status.json`.
7.  **Loop**: If `NOT_STARTED` files remain, output the "CONTINUE" command.

## JSON Schema (Neo4j)

### Nodes
- Labels: `Folder`, `File`, `Class`, `Method`, `Function`, `Enum`, `Interface`, `Lambda`, `AnonymousClass`.
- Properties: `id` (MANDATORY UNIQUE), `name`, `fqn`, `path`, `line`, `params` (full types), `returns`, `access`, `static`, `abstract`.
- Unique ID Policy:
    *   **Class/Interface**: `Package.Name`
    *   **Method/Function**: `FQN.Parent.MethodName(ParamTypes)` (to handle overloading)
    *   **Nested/Anonymous**: `FQN.Parent.SymbolName$id`

### Edges
- Types: `CONTAINS`, `CALLS`, `INHERITS`, `IMPLEMENTS`, `OVERRIDES`.

## Self-Prompting Instruction
When the AI finishes a batch, it MUST output:
"Parser Progress: [X/Y] files completed. Project tree synchronized. Continuing to next batch..."
followed by a tool call to read the next set of files.
