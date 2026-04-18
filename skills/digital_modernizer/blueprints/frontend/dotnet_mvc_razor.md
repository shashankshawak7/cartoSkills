# Blueprint: .NET Core MVC (Razor) (v2.0)

This blueprint defines the enterprise-hardened transformation for .NET Core MVC targets.

---

## 🏗️ 1. Architecture
- **Pattern**: MVC (Model-View-Controller) with Razor Views.
- **Components**: Controllers (Navigation/Logic), Views (HTML/Tag Helpers), Models (Data/ViewModels).
- **Security**: ASP.NET Core Identity, Anti-Forgery Tokens.

---

## 📂 2. Directory Structure
```text
Skillai.{Project}.Web/
  ├── Controllers/         # Logic & Navigation (@Controller)
  ├── Models/              # ViewModels (Mapping Logic)
  ├── Views/
  │   ├── Shared/          # Layouts & Partials
  │   └── {Feature}/       # Razor [.cshtml] Files
  ├── wwwroot/             # Static Assets (CSS, JS, Libs)
  ├── Program.cs          # Pipeline & DI Configuration
  └── {Project}.Web.csproj
```

---

## 📦 3. Dependency Manifest (.csproj)
- **Framework**: `Microsoft.AspNetCore.App`.
- **Logic**: `Microsoft.AspNetCore.Mvc.Razor.RuntimeCompilation`, `AutoMapper`.
- **Testing**: `xUnit`, `Microsoft.AspNetCore.Mvc.Testing`, `Playwright`.

---

## 🧬 4. Logic Mapping Patterns
- **Legacy UI Triggers** ➜ Use **ASP.NET Tag Helpers (asp-action, asp-for)**.
- **Legacy Forms** ➜ Use **Razor Form Bindings + DataAnnotations**.
- **Legacy Session** ➜ Use **Distributed Cache / Session State**.

---

## 🧪 5. Testing Protocol
- **Unit**: xUnit for Controller logic and ViewModels.
- **Integration**: `WebApplicationFactory` for View rendering verification.
- **E2E**: Playwright for UI automation and validation.

---

**Audit Standard**: `BLUEPRINT_DOTNET_MVC_V2.0_HARDENED`
