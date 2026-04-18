# Blueprint: Play Framework (Java/Scala) (v2.0)

This blueprint defines the enterprise-hardened transformation for Play Framework targets.

---

## 🏗️ 1. Architecture
- **Pattern**: MVC (Model-View-Controller) with Akka/Pekko.
- **Layers**: Controllers (Routes), Services (Context), Repositories (Anorm/Ebean), Forms (Logic).
- **Communication**: HTTP/2, Akka Streams.

---

## 📂 2. Directory Structure
```text
app/
  ├── controllers/         # Web/API Handlers
  ├── services/           # Business Logic (@Singleton)
  ├── repository/         # Database persistence
  ├── models/             # Domain POJOs
  └── views/              # Twirl Templates
conf/
  ├── application.conf
  └── routes               # Route definition
public/                  # Static Assets
```

---

## 📦 3. Dependency Manifest (build.sbt)
- **Framework**: `play-java`, `play-akka-http-server`.
- **ORMs**: `play-java-jpa`, `play-ebean`.
- **Validation**: `play-java-forms`.
- **Testing**: `play-test`, `junit-5`.

---

## 🧬 4. Logic Mapping Patterns
- **Legacy Blocking DB** ➜ Use **Play-Provided Custom ExecutionContexts**.
- **Legacy Temp-Tables** ➜ Use **Play Forms / Akka Streams**.
- **Legacy Triggers** ➜ Use **Akka Actors / Events**.

---

## 🧪 5. Testing Protocol
- **Unit**: JUnit 5 for Service logic.
- **Integration**: `Helpers.fakeRequest()` for Controller validation.
- **System**: `WithServer` for full browser/API tests.

---

**Audit Standard**: `BLUEPRINT_PLAY_V2.0_HARDENED`
