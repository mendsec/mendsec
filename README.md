# Fábio Mendes

**Security-focused ServiceOps Engineer** & **Indie Game Co-Founder** · Sysadmin & Dev in Go/Python/C · Building automated infrastructure with Proxmox, Odoo, Docker & CI/CD

---

## About Me

Security-oriented systems engineer with a background in infrastructure automation, cybersecurity, and full-stack development. I design and implement scalable, secure service delivery platforms that bridge sysadmin expertise with modern software engineering practices.

Since 2026 I've also co-founded **AuraOne Studios**, a two-person indie game studio, handling studio operations and delivery infrastructure alongside my core security and platform engineering work.

My technical work centers on:

- **Infrastructure Automation**: Proxmox, Docker, CI/CD pipelines, Odoo-based service delivery platforms
- **Cybersecurity**: Network scanning, vulnerability assessment, hardening, defense strategies
- **Systems Engineering**: Event-driven architecture, modular CLI/GUI/TUI ecosystems in Go
- **Game Development**: Studio operations, web/landing infrastructure, bilingual product delivery
- **Polyglot Development**: Go, Python, C, TypeScript, Shell

I contribute actively to open-source projects and lead initiatives at **MadeiraHackerSpace**, balancing hands-on coding with strategic architecture decisions.

---

## Flagship Projects

### [**catnet**](https://github.com/catnet-io) · Go · Security

A modular, event-driven network scanning ecosystem built for security professionals, reorganized in 2026 into its own [`catnet-io`](https://github.com/catnet-io) organization following the `client-go` / `kubectl` / `k9s` architecture pattern:

| Component | Role |
| --- | --- |
| [`engine`](https://github.com/catnet-io/engine) | Core scan logic — zero CGO, zero external deps, channel-based event API |
| [`catnet`](https://github.com/catnet-io/catnet) | CLI consumer of the engine |
| [`app`](https://github.com/catnet-io/app) | Wails + React desktop GUI |
| [`tui`](https://github.com/catnet-io/tui) | Terminal UI, currently in active development |

**Why it matters**: strict separation between scan logic and frontends means every client — CLI, desktop, terminal, eventually mobile — stays a thin, swappable consumer of the same engine.

---

### [**Overloaded**](https://auraonestudios.github.io/overloaded-game) · Construct 3 · AuraOne Studios

Co-founder of **AuraOne Studios**, a two-person indie game studio. *Overloaded* is our first release — a top-down horde survivor for desktop browsers, starring Lizzie (melee/mobility) and Archie (robot support companion).

**My role**: studio administration, web/landing infrastructure (bilingual EN/PT, CI/CD via GitHub Actions, CodeQL, Dependabot), and everything outside 2D art and game design.

---

### [**mhc-cloud-panel**](https://github.com/MadeiraHackerSpace/mhc-cloud-panel) · Python/Proxmox

Multi-tenant SaaS platform for VPS resale and infrastructure management, built on Proxmox VE — enabling MSPs to manage customer VMs, billing, and resource allocation through a unified control plane.

**Impact**: powers real infrastructure management for MadeiraHackerSpace's cloud services.

---

### [**odoo-serviceops**](https://github.com/mendsec/odoo-serviceops) · Odoo/Shell/Python

Enterprise service delivery platform combining Odoo Community with automation for IT service companies — Docker containerization, CI/CD integration, and custom service-ops modules.

---

## Technical Skills

| Category | Technologies |
| --- | --- |
| **Languages** | Go, Python, TypeScript, C, Shell/Bash |
| **Infrastructure** | Proxmox VE, Docker, CI/CD (GitHub Actions, GitLab CI) |
| **Platforms** | Odoo ERP, Linux, PostgreSQL, Redis |
| **Security** | Network scanning, vulnerability assessment, hardening, secure API design |
| **Game Dev / Web** | Construct 3, bilingual product delivery, static site CI/CD |

---

## Current Focus (2026)

- Stabilizing the `catnet-io` ecosystem — aligning `engine`, `catnet`, `app`, and `tui` release versions and CHANGELOGs
- Shipping *Overloaded* and building out AuraOne Studios' web presence
- Hardening multi-tenant infrastructure security models
- Mentoring junior engineers in systems thinking and secure development

---

## Let's Connect

Open to:

- **Security & infrastructure discussions** – networks, hardening, threat modeling
- **Open-source collaboration** – infrastructure tooling, security, and DevOps
- **Indie game development** – small-team production, web/landing delivery
- **Mentorship** – helping others break into security and systems engineering

**Contact:**

- X: [@mendsec](https://x.com/mendsec)
- LinkedIn: [in/mendsec](https://www.linkedin.com/in/mendsec)
- Email: fabiomendes@mailfence.com

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=mendsec&show_icons=true&theme=dark&hide_border=true" alt="GitHub Stats" />
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=mendsec&layout=compact&theme=dark&hide_border=true" alt="Top Languages" />
</p>
