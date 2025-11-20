# 06_Tooling_Plan - MVP Engineering Technology Selection and Planning

**Project Title:** CogniRank MVP (Minimum Viable Product)
**Objective:** Establish a backend service capable of receiving user questions, executing the 20-Set deconstruction flow, and returning a structured CogniRank report.

---

## I. AI/LLM Core Layer

This is the core computational engine of CogniRank, responsible for executing the cognitive deconstruction for all Sets.

| Component | Selection | Function | Notes |
| :--- | :--- | :--- | :--- |
| **Base LLM** | **Claude 3 Opus / GPT-4o** | Executes complex cognitive deconstruction ($\mathbf{G}, \mathbf{H}, \mathbf{P}, \mathbf{Q}$) and structured data output. | Requires strong Reasoning/Coherence capability and reliable JSON Mode output. |
| **Parallel Processing** | **LangChain / Custom Orchestrator** | Manages parallel (Layer 0, 1) and chained (Layer 3, 4) calls, adhering to $05\_Dependency\_Matrix$. | Needs optimization for latency and cost. |
| **Prompt Engineering** | **10\_Prompt\_Template\_Analysis** | Implements core prompt logic for each Set, ensuring output strictly follows $01\_CogniRank\_Schema$. | Requires integration of validation and retry mechanisms. |

---

## II. Backend Service Layer

Responsible for API routing, flow control, data processing, and interaction with the AI layer.

| Component | Selection | Function | Notes |
| :--- | :--- | :--- | :--- |
| **Main Framework** | **Python (FastAPI)** | Provides high-performance asynchronous API, facilitating easy integration with LLM APIs (typically Python SDK). | $08\_Backend\_API\_Spec$ will be written based on this framework. |
| **Flow Control** | **Queueing System (Redis/Celery)** | Handles time-consuming CogniRank deconstruction tasks to prevent API timeouts. | Essential for Sets requiring multi-turn iteration (e.g., G, H). |
| **Authentication** | **OAuth 2.0 / JWT** | Ensures only authorized users can initiate computation requests. | Foundation for billing and resource limits (Y Set). |

---

## III. Data/Storage Layer

Responsible for storing user data, computation results, and historical Set outputs.

| Component | Selection | Function | Notes |
| :--- | :--- | :--- | :--- |
| **Structured Data** | **PostgreSQL** | Stores user profiles, billing records, and structured data conforming to the **Analysis Output Schema** ($09$). | Strong JSONB support facilitates storing complex Set outputs. |
| **Caching** | **Redis** | Caches repetitive Set computation results or intermediate steps to reduce API costs and latency. | Improves computational efficiency, especially for time-sensitive Sets. |
| **Vector DB** | **Pinecone / Chroma** | Stores embeddings of historical questions and Set outputs, used to power $\mathbf{K}$ (Analogy) and $\mathbf{R}$ (Learning Set). | Enables self-evolution and refinement of the cognitive model. |

---

## IV. Frontend/User Interface Layer

Responsible for data presentation and user interaction.

| Component | Selection | Function | Notes |
| :--- | :--- | :--- | :--- |
| **Frontend Framework** | **React / Vue.js** | Quickly builds responsive, data-driven UI to display the complex report structure and meet $11\_Client\_Display\_Wireframe$ requirements. | UI development will focus on rendering data from the $09$ Schema. |
| **Visualization Library** | **D3.js / Echarts / React-Chartjs** | Implements complex charts like Radar Charts and Causal Diagrams suggested by $\mathbf{N}$ (Visualization Set). | Key task is transforming structured data from $09$ Schema into graphics defined by the $11$ Wireframe. |