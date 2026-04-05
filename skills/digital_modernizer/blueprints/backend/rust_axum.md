# Blueprint: Rust Axum (v2.0)

This blueprint defines the enterprise-hardened transformation for Rust targets.

---

## 🏗️ 1. Architecture
- **Pattern**: Type-Safe Asynchronous Handler Pattern (Statically Typed).
- **Layers**: Routers (Web), Services (Logic), Repositories (Data), Models (Entities).
- **Communication**: HTTP/S (Axum), gRPC (Tonic), Message Queues (Tokio-RS).

---

## 📂 2. Directory Structure
```text
src/
  ├── api/
  │   ├── mod.rs           # API Entry
  │   └── handlers/        # Async Handlers
  ├── services/            # Business Logic
  ├── domain/              # Entities & Models
  ├── infrastructure/      # Database (SQLx/Diesel) & External
  ├── config/              # App Settings (Donv / Config-rs)
  └── main.rs              # Application Entry
```

---

## 📦 3. Dependency Manifest (Cargo.toml)
- **Framework**: `axum`, `tokio`, `tower-http`.
- **ORMs**: `sqlx`, `diesel`, `sea-orm`.
- **Logic**: `serde`, `validator`, `anyhow`, `tracing`.
- **Testing**: `tokio-test`, `mockall`, `test-context`.

---

## 🧬 4. Logic Mapping Patterns
- **Legacy Pointers/Manual Mem** ➜ Use **Rust Borrow Checker (Refs/Ownership)**.
- **Legacy GOTO/Logic Gates** ➜ Use **Rust Enums / Pattern Matching**.
- **Legacy Global State** ➜ Use **Arc<Mutex<T>>** or **State<T>** injection.

---

## 🧪 5. Testing Protocol
- **Unit**: `cargo test` for logic parity. 100% path coverage.
- **Integration**: `reqwest` or `tower::Service` for API endpoint tests.
- **Property**: `quickcheck` for input boundary validation.

---

**Audit Standard**: `BLUEPRINT_RUST_V2.0_HARDENED`
