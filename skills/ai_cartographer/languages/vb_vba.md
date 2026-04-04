# VB / VBA Specialization Module

The **VB / VBA** Cartographer specializes in mapping event-driven, procedural code into the **Universal Meta-Model (UCCS)**.

## Structural Taxonomy Mapping

### :Container
- **MODULE (.bas, .vbs)**: Procedural container.
- **FORM / CLASS (.frm, .cls)**: Functional and UI containers.

### :Structure
- **CLASS**: Standard OOP class mapping.
- **USER-DEFINED TYPE (UDT)**: Struct-style mapping.

### :Unit
- **SUB / FUNCTION**: Logic blocks.
- **EVENT (Button1_Click, etc.)**: Specialized UI logic units.
- **PROPERTY GET/LET/SET**: State-accessor logic units.

### :Symbol
- **VARIABLE / CONSTANT**: State symbols.
- **UI CONTROL (TextBox, etc.)**: State-holding symbols linked to Form containers.

## Relationship Playbook

### [:CALLS]
- Triggered by `Call method` or `methodName`.

### [:TRIGGERS]
- Triggered by UI interaction firing a `:Unit` (Event).

### [:USES]
- Triggered by `References` (VBA/VB6 references).
- Triggered by `Set obj = New Class`.

## ID Policy (Mandatory URI)
`vba://path/to/file#SymbolPath`

## High-Precision Requirements
- **Reference Resolution**: Every external Reference (DLL/TLB) MUST be mapped as an `:External` node.
- **UI-Logic Mapping**: Forms MUST be linked to their UI controls via `[:CONTAINS]`.
