# Python Specialization Module (High-Fidelity)

The **Python** Cartographer specializes in mapping modern Python (3.10+), including decorators, type hints, and async logic, into the **Universal Meta-Model (UCCS)**.

## Structural Taxonomy Mapping

### :Container
- **MODULE (.py)**: Structural container.
- **PACKAGE**: Folder-based container with `__init__.py`.

### :Structure
- **CLASS**: Standard OOP class mapping.
- **DATACLASS**: Specialized data structures.

### :Unit
- **FUNCTION (def)**: High-level logic blocks.
- **METHOD**: Specialized logic in a Class.
- **ARROW FUNCTION / LAMBDA**: Anonymous logic units.
- **ASYNC FUNCTION (async def)**: Mapped with `async: true`.

### :Symbol
- **VARIABLE / CONSTANT**: State symbols.
- **ATTRIBUTE / FIELD**: Structure-level symbols.

### :Annotation
- **@DECORATOR**: Meta-programming mapped as `:Annotation` with `[:DECORATES]` edges.

## Relationship Playbook

### [:CALLS]
- Triggered by `func()`, `method()`, or `await obj`.
- Includes `super()` and `__init__` calls.

### [:USES]
- Triggered by `import module` or `from module import X`.
- Defines a structural dependency edge.

### [:EXTENDS]
- Triggered by `class X(BaseClass)`.

## ID Policy (Mandatory URI)
`python://path/to/file#ModulePath.SymbolPath`

## High-Precision Requirements
- **Decorator Resolution**: Every `@decorator` MUST be linked to its target.
- **Dunder Method Audit**: Methods like `__call__` or `__getitem__` MUST be mapped for structural behavior.
