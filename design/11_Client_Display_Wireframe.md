# 11_Client_Display_Wireframe - Client Report Display Wireframe

**Purpose:** Define the User Interface (UI) layout and key visualization elements for the final CogniRank report (based on $03\_Template$) to achieve optimal user experience and information dissemination (Set O).

---

## I. Report Structure Overview

The report should use a vertical scrolling layout, with a top section for key summaries and scores, followed by detailed content organized by Layer.

| Section | Corresponding Layer/Set | Content Display Focus |
| :--- | :--- | :--- |
| **A. Top Nav/Metadata** | Metadata | Task ID, Original Question, Generation Time. |
| **B. Insight Summary** | Executive Summary (G, L) | Final Recommendation, Core Insight Cards. |
| **C. Quality Dashboard** | **Overall **I** Score, Layer Scores** | Final Score, Radar Chart. |
| **D. Core Deconstruction** | Layer 1-4 (A, B, C, G, H, L) | Structured lists, key diagrams. |
| **E. Meta & Action** | Layer 5-6 (P, Q, R, M, O) | Action recommendations, Bias checklist. |

---

## II. Key Visualization Components

The frontend must render the following key charts, with data sourced from the `visualization_data_sources` field in $09\_Analysis\_Output\_Schema.json$.

### 1. Cognitive Profile Radar Chart (Set N)

* **Purpose:** Visually show the balance or bias across the six Layers.
* **Data Source:** `layer_summary_scores`.
* **Axis Definition:** The six Layer (0-6) weighted scores as the six axes of the radar chart.
* **UI Interaction:** Hover to show the average score of specific Sets within a Layer.

### 2. Causal Loop Diagram (Set H)

* **Purpose:** Illustrate the dynamic relationships in **G** (Mechanism Set) and **H** (Feedback Set).
* **Data Source:** `causal_loop_data`.
* **Chart Elements:** Nodes are core variables from **G**; edges are causal links; use different colors/symbols to distinguish Reinforcing (**R**) and Balancing (**B**) loops.

### 3. Assumption/Bias Strength Bar Chart (Sets A, Q)

* **Purpose:** Quantify and highlight the most risky **assumptions** and **biases**.
* **Data Source:** `output_data` from Sets **A** and **Q**.
* **Chart Elements:** X-axis is the Assumption/Bias name, Y-axis is the "Criticality Score" or "Mitigation Priority Score."

---

## III. Detailed Area Wireframes

### C. Quality Dashboard Layout

| Component | Description | Data Source |
| :--- | :--- | :--- |
| **Final Score** (**I**) | Large, prominent number with a brief descriptive tag (e.g., Excellent, Strong). |