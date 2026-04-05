# SKILLaI: Universal Code Cartography & Surgical Auditing Engine
## Enterprise Documentation Blueprint

This document details the exact architecture, the rigorous 100% Trust Pipeline, and deployment instructions for using SKILLaI in enterprise-grade software analysis and documentation IRMapper.

---

## 1. System Overview & Architecture

SKILLaI operates at the nexus of Large Language Model structural parsing and deterministic Python-based extraction scripts. The architecture is split into two primary orchestration paths tightly coupled through a system of JSON tracking state files.

### A. AI Code Cartographer (Strategic Mode)
Automated structural indexing of legacy and modern architecture into a format ingestible by Neo4j and analytical tools.
- **Goal**: Read every tracked file and extract its core taxonomy (`:Container`, `:Structure`, `:Unit`, etc.) and mapped relationships (`[:CALLS]`, `[:EXTENDS]`, `[:USES]`).
- **Core Entities**: 
   - `prompts/parser_worker.md`: The extractor.
   - `skills/ai_cartographer/validator.md`: The Logical Intent Review Gate.
   - `results/graph.json`: The raw output Neo4j compliant graph structure.
   - `results/symbol_table.json`: High-speed symbol lookup map.

### B. Universal Retro-Documentor (Tactical Mode)
Surgical, non-summarized generation of architectural autopsies.
- **Goal**: Generate precise, code-backed `README.md` and module-specific `md` docs for every file using the **Absolute 1-23 Standard**.
- **Core Entities**:
   - `prompts/documentor_worker.md`: The strict documentation auditor.
   - `skills/retro_documentor/template.md`: The required 1-23 template.
   - `documentation/`: The mapped 1:1 shadow directory storing all output archives.

---

## 2. The "100% Trust" Pipeline
LLMs hallucinate. Therefore, SKILLaI relies on a Zero-Trust Pipeline bridging LLM capabilities with rigorous programmatic verification.

### Check 1: The N/A Protocol (Documentor)
We explicitly prevent the AI from generating random "ROI/Metrics" or Business impacts.
- **Guardrail**: If evidence is missing, the AI is constrained and strictly forced to append `> [!NOTE] \n > N/A — No evidence found in this source artifact.`

### Check 2: Deduplication and URI Protocol
Nodes are strictly addressed via a unified Universal Code Cartography String (UCCS).
- **Format**: `lang://path#FQN(Signature)`
- **Guardrail**: If the URI schema does not match precisely, resolving dangling edges triggers an orchestrated failure forcing the LLM to reconstruct the structure.

### Check 3: Schema Adherence & Validate Graph
LLM output passes through `validator.md` for *semantic logic checks* but relies on Python and the `jsonschema` module for architectural integrity.
- **Process**: `scripts/validate_graph.py`
- **Enforcement**: Checks for dangling edges, schema drift in relations (e.g. invalid enums like `[:LIKES]`), and asserts mathematically sound JSON. A failed pass prevents the batch from merging and forces a prompt retry.

---

## 3. Global Configuration & Tuning

### Ignore Maps (`config/ignore_map.json`)
The central noise-canceling mechanism ensuring the LLM is only fed relevant context.
- Skips build folders (`target/`, `node_modules/`).
- Masks dynamic environment config unless explicitly requested to prevent data leakage in mappings.

### AI Persona Boundaries
Risk thresholds are standard to provide analytical determinism:
- `HIGH` Risk: >80 lines per method, >15 cyclomatic complexity.
- `CRITICAL` Risk: >150 lines per method, >30 cyclomatic complexity.

---

## 4. Deployment & Orchestration Guidelines

### CI/CD Deployment Strategy
Integrate SKILLaI into DevOps build pipelines:

1. **Initialization:**
   ```bash
   python scripts/init_project.py .
   python scripts/init_documentation.py .
   ```
   *Creates `status.json` and `documentation_status.json` trackers.*

2. **Cartography Batch Extraction:**
   Run an LLM agent iterating through `status.json`.
   After each extracted batch, assert graph validity:
   ```bash
   python scripts/validate_graph.py
   ```
   *If exit code `0`, append to master Graph JSON.*

3. **Documentation Generation:**
   Iterate `documentation_status.json`, triggering the Documentor Worker. Monitor outputs into the `/documentation` path structure.
   
4. **Final Sync:**
   Graph files pushed to graph databases locally, and `/documentation` checked into Source Version Control.
