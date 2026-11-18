# ප්‍රාතිමෝක්ෂ අධ්‍යයනය — Pātimokkha Study

A study app for the 227 training rules of the Bhikkhu Pātimokkha, according to the Theravāda tradition only. It is available in Sinhala, English and Chinese (简体), with a Pāli source view for the Bhūtagāma vagga (Pācittiya 11–20).

Main sources: the Pācittiya Pāḷi, the Samantapāsādikā (Pācittiya commentary) and the Kaṅkhāvitaraṇī.

- **App:** `docs/` (served by GitHub Pages: Settings → Pages → Deploy from a branch → `main` / `docs`)
- **Content:** `content/*.txt`
- **Build:** `python3 zwj.py && python3 build.py && python3 assemble.py`
- **Pāli view:** `python3 tools/pi_build.py` (verbatim source cuts), then `python3 tools/pi_verify.py`
- **Notes for continuing the work:** `HANDOFF.md`
