from flask import Flask, render_template
from main_pipeline import orchestrate_ultra_complex_system

app = Flask(__name__)

@app.route('/')
def index():
    results = orchestrate_ultra_complex_system(display_mode="dict")
    return render_template('index.html', results=results)

if __name__ == "__main__":
    app.run(debug=True)