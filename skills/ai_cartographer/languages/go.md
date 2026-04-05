# Go Specialization Module (High-Fidelity)

The **Go** Cartographer specializes in mapping Go structures, including interfaces, embedding, and goroutines, into the **Universal Meta-Model (UCCS)**.

## Structural Taxonomy Mapping

### :Container
- **PACKAGE**: The primary unit of code organization.
- **FILE (.go)**: Structural container.

### :Structure
- **STRUCT**: Data-structure mapping.
- **INTERFACE**: Method signature contracts.

### :Unit
- **FUNCTION (func)**: High-level logic blocks.
- **METHOD (receiver func)**: Specialized logic for a Struct.

### :Symbol
- **VARIABLE / CONSTANT**: State symbols.
- **FIELD**: Struct-level symbols.

## Relationship Playbook

### [:CALLS]
- Triggered by `func()` or `object.Method()`.

### [:IMPLEMENTS]
- Implicitly triggered by a Struct satisfying an Interface's method set.

### [:EXTENDS]
- Triggered by Struct Embedding (`type X struct { Y }`).

### [:USES]
- Triggered by `import "package"`.

## ID Policy (Mandatory URI)
`go://package/path#SymbolName`

## High-Precision Requirements
- **Embedding Traceability**: Every embedded struct MUST be mapped as an `[:EXTENDS]` edge.
- **Receiver Mapping**: Every receiver method MUST be linked to its Struct via `[:CONTAINS]`.
