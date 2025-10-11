# Nomimi - Ultra-Complex System Design Platform

Nomimi is a comprehensive system design and analysis platform for complex engineering projects. It provides integrated capabilities for requirements management, risk assessment, optimization, and more.

## Capabilities

Nomimi integrates nine major capability domains:

1. **Data Integration** - Load and normalize data from CSV, JSON, REST APIs, and message queues
2. **Human Factors** - Model operator fatigue, error rates, and track regulatory compliance
3. **Novelty & Innovation** - Manage hypothesis-driven prototyping and experimental cycles
4. **Multi-Objective Optimization** - Generate Pareto frontiers across competing objectives
5. **Dependency Management** - Track component dependencies with topological sorting and critical path analysis
6. **UX & Conversation** - Stateful conversational interface with context-aware guidance
7. **Validation & Testing** - Test plan generation, hardware-in-loop stubs, and field trial tracking
8. **Threat Modeling** - STRIDE-based security analysis with risk assessment
9. **Scalability Planning** - Resource planning with cost estimation for cloud deployment

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/TEARN1/Nomimi.git
cd Nomimi
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

Start the Flask development server:
```bash
python app.py
```

Visit `http://localhost:5000` in your web browser to access the dashboard.

### Running Tests

Run the test suite:
```bash
pytest -q
```

Or with verbose output:
```bash
pytest -v
```

## Project Structure

```
Nomimi/
├── app.py                      # Flask application entry point
├── main_pipeline.py            # Main orchestration pipeline
├── templates/                  # HTML templates
│   └── index.html
├── static/                     # CSS and static assets
│   └── style.css
├── tests/                      # Test suite
│   └── test_smoke.py
├── data_integration.py         # Data loading and normalization
├── human_factors.py            # Human performance modeling
├── novelty_manager.py          # Innovation and prototyping
├── optimization_engine.py      # Multi-objective optimization
├── dependency_graph.py         # Component dependency tracking
├── ux_conversation.py          # Conversational interface
├── validation_integration.py   # Testing and validation
├── threat_modeling.py          # Security threat analysis
├── scalability_planner.py      # Infrastructure planning
└── [other core modules...]     # Requirements, risk, collaboration, etc.
```

## Features

- **Web Dashboard**: Visualize all system aspects in a unified interface
- **Modular Architecture**: Each capability is implemented as an independent module
- **Graceful Degradation**: Falls back to example data when external resources unavailable
- **Extensible Design**: Easy to add new capabilities and integrate with external services
- **Comprehensive Testing**: Full test coverage with pytest

## Development

### Adding New Capabilities

1. Create a new module in the root directory
2. Import and instantiate in `main_pipeline.py`
3. Add results to the pipeline output dictionary
4. Update `templates/index.html` to display new data
5. Add tests in `tests/test_smoke.py`

### Code Style

- Follow PEP 8 guidelines
- Include docstrings for all classes and methods
- Add TODO comments for future enhancements

## License

See LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
