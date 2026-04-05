# Blueprint: Micronaut (v2.0)

This blueprint defines the enterprise-hardened transformation for Micronaut targets.

---

## 🏗️ 1. Architecture
- **Pattern**: AOT (Ahead-of-Time) Compiled Microservices.
- **Layers**: Controller (Injection), Service (Business Logic), Repository (Data JDBC), DTO.
- **Communication**: Netty-based HTTP/2, gRPC, Kafka.

---

## 📂 2. Directory Structure
```text
src/main/java/com/skillai/{module}/
  ├── controllers/      # @Controller Endpoints
  ├── services/         # @Singleton Business Logic
  ├── repositories/     # Micronaut Data JDBC
  ├── domain/           # @Introspected Domain Models
  └── Application.java  # Main Entry
src/main/resources/
  └── application.yml
```

---

## 📦 3. Dependency Manifest (pom.xml)
- **Framework**: `micronaut-http-server-netty`, `micronaut-data-jdbc`.
- **Validation**: `micronaut-validation`.
- **Security**: `micronaut-security-jwt`.
- **Testing**: `micronaut-test-junit5`, `mockito-core`.

---

## 🧬 4. Logic Mapping Patterns
- **Legacy Database Cursors** ➜ Use **Micronaut Data JDBC Queries**.
- **Legacy Triggers** ➜ Use **AOP Interceptors (@Around)**.
- **Legacy Global State** ➜ Use **Micronaut Cache (@Cacheable)**.

---

## 🧪 5. Testing Protocol
- **Unit**: JUnit 5 with Mockito for Service logic.
- **Integration**: `@MicronautTest` for Full HTTP Client validation.
- **Native**: GraalVM native-image verification.

---

**Audit Standard**: `BLUEPRINT_MICRONAUT_V2.0_HARDENED`
