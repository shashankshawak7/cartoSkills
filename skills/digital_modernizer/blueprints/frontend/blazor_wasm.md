# Blueprint: Blazor WebAssembly (v2.0)

This blueprint defines the enterprise-hardened transformation for Blazor WASM targets.

---

## 🏗️ 1. Architecture
- **Pattern**: Component-Driven C# (WebAssembly).
- **Communication**: HttpClient (JSON/REST), SignalR (Real-time).
- **Security**: MSAL / OIDC (Azure AD/Auth0).

---

## 📂 2. Directory Structure
```text
Skillai.{Project}.Client/
  ├── Pages/               # Routable Razor Components
  ├── Shared/              # Layouts & NavMenu
  ├── Components/          # Reusable UI Components
  ├── Services/            # Business Logic & API Clients
  ├── wwwroot/             # Static Assets & index.html
  ├── Program.cs          # Pipeline & Dependency Injection
  └── {Project}.Client.csproj
```

---

## 📦 3. Dependency Manifest (.csproj)
- **Framework**: `Microsoft.AspNetCore.Components.WebAssembly`.
- **UI**: `MudBlazor` or `Radzen.Blazor`.
- **Logic**: `Microsoft.Extensions.Http`, `Blazored.LocalStorage`.
- **Testing**: `bUnit`, `xUnit`, `Moq`.

---

## 🧬 4. Logic Mapping Patterns
- **Legacy UI Events** ➜ Use **C# EventHandlers (@onclick, @onchange)**.
- **Legacy State Mapping** ➜ Use **Scoped Services / State Container**.
- **Legacy UI Controls** ➜ Use **MudBlazor / Fluent UI components**.

---

## 🧪 5. Testing Protocol
- **Unit**: bUnit for Component rendering and state flow.
- **Service**: xUnit for API client logic.
- **E2E**: Playwright for full WASM execution validation.

---

**Audit Standard**: `BLUEPRINT_BLAZOR_V2.0_HARDENED`
