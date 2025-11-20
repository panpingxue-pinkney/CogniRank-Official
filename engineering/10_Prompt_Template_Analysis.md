# 10_Prompt_Template_Analysis - Core Prompt Template Analysis

**Purpose:** Define high-level prompting strategies and instructions for the Sets (G, H, P, Q) requiring deep cognitive deconstruction in the CogniRank process.

---

## I. General Prompt Structure

All Set prompts must include the following five core sections to ensure LLM output reliability and structure:

1.  **Role Assignment:** Set the LLM role as a "Cognitive Deconstruction Expert" or "Critical Thinking Analyst."
2.  **Input Data:** Explicitly provide the output results of prerequisite Sets (as required by $05\_Dependency\_Matrix$).
3.  **Core Instruction:** State specific analysis tasks and constraints based on the current Set's objective (e.g., "Must identify non-obvious causal chains").
4.  **Output Format:** Mandate the LLM output **strictly adheres** to the corresponding Set's JSON structure in $01\_CogniRank\_Schema$.
5.  **Evaluation Criteria:** Remind the LLM to reference the criteria in $02\_Scoring\_Guide$ (e.g., **Depth, Actionability**) for self-assessment and optimization.

---

## II. Advanced Prompting Strategies for Complex Sets

### 1. G. Mechanism Set (Layer 3)

| Strategy | Goal | Key Instruction Elements |
| :--- | :--- | :--- |
| **Reverse Engineering** | Discover core driving variables. | Start from the **result state** provided by Set C (Context) and Set B (Boundary), and reverse-engineer the **minimum necessary** Set G to reproduce that result. |
| **Assumption Testing** | Verify the validity of Set A. | For the highest-scoring assumption in Set A, ask the LLM to **construct a scenario where that assumption is excluded**, and detail how Set G changes as a consequence. |

### 2. H. Feedback Set (Layer 3)

| Strategy | Goal | Key Instruction Elements |
| :--- | :--- | :--- |
| **Dynamic Simulation** | Identify reinforcing and balancing loops. | Instruct the LLM to simulate a **10% fluctuation in a core G variable**, and map its cascading effect on **all coupled variables** in Set E (Connectivity) to identify Set H. |
| **Time-Lag Analysis** | Assess the effectiveness of Set I. | Explicitly ask for the **time-lag** of each loop: how long until positive feedback accelerates the system? How long until negative feedback begins to suppress it? |

### 3. P & Q. Meta-Cognition & Bias Sets (Layer 6)

| Strategy | Goal | Key Instruction Elements |
| :--- | :--- | :--- |
| **Role Reversal Critique** | Discover blind spots for Set P (Meta-Cognition). | Instruct the LLM to play the role of a **"Malicious Opponent,"** seeking the **weakest logical link** in the deconstruction based on Set A (Assumption) and Set C (Context). |
| **Forced Bias Exclusion** | Discover Set Q (Cognitive Bias). | Force the LLM to assume **"Confirmation Bias"** exists and propose a logically consistent explanation that is **diametrically opposed** to the current G and L conclusions. |

---

## III. Output Validation & Quality Control

Before the final output to $09\_Analysis\_Output\_Schema$, the backend service must perform the following steps:

1.  **JSON Format Validation:** Confirm LLM output is valid JSON and strictly matches the data types and fields of the corresponding Set in $01\_Schema$.
2.  **Dependency Check:** Ensure all Set outputs reference the correct **prerequisite Set data** (from the **05** Matrix), and reduce their **Q(S**_i\**)** score if non-sequential referencing is detected.
3.  **Consistency Scoring:** Specifically check for logical contradictions between the Framing Layer (**A**, **B**, **C**) and the Dynamic Layer (**G**, \**H**) (using the **Consistency** dimension of the **02** Scoring Guide).