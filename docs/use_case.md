# Use Case: Acme Running Customer Service Chatbot

## Overview

The unifying use case across all curriculum exercises is a **customer service chatbot for Acme Running**, the premium sportswear and running shoe brand. Every topic and technique in this curriculum is taught in the context of building progressively more capable versions of this system.

The chatbot handles multi-turn customer conversations covering product enquiries, order management, quality complaints, technical support, and general customer service. This single domain is rich enough to exercise every AI engineering pattern in the curriculum, from basic LLM API calls through to multi-agent orchestration with human-in-the-loop escalation.

## Why This Use Case

- **Universally understood domain.** Everyone has interacted with customer support. No specialist knowledge is required to understand the problem space.
- **Naturally multi-faceted.** Five distinct issue categories require routing, classification, and specialised handling, which directly maps to orchestration patterns.
- **Requires retrieval.** Product catalogues, order databases, and policy documents create a natural need for RAG, knowledge graphs, and hybrid search.
- **Requires memory.** Multi-turn conversations where customers switch topics, provide incremental context, and reference earlier messages demand robust memory patterns.
- **Requires tools.** Looking up orders, searching products, checking inventory, and creating support tickets are natural tool-use scenarios.
- **Requires safety.** Handling PII (order numbers, addresses, payment info), staying on-topic, and preventing hallucinated product information are genuine guardrail concerns.
- **Requires evaluation.** Classification accuracy, response relevance, faithfulness to product data, and resolution rates are concrete, measurable metrics.
- **Implementation-agnostic.** The same business problem can be solved using static task decomposition (predefined pipelines), dynamic task decomposition (autonomous agents), or any hybrid approach, making it ideal for comparing different architectural patterns.

## The Business Problem

Acme Running receives customer enquiries across multiple channels. Customers contact support about a wide range of issues, often raising multiple topics within a single conversation. The chatbot must:

1. Understand what the customer is asking about.
2. Determine whether enough context has been provided to help.
3. Ask clarifying questions when information is missing.
4. Classify the issue to route it to the appropriate knowledge and tools.
5. Provide accurate, helpful responses grounded in Acme Running's actual product data and policies.
6. Recognise when an issue requires human escalation.

## Customer Issue Categories

### Product Information

Customers ask about shoe models, specifications, features, pricing, availability, sizing guidance, and product comparisons. Example questions:

- "What is the difference between the Stridewave 5 and Stridewave 6?"
- "Which Acme Running shoe is best for trail running?"
- "Do you have the Tempo Pro in size 10.5 in blue?"
- "What cushioning technology does the CloudSurge use?"

### Order Status

Customers enquire about existing orders, delivery tracking, shipping timeframes, order modifications, and cancellations. Example questions:

- "Where is my order AR-2024-78432?"
- "Can I change the delivery address on my recent order?"
- "How long does standard shipping take to Manchester?"
- "I want to cancel my order placed yesterday."

### Product Quality Issues

Customers report problems with purchased products, including defects, comfort issues, durability concerns, and warranty or return claims. Example questions:

- "My Stridewave 5s are causing blisters after only two runs."
- "The sole is separating from the upper after three months of use."
- "I received a pair with a manufacturing defect on the left shoe."
- "What is your warranty policy for running shoes?"

### Mobile App Support

Customers experience technical difficulties with Acme Running's mobile application, including crashes, login problems, authentication failures, and feature malfunctions. Example questions:

- "The app crashes every time I try to open my order history."
- "I cannot reset my password. The reset email never arrives."
- "The app is not syncing my running data with my account."
- "Which Android version is required for the latest app update?"

### General Enquiries

Questions that do not fall neatly into the above categories, including account management, return policies, company information, promotional offers, loyalty programmes, and general feedback. Example questions:

- "How do I join the Acme Running loyalty programme?"
- "What is your return policy for online purchases?"
- "Do you offer student discounts?"
- "I would like to provide feedback about my recent store visit."

## Domain Knowledge

The chatbot operates over the following knowledge domains:

### Product Catalogue

Acme Running's running shoe range, including models (Stridewave, Tempo Pro, CloudSurge, TrailGrip, Velocity Elite, etc.), specifications (weight, heel-to-toe drop, stack height, materials), proprietary technologies (AcmeWave energy plate, BounceFoam midsole, BreezeKnit upper, GripTech rubber outsole), available colourways, recommended use cases (daily training, racing, trail, stability), and pricing.

### Order and Shipping Data

Order records (order numbers in format AR-YYYY-NNNNN), order dates, item details, delivery estimates, tracking information, shipping partner details, and regional distribution centre status. Shipping policies including free shipping thresholds (e.g. free shipping on orders over $99), standard and express delivery timeframes by region.

### Company Policies

Return and exchange policies, warranty terms, refund procedures, loyalty programme rules and benefits, promotional offer terms, privacy policy, and data handling practices.

### Technical Documentation

Mobile app installation requirements, supported devices and OS versions, account creation and authentication procedures, troubleshooting guides for common app issues, and known issues with workarounds.

## Conversation Characteristics

Real customer service conversations have properties that make them challenging for AI systems:

- **Multi-turn context accumulation.** Customers provide information incrementally across multiple messages rather than in a single complete request.
- **Topic switching.** A customer might start asking about an order, then switch to a product question, then return to the order topic.
- **Ambiguity.** Messages like "it is not working" require clarification before the system can help.
- **Emotional context.** Frustrated customers with defective products require different handling than customers casually browsing products.
- **Implicit references.** "The same shoe but in blue" requires understanding what was previously discussed.
- **Variable resolution.** Some issues are resolved in one exchange; others require multiple rounds of clarification, tool lookups, and follow-up.

## Sample Customer Personas

### Alex (Product Researcher)

A recreational runner looking to upgrade from a competitor's shoe to Acme Running. Asks detailed questions about shoe specifications, comparisons between models, and sizing relative to other brands. Needs product information retrieval and recommendation logic.

### Sam (Order Tracker)

An existing customer who placed an order five days ago and wants to know when it will arrive. Provides an order number and expects the system to look it up and provide real-time status. Needs tool use (order lookup) and structured data retrieval.

### Jordan (Quality Complainant)

A loyal Acme Running customer whose recent purchase has a defect. Frustrated and expects a quick resolution. Needs empathetic handling, policy retrieval (warranty, returns), and potential human escalation for complex claims.

### Riley (App Troubleshooter)

A customer who cannot log into the Acme Running mobile app and has already tried basic troubleshooting. Needs technical documentation retrieval and step-by-step guidance. May require escalation if the issue is a known backend problem.

### Morgan (General Enquirer)

A new customer with broad questions about Acme Running's loyalty programme, return policy, and current promotions. Needs policy retrieval and clear, structured responses covering multiple topics.
