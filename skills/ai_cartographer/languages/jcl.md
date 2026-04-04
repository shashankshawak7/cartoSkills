# JCL Specialization Module

The **JCL** Cartographer specializes in mapping job-flow execution and dataset dependencies into the **Universal Meta-Model (UCCS)**.

## Structural Taxonomy Mapping

### :Container
- **JOB**: The root container for job execution.

### :Structure
- **PROC**: A reusable job-flow template structure.

### :Unit
- **STEP (EXEC)**: The fundamental execution unit that invokes a Program or Proc.

### :Symbol
- **DD (Data Definition)**: Dataset reference symbols.
- **PARM**: Execution parameter symbols.

### :External
- **PROCLIB**: External proc library dependency.
- **DATASET (DSN)**: External file reference.

## Relationship Playbook

### [:CALLS]
- Triggered by `EXEC PGM=program-name` (Calls a `:Unit` or `:External`).
- Triggered by `EXEC proc-name` (Calls a `:Structure`).

### [:USES]
- Triggered by `DD DSN=dataset-name` (Links a `:Unit` to a `:Symbol` or `:File`).
- Triggered by `JCLLIB` or `PROCLIB` statements.

## ID Policy (Mandatory URI)
`jcl://path/to/file#JobName.StepName`

## High-Precision Requirements
- **Program Linkage**: Every `EXEC PGM` statement MUST have a `[:CALLS]` edge to the target Program ID, which may reside in a COBOL or C module.
- **Dataset Traceability**: Every `DD` dataset must be mapped as a `[:USES]` edge to facilitate data-lineage analysis.
