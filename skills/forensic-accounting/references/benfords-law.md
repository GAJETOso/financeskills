# Benford’s Law: Statistical Fraud Detection

A mathematical tool used by forensic accountants to detect manufactured or manipulated numbers in financial datasets.

## 🏛️ The Concept
Benford's Law (the First-Digit Law) states that in many naturally occurring collections of numbers, the leading significant digit is likely to be small.
- The digit **1** appears as the first digit about **30%** of the time.
- The digit **9** appears as the first digit less than **5%** of the time.

## 🔍 When to Apply
- **Accounts Payable**: Large datasets of vendor payments.
- **Inventory Counts**: Checking for "plug numbers."
- **Sales Data**: Identifying fabricated invoices.

**Warning**: Benford's Law does not work on datasets with assigned numbers (e.g., zip codes, phone numbers) or datasets with a narrow range (e.g., heights of humans).

---

## 🛠️ Interpretation
If a dataset significantly deviates from the Benford curve (e.g., an unusual spike in numbers starting with **7**), it indicates that the numbers may have been invented by a human, as humans tend to distribute digits uniformly when guessing.

## 🔗 Sources
- [Journal of Accountancy: Benford's Law and Fraud Detection](https://www.journalofaccountancy.com/issues/2017/apr/benfords-law-fraud-detection.html)
- [ACFE: Using Benford's Law in Fraud Examination](https://www.acfe.com/fraud-resources/benfords-law)
