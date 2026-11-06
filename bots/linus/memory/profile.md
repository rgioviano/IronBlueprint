# About the user

<!-- Enduring facts: who the user is, how to address them, lasting preferences.
     Kept in mind every turn. Safe to read, grep, and edit.
     One fact per line, as "- (YYYY-MM-DD) <fact>". -->
- (2026-08-25) The user's name is Ryne Gioviano
- (2026-08-25) Wants the assistant as a high-level expert full-stack software engineer covering products, apps, backends, frontends, infra, architecture, reviews, debugging, and hardware when it comes up
- (2026-08-25) Prefers skip-the-ceremony, figure-it-out, ship-it style with no fluff
- (2026-08-25) Uses a NVIDIA DGX Spark
- (2026-08-25) Ryne has an NVIDIA DGX Spark and is evaluating SGLang for running models on it.
- (2026-08-25) Ryne is non-technical and learning engineering. Explain concepts in simple pieces. He wants to download models onto the DGX Spark and run them locally from disk, not stream them from the cloud.
- (2026-08-25) Ryne’s daily Mac is 8 GB RAM and often hits memory pressure (heavy swap). Brave left open for days is a common hog. DGX Spark is a separate machine and does not use the Mac’s RAM.
- (2026-09-03) In the IronBlueprint group, Ryne wants messages only when they contain something important; otherwise remain silent.
- (2026-09-04) Ryne wants IronBlueprint meeting summaries (including his action items) and Web & Mobile Tasks additions formatted as bulleted lists.
- (2026-09-04) Engineer also owns the former Grok Build lane: for heavy apps, code, and deep research on the agent computer, use the real `grok` CLI (`grok update` first when a real job needs it; default `--effort medium`; never pin a model unless Ryne names one; keep auto-update on). No Daily Grok Build self-improve routine - never recreate it.
- (2026-09-04) Local IronBlueprint Nexus path on Ryne’s Mac: /Users/rynegioviano/Projects/IronBlueprint (GitHub IronBluePrint/nexus-ai-agent).
- (2026-09-07) Ryne downloads models to an external hard drive first, then transfers them to the DGX Spark when home. He is often away from the Spark when planning setup.
- (2026-09-07) For NVIDIA Nemotron 3.5 Lightning 30B-A3B on Ryne’s DGX Spark, always use the MiaAI Lab recipe https://github.com/MiaAI-Lab/Nemotron3.5-Lightning-DGX-Spark-RTX-5090-6000-PRO (SGLang + DSpark, ./start.sh) - not the plain vLLM docker serve that was previously on :8000.
