# Java Specialization Module (High-Fidelity)

The **Java** Cartographer specializes in mapping modern enterprise Java (Spring/Jakarta), including annotations, generics, and lambda logic, into the **Universal Meta-Model (UCCS)**.

## Structural Taxonomy Mapping

### :Container
- **PACKAGE**: Logical grouping container.
- **FILE (.java)**: Structural container.

### :Structure
- **CLASS / INTERFACE / ENUM**: Standard OOP structures.
- **RECORD**: Pattern-matching data structures.
- **ANNOTATION TYPE**: Metadata contract structures.

### :Unit
- **METHOD / CONSTRUCTOR**: High-level logic blocks.
- **LAMBDA / METHOD REFERENCE**: Anonymous logic units.
- **INITIALIZER BLOCK**: Anonymous structural logic.

### :Symbol
- **FIELD / CONSTANT**: State symbols.
- **LOCAL VARIABLE**: Logic-level symbols.

### :Annotation
- **@ANNOTATION**: Metadata mapped as `:Annotation` with `[:DECORATES]` edges.

## Relationship Playbook

### [:CALLS]
- Triggered by `method()`, `new Class()`, or `super()`.
- Includes `this::method` references.

### [:IMPLEMENTS]
- Triggered by `implements Interface`.

### [:EXTENDS]
- Triggered by `extends BaseClass`.

### [:OVERRIDES]
- Triggered by `@Override` or explicit signature matching.
- Defines a polymorphic linkage edge.

### [:DECORATES]
- Triggered by Spring/Jakarta annotations (e.g., `@Controller`, `@Bean`).

## ID Policy (Mandatory URI)
`java://path/to/file#Package.Class.Method(Signature)`

## High-Precision Requirements
- **Polymorphic Tracing**: Every `@Override` MUST have an `[:OVERRIDES]` edge to the parent declaration.
- **Annotation-Trigger Mapping**: Spring `@Bean` or `@Service` MUST be linked to their Registry via `[:DECORATES]`.
- **Generics Fidelity**: Capture full type information in IDs (e.g., `java://List<Owner>#add(Owner)`).
