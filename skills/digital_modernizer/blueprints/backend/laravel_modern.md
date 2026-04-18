# Blueprint: Laravel Modern (v2.0)

This blueprint defines the enterprise-hardened transformation for Laravel targets.

---

## 🏗️ 1. Architecture
- **Pattern**: MVC (Model-View-Controller) with Service-Repository pattern.
- **Layers**: Controllers (Web/API), Services (Logic), Repositories (Eloquent), Models (Data).
- **Communication**: REST API, Livewire (Fullstack), Sockets (Pusher/Echo).

---

## 📂 2. Directory Structure
```text
project_root/
  ├── app/
  │   ├── Http/Controllers/  # Web/API handlers
  │   ├── Services/         # Business Logic
  │   ├── Repositories/     # Eloquent / DB Logic
  │   ├── Models/           # Database Entities
  │   └── Providers/        # Dependency Injection
  ├── routes/               # api.php, web.php
  ├── resources/            # Views (Blade/Livewire)
  └── composer.json         # Dependencies
```

---

## 📦 3. Dependency Manifest (composer.json)
- **Framework**: `laravel/framework`, `laravel/sanctum`, `laravel/tinker`.
- **Logic**: `spatie/laravel-permission`, `barryvdh/laravel-debugbar`.
- **Testing**: `pestphp/pest`, `orchestra/testbench`, `fakerphp/faker`.

---

## 🧬 4. Logic Mapping Patterns
- **Legacy Temp-Tables** ➜ Use **Laravel Collections** or **Temporal Models**.
- **Legacy Triggers** ➜ Use **Eloquent Observers** or **Laravel Events**.
- **Legacy Pointers** ➜ Use **PHP Objects (Pass-by-ref)**.

---

## 🧪 5. Testing Protocol
- **Unit**: Pest/PHPUnit for Service logic. 100% path coverage.
- **Feature**: End-to-end HTTP request/response validation.
- **Browser**: Laravel Dusk for frontend interaction.

---

**Audit Standard**: `BLUEPRINT_LARAVEL_V2.0_HARDENED`
