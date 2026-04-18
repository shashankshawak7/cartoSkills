# Blueprint: Vue / Nuxt (v2.0)

This blueprint defines the enterprise-hardened transformation for Vue / Nuxt targets.

---

## 🏗️ 1. Architecture
- **Pattern**: Composition API with Nuxt 3 (SSR/Hybrid).
- **Layers**: Pages (Routing), Components (UI), Composables (Logic), Server (API/Middleware).
- **Communication**: UseFetch/UseAsyncData (Nuxt), Axios.

---

## 📂 2. Directory Structure
```text
nuxt-app/
  ├── components/          # Vue Components
  ├── composables/         # Shared Business Logic (Hooks)
  ├── pages/               # File-based Routing
  ├── layouts/             # Shared App Layouts
  ├── public/              # Static Assets (Favicon, etc)
  ├── server/              # Server-side API & Middleware
  ├── store/               # Pinia State Management
  ├── types/               # TS Interfaces
  ├── app.vue              # Main Entry
  └── nuxt.config.ts       # Configuration & Modules
```

---

## 📦 3. Dependency Manifest (package.json)
- **Framework**: `nuxt`, `vue`, `@vueuse/core`.
- **UI**: `tailwindcss`, `@pinia/nuxt`.
- **Logic**: `zod`, `axios`.
- **Testing**: `vitest`, `@vue/test-utils`, `playwright`.

---

## 🧬 4. Logic Mapping Patterns
- **Legacy Forms** ➜ Use **VeeValidate / Zod + Composition API**.
- **Legacy Triggers** ➜ Use **Vue Watchers / Event Handlers**.
- **Legacy State** ➜ Use **Pinia Store / Composables**.

---

## 🧪 5. Testing Protocol
- **Unit**: Vitest for Composables and Utility logic.
- **Component**: Vue Test Utils for UI behavior.
- **E2E**: Playwright for full SSR/Client hydration validation.

---

**Audit Standard**: `BLUEPRINT_VUE_NUXT_V2.0_HARDENED`
