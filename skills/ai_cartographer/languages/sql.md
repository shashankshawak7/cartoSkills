# SQL Specialization Module

The **SQL** Cartographer specializes in mapping data-layer logic, procedures, and schema definitions into the **Universal Meta-Model (UCCS)**.

## Structural Taxonomy Mapping

### :Container
- **SCHEMA / DATABASE**: The primary logical containers.

### :Structure
- **TABLE**: Data-structure mapping of rows and columns.
- **VIEW**: Computed data structures.
- **TYPE**: Custom data definitions.

### :Unit
- **STORED PROCEDURE**: Logic blocks including procedural T-SQL/PL-SQL.
- **FUNCTION**: Logic blocks.
- **TRIGGER**: Event-driven logic units.

### :Symbol
- **COLUMN**: Table-level state symbols.
- **VARIABLE**: Local logic symbols.
- **INDEX**: Performance-oriented data symbols.

## Relationship Playbook

### [:CALLS]
- Triggered by `EXEC procedure-name` or `SELECT function-name()`.

### [:USES]
- Triggered by `JOIN table-name` or `FROM view-name`.
- Defines a dependency edge from `:Unit` (Procedure) to `:Structure` (Table).

### [:TRIGGERS]
- Triggered by DML operations (INSERT, UPDATE) that fire a `:Unit` (Trigger).

## ID Policy (Mandatory URI)
`sql://server/db/schema#SymbolPath`

## High-Precision Requirements
- **Table-Procedure Traceability**: Every SQL query MUST be mapped as a `[:USES]` edge to the involved tables/views.
- **Event-Logic Linkage**: Triggers MUST be explicitly linked to the tables that fire them via `[:TRIGGERS]`.
