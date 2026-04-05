# Blueprint: Flutter Clean Architecture (v2.0)

This blueprint defines the enterprise-hardened transformation for Flutter targets.

---

## 🏗️ 1. Architecture
- **Pattern**: Clean Architecture (Entity-UseCase-Data).
- **Layers**: Domain (Business Logic), Data (Repository/Source), Presentation (UI/State).
- **Communication**: Bloc / Provider (State Management), Dio (HTTP).

---

## 📂 2. Directory Structure
```text
lib/
  ├── core/                # Shared Errors, Params, Utils
  ├── features/
  │   ├── {module}/
  │   │   ├── domain/      # Entities, Repositories, UseCases
  │   │   ├── data/        # Models, DataSources, RepoImpl
  │   │   └── presentation/ # Bloc, Pages, Widgets
  ├── main.dart            # Dependency Injection (GetIt)
```

---

## 📦 3. Dependency Manifest (pubspec.yaml)
- **Framework**: `flutter`, `flutter_bloc`, `get_it`.
- **Logic**: `dartz`, `equatable`, `json_annotation`.
- **Testing**: `flutter_test`, `mockito`, `bloc_test`.

---

## 🧬 4. Logic Mapping Patterns
- **Legacy UI Triggers** ➜ Use **Flutter Bloc Events**.
- **Legacy State Mapping** ➜ Use **Clean Domain Entities**.
- **Legacy Database** ➜ Use **Floor (SQLite)** or **Hive**.

---

## 🧪 5. Testing Protocol
- **Unit**: Mockito for Bloc and UseCase logic.
- **Widget**: Component-level smoke tests.
- **Golden**: UI Visual regression tests.

---

**Audit Standard**: `BLUEPRINT_FLUTTER_V2.0_HARDENED`
