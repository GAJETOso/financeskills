# Plaid Integration Guide

Use Plaid to securely connect to bank accounts, fetch transaction history, and verify identity.

## 🏛️ Capabilities
- **Transactions**: Retrieve historical bank transactions for reconciliation.
- **Identity**: Verify account owner information (KYC/KYB).
- **Balance**: Check real-time balances to prevent NSF (Non-Sufficient Funds).

## 🔍 Common Operations
### Get Transactions
`POST /transactions/get`
Used for automated reconciliation and cash flow analysis.

### Get Identity
`POST /identity/get`
Used for auditing customer or vendor bank details.

## 🔗 Resources
- [Plaid API Documentation](https://plaid.com/docs/api/)
