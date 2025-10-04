from flask import Flask, render_template, jsonify
from main_pipeline import orchestrate_ultra_complex_system

# Optional advanced pipeline
try:
    from main_pipeline_advanced import orchestrate_advanced_system
    HAS_ADVANCED = True
except Exception:
    orchestrate_advanced_system = None
    HAS_ADVANCED = False

app = Flask(__name__)

@app.route('/')
def index():
    results = orchestrate_ultra_complex_system(display_mode="dict")
    return render_template('index.html', results=results, has_visual=False)

@app.route('/advanced')
def advanced():
    if not HAS_ADVANCED:
        return jsonify({"error": "Advanced pipeline not available yet. Add main_pipeline_advanced.py and modules."}), 501
    results = orchestrate_advanced_system()
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)