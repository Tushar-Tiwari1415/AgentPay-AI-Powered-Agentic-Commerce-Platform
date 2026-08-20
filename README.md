# 🚀 AgentPay — AI-Powered Agentic Commerce Platform

AgentPay is an AI-powered agentic commerce platform that allows users to search, compare, and purchase products using natural-language conversations.

Instead of simply responding to user queries, AgentPay uses AI agents to understand user intent, discover products, compare prices, make recommendations, and execute commerce workflows through tools and APIs.

The platform is designed around the idea of **AI agents that can take actions**, while keeping users in control of sensitive financial operations.

---

## 🎯 Problem Statement

Traditional e-commerce requires users to manually:

1. Search for products
2. Compare different options
3. Check prices
4. Decide which product to purchase
5. Complete checkout and payment

AgentPay aims to simplify this workflow by allowing users to express their requirements naturally.

### Example

> "Find me the best laptop under ₹60,000 with 16GB RAM and good battery life."

The AI agent can:

- Understand the user's requirements
- Search available products
- Compare prices and specifications
- Recommend the best option
- Ask for user approval
- Initiate the payment
- Verify the payment
- Confirm the order

---

## 🧠 System Architecture

```text
                         USER
                           |
                           v
                  +----------------+
                  |   AI Planner   |
                  +----------------+
                           |
                           v
              +-------------------------+
              |   Agent Orchestrator    |
              |       LangGraph         |
              +-------------------------+
                    /     |      \
                   /      |       \
                  v       v        v
          +---------+ +---------+ +-------------+
          | Product | | Compare | |Recommendation|
          |  Agent  | |  Agent  | |    Agent    |
          +---------+ +---------+ +-------------+
                  \      |       /
                   \     |      /
                    v    v     v
                 +----------------+
                 | User Approval  |
                 +----------------+
                         |
                         v
                 +----------------+
                 | Payment Agent  |
                 +----------------+
                         |
                         v
                  Razorpay API
                         |
                         v
                      Webhook
                         |
                         v
                Payment Verification
                         |
                         v
                  Order Confirmation
