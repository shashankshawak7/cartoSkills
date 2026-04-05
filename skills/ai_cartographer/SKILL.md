# AI Code Cartographer Skill: Enterprise Audit Edition

The **AI Code Cartographer** is the definitive, client-facing engine for mapping the architectural and execution hierarchy of any enterprise codebase. It employs the **Universal Meta-Model (UCCS)** to unify diverse paradigms into a high-fidelity, strictly validated Neo4j graph suitable for executive modernization planning and compliance audits.

---

## 🛡️ Enterprise Core Capabilities & Mandatory Guardrails
1.  **Absolute Proprietary Taxonomy**: Enforce strict reduction of all languages into exactly six primitives (`:Container`, `:Structure`, `:Unit`, `:Symbol`, `:Annotation`, `:External`). **No custom or hallucinated labels are permitted.**
2.  **Zero Hallucination Protocol**:
    - Do not invent dependencies. If a dynamic or reflective `CALL` obscures the target, map it strictly as `[:UNKNOWN_RELATION]` rather than guessing the target class.
    - If a file cannot be fully parsed due to complexity or obfuscation, immediately flag the parent `:Container` node with `"audit_status": "MANUAL_REVIEW_REQUIRED"`.
3.  **Enterprise URI ID Protocol (`lang://path#Symbol`)**: Every single Node ID must be mathematically deduplicable. Inconsistencies will corrupt the executive dataset.
4.  **Zero-Dangling-Edge Mandate**: Every unique reference target MUST be instantiated as an actual node. If external, use `:External`. 
5.  **Unobtrusive Code Scanning**: Treat the source code as absolute Ground-Truth. The engine must extract reality, not an idealized version of the code.

---

## 🛠️ Universal Taxonomy Matrix (UCCS)

| Enterprise Category | Applicable Code Paradigms (Strict Enforcement) |
| :--- | :--- |
| **:Container** | Folder, File, Namespace, Package, Module, COBOL Program, JCL Job, Delphi Unit. |
| **:Structure** | Class, Struct, Interface, Trait, Enum, COBOL Section, P4GL Temp-Table, C++ Template. |
| **:Unit** | Method, Function, Lambda, COBOL Paragraph, JCL Step, Shell Command, PL/SQL Procedure. |
| **:Symbol** | Field, Property, Variable, Constant, COBOL Data Item, CSS Selector. |
| **:Annotation** | Decorator, Attribute, Macro, Metadata, Pragma, JS JSDoc. |
| **:External** | SaaS dependencies, imported third-party SDKs, CDN assets, unsourced DLLs. |

---

## 🕹️ Operational Protocol (Enterprise Audit Workflow)

### 1. Initialization
Run `init_project.py` to establish the environment and strictly validate `status.json`. The baseline graph must explicitly feature URI-validated `:Container` nodes for the directory structure.

### 2. Recursive Parsing & Validation Loop
1.  **Extract**: Utilize the **Enterprise Parser Worker** to extract UCCS meta-model primitives.
2.  **Validate**: Pass all output into the **Enterprise Quality Validator Skill** to enforce URI constraints, schema validity, and risk-tagging.
3.  **Merge**: Only successfully validated JSON payloads are merged.
4.  **Enforce**: If validation fails, force parser self-correction. Loop until `status.json` resolves to 100%.

---

## 🧠 Architectural Risk Tagging
During abstraction, if the Cartographer detects "High Cyclomatic Complexity" (massive functions) or "God Classes," it must append the property `"architectural_risk": "HIGH"` (Standard Enum: LOW, MEDIUM, HIGH, CRITICAL) directly to the Node's JSON metadata to flag it for the modernization pipeline.
