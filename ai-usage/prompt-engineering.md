# Prompt Engineering for Finance

Effective financial analysis with AI requires precise prompting to ensure numerical accuracy and logical consistency.

## 🏗️ The "S-C-R" Framework
- **Situation**: Define the financial context (e.g., "I am analyzing a Q3 Earnings Report").
- **Constraint**: Set boundaries (e.g., "Use only the attached PDF data", "Format as a table").
- **Requirement**: Specific task (e.g., "Calculate the Debt-to-Equity ratio").

## 💡 Pro-Tips
1.  **Chain-of-Thought**: Always ask the AI to "Show your work step-by-step" to catch calculation errors.
2.  **Role Prompting**: "Act as a Senior Investment Analyst with 20 years of experience in the Fintech sector."
3.  **Few-Shotting**: Provide examples of how you want the data formatted.

## 🚫 Common Pitfalls
- **Hallucinations**: AI may make up numbers if it doesn't find them in the source. Always verify with Python.
- **Ambiguity**: Avoid "Tell me about this company". Use "Extract the Net Interest Margin for the last 4 quarters".
