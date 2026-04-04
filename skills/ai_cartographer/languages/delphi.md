# Delphi (Object Pascal) Specialization Module

The **Delphi** Cartographer specializes in mapping Unit-based, event-driven, and object-oriented Pascal code into the **Universal Meta-Model (UCCS)**.

## Structural Taxonomy Mapping

### :Container
- **DELPHI UNIT**: The primary source code container (.pas).
- **DELPHI PROJECT**: The application container (.dpr).

### :Structure
- **INTERFACE SECTION**: A structural contract mapping of declarations.
- **IMPLEMENTATION SECTION**: A structural container mapping of definitions.
- **CLASS / RECORD**: OOP structures.
- **INTERFACE**: Method signature contracts.

### :Unit
- **PROCEDURE / FUNCTION**: Logic blocks.
- **METHOD**: Specialized logic in a Class.
- **CONSTRUCTOR / DESTRUCTOR**: Allocation logic.
- **EVENT HANDLER**: Triggers for UI actions.

### :Symbol
- **PROPERTY**: Encapsulated state symbols.
- **PROPERTY READ/WRITE Accessor**: Linked to `:Unit` or `:Symbol`.
- **VARIABLE**: State symbols.

### :Annotation
- **[Directive]**: (deprecated, inline, virtual).

## Relationship Playbook

### [:CALLS]
- Triggered by `Object.Method()`.
- Triggered by procedural calls within a Unit.

### [:USES]
- Triggered by `uses UnitName` in interface or implementation sections.
- Defines a structural dependency edge between `:Container` nodes.

### [:IMPLEMENTS]
- Triggered by `Class = class(TInterfacedObject, IMyInterface)`.

## ID Policy (Mandatory URI)
`delphi://path/to/file#UnitName.SymbolPath`

## High-Precision Requirements
- **Uses Clause Mapping**: Every entry in the `uses` list MUST be a `[:USES]` edge.
- **Property Resolution**: Properties MUST be linked to their backing fields or getter/setter methods.
