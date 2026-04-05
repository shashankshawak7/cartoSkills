# Blueprint: .NET Core Clean Architecture (v2.0)

This blueprint defines the enterprise-hardened transformation for .NET Core targets.

---

## 🏗️ 1. Architecture
- **Pattern**: Clean Architecture (Hexagonal) with MediatR.
- **Layers**: API (Presentation), Application (Use Cases), Domain (Entities), Infrastructure (External).
- **Communication**: REST API (Minimal APIs or Controllers), SignalR (Real-time).

---

## 📂 2. Directory Structure
```text
src/Skillai.{Project}.Api/
  ├── Controllers/         # API Endpoints
  ├── Program.cs          # DI & Middleware Configuration
src/Skillai.{Project}.Application/
  ├── Features/           # MediatR Commands/Queries (CQRS)
  ├── Interfaces/         # Interface definitions
  ├── Mappers/            # AutoMapper / Mapping logic
src/Skillai.{Project}.Domain/
  ├── Entities/           # Domain Models
  ├── ValueObjects/       # Immutable Values
src/Skillai.{Project}.Infrastructure/
  ├── Data/               # Entity Framework Core DbContext
  ├── Services/           # External service implementations
```

---

## 📦 3. Dependency Manifest (.csproj)
- **Framework**: `Microsoft.AspNetCore.App`, `Microsoft.EntityFrameworkCore.SqlServer`.
- **Logic**: `MediatR`, `AutoMapper`, `FluentValidation`.
- **Testing**: `xUnit`, `Moq`, `FluentAssertions`.
- **Documentation**: `Swashbuckle.AspNetCore` (Swagger).

---

## 🧬 4. Logic Mapping Patterns
- **Legacy Pointers/Ref** ➜ Use **Span<T>** or **ref** in C#. 
- **Legacy Triggers** ➜ Use **Domain Events** or **MediatR Notifications**.
- **Legacy UI Coupling** ➜ Use **ViewModel/DTO** projection.

---

## 🧪 5. Testing Protocol
- **Unit**: xUnit with Moq for Command/Query handlers. 100% logic parity.
- **Integration**: `WebApplicationFactory` with In-Memory DB or Respawn.
- **BDR**: `SpecFlow` for business outcome verification.

---

**Audit Standard**: `BLUEPRINT_DOTNET_V2.0_HARDENED`
