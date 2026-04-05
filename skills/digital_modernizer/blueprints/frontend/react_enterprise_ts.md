# Blueprint: React Enterprise TS (v2.0)

This blueprint defines the enterprise-hardened transformation for React SPA targets.

---

## 🏗️ 1. Architecture
- **Pattern**: Component-Driven Development with Container/Presentational separation.
- **Layers**: Components (UI), Hooks (Logic), Services (API), Context (State).
- **Communication**: TanStack Query (Server State), Zustand/Redux (Client State).

---

## 📂 2. Directory Structure
```text
src/
  ├── components/
  │   ├── ui/               # Radix/Shadcn primitives
  │   ├── shared/           # Common Layouts
  │   └── features/         # Logic-heavy components
  ├── hooks/                # Custom React Hooks
  ├── services/             # Axios/Fetch clients
  ├── store/                # Zustand/Redux state
  ├── providers/            # React Context Providers
  ├── types/                # TS Interfaces
  └── utils/                # Shared logic
```

---

## 📦 3. Dependency Manifest (package.json)
- **Framework**: `react`, `react-dom`, `framer-motion`.
- **Query**: `@tanstack/react-query`, `axios`.
- **Form**: `react-hook-form`, `zod`, `@hookform/resolvers`.
- **Testing**: `vitest`, `@testing-library/react`, `msw`.

---

## 🧬 4. Logic Mapping Patterns
- **Legacy Forms** ➜ Use **React Hook Form + Zod Schema**.
- **Legacy Triggers** ➜ Use **React useEffect / UseCallback**.
- **Legacy Global State** ➜ Use **Zustand Store / Context API**.

---

## 🧪 5. Testing Protocol
- **Unit**: Vitest for utility functions and hooks.
- **Component**: RTL for UI interaction and state updates.
- **E2E**: Playwright for critical user flows.

---

**Audit Standard**: `BLUEPRINT_REACT_V2.0_HARDENED`
