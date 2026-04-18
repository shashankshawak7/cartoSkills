# Blueprint: Angular Enterprise (v2.0)

This blueprint defines the enterprise-hardened transformation for Angular targets.

---

## 🏗️ 1. Architecture
- **Pattern**: Component-Driven Architecture with Signals & Observables.
- **Layers**: Components (UI), Services (Logic), Models (Data), Guards/Interceptors.
- **Communication**: RXJS (Streams), TanStack Query (Server State), Signals (Local State).

---

## 📂 2. Directory Structure
```text
src/app/
  ├── components/
  │   ├── shared/           # Common components
  │   └── features/         # Logic-heavy components
  ├── services/            # Logic & API clients (@Injectable)
  ├── models/              # TS Interfaces
  ├── shared/              # Pipes, Directives, Utils
  ├── core/                # Guards, Interceptors, Config
  └── app.routes.ts        # Enterprise Routing
```

---

## 📦 3. Dependency Manifest (package.json)
- **Framework**: `@angular/common`, `@angular/core`, `@angular/material`.
- **Logic**: `rxjs`, `@ngneat/query`, `zod`.
- **Testing**: `vitest`, `@testing-library/angular`, `cypress`.

---

## 🧬 4. Logic Mapping Patterns
- **Legacy Forms** ➜ Use **Angular Reactive Forms + Zod Validator**.
- **Legacy Triggers** ➜ Use **Angular Signals / RXJS Subjects**.
- **Legacy Hierarchy** ➜ Use **Angular Dependency Injection**.

---

## 🧪 5. Testing Protocol
- **Unit**: Vitest for Service logic and Signal state.
- **Component**: Testing Library for UI interaction.
- **E2E**: Cypress for full user story validation.

---

**Audit Standard**: `BLUEPRINT_ANGULAR_V2.0_HARDENED`
