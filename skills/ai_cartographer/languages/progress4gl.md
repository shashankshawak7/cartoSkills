# Progress 4GL (OpenEdge) Specialization Module

The **Progress 4GL** Cartographer specializes in decomposing ABL (Advanced Business Language) constructs into the nuance-free **Universal Meta-Model (UCCS)**.

## Structural Taxonomy Mapping

### :Container
- **Procedure File (.p)**: Root file container.
- **Class File (.cls)**: Structural file container.
- **Include File (.i)**: Shared structural dependency.

### :Structure
- **CLASS**: Mapped as a logic structure.
- **INTERFACE**: Mapped as a contract structure.
- **TEMP-TABLE**: Mapped as a data structure with `:Symbol` children for fields.
- **DATASET / DATA-SOURCE**: Mapped as complex data structures.

### :Unit
- **PROCEDURE**: Mapped as a logic block.
- **FUNCTION**: Mapped as a logic block.
- **METHOD**: Mapped as a logic block within a Class.
- **CONSTRUCTOR / DESTRUCTOR**: Specialized logic units.
- **ON EVENT ... DO**: Mapped as an event-driven logic unit.

### :Symbol
- **VARIABLE**: Local or global symbol.
- **BUFFER**: Specialized data-pointer symbol.
- **QUERY**: Data-access symbol.
- **TEMP-TABLE Field**: Symbol contained within a `:Structure`.

### :Annotation
- **[Preprocessing Directives]**: (&scoped-define, etc.)

## Relationship Playbook

### [:CALLS]
- Triggered by `RUN procedure-name`.
- Triggered by `object:method-name()`.
- Triggered by `DYNAMIC-FUNCTION('name')`.

### [:USES]
- Triggered by `{include_file.i}` (Include references).
- Triggered by `USING package.name.*`.
- Triggered by `DEFINE BUFFER buf FOR table-name`.

### [:TRIGGERS]
- Triggered by `PUBLISH 'event-name'`.
- Triggered by `SUBSCRIBE TO 'event-name'`.

## ID Policy (Mandatory URI)
`progress://path/to/file#SymbolPath(Signature)`

## High-Precision Requirements
- **Recursiveness**: Every `{}` include MUST be extracted as a `[:USES]` edge.
- **Dynamic Logic**: Capture `RUN VALUE(var)` as a `[:CALLS]` to a `placeholder: true` node if the target is unknown at parse-time.
