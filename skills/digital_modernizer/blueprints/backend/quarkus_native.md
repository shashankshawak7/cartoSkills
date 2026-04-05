# Blueprint: Quarkus Native (v2.0)

This blueprint defines the enterprise-hardened transformation for Quarkus targets.

---

## 🏗️ 1. Architecture
- **Pattern**: Supersonic Subatomic Java (K8s-Native).
- **Layers**: Resource (REST), Service (Logic), Entity (Panache), DTO.
- **Communication**: gRPC, RESTEasy Reactive, Kafka.

---

## 📂 2. Directory Structure
```text
src/main/java/com/skillai/{module}/
  ├── resource/        # REST Endpoints (@Path)
  ├── service/         # Business Logic (@ApplicationScoped)
  ├── model/           # Panache Entities (@Entity)
  └── dto/             # Data Transfer Objects
src/main/resources/
  ├── application.properties
  └── import.sql       # Initial Data
```

---

## 📦 3. Dependency Manifest (pom.xml)
- **Framework**: `quarkus-resteasy-reactive`, `quarkus-hibernate-orm-panache`.
- **Validation**: `quarkus-hibernate-validator`.
- **Security**: `quarkus-oidc`, `quarkus-jose`.
- **Testing**: `quarkus-junit5`, `mockito-core`, `rest-assured`.

---

## 🧬 4. Logic Mapping Patterns
- **Legacy Database Cursors** ➜ Use **Panache Queries / Streams**.
- **Legacy Triggers** ➜ Use **CDI Observers (@Observes)**.
- **Legacy Global State** ➜ Use **Redis Clients (@Inject)**.

---

## 🧪 5. Testing Protocol
- **Unit**: JUnit 5 with Mockito for Service logic.
- **Integration**: `@QuarkusTest` for REST API validation.
- **Native**: `@QuarkusIntegrationTest` for GraalVM native binary verification.

---

**Audit Standard**: `BLUEPRINT_QUARKUS_V2.0_HARDENED`
