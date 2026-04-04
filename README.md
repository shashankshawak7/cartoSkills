# 🗺️ cartoSkills: AI Code Cartographer

**cartoSkills** is a high-fidelity, AI-driven engine designed to exhaustively parse complex codebases and generate structural, relationship-mapped graphs compatible with **Neo4j**.

---

## 🚀 Overview

The **AI Code Cartographer** moves beyond simple static analysis by leveraging advanced LLM reasoning to identify not just definitions, but deep polymorphic relationships, cross-module calls, and structural hierarchies.

### ✨ Key Features
- **Exhaustive Scanning**: Traverses every folder and file in a workspace, maintaining a persistent state via `status.json`.
- **Advanced Polymorphism**: Precise resolution of method overrides and overloads using a unique Fully Qualified Name (FQN) ID system.
- **Relationship Mapping**: Detects `CALLS`, `DEFINES`, `INHERITS`, `IMPLEMENTS`, and `OVERRIDES` links with line-level accuracy.
- **Neo4j Ready**: Generates a structured `graph.json` ready for ingestion into graph databases for visualization and analysis.
- **Process Memory**: A recursive loop architecture that allows the AI to handle massive projects in logical, verifiable batches.

---

## 🏗️ Architecture

The system operates on an **Orchestrator-Worker** pattern to ensure precision and handle large context windows effectively.

### 1. 🧠 [Manager Prompt](file:///c:/Users/shash/OneDrive_x/Desktop/SKILLaI/prompts/manager.md)
The Manager acts as the orchestrator, tracking overall progress, mapping the physical directory tree to `:Folder` nodes, and validating the work of the parser.

### 2. 🛠️ [Worker Prompt](file:///c:/Users/shash/OneDrive_x/Desktop/SKILLaI/prompts/parser_worker.md)
The Worker is the specialized surgical tool. It reads individual source files and extracts every class, method, parameter, and call reference according to strict metadata rules.

### 3. 📂 [Results Layer](file:///c:/Users/shash/OneDrive_x/Desktop/SKILLaI/results/)
- `graph.json`: The final Neo4j-compatible delivery.
- `symbol_table.json`: Global lookup for cross-file symbol resolution.
- `status.json`: Tracking system for 100% completion auditing.
- `project_tree.json`: Hierarchical map of the physical workspace.

---

## 🕹️ Usage: The AI Start Prompt

To begin the exhaustive mapping process, copy and paste the following prompt into the chat window. This activates the recursive logic defined in the project instructions:

> [!TIP]
> **COPY AND PASTE THIS PROMPT:**
>
> *"Start the AI Code Cartographer recursive parsing loop. Follow the protocol in `SKILL.md` and `manager.md` to parse all `NOT_STARTED` files in batches of 5-10. Update the `graph.json`, `symbol_table.json`, and `status.json` after each batch, then automatically output the 'CONTINUE' command until 100% completion is reached."*

---

## 🛡️ Edge Case Resolution

| Case | Handling Strategy |
| :--- | :--- |
| **Overloading** | Unique IDs using signatures: `Class.Method(ParamTypes)`. |
| **Lambdas** | Captured as nested `FQN.Parent$lambda_1` nodes. |
| **Generics** | Preservation of type parameters (e.g., `List<Owner>`). |
| **External Libs** | Calls to libraries (e.g., SpringBoot) are mapped as external nodes. |

---

> [!IMPORTANT]
| The AI Cartographer is designed for **zero-data-loss** structural mapping. If a file is modified during parsing, re-run `init_project.py` to synchronize the state.
