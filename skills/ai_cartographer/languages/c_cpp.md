# C / C++ Specialization Module

The **C / C++** Cartographer specializes in mapping systems-level, procedural, and object-oriented code, including templates, macros, and namespaces, into the **Universal Meta-Model (UCCS)**.

## Structural Taxonomy Mapping

### :Container
- **FILE (h, cpp, c, hpp)**: The root source code containers.
- **NAMESPACE**: Logical structural grouping.

### :Structure
- **CLASS / STRUCT**: Structural object mapping (including Template specialization).
- **TEMPLATE**: A reusable structural blueprint mapping.
- **UNION / ENUM**: Data structures.

### :Unit
- **FUNCTION / METHOD**: High-level logic blocks.
- **CONSTRUCTOR / DESTRUCTOR**: Resource-lifecycle logic.
- **OPERATOR OVERLOADING**: Specialized logic.

### :Symbol
- **VARIABLE / CONSTANT**: State symbols.
- **POINTER / REFERENCE**: Specialized data-pointer symbols.
- **DATA FIELD**: Structure-level symbols.

### :Annotation
- **#DEFINE**: Macro-level annotations.
- **PRAGMA**: System-level metadata.

## Relationship Playbook

### [:CALLS]
- Triggered by `func()`, `method()`, or `->` calls.

### [:USES]
- Triggered by `#include` (structural file dependency).
- Triggered by `using namespace` or `using Type`.

### [:EXTENDS]
- Triggered by `class X : public Y` (Inheritance).

## ID Policy (Mandatory URI)
`cpp://path/to/file#Namespace.SymbolPath`

## High-Precision Requirements
- **Preprocessor Traceability**: Every `#include` MUST be a `[:USES]` edge to a File node.
- **Static vs Instance**: Methods MUST be flagged as `static: true` for architectural analysis.
- **Template Instantiation**: Capture the generic type in the ID (e.g., `cpp://List<int>#size()`).
