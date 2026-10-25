# Example: safe local installation

With `PYTHONPATH=src` configured:

    python -m vibe_skills search completion
    python -m vibe_skills install --dry-run completion-claims-auditor
    python -m vibe_skills install completion-claims-auditor

After installation, editing the installed copy causes a later `update` to stop rather than overwrite the local modification. Remove only operates on skills recorded as installer-managed.

