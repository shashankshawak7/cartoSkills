# 🏗️ Universal Code Cartography & Surgical Auditing Engine

> **The Enterprise Standard for Systemic Retro-Documentation and Strategic Code Analysis.**

The **Universal Retro-Documentation Engine** is a high-performance auditing suite designed to extract machine-readable architectural patterns and human-readable surgical archives from complex codebases. It enforces a strict **"Absolute 1-23 Standard"** for every audited artifact, ensuring zero-omission knowledge capture for both legacy and modern systems.

---

## 🛰️ Operational Modes

### 1. **Strategic Mode (AI Cartographer)** 🗺️
**Objective**: Build a high-fidelity topological map of the entire project, identifying cross-stack dependencies and architectural hotspots.
- **Primary Artifacts**: `results/graph.json`, `results/symbol_table.json`

### 2. **Tactical Mode (Surgical Documentor)** 📝
**Objective**: Perform a line-by-line logical autopsy of core source files and UI views to produce exhaustive 23-section archives.
- **Primary Artifacts**: `documentation/` (Mirror root of the source tree)

---

## 🧠 Master Operational Prompts (LLM-Optimized)

### A. To Trigger the AI Cartographer
**Use this prompt for strategic architectural mapping.**
> "Activate the **AI Cartographer**. Perform a systemic sweep of the `results/status.json` file list. Identify all class relationships, service orchestrations, and data-flow call-chains. Update `results/graph.json` and `results/symbol_table.json` with 100% architectural parity. Construct a high-level `README.md` in the `documentation/` root summarizing the project's macro-topology."

### B. To Trigger the Surgical Documentor
**Use this prompt for exhaustive, 1:1 tactical auditing.**
> "Switch to the **Surgical Documentor**. Mirror the project source structure in the `documentation/` folder. For every file in the tracker, generate a **Surgical Archive** following the **Absolute 1-23 Standard**. Enforce a 'Logical Branching Matrix' for every method and include professional Mermaid diagrams for class interactions. No placeholders, no summarization, zero-omission auditing only."

---

## 📏 The Absolute 1-23 Surgical Standard
Every audit archive produced by the engine must contain the following 23 sections to ensure systemic compliance:

1.  📑 **Executive Summary & Business Intent**
2.  🏗️ **System Architecture & Alignment**
3.  🔗 **Integration Context & Interfaces**
4.  📂 **Structural Codebase Taxonomy**
5.  🧠 **Functional Decomposition (Logical Mapping)**
6.  🔄 **Execution Flow (Block-by-Block Trace)**
7.  📞 **Call Graph & Dependency Chain**
8.  🗄️ **Data Architecture & Persistence DNA (State)**
9.  🔧 **Configuration, Constants & Environmentals**
10. 🧪 **Instructional & Utility Logic**
11. 🛡️ **Cross-Cutting Concerns (Logging/Observability)**
12. 🚨 **Fault Tolerance & Operational Resilience**
13. 🔐 **Security, Risk & Compliance Model**
14. ⚡ **Performance & Telemetry Characteristics**
15. 🧪 **Quality Assurance & Validation Logic**
16. 🧯 **Technical Debt & Risk Assessment**
17. 🔄 **Governance & Change Control**
18. 📖 **Reference Manifest & Artifact Links**
19. 🧩 **Procedural Summary (Surgical Deconstruction)**
20. 🧬 **Architectural Justification (Reverse Engineered)**
21. 🚀 **Modernization & Migration Roadmap**
22. 📊 **Visual Engineering (Mermaid Diagrams)**
23. 🔏 **System Integrity Checksum (Final Audit)**

---

## 📂 Initialization Orchestration
Before initiating an audit, run the following commands to synchronize the trackers:
```powershell
# Step 1: Initialize the Cartography Tracker
python .\scripts\init_project.py <PROJECT_PATH>

# Step 2: Initialize the Documentation Seeder
python .\scripts\init_documentation.py <PROJECT_PATH>
```

### ⚙️ Clinical Pruning (`config/ignore_map.json`)
The engine uses a centralized **Ignore Map** to strictly exclude environmental noise (`node_modules`, `.venv`, `target`) while focusing purely on core source code.
- **Location**: `config/ignore_map.json`
- **Supported Paradigms**: Wildcard prefixing (e.g., `.venv*`), language-specific directory skips, and global artifact exclusion (e.g., `.gitignore`).

---

## 📦 Core Architecture
- `scripts/`: Initialization and auditing automation.
- `config/`: The centralized **Clinical Pruning** engine rules.
- `documentation/`: The **Shadow Root** for all generated surgical archives.
- `results/`: JSON-based graph data and symbol tables for systemic analysis.
- `prompts/`: Master worker personas for consistent LLM execution.
