# Blueprint: Next.js Fullstack (v2.0)

This blueprint defines the enterprise-hardened transformation for Next.js targets.

---

## 🏗️ 1. Architecture
- **Pattern**: App Router with Server Components & Server Actions.
- **Layers**: App (Routing), Components (UI), Lib (Logic/Clients), Hooks (State).
- **Communication**: RSC (Direct DB access), Server Actions (Form Mutation), API Routes (External).

---

## 📂 2. Directory Structure
```text
next-app/
  ├── app/                  # App Router Logic
  ├── components/           # UI Components
  ├── lib/                  # Shared utilities
  ├── hooks/                # React Hooks
  ├── test/                 # Mirrored Testing Hierarchy
  │   ├── app/              # Router / Page Tests
  │   ├── components/       # Component Tests
  │   └── hooks/            # Hook Tests
  └── types/                # TS Interfaces
```

---

## 📦 3. Dependency Manifest (package.json)
- **Framework**: `next@latest`, `react@latest`, `lucide-react`.
- **UI**: `tailwindcss`, `shadcn/ui`, `framer-motion`.
- **Data**: `zod`, `react-hook-form`, `tanstack/react-query`.
- **Testing**: `vitest`, `@testing-library/react`, `msw`.

---

## 🧬 4. Logic Mapping Patterns
- **Legacy Forms** ➜ Use **React Hook Form + Zod Validation**.
- **Legacy Triggers** ➜ Use **React useEffect / Event Handlers**.
- **Legacy State Mapping** ➜ Use **React Context / Zustand**.

---

## 🧪 5. Testing Protocol
- **Unit**: Vitest for utility functions and hooks.
- **Component**: RTL for UI interaction and state updates.
- **E2E**: Playwright for critical user flows.

---

**Audit Standard**: `BLUEPRINT_NEXTJS_V2.0_HARDENED`
