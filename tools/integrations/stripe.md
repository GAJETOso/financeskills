# Stripe Integration Guide

Use Stripe for processing payments, managing subscriptions, and generating financial reports.

## 🏛️ Capabilities
- **Invoicing**: Create and send invoices to customers.
- **Reporting**: Export balance summaries and transaction logs.
- **Tax**: Calculate sales tax and VAT globally.

## 🔍 Common Operations
### List Balance Transactions
`GET /v1/balance_transactions`
Used for reconciling bank payouts with internal ledger entries.

### Create Customer
`POST /v1/customers`
Used when onboarding new clients during a contract setup.

## 🔗 Resources
- [Stripe API Reference](https://stripe.com/docs/api)
- [Stripe MCP Server](https://github.com/stripe/mcp-server)
