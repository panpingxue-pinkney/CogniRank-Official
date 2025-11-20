# 07_MVP_Workflow_Diagram - MVP Workflow Diagram Description

**Project Title:** CogniRank MVP Execution Flow
**Purpose:** Describe the complete computational sequence of the CogniRank system from user input to final report output, strictly adhering to the dependencies defined in $05\_Dependency\_Matrix$.

---

## I. Workflow Stage Segmentation

The entire deconstruction process is divided into five main stages, corresponding to the computational dependencies of the Layers:

### Stage 1: Intent & Initial Framing
* **Input:** User Question.
* **Parallel Computation:**
    * **Layer 0:** Compute **Z** (Objective Clarity) and **Y** (Resource Constraints).
    * **Layer 1 (Foundation):** Initiate computation of **C** (Contextual Setting).
* **Output:** Foundational constraints and context.

### Stage 2: Core Framing & Complexity Analysis
* **Prerequisite:** Output of **Z** must be complete (Z -> A, B strong dependency).
* **Parallel Computation:**
    * **Layer 1 (Completion):** Compute **A** (Potential Assumptions) and **B** (Boundary Conditions).
    * **Layer 2 (Foundation):** Initiate computation of **D** (Concept Clarity) and **F** (Cross-Discipline Mapping).
* **Output:** Clear assumptions, boundaries, and initial concept definitions.

### Stage 3: Dynamic Layer Generation
* **Prerequisite:** Outputs of **A, B, D, E** must be complete (All strong dependencies for **G**).
* **Sequential Computation:**
    * First, compute **E** (Connectivity Network) [E depends on D].
    * **Layer 3 Core:** Utilize results from **A, B, D, E** to compute **G** (Mechanism Set).
    * Compute **H** (Feedback Loops) [H depends on G, E].
    * Compute **I** (Temporal Dimension) [I depends on G, H].
* **Output:** Core causal mechanisms, system dynamics, and temporal evolution.

### Stage 4: Insight & Meta-Cognition
* **Prerequisite:** Outputs of **G, I** must be complete.
* **Parallel Computation:**
    * **Layer 4:** Compute **J** (Perspective Set), **K** (Analogy Set), and **L** (Value Set).
    * **Layer 6 (Foundation):** Utilize results from **A}, \mathbf{J** to initiate computation of **P** (Meta-Cognition) and **Q** (Cognitive Bias).
* **Output:** Key insights, value proposition, and initial self-critique.

### Stage 5: Representation & Conclusion
* **Prerequisite:** Outputs of **G, L** must be complete.
* **Parallel Computation:**
    * **Layer 5:** Compute **M** (Model Set), **N** (Visualization Set), and **O** (Communication Set).
    * **Layer 6 (Completion):** Compute **R** (Learning Dynamics Set) and the **Final Score** (**I** - based on quality and weighted dependencies).
* **Output:** Structured Report ($03\_Template$), Final **I** Score.

---

## II. Diagram Code (Mermaid)

This code can be pasted into any Mermaid-supported editor to generate a clear flowchart.

```mermaid
graph TD
    subgraph A[Stage 1: Intent & Initial Framing]
        USER[User Question] --> Z(Z: Objective Clarity);
        USER --> Y(Y: Resource Constraints);
        Z --> A_PRE(Z-A, Z-B Strong Dependency);
        USER --> C(C: Contextual Setting);
        A_PRE --> B_INIT;
    end
    
    subgraph B[Stage 2: Core Framing & Complexity]
        B_INIT(Prerequisites Done);
        C --> D(D: Concept Clarity);
        C --> A(A: Potential Assumption);
        A --> E_PRE(A-E Strong Dependency);
        A_PRE --> B(B: Boundary Conditions);
        D --> E(E: Connectivity Network);
        C --> F(F: Cross-Discipline Mapping);
        B & D & E & A --> G_PRE(G Prerequisite Ready);
    end

    subgraph C[Stage 3: Dynamic Layer Generation]
        G_PRE --> G(G: Mechanism Set);
        G --> H(H: Feedback Loops);
        G & H --> I(I: Temporal Dimension);
        G --> J_PRE(G-J, G-L Dependencies Ready);
    end

    subgraph D[Stage 4: Insight & Meta-Cognition]
        J_PRE --> J(J: Perspective Set);
        F --> K(K: Analogy Set);
        G & I --> L(L: Value Set);
        A & J --> P(P: Meta-Cognition Set);
        A & J --> Q(Q: Cognitive Bias Set);
        L --> M_PRE(L-M, L-N, L-O Dependencies Ready);
    end
    
    subgraph E[Stage 5: Representation & Conclusion]
        M_PRE --> M(M: Model Set);
        M --> N(N: Visualization Set);
        L & M & N --> O(O: Communication Set);
        P & Q & O & L --> R(R: Learning Dynamics Set);
        R --> FINAL_SCORE{I: Final Score};
    end