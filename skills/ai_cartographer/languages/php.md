# PHP Specialization Module (High-Fidelity)

The **PHP** Cartographer specializes in mapping PHP 8+ structures, including attributes and traits, into the **Universal Meta-Model (UCCS)**.

## Structural Taxonomy Mapping

### :Container
- **FILE (.php)**: Structural container.
- **NAMESPACE**: Logical grouping container.

### :Structure
- **CLASS**: Standard OOP class mapping.
- **INTERFACE**: Contract structures.
- **TRAIT**: Reusable structural blocks.

### :Unit
- **FUNCTION / METHOD**: High-level logic blocks.
- **CLOSURE**: Anonymous logic units.

### :Symbol
- **VARIABLE / CONSTANT**: State symbols.
- **PROPERTY**: Structure-level symbols.

### :Annotation
- **#[Attribute]**: Metadata mapped as `:Annotation`.

## Relationship Playbook

### [:CALLS]
- Triggered by `func()` or `$obj->method()`.

### [:IMPLEMENTS]
- Triggered by `class X implements IY`.

### [:EXTENDS]
- Triggered by `class X extends Y`.

### [:USES]
- Triggered by `use TraitName` within a Class.
- Triggered by `use Namespace\Class`.

## ID Policy (Mandatory URI)
`php://path/to/file#Namespace.Class.Method`

## High-Precision Requirements
- **Trait Linkage**: Every `use` of a Trait MUST be mapped as a structural dependency.
