# COBOL Specialization Module

The **COBOL** Cartographer specializes in decomposing procedural, monolithic structures into the **Universal Meta-Model (UCCS)**.

## Structural Taxonomy Mapping

### :Container
- **COBOL PROGRAM**: The root container for divisions and sections.

### :Structure
- **IDENTIFICATION DIVISION**: High-level metadata structure.
- **ENVIRONMENT DIVISION / DATA DIVISION**: Declarative structures.
- **PROCEDURE DIVISION**: The execution flow structure.
- **SECTION**: A logic grouping structure within the Procedure Division.

### :Unit
- **PARAGRAPH**: The fundamental logic unit.
- **DECLARATIVE SECTION**: Specialized logic blocks.

### :Symbol
- **DATA ITEM (01-77)**: Symbolic data references.
- **FD (File Descriptor)**: Dataset mapping symbol.

### :External
- **COPYBOOK**: External file dependency.
- **EXTERNAL PROGRAM**: Link to another executable.

## Relationship Playbook

### [:CALLS]
- Triggered by `PERFORM paragraph-name`.
- Triggered by `CALL program-name`.
- Triggered by `GO TO paragraph-name`.

### [:USES]
- Triggered by `COPY copybook-name`.
- Triggered by `DATA DIVISION` references to File Descriptors.

## ID Policy (Mandatory URI)
`cobol://path/to/file#SymbolPath`

## High-Precision Requirements
- **Copybook Expansion**: Every `COPY` statement MUST be mapped as a `[:USES]` edge to a `:Container` node.
- **Paragraph Graphing**: Every jump (`GO TO` or `PERFORM`) MUST be a `[:CALLS]` edge to a corresponding `:Unit`.
