# Language Mapping: Oracle Forms & Reports (XML/REX/RDF)

This document defines the **UCCS (Universal Code-Base Structural Mapping)** standard for Oracle Forms and Reports artifacts, ensuring they are correctly captured for both Cartography and IRMapper.

---

## 🏗️ Structural Mapping (UCCS)

### 1. 📂 [:CONTAINER] - Files & Modules
- **Forms (.xml / .fmb)**: The entire form module.
- **Reports (.rex / .rdf)**: The entire report module.
- **Attached Libraries (.pll)**: Mapped as external or internal dependencies depending on visibility.

### 2. 🏛️ [:STRUCTURE] - High-Level Components
- **Forms Data Blocks**: Mapped as `:Structure` (Data Entities).
- **Forms Canvases / Windows**: Mapped as `:Structure` (Layout Units).
- **Reports Data Model**: Groups and Queries mapped as `:Structure`.
- **Reports Layout**: Header, Body, Trailer sections.

### 3. 🧩 [:UNIT] - Executable Blocks
- **Triggers**: All triggers (e.g., `WHEN-BUTTON-PRESSED`, `PRE-QUERY`, `BEFORE-REPORT`) are mapped as `:Unit`.
- **Program Units**: PL/SQL stored procedures and functions within the form/report.
- **Form Items with Logic**: Items with validation logic.

### 4. 🏷️ [:SYMBOL] - Data Elements
- **Items**: Data Block Items and Control Items.
- **Parameters**: Form/Report parameters.
- **Global Variables**: `:Global` context variables.
- **Record Groups**: Defined data sets.
- **Summary/Formula Columns**: Complex logic symbols in Reports.

---

## 🔗 Relationship Logic
- **[:CALLS]**: When a trigger or program unit calls `GO_BLOCK`, `EXECUTE_QUERY`, or another PL/SQL unit.
- **[:USES]**: When an item points to a database column or a record group.
- **[:CONTAINS]**: Form ➜ Data Block ➜ Item; Report ➜ Data Model ➜ Query.

---

## 🚨 Risk Indicators
- **Dynamic SQL**: Use of `EXECUTIVE_IMMEDIATE` or `FORMS_DDL`.
- **Hard-coded Credentials**: Passwords in connection strings.
- **Massive Triggers**: Triggers with >100 lines of PL/SQL logic.

---

**Audit Standard**: `ORACLE_FORMS_UCCS_V1.0`
