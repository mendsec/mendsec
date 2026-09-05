<div align="center">

# Fábio Mendes

**Cybersecurity Analyst · SysAdmin · Platform & Infrastructure Automation**

*Offensive & defensive security · Go / Python / Shell · Linux, Proxmox, DevSecOps*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mendsec)
[![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/mendsec)
[![Email](https://img.shields.io/badge/Email-3A76F0?style=for-the-badge&logo=mailfence&logoColor=white)](mailto:fabiomendes@mailfence.com)
[![CatNet](https://img.shields.io/badge/catnet--io-00875A?style=for-the-badge&logo=go&logoColor=white)](https://github.com/catnet-io)

![Profile Views](https://komarev.com/ghpvc/?username=mendsec&abbreviated=true&style=for-the-badge&color=00875A)

</div>

---

## About Me

Cybersecurity analyst with 10+ years across offensive and defensive work, systems
administration and IT management. I build and operate the boring, load-bearing parts of
security: hardened Linux fleets, endpoint protection rollouts, scanning tooling, and
CI/CD pipelines that fail loudly when something is wrong.

Most of my public code lives in three places: the **[catnet-io](https://github.com/catnet-io)**
scanning ecosystem (Go), infrastructure automation for **[MadeiraHackerSpace](https://github.com/MadeiraHackerSpace)**,
and security operations runbooks under **[@portosoft](https://github.com/portosoft)**.

- 🔭 **Currently building** — the `catnet-io` ecosystem: one Go scanning engine, many thin frontends
- 🛡️ **Day to day** — endpoint security (Kaspersky Security Center), Linux hardening, Proxmox, incident response
- 🎓 **Education** — Information Security & CyberDefense · postgraduate in Cybersecurity
- 🐧 **Daily drivers** — Pop!\_OS, Rocky Linux, Ubuntu, Void Linux
- 🧪 **Interests** — threat intelligence, malware analysis, DevSecOps, game development
- 📍 **Porto Velho, Rondônia — Brazil** · 🇧🇷 PT-BR / 🇺🇸 EN

---

## Skills

<div align="center">

![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-4EAA25?style=flat-square&logo=gnubash&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=c&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)

![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![Proxmox](https://img.shields.io/badge/Proxmox_VE-E57000?style=flat-square&logo=proxmox&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Oracle Cloud](https://img.shields.io/badge/Oracle_Cloud-F80000?style=flat-square&logo=oracle&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)

![Kaspersky Security Center](https://img.shields.io/badge/Kaspersky_Security_Center-006D5C?style=flat-square&logo=kaspersky&logoColor=white)
![Network Scanning](https://img.shields.io/badge/Network_Scanning-1A1A1A?style=flat-square&logo=wireshark&logoColor=white)
![Hardening](https://img.shields.io/badge/Linux_Hardening-2D2D2D?style=flat-square&logo=linuxfoundation&logoColor=white)
![DevSecOps](https://img.shields.io/badge/DevSecOps-7B2FBE?style=flat-square&logo=snyk&logoColor=white)
![CodeQL](https://img.shields.io/badge/CodeQL-2088FF?style=flat-square&logo=github&logoColor=white)
![Semgrep](https://img.shields.io/badge/Semgrep-1B2B34?style=flat-square&logo=semgrep&logoColor=white)

</div>

---

## Featured Projects

### 🐾 [catnet-io](https://github.com/catnet-io) · Go · MIT

Modular, event-driven network scanning ecosystem. Strict separation between scan logic and
frontends — every client is a thin, swappable consumer of the same engine
(`client-go` / `kubectl` / `k9s` pattern).

| Repo | Role | Release |
| :--- | :--- | :--- |
| [`engine`](https://github.com/catnet-io/engine) | Core scan logic — zero CGO, zero external deps, channel-based event API | ![](https://img.shields.io/github/v/release/catnet-io/engine?style=flat-square&label=) |
| [`catnet`](https://github.com/catnet-io/catnet) | CLI (Cobra) — [docs](https://catnet-io.github.io/catnet/) | ![](https://img.shields.io/github/v/release/catnet-io/catnet?style=flat-square&label=) |
| [`app`](https://github.com/catnet-io/app) | Desktop GUI (Wails + React) | ![](https://img.shields.io/github/v/release/catnet-io/app?style=flat-square&label=) |
| [`tui`](https://github.com/catnet-io/tui) | Terminal UI (Bubble Tea) — [docs](https://catnet-io.github.io/tui/) | ![](https://img.shields.io/github/v/release/catnet-io/tui?style=flat-square&label=) |

Distributed via [Homebrew tap](https://github.com/catnet-io/homebrew-tap) and
[Scoop bucket](https://github.com/catnet-io/scoop-bucket). Every repo runs `golangci-lint`,
`govulncheck` and branch-protection enforcement in CI.

---

### 🛡️ [ksc-deployment-runbook](https://github.com/portosoft/ksc-deployment-runbook) · Python/Shell · Apache-2.0

Deployment, automation and troubleshooting runbook for **Kaspersky Security Center 16.x** on
Linux and virtualized environments — pre-checks, guided install, compatibility matrix, and
recovery procedures drawn from real rollouts.

Pipeline: CodeQL · Semgrep · Aikido · integration CI.

---

### ☁️ [mhc-cloud-panel](https://github.com/MadeiraHackerSpace/mhc-cloud-panel) · Python · Proxmox VE

Multi-tenant SaaS control plane for VPS resale and infrastructure management on Proxmox VE —
customer VMs, billing, node scheduling and resource allocation. Runs the real cloud services
of MadeiraHackerSpace.

---

### 🏗️ [MadeiraHackerSpace/infra](https://github.com/MadeiraHackerSpace/infra) · Shell · GitOps

Homelab and community infrastructure managed as code, plus
[`status-bot`](https://github.com/MadeiraHackerSpace/status-bot) for service monitoring.

---

### 🎮 [Overloaded](https://auraonestudios.github.io/overloaded-game/) · [AuraOne Studios](https://github.com/AuraOneStudios)

Co-founder of a two-person indie studio. Top-down horde survivor for desktop browsers.
My side: studio ops and delivery infrastructure — bilingual EN/PT landing, GitHub Actions,
CodeQL, Dependabot. Everything outside 2D art and game design.

---

## Maintained Forks & Tools

Small fixes that solve real Linux desktop problems, kept in sync upstream:

- **[redragon-hs-companion](https://github.com/mendsec/redragon-hs-companion)** — corrects PCM channel desync on wireless Redragon headsets under PipeWire
- **[antigravity-ide-installer](https://github.com/mendsec/antigravity-ide-installer)** — installer/updater for Google Antigravity IDE on Ubuntu/Debian, with profile backup and safe rollback ([gist](https://gist.github.com/mendsec/81a91514d492c20311eb3805e2765ad2))
- **[xbrowsersync-app-community](https://github.com/mendsec/xbrowsersync-app-community)** — xBrowserSync with Manifest V3 fixes

---

## GitHub Stats

<div align="center">

![Stats](https://github-readme-stats.vercel.app/api?username=mendsec&show_icons=true&theme=github_dark&hide_border=true&include_all_commits=true&count_private=true)
![Streak](https://streak-stats.demolab.com?user=mendsec&theme=github-dark&hide_border=true)

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=mendsec&layout=compact&theme=github_dark&hide_border=true&langs_count=8&hide=html,css)

![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=mendsec&theme=github-compact&hide_border=true)

</div>

---

## Let's Connect

Open to **security & infrastructure discussions**, **open-source collaboration** on tooling
and DevOps, **indie game development**, and **mentorship** for people breaking into security
and systems engineering.

<div align="center">

**[LinkedIn](https://www.linkedin.com/in/mendsec) · [X](https://x.com/mendsec) · [fabiomendes@mailfence.com](mailto:fabiomendes@mailfence.com)**

*Ferramenta boa é a que falha alto e cedo.*

</div>
