# 08_Backend_API_Spec - Backend API Specification Documentation

**Service Name:** CogniRank Analysis Service (CAS)
**Base URL:** /api/v1/cognirank
**Goal:** Provide a set of RESTful API endpoints for submission, status query, and retrieval of the final CogniRank report.

---

## I. API Endpoints List

| No. | Method | Path | Description |
| :--- | :--- | :--- | :--- |
| **1.0** | `POST` | `/submit_question` | Submits a question and initiates the asynchronous deconstruction process. |
| **2.0** | `GET` | `/status/{task_id}` | Queries task status and currently completed Sets. |
| **3.0** | `GET` | `/report/{task_id}` | Retrieves the final report or partially completed structured data. |

---

## II. Detailed API Specification

### 1.0 Submit Question

**Path:** `POST /api/v1/cognirank/submit_question`

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `user_id` | `String` | Yes | Unique ID of the user submitting the task (used for authorization and billing). |
| `question_text` | `String` | Yes | The **original question** the user wants CogniRank to deconstruct. |
| `priority` | `Enum (low/standard/high)` | No | Task priority (affects time constraint parameters in the $\mathbf{Y}$ Set). |

**1.1 Request Body (JSON):**

```json
{
  "user_id": "user_12345",
  "question_text": "How can I quantify my deep thinking ability?",
  "priority": "standard"
}