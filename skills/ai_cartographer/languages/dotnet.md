# .NET (C# / F#) Specialization Module

The **.NET** Cartographer specializes in mapping modern C#/F# structures, including partial classes, events, and async logic, into the **Universal Meta-Model (UCCS)**.

## Structural Taxonomy Mapping

### :Container
- **NAMESPACE**: Logical grouping container.
- **PROJECT (csproj/fsproj)**: External/Internal project boundary.

### :Structure
- **CLASS / STRUCT**: Generic or concrete data structures.
- **INTERFACE**: Contract structures.
- **RECORD**: Pattern-matching structures.
- **PARTIAL CLASS**: Merged or linked structural nodes.

### :Unit
- **METHOD / FUNCTION**: Logic blocks (mapped as `async: true` if applicable).
- **PROPERTY**: Mapped as a `:Symbol` but with `[:CALLS]` edges from Get/Set logic.
- **EVENT**: Specialized `:Unit`/`:Symbol` for pub-sub.
- **DELEGATE**: Mapped as a contract structure.

### :Symbol
- **FIELD**: State symbols.
- **CONSTANT**: Static symbols.

### :Annotation
- **[Attribute]**: Metadata mapped as `:Annotation` with `[:DECORATES]` edges.

## Relationship Playbook

### [:CALLS]
- Triggered by `Method()`, `await Task`, or `Invoke()`.

### [:TRIGGERS]
- Triggered by `event += handler` or event firing.

### [:IMPLEMENTS]
- Triggered by `Class : IInterface`.

### [:EXTENDS]
- Triggered by `Class : BaseClass`.

## ID Policy (Mandatory URI)
`dotnet://path/to/file#Namespace.Class.Method(Params)`

## High-Precision Requirements
- **Partial Class Union**: Multiple files defining one Class MUST result in a single `:Structure` node or explicit `[:EXTENDS]`-style merging.
- **LINQ Resolution**: Mapped as unit-internal `[:CALLS]` to the System.Linq library.
