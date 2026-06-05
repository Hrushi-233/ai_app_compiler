def generate_runtime(api_schema):

    code = """
from fastapi import FastAPI

app = FastAPI()
"""

    for endpoint in api_schema["endpoints"]:

        method = endpoint["method"].lower()

        path = endpoint["path"]

        endpoint_name = (
            path.replace("/", "_")
                .replace("{", "")
                .replace("}", "")
                .replace("-", "_")
                .replace(":", "_")
        )

        function_name = f"{method}{endpoint_name}"

        code += f"""

@app.{method}("{path}")
def {function_name}():
    return {{"status": "ok"}}
"""

    with open(
        "generated_app.py",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(code)

    return "generated_app.py"