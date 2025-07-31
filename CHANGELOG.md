# CHANGELOG.md

Offline Feedback Collector
This document logs all meaningful code changes, grouped by semantic version and date.

---

## [v0.3.1] 2025-07-31

### Fixed
- Pointed templates to compiled CSS instead of SCSS
- Added static file serving in development via `core.urls`

## [v0.3.2] 2025-07-31

### Fixed
- Corrected sidebar markup and overlay for responsive layout

## [v0.3.3] 2025-07-31

### Fixed
- Sidebar stretches full page height and collapses uniformly

## [v0.3.0] 2025-07-30

### Added
- Extracted and integrated Yuri theme’s `static/` and `templates/` into project  
- Configured Docker Compose with Django web service and PostgreSQL database  
- Moved `SECRET_KEY` and database credentials into `.env`, loaded via `python-dotenv`  
- Enabled version-driven `DEBUG` flag by reading `environment` from `version.json`  
- Switched from SQLite to PostgreSQL in `settings.py` using env vars  
- Created `users` app with custom `EmailUser` model (email-based authentication)  
- Built full registration flow:  
  - `RegistrationForm`, `RegisterView`, `/register/` route  
  - `register.html` template extending `base-other-page.html` with themed card layout  
- Built full login flow:  
  - `UserLoginView`, `/login/` route  
  - `login.html` template matching theme styling
- Introduced `base-public.html` layout for all public‐facing pages (navbar with logo, login/register links, and footer)  
- Created `landing.html` extending `base-public.html`  
  - Built Hero section with headline, subtext, and “Get Started” / “Login” CTAs  
- Updated `core/urls.py` to route `/` to `landing.html`  
- Added “How It Works” section (three steps: Generate QR, Scan & Respond, View Insights)  
- Integrated Feather icons correctly:  
  - Included `feather.min.js` and `feather-icon.js` in `base-public.html`  
  - Initialized with `feather.replace()`  
  - Applied `text-primary` class for visible icon color on light background
- Added subscription auto expire middleware

### Fixed
- JS code for bootstrap to call from official link
- Bootstrap code in Landing to fix icon colors


## 🧭 Build RoadMap

This section maps the full project journey — all core components we plan to build or refine, written as sequential goals.

- Set up a clean public Django project with versioning and changelog rules
- Integrate a downloaded Bootstrap 5 theme into Django templates
- Create models for Business, Branch, and Feedback
- Build public feedback form (mobile-first, QR-linked)
- Implement QR code generation logic and store QR per branch
- Add Django admin customization for business owners and branch managers
- Implement login/logout and permission-based dashboard views
- Build dashboard UI for viewing feedback entries
- Add basic stats summary (e.g., satisfaction average, counts)
- Implement CSV export for feedback entries
- Style dashboard using Bootstrap components
- Create a simple printable flyer view with QR and instructions
- Finalize clean UX for feedback form and thank-you screen
- Add project metadata via version.json
- Document versioning, agent behavior, and changelog rules
- Containerize the app with Docker (planned)
- Add a read-only `/version/` endpoint (planned)
- Add JWT token handling (Hybrid, keep it stateful)
- Add Password Reset

This list will expand or shift as the project evolves.