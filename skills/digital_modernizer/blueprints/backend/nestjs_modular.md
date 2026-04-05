# Blueprint: NestJS Modular Monolith (v2.0)

This blueprint defines the enterprise-hardened transformation for NestJS targets.

---

## 🏗️ 1. Architecture
- **Pattern**: Modular Monolith (Domain-Driven Design).
- **Layers**: Controller (Web), Service (Logic), Provider (Infrastructure), Module (Scope).
- **Communication**: Internal Events (EventEmitter2), REST API, Microservice Transporters.

---

## 📂 2. Directory Structure
```text
src/modules/{feature}/
  ├── controllers/         # API Endpoints (@Controller)
  ├── services/            # Business Logic (@Injectable)
  ├── providers/           # Database / External Clients
  ├── dto/                 # Data Transfer Objects
  └── {feature}.module.ts  # Module definition
test/modules/{feature}/    # Mirrored Testing Hierarchy
  ├── controllers/         # Controller Tests
  ├── services/            # Service Tests
  └── providers/           # Provider Tests
```

---

## 📦 3. Dependency Manifest (package.json)
- **Framework**: `@nestjs/common`, `@nestjs/core`, `@nestjs/typeorm`.
- **Logic**: `class-validator`, `class-transformer`, `@nestjs/event-emitter`.
- **Testing**: `vitest`, `@nestjs/testing`, `supertest`.
- **Maintenance**: `prettier`, `eslint`, `husky`.

---

## 🧬 4. Logic Mapping Patterns
- **Legacy TEMP-TABLEs** ➜ Use **TypeORM Entities** or **In-memory Modules**.
- **Legacy Internal Procedures** ➜ Use **Private Service Methods**.
- **Legacy Triggers** ➜ Use **NestJS Interceptors** or **Event Decorators**.

---

## 🧪 5. Testing Protocol
- **Unit**: Vitest for Service logic. 100% logic gate parity.
- **Integration**: `@nestjs/testing` with `TestingModule`.
- **E2E**: Supertest for full request-response validation.

---

**Audit Standard**: `BLUEPRINT_NESTJS_V2.0_HARDENED`
