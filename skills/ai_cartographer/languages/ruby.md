# Ruby Specialization Module (High-Fidelity)

The **Ruby** Cartographer specializes in mapping dynamic Ruby structures into the **Universal Meta-Model (UCCS)**.

## Structural Taxonomy Mapping

### :Container
- **FILE (.rb)**: Structural container.

### :Structure
- **CLASS**: Standard OOP class mapping.
- **MODULE**: Namespace or Mixin container.

### :Unit
- **METHOD (def)**: High-level logic blocks.
- **BLOCK / PROC / LAMBDA**: Captured logic units.

### :Symbol
- **VARIABLE / CONSTANT**: State symbols.
- **INSTANCE VARIABLE (@var)**: Structure-level symbols.

## Relationship Playbook

### [:CALLS]
- Triggered by method invocation.

### [:EXTENDS]
- Triggered by `class X < Y` (Inheritance) or `extend Module`.

### [:USES]
- Triggered by `require` or `include Module` (Mixins).

## ID Policy (Mandatory URI)
`ruby://path/to/file#ClassName.MethodName`

## High-Precision Requirements
- **Mixin Traceability**: Every `include` or `extend` MUST be mapped for structural lineage.
