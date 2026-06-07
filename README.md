<div align="center">

# Fábio Mendes · `mendsec`

**Security Engineer · Offensive & Defensive**

_Building the tools that find gaps. Running the systems that close them._

[![X (Twitter)](https://img.shields.io/badge/@mendsec-%23000000.svg?style=flat&logo=x&logoColor=white)](https://x.com/mendsec)
[![LinkedIn](https://img.shields.io/badge/in%2Fmendsec-%230A66C2.svg?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mendsec)
[![Email](https://img.shields.io/badge/fabiomendes@mailfence.com-%23009688.svg?style=flat&logo=minutemailer&logoColor=white)](mailto:fabiomendes@mailfence.com)
[![GitHub followers](https://img.shields.io/github/followers/mendsec?style=flat&label=Followers&color=555)](https://github.com/mendsec?tab=followers)

RO · Brazil · UTC −04:00

</div>

---

## What I do

I work across both sides of the security boundary. On the offensive side, I build tooling and run assessments — network enumeration, protocol analysis, red team infrastructure. On the defensive side, I design and operate hardened multi-tenant platforms in production.

That dual exposure isn't incidental. Understanding how systems fail under adversarial pressure is what makes me a better architect — and running real infrastructure is what keeps my threat model grounded.

I write primarily in **Go** and Python. I care about correctness, auditability, and operational reproducibility.

---

## Work

### [`catnet`](https://github.com/mendsec/catnet) — Network Scanner (Go)

A concurrent network scanner built for real engagements. Refactored from the ground up in Go: zero external dependencies in the core engine, context-based cancellation, race-detector-clean, and a scriptable CLI consumer. Designed to be extended, not just used.

> Concurrent scanning · Custom protocol handling · Clean architecture · CI with govulncheck

---

### [`mhc-cloud-panel`](https://github.com/MadeiraHackerSpace/mhc-cloud-panel) — Multi-tenant Cloud Panel (Python)

VPS provisioning and management platform built on the Proxmox VE API. Handles VM lifecycle, resource isolation, billing, and customer boundaries in a unified control plane. In production at MadeiraHackerSpace.

> Proxmox VE · PostgreSQL · REST API · Multi-tenancy · Isolation boundaries

---

### [`odoo-serviceops`](https://github.com/mendsec/odoo-serviceops) — Hardened ERP Infrastructure (Shell / Docker)

Infrastructure-as-code approach to running Odoo Community as a security-conscious service. Automated deployment, update pipelines, backup orchestration, and hardening applied end-to-end — treating ERP like the attack surface it is.

> Docker · CI/CD · Ansible · Privilege separation · Reproducible deployments

---

## Technical profile

| Domain | Detail |
|---|---|
| **Offensive** | Network scanning, enumeration, red team infrastructure |
| **Defensive** | Hardening, secure architecture, threat modelling, IaC auditing |
| **Languages** | Go · Python · Shell · C · Lua · JavaScript |
| **Infrastructure** | Linux · Proxmox VE · Docker · Ansible · GitHub Actions |
| **Platforms** | PostgreSQL · Nginx · Redis · Odoo · Self-hosted services |

---

## Currently

- Extending `catnet` with additional protocol coverage and evasion-aware scanning
- Hardening isolation and privilege separation in multi-tenant environments
- Improving observability and incident response posture for self-hosted platforms
- Contributing to Proxmox tooling and security automation open-source

---

<div align="center">

Active at [MadeiraHackerSpace](https://github.com/MadeiraHackerSpace) and [Portosoft](https://github.com/portosoft).

_Last updated: June 2026_

</div>
