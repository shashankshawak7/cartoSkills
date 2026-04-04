# Shell Scripting Specialization Module

The **Shell** Cartographer specializes in mapping command-line execution, script entry points, and process communication into the **Universal Meta-Model (UCCS)**.

## Structural Taxonomy Mapping

### :Container
- **SCRIPT FILE (.sh, .bash, .ps1)**: The root execution container.

### :Unit
- **FUNCTION**: Logic blocks.
- **COMMAND INVOCATION (ls, grep, etc.)**: Execution units.
- **GLOBAL SCOPE**: The implicit entry point `:Unit` (`entry_point: true`).

### :Symbol
- **VARIABLE / ENVIRONMENT VARIABLE**: State symbols.
- **PIPE / REDIRECT**: Data-flow symbols.

## Relationship Playbook

### [:CALLS]
- Triggered by invoking a binary, script, or function.
- Every command and its arguments MUST be mapped for process lineage.

### [:USES]
- Triggered by `source` or `.` (Script sourcing).
- Defines a structural dependency edge between Scripts.

### [:TRIGGERS]
- Triggered by alias or trap hooks.

## ID Policy (Mandatory URI)
`shell://path/to/file#SymbolPath`

## High-Precision Requirements
- **Implicit Entry Point Mapping**: Every script MUST have a `:Unit` node representing its execution body.
- **Process Lineage**: Every external command MUST be a `[:CALLS]` to an `:External` or internal `:Unit`.
