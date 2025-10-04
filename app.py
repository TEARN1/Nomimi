from flask import Flask, render_template, jsonify, request
from main_pipeline import orchestrate_ultra_complex_system

# Optional advanced pipeline
try:
    from main_pipeline_advanced import orchestrate_advanced_system
    HAS_ADVANCED = True
except Exception:
    orchestrate_advanced_system = None
    HAS_ADVANCED = False

# Optional generation ship pipeline
try:
    from main_pipeline_generation_ship import orchestrate_generation_ship
    HAS_GENSHIP = True
except Exception:
    orchestrate_generation_ship = None
    HAS_GENSHIP = False

app = Flask(__name__)

@app.route('/')
def index():
    results = orchestrate_ultra_complex_system(display_mode="dict")
    return render_template('index.html', results=results, has_visual=False)

@app.route('/advanced')
def advanced():
    if not HAS_ADVANCED:
        return jsonify({"error": "Advanced pipeline not available."}), 501
    return jsonify(orchestrate_advanced_system())

@app.route('/generation-ship')
def generation_ship():
    if not HAS_GENSHIP:
        return jsonify({"error": "Generation ship pipeline not available. Add generation_ship_planner.py and main_pipeline_generation_ship.py"}), 501
    population = int(request.args.get("population", 5_000_000))
    cycles = int(request.args.get("cycles", 2))
    result = orchestrate_generation_ship(population=population, cycles=cycles)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)