# Blueprint: Ruby on Rails (v2.0)

This blueprint defines the enterprise-hardened transformation for Ruby on Rails targets.

---

## 🏗️ 1. Architecture
- **Pattern**: MVC (Model-View-Controller) with Active Record.
- **Layers**: Models (Data/Logic), Controllers (Web/API), Views (HTML/JSON), Services (Complex Logic).
- **Communication**: REST API (jbuilder), Hotwire (Turbo/Stimulus), Sidekiq (Async).

---

## 📂 2. Directory Structure
```text
project_root/
  ├── app/
  │   ├── controllers/      # Web/API handlers
  │   ├── models/           # Data & Logic
  │   ├── services/         # Business transformation
  │   ├── jobs/             # Sidekiq/ActiveJob
  │   └── views/            # Turbo/ERB templates
  ├── config/               # Settings & Initializers
  ├── db/                   # Migrations & Seeds
  └── Gemfile               # Dependencies
```

---

## 📦 3. Dependency Manifest (Gemfile)
- **Framework**: `rails`, `pg`, `redis`.
- **Logic**: `sidekiq`, `devise`, `pundit`.
- **Testing**: `rspec-rails`, `factory_bot_rails`, `capybara`, `simplecov`.

---

## 🧬 4. Logic Mapping Patterns
- **Legacy Database Cursors** ➜ Use **Active Record Scopes / Batches**.
- **Legacy Triggers** ➜ Use **Active Record Callbacks**.
- **Legacy GOTO** ➜ Use **Ruby Private Methods / Modules**.

---

## 🧪 5. Testing Protocol
- **Unit**: RSpec for Models and Services. 100% path coverage.
- **Request**: Controller-level integration tests.
- **System**: Capybara for full user interaction.

---

**Audit Standard**: `BLUEPRINT_RAILS_V2.0_HARDENED`
