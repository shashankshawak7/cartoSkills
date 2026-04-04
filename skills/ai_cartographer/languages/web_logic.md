# Web Logic (JS / TS) Specialization Module

The **Web Logic** Cartographer specializes in mapping modern JavaScript and TypeScript structures, including closures, arrow functions, and decorators, into the **Universal Meta-Model (UCCS)**.

## Structural Taxonomy Mapping

### :Container
- **MODULE**: The primary source code container (.js, .ts).
- **NAMESPACE**: Logical TS namespace container.

### :Structure
- **CLASS**: Standard OOP class mapping.
- **INTERFACE**: TS-only structural contract.
- **TYPE ALIAS**: TS-only structural definition.
- **ENUM**: Constant grouping structure.

### :Unit
- **FUNCTION / METHOD**: High-level logic blocks.
- **ARROW FUNCTION / LAMBDA**: Anonymous units (often child nodes).
- **CONSTRUCTOR**: Initialization logic.
- **CLOSURE**: A logic unit that captures its lexical scope (mapped with `lambda: true` and `[:USES]` edges).

### :Symbol
- **VARIABLE / CONSTANT**: State symbols.
- **FIELD / PROPERTY**: Structure-level symbols.

### :Annotation
- **@DECORATOR**: TS-only attribute mapped as `:Annotation` with `[:DECORATES]` edges.
- **JSDoc**: Structural metadata mapped as properties.

## Relationship Playbook

### [:CALLS]
- Triggered by `func()`, `method()`, or `await Promise`.
- Includes `import` calls as structural USES.

### [:USES]
- Triggered by `import { X } from 'Y'`.
- Triggered by closure captures.

### [:IMPLEMENTS]
- Triggered by `class X implements IY`.

### [:EXTENDS]
- Triggered by `class X extends Y`.

## ID Policy (Mandatory URI)
`web_logic://path/to/file#Namespace.SymbolPath`

## High-Precision Requirements
- **Closure Capture Mapping**: Every variable referenced from a parent scope MUST be a `[:USES]` edge.
- **Decorator Resolution**: Every `@decorator` MUST be linked to its target (Class or Method).
- **External CDN Mapping**: Imports from URLs MUST be mapped as `:External` nodes.
