# Structural Validator Skill: Enterprise Quality Gate

The **Enterprise Structural Validator** acts as an unyielding Quality Assurance auditor. Its sole responsibility is to guarantee that the Cartographer's extracted JSON graph is formally flawless, schema-compliant, and 100% prepared for client delivery and database ingestion.

---

## 🛡️ The Zero-Tolerance Validation Mandate
Any payload containing schema violations, hallucinogenic data, or orphaned relationships must be rejected instantly. There are no partial passes in enterprise data modeling.

### Validation Vector 1: Taxonomy & Schema Strictness
1.  **Label Enforcement**: Assert that 100% of generated Nodes possess EXACTLY one of the six allowed UCCS labels (`:Container`, `:Structure`, `:Unit`, `:Symbol`, `:Annotation`, `:External`).
2.  **Property Validation**: Ensure no extra, hallucinated keys exist beyond the approved schema (`name`, `fqn`, `line`, `lang`, `abstract`, `entry_point`, `architectural_risk`).

### Validation Vector 2: URI Identity Integrity
1.  **Format Compliance**: Validate that every `$id` string adheres precisely to: `lang://relative_path#FQN(Signature)`.
2.  **Collision Prevention**: Prevent two logically distinct nodes from mapping to identical URIs.

### Validation Vector 3: Exhaustiveness & Risk Compliance
1.  **Orphan Check**: Identify explicit missing logical blocks (e.g., verifying that a Class node actually contains its corresponding Method nodes).
2.  **Dangling Edge Audit**: Every explicitly listed `["target": "URI"]` within an Edge array MUST resolve to a Node declared either in this payload or in the global `symbol_table.json`.
3.  **Risk Verification**: Ensure that massive, monolithic blocks are correctly carrying the `"architectural_risk": "HIGH"` metadata flag.

---

## 🛑 Corrective Failure Protocol
When an error is detected, output a formalized rejection trace without conversational padding.

**Example Matrix:**
```json
{
  "validation": "FAILED",
  "reason": "Dangling Edge Violation. Edge [:CALLS] points to lang://unknown#Target which is undefined.",
  "action": "HALT_AND_FIX"
}
```
Instruct the specific parsing worker to re-read the module, trace the missing target, instantiate the `:External` or internal Node, and resubmit a flawless payload.
