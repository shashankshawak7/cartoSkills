# Blueprint: Spring Boot Microservices (v2.0)

This blueprint defines the enterprise-hardened transformation for Spring Boot targets.

---

## 🏗️ 1. Architecture
- **Pattern**: Clean Architecture (Onion) with Spring Cloud.
- **Layers**: Controller (Web), Service (Logic), Repository (Persistence), DTO (External), Entity (Internal).
- **Communication**: REST API (Synchronous), Kafka/RabbitMQ (Asynchronous).

---

## 📂 2. Directory Structure
```text
src/main/java/com/skillai/{module}/   # Logic & Services
  ├── api/             # Controllers (@RestController)
  ├── application/      # Services (@Service)
  ├── domain/          # Entities (@Entity) & Domain logic
  ├── infrastructure/  # Repositories (@Repository) & Adapters
  ├── shared/          # Exceptions, Utils, Constants
  └── dtos/            # Mappers (MapStruct) & Data Transfer
src/test/java/com/skillai/{module}/   # Mirrored Testing Hierarchy
  ├── api/             # Controller Tests
  ├── application/      # Service Tests
  └── infrastructure/  # Repository Tests
```

---

## 📦 3. Dependency Manifest (pom.xml)
- **Framework**: `spring-boot-starter-web`, `spring-boot-starter-data-jpa`.
- **Validation**: `spring-boot-starter-validation`.
- **Security**: `spring-boot-starter-security`, `jjwt`.
- **Testing**: `spring-boot-starter-test` (JUnit 5, Mockito, AssertJ).
- **Hardening**: `micrometer`, `prometheus`, `resilience4j-spring-boot3`.

---

## 🧬 4. Logic Mapping Patterns
- **Legacy PERFORM/GOTO** ➜ Use **Service Redirection** or **Chain of Responsibility**.
- **Legacy Global State** ➜ Use **ThreadLocal Context** or **Redis State Stores**.
- **Legacy Database Cursor** ➜ Use **Spring Data Streams** or **JPA Projections**.

---

## 🧪 5. Testing Protocol
- **Unit**: Mockito for Services and Logic. 100% path coverage.
- **Integration**: `@SpringBootTest` with TestContainers (Postgres/MySQL).
- **Contract**: Spring Cloud Contract for API boundaries.

---

**Audit Standard**: `BLUEPRINT_SPRING_BOOT_V2.0_HARDENED`
