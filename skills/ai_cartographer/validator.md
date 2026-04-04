# Structural Validator Skill (All-Stack Edition)

The **Structural Validator** is the final quality gate. It verifies that the AI Code Cartographer's output is **Nuance-Free**, **Exhaustive**, and **Paradigm-Consistent**.

## Validation Mission
1.  **Universal Taxonomy Check**: Verify that all nodes use UCCS labels (`:Container`, `:Structure`, `:Unit`, `:Symbol`, `:Annotation`, `:External`).
2.  **URI Policy Verification**: Mandate `lang://path#Symbol` format for 100% of nodes.
3.  **Exhaustiveness Audit**: 
    - Verify that COBOL Paragraphs, JCL Steps, and C Functions are counted accurately.
    - Check for "Phantom Entry Points" (missing synthetic units for global code).
4.  **Edge-Case Integrity**:
    - **Python**: Verify `@decorator` triggers `[:DECORATES]`.
    - **Go**: Verify embedded structs have implicit `[:EXTENDS]` edges.
    - **C++**: Verify template structures are flagged correctly.

## Audit Protocol
- ### Pass 0: JSON Schema Validation
1. Use the formal schemas in `schemas/` to validate the incremental JSON output.
   - `node.schema.json` for every node.
   - `edge.schema.json` for every relationship.
2. **Failure Condition**: Any schema violation (e.g., malformed URI, missing UCCS label, invalid property type).

- ### Pass 1: Lexical Symbol Scanning
- **Pass 1**: Lexical scan against source to ensure no missed logic blocks.
- **Pass 2**: Edge target list comparison against node list. Zero dangling entries allowed.
- **Pass 3**: Hierarchical audit (Container -> Structure -> Unit).

## Corrective Failure
"Structural Failure: Missing UCCS Mapping in File X. URI Collision in Batch Y. Danling Edges detected in Z."
Instruct the manager to re-read with "Absolute Primitive Precision".
