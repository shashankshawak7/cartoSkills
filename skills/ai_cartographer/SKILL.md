# AI Code Cartographer Skill (All-Stack Universal Edition)

The **AI Code Cartographer** is the definitive engine for mapping the architectural and execution hierarchy of any enterprise codebase. It employs the **Universal Meta-Model (UCCS)** to unify diverse paradigms—Procedural, Object-Oriented, Scripting, and Batch Processing—into a high-fidelity Neo4j graph.

## Core Capabilities
1.  **Primitive-First Taxonomy**: Boils all language-specific constructs down to four universal labels: `:Container`, `:Structure`, `:Unit`, and `:Symbol`.
2.  **Detect**: Identify the programming language of the target batch.
3.  **Map**: Trigger the relevant **High-Precision Specialization Module** (e.g., `languages/java.md`, `languages/cobol.md`) to extract symbols according to UCCS standards.
4.  **Cross-Reference**: Apply the URI ID policy (`lang://path#Symbol`) to link internal and cross-language calls.
5.  **Multi-Paradigm Support**: Natively handles the "Infinite Stack"—COBOL, JCL, Progress 4GL, Delphi, .NET, Java, C/C++, Rust, HTML, CSS, TypeScript, SQL, and Shell—with absolute structural precision.
6.  **Cross-Paradigm Resolution**:
    - **Procedural (COBOL/C/4GL)**: Maps Paragraphs/Sections/Procedures as `:Unit` nodes.
    - **Batch (JCL)**: Maps Jobs as `:Container` and Steps as `:Unit`.
    - **Systems (C++/Go)**: Maps Templates, Namespaces, and Embedding as structural relationships.
    - **Modern (JS/.NET)**: Maps Closures, Prototypes, and Async Triggers.
3.  **Absolute ID Uniqueness**: Mandates a URI-based stable ID format (`lang://path/to/file#SymbolPath`) for zero collisions in polyglot projects.
4.  **Zero-Dangling-Edge Mandate**: Every reference target must be instantiated as a node (Internal or External).
5.  **Implicit Entry Point Detection**: Automatically identifies execution blocks outside named functions (Shell, COBOL, Python) and maps them as entry-point `:Units`.

## Universal Taxonomy (UCCS)

| Category | Constructs (Full Matrix) |
| :--- | :--- |
| **:Container** | Folder, File, Namespace, Package, Module, **COBOL Program**, **JCL Job**, **Delphi Unit**. |
| **:Structure** | Class, Struct, Interface, Trait, Enum, **COBOL Section**, **Progress 4GL Temp-Table**, **C++ Template**. |
| **:Unit** | Method, Function, Lambda, **COBOL Paragraph**, **JCL Step**, **Shell Command**, **SQL Procedure**. |
| **:Symbol** | Field, Property, Variable, Constant, **COBOL Data Item**, **JCL DD Statement**, **CSS Selector**. |
| **:Annotation** | Decorator, Attribute, Macro, Metadata, Pragma, **JS JSDoc**. |
| **:External** | Any symbol residing in an external library, DLL, Copybook, or CDN. |

## Operational Protocol

### 1. Initialization
Run `init_project.py` to seed `status.json`.
Initialize the base graph with URI-compliant `:Container` nodes for the directory structure.

### 2. Recursive Parsing Loop
1.  **Analyze**: Use the **All-Stack Playbook** (parser_worker.md) to extract meta-model primitives.
2.  **Validate**: Trigger the **Structural Validator Skill** for Case Audit and ID consistency. 
3.  **Integrate**: Merge JSON if validation PASSED.
4.  **Loop**: Output "CONTINUE" until `status.json` is 100%.

## JSON Schema (Neo4j)

### Node Properties
- `id`: `lang://relative_path#FQN(Signature)`
- `label`: UCCS Label (e.g., `:Unit`)
- `properties`: {name, fqn, line, lang, abstract, entry_point}

### Edge Types
- `[:CONTAINS]`, `[:CALLS]`, `[:EXTENDS]`, `[:IMPLEMENTS]`, `[:USES]`, `[:DECORATES]`, `[:TRIGGERS]`.

## Self-Prompting Instruction
"Parser Progress: [X/Y] files. All-Stack Meta-Model synchronized."
