## 🤝 CONTRIBUTING.md - Contribution Guide

Welcome to the **CogniRank: The Socratic Sequence (Cognitive Rating)** project. Your contribution is key to defining the core value of human intelligence in the age of AI.

This project aims to deconstruct complex problems into 6 Layers and 20 Structured Cognitive Sets, establishing a quantifiable and learnable critical thinking model.

---

## 🎯 Our Commitment: Structured Contribution

To maintain the high quality and learnability of project data, all contributions must follow a strict structural process. We do not accept unstructured text or code fragments.

### 1. Code of Conduct

All contributors are expected to adhere to the [Code of Conduct Link] (Please replace with your link). We are committed to providing an open, welcoming, and inclusive community.

### 2. How to Get Started (Quick Start)

Before submitting any code or documentation, please familiarize yourself with the project's core structure:

1.  **Data Authority:** Carefully review `/schemas/01_CogniRank_Schema.json` to understand the detailed data structure of the **20 Sets (Z to R)**.
2.  **Methodology:** Understand the scoring dimensions (Depth, Consistency, Actionability) defined in `/docs/02_Scoring_Guide.md`.
3.  **Engineering Structure:** Refer to `/engineering/07_MVP_Workflow_Diagram.md` to understand the computational dependencies of the entire process.

---

## 🚀 Types of Contributions

We welcome contributions in the following three main areas:

### A. Conceptual & Documentation (Docs & Methodology)

If you are a thinker, analyst, or technical documentation expert:

| File/Folder | Focus Area | Submission Guidance |
| :--- | :--- | :--- |
| **`/docs` folder** | Cognitive depth, scoring, user experience | Optimize wording and ensure all documentation (e.g., `02_Scoring_Guide.md`) aligns with the latest engineering implementation. |
| **Case Study** | Practical application and validation | Submit new case studies conforming to the `/docs/03_Case_Study_Template.md` structure to enrich training data. |
| **Dependency Logic** | Dependency optimization | Challenge the logic within `/engineering/05_Dependency_Matrix.md` or `.csv`, proposing optimal inter-Set computational paths. |

**✅ Submission Steps:** Discuss your conceptual optimization for a specific Set > Fork > Modify the corresponding `.md` or `.csv` file > Submit a Pull Request.

### B. Engineering & API (Engineering & Code)

If you are a developer, architect, or MLOps engineer:

| Focus Area | Core Files | Submission Guidance |
| :--- | :--- | :--- |
| **Backend API** | `/engineering/08_Backend_API_Spec.md` | Implement or optimize the RESTful endpoints, especially the validation logic for `/submit_question`. |
| **LLM Orchestration** | `/engineering/10_Prompt_Template_Analysis.md` | Contribute code or process flows to execute the advanced LLM prompting strategies for complex Sets like G, H, P, and Q. |
| **Frontend/Visualization** | `/docs/11_Client_Display_Wireframe.md` | Implement or optimize frontend components (e.g., Radar Charts, Causal Loop Diagrams) and their data binding. |

**✅ Submission Steps:** Propose a solution for a specific engineering task in Issues > Fork > Write code > Ensure compliance with CI/CD checks (if applicable) > Submit a Pull Request.

### C. Architecture & Schema (Schema & Data Structure)

If you are a data scientist or architect:

* **Goal:** Ensure the JSON structures within the `/schemas` folder are maximally efficient and learnable.
* **Guidance:** Any change to a Set's fields (e.g., adding, removing, or renaming) must be thoroughly discussed in Issues, as it impacts the entire system's dependencies.

---

## 3. Pull Request (PR) Process

1.  **Fork** the repository and clone it locally.
2.  **Create a Branch:** Use a clear naming convention, e.g., `feature/add-set-g-validation` or `docs/fix-scoring-guide`.
3.  **Make Your Changes** and ensure all altered files follow the defined project structure.
4.  **Commit Standards:** Use concise and descriptive commit messages. We recommend the [Conventional Commits] (https://www.conventionalcommits.org/en/v1.0.0/) format (e.g., `feat: add new API endpoint for status query`).
5.  **Submit PR:**
    * **Title:** Briefly summarize your contribution.
    * **Description:** Reference the relevant Issue ID and explain in detail what your changes do and how they solve the problem or improve the project.
    * **Checklist:** Confirm that your changes do not break any existing schemas or dependencies.

Thank you for being part of the CogniRank community! We look forward to your profound insights and excellent contributions.