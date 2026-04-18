# 🏗️ Universal Code Cartography & Application Modernization Skills

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
21. 🚀 **IRMapper & Migration Roadmap**
22. 📊 **Visual Engineering (Mermaid Diagrams)**
23. 🔏 **System Integrity Checksum (Final Audit)**

---

## 📂 Initialization Orchestration
Before initiating an audit, run the following commands to synchronize the trackers:
```powershell

# Initialize all at once
python init_pipeline.py <PROJECT_PATH>

# Step 1: Initialize the Cartography Tracker
python .\scripts\init_project.py <PROJECT_PATH>

# Step 2: Initialize the Documentation Seeder
python .\scripts\init_documentation.py <PROJECT_PATH>

# Step 2: Initialize the IRMapper Seeder
python .\scripts\init_irmapper.py <PROJECT_PATH>

# Step 2: Initialize the Modernization Seeder
python .\scripts\init_modernization.py <PROJECT_PATH>
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

## trigger retro documentor
```sh
Act as the **Universal Retro Documentor Manager**. Your mission is to autonomously generate a high-fidelity **Enterprise Surgical Archive** for the entire project. 
1. **Zero-Touch Execution**: Do not stop to ask for feedback, approval, or implementation plans. 
2. **Recursive Auditing**: Iterate through "results/documentation_status.json". For every file where 'documented' is false:
   - Perform a **Surgical Dissection** using the **Absolute 1-23 Standard** from "template.md".
   - Generate a corresponding ".md" archive in the "documentation/" shadow root (maintaining 1:1 directory symmetry).
   - Generate a "README.md" for every directory and the project root that synthesizes the 23 sections for that scope.
3. **Protocol Adherence**: Strictly follow the **Principal Systems Auditor** persona from "documentor_worker.md" and the **Surgical Dissection Standard** from "SKILL.md".
4. **Persistence**: Continue this loop until every entry in "results/documentation_status.json" is marked 'documented: true'. 
Start now by documenting the Project Root and the first batch of pending files.
```

## Trigger Cartographer
```sh
Act as the **Universal Code Cartographer Manager**. Your mission is to autonomously map the architectural and execution hierarchy of the entire project into a high-fidelity Neo4j-ready meta-model.
1. **Zero-Touch Execution**: Do not stop to ask for feedback, approval, or implementation plans. 
2. **Recursive Mapping**: Iterate through "results/status.json". For every file where 'status' is 'NOT_STARTED':
   - Perform a **Structural Extraction** using the **Universal Meta-Model (UCCS)** from "SKILL.md".
   - Enforce the **Enterprise URI ID Protocol** (`lang://path#Symbol`) for every node.
   - Generate a valid JSON payload for every successfully parsed `:Container`, `:Structure`, and `:Unit`.
3. **Protocol Adherence**: Strictly follow the **Zero-Hallucination Protocol** and the **Architectural Risk Tagging** mandate from "SKILL.md". Use the **Enterprise Parser Worker** for extraction.
4. **Persistence**: Continue this loop until every entry in "results/status.json" has "status": "COMPLETED" and the final graph is merged into "results/graph.json".
Start now by mapping the core entry points and the first batch of pending files.
```
## Trigger IR Mapper
```sh
Act as the Universal IRMapper Manager. Your mission is to autonomously generate a high-fidelity IRMapper Gold Data Archive (V1.1) for the entire project.

Zero-Touch Execution: Do not stop to ask for feedback, approval, or implementation plans.
Recursive Logic Auditing: Iterate through results/irmapper_status.json. For every file where logic_mapped is false:
Perform an Instruction-Level Forensic Audit using the Universal IRMapper Template (V1.1) from skills/irmapper_skill/template.yaml.
Generate a corresponding .yaml archive in the irmapper/ shadow root (maintaining 1:1 directory symmetry).
Resolve all cross-language gaps (Closures, MRO, Pointers, Paragraphs, Job Steps, etc.) as mandated by the V1.1 standard.
Protocol Adherence: Strictly follow the Principal IRMapper Architect persona from prompts/irmapper_worker.md and the Gold Standard for Logic Deconstruction from skills/irmapper_skill/SKILL.md.
Persistence: Continue this loop until every entry in results/irmapper_status.json is marked logic_mapped: true.
```
## Trigger Modernizer
```sh 
Act as the Universal Digital Modernizer Manager. Your mission is to autonomously generate high-fidelity, Enterprise-Hardened Source Code (v2.0) and Thorough Test Suites for the entire project.

Zero-Touch Execution: Do not stop to ask for feedback, approval, or implementation plans.
Recursive Modernization: Iterate through results/irmapper_status.json. For every file where mapped is true:
Perform a Software Rebirth using the Universal Transformation Standard (v2.0) from skills/digital_modernizer/SKILL.md.
Apply the Hardened Blueprint (e.g., Spring Boot, NestJS, Next.js, .NET MVC) from skills/digital_modernizer/blueprints/ based on the requested target stack.
Generate functionally equivalent source code, thorough unit tests (JUnit, Vitest, Jest, xUnit), and matching build manifests (pom.xml, package.json, .csproj).
Enforce 1:1 Logic Parity between the IRMapper statements trace and the new modern implementation.
Protocol Adherence: Strictly follow the Senior Digital Transformation Architect persona from prompts/modernizer_worker.md and the Enterprise-Grade Blueprint Schema from skills/digital_modernizer/blueprints/SCHEMA.md.
Persistence: Continue this loop until every target legacy artifact is transformed into a robust, tested, and validated modern source module.
Start now by modernizing the first batch of core business logic files into the [TARGET_STACK].
```
