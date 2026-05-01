# CLAUDE.md - FinanceSkills Rules

## Project Overview
FinanceSkills is a repository designed to enable AI agents to perform complex financial tasks with high precision and reliability.

## Style Guidelines
- **Financial Accuracy**: Always verify calculations using code (Python/Pandas) rather than mental math.
- **Data Privacy**: Never hardcode sensitive financial data. Use environment variables or mock data for examples.
- **Documentation**: Every skill must follow the `SKILL.md` template structure.

## Technical Standards
- **Python**: Use type hints for all financial functions.
- **Testing**: Include unit tests for any data transformation logic in `evals/` folders.
- **Formatting**: Use Black for Python formatting and Prettier for Markdown.

## Execution Rules
- Before executing a skill, perform the "Initial Assessment" defined in the `SKILL.md`.
- Report confidence levels if a financial inference is ambiguous.
