from fastapi import FastAPI

from pipeline.intent_extractor import extract_intent
from pipeline.system_designer import design_system
from pipeline.schema_generator import generate_schema
from pipeline.validator import validate
from pipeline.repair_engine import repair
from pipeline.runtime_generator import generate_runtime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://ai-app-compiler-eight-delta.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/generate")
def generate(data: dict):

    prompt = data["prompt"]

    # Stage 1: Intent Extraction
    intent = extract_intent(prompt)

    print("\n===== INTENT =====")
    print(intent.model_dump())

    # Stage 2: System Design
    design = design_system(intent)

    print("\n===== DESIGN =====")
    print(design.model_dump())

    # Stage 3: Schema Generation
    schema = generate_schema(design)

    print("\n===== GENERATED SCHEMA =====")
    print(schema)

    # Stage 4: Validation
    errors = validate(schema)

    print("\n===== VALIDATION ERRORS =====")
    print(errors)

    # Stage 5: Repair
    repaired_schema, logs = repair(
        schema,
        errors
    )

    print("\n===== REPAIR LOGS =====")
    print(logs)

    # Stage 6: Runtime Generation
    runtime_file = generate_runtime(
        repaired_schema["api"]
    )

    print("\n===== RUNTIME FILE =====")
    print(runtime_file)

    return {
        "intent": intent.model_dump(),
        "design": design.model_dump(),
        "schema": repaired_schema,
        "validation_errors": errors,
        "repair_logs": logs,
        "runtime_file": runtime_file
    }

@app.get("/")
def home():
    return {
        "status": "healthy",
        "service": "AI App Compiler"
    }