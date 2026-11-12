# Data Model - Team Request & Live Chat Hub

## Entity Overview
The system manages three core entities: **UserSession** (client-side session state), **Request** (persisted task/feedback items), and **ChatMessage** (persisted conversation entries).

---

## 1. UserSession
Represents the active participant in the browser session prior to and during chat participation.

| Field | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `session_id` | `string` (UUID) | Primary Key, Required | Unique identifier generated per browser session |
| `username` | `string` | Required, 1–30 chars, Non-empty | Display name entered by the user to unlock chat |
| `joined_at` | `string` (ISO 8601) | Required | Timestamp when the user joined the chat view |

---

## 2. Request
Represents a structured request or feedback item submitted via the Requests tab and stored in `ValStorage`.

| Field | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `string` (UUID) | Primary Key, Required | Unique identifier for the request entry |
| `content` | `string` | Required, 1–500 chars | Text body of the submitted request |
| `created_at` | `string` (ISO 8601) | Required | Timestamp recorded when the request was saved |
| `status` | `string` | Default: `"open"` | Current state of the request (`"open"` or `"resolved"`) |

---

## 3. ChatMessage
Represents an individual message posted in the live chat thread and stored in `ValStorage`.

| Field | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `string` (UUID) | Primary Key, Required | Unique identifier for the chat message |
| `session_id` | `string` (UUID) | Foreign Key -> `UserSession.session_id` | Links the message to the sender's active session |
| `username` | `string` | Required, 1–30 chars | Display name of the sender shown in the chat feed |
| `message` | `string` | Required, 1–1000 chars | Text content of the chat message |
| `sent_at` | `string` (ISO 8601) | Required | Timestamp recorded when the message was posted |

---

## Entity Relationships
- **UserSession (1) -> ChatMessage (0..N):** One user session can author zero or many chat messages, linked via `session_id` and attributed via `username`.
- **Request (Standalone Collection):** Stored independently in `ValStorage` (capped at 100 entries) and ordered chronologically by `created_at`.
