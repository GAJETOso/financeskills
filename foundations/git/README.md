# Git for Financial Models

Financial models are code. Versioning them correctly is essential for auditability and collaboration.

## 🌿 Branching Strategy
- **main**: Production-ready models and skills.
- **develop**: Integration branch for new features.
- **feature/**: Specific model improvements or new data pipelines.
- **audit/**: Static branches representing a snapshot of a model during a specific audit period.

## 🔍 Commit Guidelines
Use Conventional Commits to make the history readable for both humans and AI:
- `feat`: New skill or model logic.
- `fix`: Correcting a formula or data bug.
- `docs`: Updates to SKILL.md or README.
- `refactor`: Improving code structure without changing output.

## 🛡️ Avoiding "Big Binary" Issues
- **Large Datasets**: Do not commit large CSV or Excel files. Use `.gitignore` and store data in a cloud bucket or local `data/` folder (ignored).
- **Notebooks**: Use `nbstripout` or similar tools to clear Jupyter Notebook outputs before committing to avoid massive diffs.

## 📝 Example: Git Workflow for an Audit
```bash
# Create a dedicated audit branch
git checkout -b audit/2023-q4-reporting

# Tag the snapshot
git tag -a v2023.4.0 -m "Finalized model for Q4 2023 audit"

# Push to remote
git push origin audit/2023-q4-reporting --tags
```
