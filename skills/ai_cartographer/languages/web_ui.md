# Web UI (HTML / CSS) Specialization Module

The **Web UI** Cartographer specializes in mapping the visual and structural components of a frontend into the **Universal Meta-Model (UCCS)**.

## Structural Taxonomy Mapping

### :Container
- **HTML DOCUMENT**: The root container for structural layout.
- **STYLE SHEET**: The root container for visual rules (.css, .scss).

### :Structure
- **ELEMENT / COMPONENT**: Interactive or structural HTML elements (e.g., `<button>`, `<div>`).
- **CSS RULE**: A selector-based structural block.

### :Unit
- **UI HOOK (onclick, etc.)**: Inline or reactive logic within HTML.
- **KEYFRAME / ANIMATION**: Visual temporal units.

### :Symbol
- **HTML ID / CLASS**: Target symbols for styling.
- **CSS PROPERTY**: Visual trait symbols.
- **CSS VARIABLE**: Global or local style symbols.

## Relationship Playbook

### [:STYLES]
- Triggered by a CSS Rule matching an HTML ID or Class.
- Defines a bridge edge from `:Container` (CSS) to `:Container` (HTML).

### [:CALLS]
- Triggered by a UI Hook (e.g., `<button onclick='logic()'>`) referencing a JS `:Unit`.

### [:USES]
- Triggered by `<link>`, `<script>`, or `@import`.
- Triggered by `var(--name)` in CSS.

## ID Policy (Mandatory URI)
`web_ui://path/to/file#ElementID` OR `web_ui://path/to/style#SelectorPath`

## High-Precision Requirements
- **DOM-Logic Bridge**: Every inline JS hook MUST be a `[:CALLS]` edge to the corresponding JS node.
- **Style Invalidation Audit**: Every CSS rule MUST be linked to at least one HTML element (or marked as `unused: true`).
