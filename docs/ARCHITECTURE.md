# Public architecture / Arquitetura pública

## One project, progressive levels of use

```text
Researcher / pesquisador
    |
    +-- Public documentation (available now)
    |      +-- README and guided first conversation
    |      +-- method, limitations, release roadmap
    |
    +-- Portable Autoboot (planned; not released)
    |      +-- minimal plain-text starting context
    |      +-- optional skills, loaded as required
    |
    +-- Browser Navigator (planned; not released)
    |      +-- offline interactive guidance
    |      +-- illustrative educational simulations
    |
    +-- Research Kit (planned; not released)
           +-- templates and schemas
           +-- optional code and validation tools
```

The intended architecture separates **conversation and planning**, **scientific execution**, and **evidence/provenance**. The public repository currently contains only the documentation tier. It is neither an autonomous runtime nor a cloud compute service.

A future Autoboot is intended to remain usable as plain text on services without native agent-skill support. Reading an instruction file does not give an AI internet access, persistent memory, compute tools or authority over external actions.

## Custody and authorization boundaries

- **Public distribution:** selected and reviewed documentation, followed by independently tested downloadable releases.
- **Scientific workspaces:** research-specific assumptions, code, data, decisions and records under their owners' control.
- **Private development/custody:** historical scientific evidence and unreleased artifacts, not imported here by default.

Public research case studies and reproducibility packages require independent rights and validation reviews. Version labels and file hashes identify artifacts; they do not, by themselves, establish scientific validity or human approval.
