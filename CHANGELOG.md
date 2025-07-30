# CHANGELOG.md

Offline Feedback Collector  
This document logs all meaningful code changes, grouped by semantic version and date.

---

## v0.1.0

### 2025-07-30
- Created README.md to describe the project
- Wrote AGENT.md to define the app's role and AI behavior rules
- Defined rules for semantic versioning, changelog, and version.json
- Added structure for changelog roadmap


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

This list will expand or shift as the project evolves.