# Architecture / Arquitetura pública

```text
Researcher's idea or technical question / Ideia do pesquisador
                       |
             Conversational FPM Companion
             understand → orient → concretize
                       |
       suitable methods + available AI tools
                       |
      plan or execution → actual evidence → interpretation
                       |
        human decision + optional short handoff
```

The **public starter is a Markdown interaction layer**, independent of model vendor. It can be used in a general AI chat. It neither executes code nor installs external agents by itself. It does not provide persistent memory, browsing, credentials, literature or computing resources.

The Ising source is **optional local Python code** with its own dependencies. It is a scientific teaching example, not an AI backend. The full internal FPM governance, research custody, advanced Autoboot, Navigator and Research Kit are **not distributed**.

Separation of concerns: the researcher defines the scientific goal and authorizes actions; the Companion helps interpret, design and route work; real tools produce data; external controls and researcher review evaluate claims. Research data and source publications remain in their own repositories under appropriate authorization.

The FPM Project may in the future adapt external open-source research tools. The v0.1 starter does **not** implement self-updating discovery or automatic tool installation. Scope and rights for future components will be decided separately.
