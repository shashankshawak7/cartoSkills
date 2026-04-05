# IRMapper to Digital Modernizer: Blueprint Schema (v2.0)

This schema defines the mandatory forensic and architectural standard for all modernization blueprints. Every generation target MUST adhere to this blueprint to guarantee Enterprise-Grade robustness.

---

## 🏗️ 1. Architecture Style
Define the target architectural pattern:
- **Modular Monolith**: Internal separation of concerns via modules.
- **Microservices**: Independent deployables with API Gateway/Service Mesh.
- **Serverless**: Event-driven handlers (Lambda/Functions).
- **Clean Architecture**: Entities -> Use Cases -> Controllers -> External.

---

## 📂 2. Directory Structure (Canonical)
List the exact folder hierarchy for the target stack.
- **Source**: `src/` (All logic, controllers, models).
- **Tests**: `test/` or `tests/` (Top-level directory mirroring the `src/` hierarchy).
- **Example (NestJS)**: 
    - `src/orders/order.service.ts`
    - `test/orders/order.service.spec.ts`
- **Example (Spring)**: 
    - `src/main/java/com/package/Service.java`
    - `src/test/java/com/package/ServiceTest.java`

---

## 📦 3. Dependency Manifest
Specify the required `pom.xml`, `package.json`, or `.csproj` versions.
- Must include **Test Frameworks**: (JUnit, Vitest, etc.).
- Must include **Validation/Mappers**: (Zod, AutoMapper, MapStruct).
- Must include **Security**: (Spring Security, Passport, JWT).

---

## 🧬 4. Logic Mapping Patterns
Define how legacy primitives map to this specific stack:
- **Legacy Triggers** ➜ (Middleware / Events / Hooks).
- **Legacy TEMP-TABLEs** ➜ (DTOs / Entities / Streams).
- **Legacy Global State** ➜ (Stateless Context / Redis / Atomic Stores).

---

## 🧪 5. Testing Protocol (Mandatory)
Defined the "Thorough Testing" requirement for this stack:
- **Unit**: 1:1 logic gate parity.
- **Integration**: API endpoint / Service boundary contracts.
- **Parity Check**: Specific test cases that verify "Legacy Input A yields Modern Output B".

---

**Audit Standard**: `BLUEPRINT_SCHEMA_V2.0_ENTERPRISE_HARDENED`
