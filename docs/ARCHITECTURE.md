# Architecture / Arquitetura pública

```text
Researcher's intention / Intenção humana
                |
       Conversational FPM Companion
     understand → orient → concretize
                |
  methods, alternatives and accessible tools
                |
      proposal or actual execution
                |
      evidence → scoped review → interpretation
                |
   researcher decision + optional short handoff
```

The **public Companion is a portable Markdown interaction layer**, not an installed AI backend. Its ability to search, read papers, run code or access data comes only from the AI service and tools actually available to the researcher. The optional Ising 2D source is local Python code with its own dependencies, not a computational service.

## Internal method ↔ public expression

FPM's **internal research and governance layer** is the authoritative source for ratified methodology. The public Companion is a curated translation of **generalizable, releasable** scientific lessons; it is not a mirror of private datasets, decisions, provenance bundles or the full internal Autoboot/Navigator/Research Kit.

Propagation is **incremental and reviewed**, not an automatic data feed: a relevant accepted internal lesson is assessed for generality, evidence, permissions and user-facing value, adapted to the smallest appropriate public file, then reviewed and published by the maintainer. Public feedback can suggest internal improvements but cannot automatically ratify a canonical decision. A small change should not trigger a full rebuild.

Responsibility remains separated: researcher authorizes and judges, Companion helps formulate and select, real tools produce evidence, checking assesses a defined claim and human acceptance remains explicit. Code output is not a substitute for empirical support.

Future tools may be integrated when scientifically useful and permitted; v0.2.0 does **not** implement agent orchestration, persistent memory, automatic discovery, self-updates or access to unpublished FPM custody.
