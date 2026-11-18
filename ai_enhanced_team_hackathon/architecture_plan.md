High-Level Architecture Plan

1. System Overview

The AI-Powered Learning Roadmap & Study Planner follows a modern three-tier client-server architecture enhanced with an external Large Language Model (LLM) service. The frontend provides a responsive dashboard for syllabus tracking and quiz-taking, the backend orchestrates business logic and prompt engineering, and the database persists user roadmaps and progress.

2. Architecture Diagram

+-------------------------------------------------------------------+
|                        Frontend (Client)                          |
|   React / Next.js + Tailwind CSS                                  |
|   - Goal Input Form      - Interactive Roadmap View               |
|   - Progress Dashboard   - Micro-Quiz Modal                       |
+---------------------------------+---------------------------------+
                                  | REST API (JSON over HTTPS)
                                  v
+-------------------------------------------------------------------+
|                     Backend API & AI Orchestrator                 |
|   Node.js (Express) or Python (FastAPI)                           |
|   - Auth & Session Middleware                                     |
|   - Roadmap & Progress Controller                                 |
|   - Prompt Engineering & JSON Schema Validator                    |
+----------------+----------------------------------+---------------+
                 | SQL / ORM                        | HTTPS / SDK
                 v                                  v
+--------------------------------+ +--------------------------------+
|      Relational Database       | |       External LLM API         |
|   PostgreSQL / SQLite          | |   (OpenAI / Gemini API)        |
|   - Users & Roadmaps           | |   - Structured JSON Outputs    |
|   - Modules & Quiz Attempts    | |   - Syllabus & Quiz Generation |
+--------------------------------+ +--------------------------------+


3. Component Breakdown

A. Frontend Layer (Presentation)

Tech Stack: React (Vite or Next.js) with Tailwind CSS for rapid hackathon UI development.

Key Views:

Onboarding / Generator View: Clean form capturing target_skill, proficiency_level, and hours_per_week.

Roadmap Workspace: Collapsible week-by-week accordion displaying daily modules, completion checkboxes, and a dynamic progress bar.

Module Detail & Quiz Drawer: Displays AI-generated concept summaries and launches the interactive 3–5 question micro-quiz.

B. Backend Layer (Application & AI Orchestration)

Tech Stack: Python (FastAPI) or Node.js (Express) — chosen for fast JSON handling and native LLM SDK support.

Responsibilities:

Prompt Construction: Injects user parameters into carefully tuned system prompts to ensure realistic pacing and structured curriculum design.

Structured Output Enforcement: Uses LLM JSON-mode / schema validation (e.g., Pydantic or Zod) to guarantee that generated syllabi and quizzes strictly conform to expected JSON formats before saving to the database.

Timeline Recalculation Logic: Handles date-shifting algorithms when a user requests to reschedule unfinished modules.

C. AI Integration Layer (LLM Service)

Model Strategy: Fast, cost-effective frontier model (e.g., gemini-2.5-flash or gpt-4o-mini) to keep roadmap generation latency under 5 seconds.

Core AI Workflows:

Curriculum Generation Prompt: Takes (skill, level, hours) $\rightarrow$ outputs a multi-week JSON tree of modules.

Micro-Quiz Prompt: Takes (module_title, summary_content) $\rightarrow$ outputs 3–5 MCQs with explanations.

D. Data Persistence Layer

Tech Stack: SQLite (for zero-config local hackathon development) or PostgreSQL (Supabase/Neon for instant cloud deployment).

Data Flow: Once the backend validates the LLM's JSON response, it atomically inserts the Roadmap and child Study_Modules records so subsequent page loads require zero redundant LLM API calls.

4. API Endpoints (MVP Specification)

Method

Endpoint

Description

POST

/api/roadmaps/generate

Accepts user goal parameters, calls LLM, stores and returns the new roadmap.

GET

/api/roadmaps/:id

Retrieves a saved roadmap along with all weeks, modules, and completion stats.

PATCH

/api/modules/:id/complete

Toggles a module's is_completed status and recalculates overall progress.

POST

/api/roadmaps/:id/reschedule

Shifts scheduled_date values forward for all incomplete modules.

POST

/api/modules/:id/quiz

Generates (or fetches cached) 3–5 question micro-quiz for the specific module.

POST

/api/quizzes/:id/submit

Evaluates user answers, records score in Quiz_Attempts, and returns explanations.

5. Key Technical Risks & Mitigations

Malformed LLM Responses: Mitigated by enforcing strict JSON Schema / Structured Outputs at the API level and implementing a single automatic retry on parse failure.

Generation Latency: Mitigated by displaying a skeleton loading state with progress indicators while the initial syllabus generates, and caching generated quizzes in the database so repeat views are instantaneous.
