# 🚀 AI App Compiler

AI App Compiler is a compiler-inspired AI system that transforms natural language application requirements into structured software blueprints through a multi-stage pipeline.

Instead of generating code directly from a single prompt, the system decomposes the problem into multiple compiler-like stages including Intent Extraction, System Design, Schema Generation, Validation, Repair, and Runtime Generation.

---

## 🌐 Live Demo

Frontend (Vercel)

https://ai-app-compiler-eight-delta.vercel.app/

Backend (Render)

https://ai-app-compiler-jfik.onrender.com

---

## 🏗️ Architecture

```text
User Prompt
      │
      ▼
Intent Extraction
      │
      ▼
System Design
      │
      ▼
Schema Generation
      │
      ▼
Validation Engine
      │
      ▼
Repair Engine
      │
      ▼
Runtime Generation
      │
      ▼
Executable Application Blueprint
```

---

# 🔄 Pipeline Stages

## 1. Intent Extraction

Converts natural language into structured intent.

### Input

```text
Build a CRM with contacts, subscriptions and payments.
```

### Output

```json
{
  "app_type": "CRM",
  "features": [
    "contacts",
    "subscriptions",
    "payments"
  ],
  "roles": [
    "admin"
  ]
}
```

### Responsibilities

- Understand user requirements
- Normalize features
- Normalize roles
- Produce deterministic JSON output

---

## 2. System Design

Transforms intent into a software architecture plan.

### Example Output

```json
{
  "entities": [
    "User",
    "Contact",
    "Subscription",
    "Payment"
  ],
  "flows": [
    "Login",
    "Manage Contacts",
    "Manage Subscriptions",
    "Process Payments"
  ]
}
```

### Responsibilities

- Identify business entities
- Generate user workflows
- Define application structure

---

## 3. Schema Generation

Compiles architecture into a complete application schema.

### Generated Sections

- UI Pages
- API Endpoints
- Database Tables
- Authentication Roles

### Example

```json
{
  "ui": {},
  "api": {},
  "db": {},
  "auth": {}
}
```

### Responsibilities

- Create complete software blueprint
- Generate backend specifications
- Generate frontend specifications

---

## 4. Validation Engine

Performs consistency checks across generated artifacts.

### Validation Rules

#### API ↔ Database Validation

Example:

```text
Endpoint:
GET /payments

Expected:
payments table
```

If table is missing:

```text
Missing DB table for endpoint /payments
```

#### Authentication Validation

Ensures:

```text
Admin role exists
```

#### Structural Validation

Checks:

- UI pages
- API endpoints
- Database tables
- Authentication definitions

---

## 5. Repair Engine

Automatically repairs detected issues.

### Example

Validation Error:

```text
Missing DB table for endpoint /payments
```

Repair Action:

```json
{
  "name": "Payment",
  "fields": [
    {
      "name": "id",
      "type": "UUID"
    }
  ]
}
```

### Benefits

- Self-healing pipeline
- Increased robustness
- Improved reliability

---

## 6. Runtime Generator

Generates executable FastAPI endpoints from schema definitions.

### Example

Generated Endpoint

```python
@app.get("/contacts")
def handler():
    return {"status": "ok"}
```

### Output

```text
generated_app.py
```

### Purpose

Transforms blueprint into executable runtime artifacts.

---

# 🧠 LLM Usage

The system uses Google Gemini 2.5 Flash at multiple stages.

### Intent Extraction

Natural Language → Structured Intent

### System Design

Intent → Architecture

### Schema Generation

Architecture → Application Schema

---

# 🛡️ Reliability Features

## JSON Enforcement

All LLM responses are constrained to valid JSON.

## Schema Validation

Generated schemas are validated before use.

## Error Detection

Detects:

- Missing tables
- Missing roles
- Structural inconsistencies

## Automatic Repair

Repairs detected issues before returning results.

## Runtime Safety

Prevents malformed schemas from progressing through the pipeline.

---

# ⚙️ Tech Stack

## Frontend

- React
- Vite
- Axios

## Backend

- FastAPI
- Pydantic
- Python

## AI Layer

- Google Gemini 2.5 Flash

## Deployment

### Frontend

- Vercel

### Backend

- Render

---

# 📂 Project Structure

```text
AI App Compiler
│
├── backend
│   ├── main.py
│   ├── pipeline
│   │   ├── intent_extractor.py
│   │   ├── system_designer.py
│   │   ├── schema_generator.py
│   │   ├── validator.py
│   │   ├── repair_engine.py
│   │   └── runtime_generator.py
│   │
│   ├── schemas
│   │   ├── intent.py
│   │   └── design.py
│   │
│   └── services
│       └── gemini_client.py
│
├── frontend
│   ├── src
│   ├── public
│   └── package.json
│
└── README.md
```

---

# 🚀 Local Setup

## Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# 🎯 Key Highlights

✅ Multi-stage compiler-inspired architecture

✅ Natural language to software blueprint generation

✅ Schema validation and consistency checking

✅ Automatic repair engine

✅ Runtime code generation

✅ Full-stack deployment

✅ Production-ready API architecture

✅ AI-assisted software design pipeline

---

# 📈 Future Improvements

- Multi-language code generation
- React page generation
- Database migration generation
- OpenAPI export
- Docker deployment generation
- CI/CD pipeline generation
- Visual architecture diagrams
- Multi-agent orchestration

---

# 👨‍💻 Author

**Hrushikesh Bobbili**

AI/ML Enthusiast | Software Developer | System Design Explorer

GitHub:
https://github.com/Hrushi-233

---

## License

MIT License
