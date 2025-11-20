# 05_Dependency_Matrix.md – Dependency Matrix Explanation

**File Name:** 05_Dependency_Matrix.csv  
**Purpose:** Defines the computational prerequisite dependencies between the 20 cognitive dimensions (Sets) in CogniRank.

---

## I. Coding Rules

The values in the matrix indicate the dependency strength of the **Row Set** on the **Column Set**.

| Value | Strength | Meaning |
| :--- | :--- | :--- |
| **0** | None | No direct relationship, can be computed independently. |
| **1** | Weak | Optimizing input; improves Quality Q(Si). |
| **2** | Strong | Required prerequisite; computation fails if incomplete. |

---

## II. Key Dependency Logic Explanation

### 1. Core Engine — G (Mechanism Set)
G is the central computational driver of CogniRank.  
It must be calculated only after the Framing Layer stabilizes.  
Therefore, **G depends on A (Assumption), B (Boundary), D (Definitional), and E (Connectivity)** with a value of **2 (Strong Dependency)**.

### 2. Intent Layer — Z’s Restriction on Framing
Z (Objective Set) dictates the scope and depth of thinking.  
If the objective is unclear, A (Assumption) and B (Boundary) cannot be defined.  
Thus, Z’s influence on A and B is a **2 (Strong Dependency)**.

### 3. Representation Layer Depends on Insight
M, N, and O (Model, Visualization, Communication) depend on core insights such as L (Value) and G (Mechanism).  
These dependencies are **1 (Weak)** or **2 (Strong)** depending on complexity.

### 4. Meta Layer — Self-Critique
P and Q (Meta-Cognition and Bias Sets) require critique of **established Framing (A)** and **discovered Perspectives (J)**.  
Therefore, they depend on A and J with values **1 or 2**.