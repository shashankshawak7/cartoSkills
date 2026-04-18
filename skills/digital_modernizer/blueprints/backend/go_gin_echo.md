# Blueprint: Go Gin / Echo (v2.0)

This blueprint defines the enterprise-hardened transformation for Go targets.

---

## 🏗️ 1. Architecture
- **Pattern**: Handler-Service-Repository (Hexagonal-lite).
- **Layers**: Handlers (Web), Services (Logic), Repositories (Data), Models (Entities).
- **Communication**: HTTP/S (Gin/Echo), gRPC (Protobuf), WebSockets.

---

## 📂 2. Directory Structure
```text
cmd/skillai/main.go        # Main Entry
internal/
  ├── app/
  │   ├── handlers/         # HTTP Handlers
  │   ├── services/         # Business Logic
  │   └── repositories/     # SQLite/Postgres/Mongo
  ├── domain/              # Entities & Domain Models
  ├── platform/            # External Clients (Redis/Kafka)
  └── pkg/                 # Internal Shared Utilities
```

---

## 📦 3. Dependency Manifest (go.mod)
- **Framework**: `gin-gonic/gin` or `labstack/echo/v4`.
- **ORMs**: `gorm.io/gorm`, `entgo.io/ent`.
- **Validation**: `go-playground/validator/v10`.
- **Testing**: `stretchr/testify`, `vektra/mockery`.

---

## 🧬 4. Logic Mapping Patterns
- **Legacy PERFORM/GOTO** ➜ Use **Go Handlers & Private Methods**.
- **Legacy Database Cursors** ➜ Use **Go Iterators / GORM Scopes**.
- **Legacy Memory Management** ➜ Use **Go Garbage Collection / Slices**.

---

## 🧪 5. Testing Protocol
- **Unit**: `testify` for Service and Handler logic. 100% logic parity.
- **Integration**: `testcontainers-go` for Database container testing.
- **Fuzzing**: `go test -fuzz` for input robustness.

---

**Audit Standard**: `BLUEPRINT_GO_V2.0_HARDENED`
