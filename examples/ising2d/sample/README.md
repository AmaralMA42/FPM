# Exploratory Ising outputs / Saídas exploratórias

These files are retained from a **local exploratory quick run on 2026-11-04**, executed before this distribution was prepared. They are provided to make the example inspectable without requiring the visitor to install Python.

- `magnetization.png`: finite-size mean absolute magnetization versus temperature; dashed line is the exact **infinite-size** Tc reference, not a fit.
- `snapshot_T*.png`: three single-replica spin snapshots, not independent evidence of a phase transition.
- `replicas.csv`, `summary.csv`: recorded finite-size samples and averages, with the original grouping/replica logic.
- `metadata.json`: program configuration, seeds and environment of the recorded execution.

**Not shown:** robust critical uncertainty, independent scientific reproduction, finite-size extrapolation, production simulation results. The snapshots/plots are not claims that an AI ran code in the viewer's current chat. Run `ising2d.py` locally to generate a fresh result, if needed.

---

Arquivos preservados de uma execução local exploratória em 04/11/2026. Os gráficos e CSVs **não** estimam Tc com precisão nem foram produzidos na conversa de quem estiver usando o Companion. O arquivo de metadados informa a origem e o protocolo.
