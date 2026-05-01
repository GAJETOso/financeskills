# Project: AI-Powered Finance Assistant

## Overview
A conversational interface that allows users to query their financial data using natural language. It leverages the `financial-analysis` skill and `python` foundations to provide real-time insights.

## Architecture
1.  **Frontend**: Streamlit or Next.js UI for chat.
2.  **Orchestrator**: LangChain or LlamaIndex to route queries.
3.  **Engine**: OpenAI GPT-4o or Claude 3.5 Sonnet.
4.  **Tools**: Custom Python functions for calculating KPIs and fetching market data.

## Features
- "What was our net margin in Q2?"
- "Compare our R&D spend to our top 3 competitors."
- "Alert me if our cash-on-hand drops below 3 months of runway."

## Getting Started
1.  Install dependencies: `pip install -r requirements.txt`
2.  Set API keys in `.env`.
3.  Run the app: `streamlit run app.py`
