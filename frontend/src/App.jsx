import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [prompt, setPrompt] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateApp = async () => {
    try {
      setLoading(true);

      const response = await axios.post(
        "https://ai-app-compiler-jfik.onrender.com/generate",
        {
          prompt,
        }
      );

      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Generation Failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <div className="hero">
        <h1>BUILD YOUR APP</h1>
        <p>
          From idea to architecture, schema, validation, and runtime generation
        </p>
      </div>

      <div className="prompt-card">
        <textarea
          rows="5"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Describe the application you want to build..."
        />

        <button onClick={generateApp}>
          {loading ? "Generating..." : "Generate Blueprint"}
        </button>
      </div>

      <div className="pipeline">
  <div className="pipeline-card">🟢 Intent Extraction</div>
  <div className="pipeline-card">🟢 System Design</div>
  <div className="pipeline-card">🟢 Schema Generation</div>
  <div className="pipeline-card">🟢 Validation</div>
  <div className="pipeline-card">🟢 Runtime</div>
</div>

      {result && (
        <>

        <div className="stats">
  <div className="stat-card">
    <h3>Entities</h3>
    <p>{result.design.entities.length}</p>
  </div>

  <div className="stat-card">
    <h3>Endpoints</h3>
    <p>{result.schema.api.endpoints.length}</p>
  </div>

  <div className="stat-card">
    <h3>Tables</h3>
    <p>{result.schema.db.tables.length}</p>
  </div>

  <div className="stat-card">
    <h3>Roles</h3>
    <p>{result.schema.auth.roles.length}</p>
  </div>
</div>


          <details className="section" open>
  <summary>🧠 Intent Extraction</summary>
  <pre>{JSON.stringify(result.intent, null, 2)}</pre>
</details>

          <details className="section">
  <summary>🏗️ System Design</summary>
  <pre>{JSON.stringify(result.design, null, 2)}</pre>
</details>

          <details className="section">
  <summary>📄 Generated Schema</summary>
  <pre>{JSON.stringify(result.schema, null, 2)}</pre>
</details>

          <details className="section">
            <summary>✅ Validation</summary>
            <pre>
              {result.validation_errors.length === 0
                ? "No validation errors found."
                : JSON.stringify(
                    result.validation_errors,
                    null,
                    2
                  )}
            </pre>
          </details>

          <details className="section">
            <summary>🔧 Repair Engine</summary>
            <pre>
              {result.repair_logs.length === 0
                ? "No repairs required."
                : JSON.stringify(
                    result.repair_logs,
                    null,
                    2
                  )}
            </pre>
          </details>

          <details className="section">
            <summary>⚙️ Runtime Generation</summary>
            <pre>{result.runtime_file}</pre>
          </details>
        </>
      )}

      <div className="footer">
  AI App Compiler • Multi-Stage Generation Pipeline • Validation & Runtime Aware
</div>

    </div>

    
  );
}

export default App;