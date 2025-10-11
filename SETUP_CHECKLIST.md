# Nomimi Setup & Running Checklist

## 1. Python Environment
- [ ] Python 3.8+ installed
- [ ] Virtual environment created (`python -m venv venv`)
- [ ] Activate environment (`source venv/bin/activate` or `venv\Scripts\activate`)
- [ ] Install requirements (`pip install -r requirements.txt`)

## 2. Project Structure
- [ ] All `.py` modules in root or organized as needed
- [ ] `app.py` in root
- [ ] `templates/` folder with `index.html`
- [ ] `static/` folder with `style.css`
- [ ] All logic modules present:
    - main_pipeline.py
    - spaceship_design.py
    - knowledge_integration.py
    - requirements_management.py
    - trade_study.py
    - risk_management.py
    - collaboration.py
    - visualization.py
    - regulatory_compliance.py
    - supply_chain.py
    - security_privacy.py
    - feedback_user_interaction.py
    - deployment_scalability.py
    - base_layer.py
    - meta_optimizer.py
    - simulation_engine.py
    - data_integration.py
    - human_factors.py
    - novelty_manager.py
    - optimization_engine.py
    - dependency_graph.py
    - ux_conversation.py
    - validation_integration.py
    - threat_modeling.py
    - scalability_planner.py

## 3. Imports & File Connections
- [ ] All imports resolved (no ModuleNotFoundError)
- [ ] All functions/classes called as expected

## 4. Flask App
- [ ] `app.py` runs (`python app.py`)
- [ ] Visit `http://localhost:5000` to see dashboard

## 5. Testing
- [ ] Dashboard displays all sections (design, metrics, knowledge, requirements, risks, etc.)
- [ ] No template or runtime errors
- [ ] Data shown matches pipeline output
- [ ] Run tests with `pytest -q` (all tests should pass)

## 6. Visualization
- [ ] Design summary, metrics, risks, trade study, compliance, etc. all visible
- [ ] CSS loads for styling

## 7. Optional
- [ ] Add README.md with project description and usage
- [ ] Add sample test script if needed

---

## Troubleshooting

- If you see import errors, check PYTHONPATH and file locations.
- If Flask can't find your template or static files, check folder names and placement.
- If dashboard is blank or missing data, check pipeline return values and template keys.

---

## Next Steps

- Run basic test
- Add more logic, visualization, or user interface as needed