# Nomimi - Ultra-Complex System Design Platform

Nomimi is an advanced system design platform that integrates multiple capabilities for designing, analyzing, and validating complex engineering projects, particularly focused on large-scale aerospace and industrial systems.

## Overview

Nomimi provides a comprehensive framework for managing the entire lifecycle of complex system design, from initial requirements through deployment and scaling. It integrates nine key capability areas:

### Nine Core Capabilities

#### 1. Real-World Data Integration
- CSV/JSON file loaders for local data sources
- REST API connectors for remote data integration
- MQTT/WebSocket support (stub) for real-time streaming data
- Data normalization and validation pipelines

#### 2. Human Factors & Soft Constraints
- Task load modeling and error rate prediction
- Crew member management and shift scheduling
- Performance factor calculations based on workload
- Regulatory standards monitoring (ISO, FAA, etc.)
- Policy change feed tracking (stub)

#### 3. Planning for Novel/Unprecedented Projects
- Iterative prototyping loops for ambiguous requirements
- Hypothesis generation and experiment design
- Results tracking across multiple iterations
- Automatic convergence detection (planned)

#### 4. Deep Domain-Specific Optimization & Multi-Objective Simulation
- NSGA-II-style multi-objective optimization (stub implementation)
- Support for cost, risk, efficiency, and custom objectives
- Pareto-optimal solution generation
- Integration with simulation engine for performance validation

#### 5. Interdisciplinary Dependency Integration
- Dependency graph modeling across disciplines
- Topological sorting and critical path analysis
- Circular dependency detection
- Change impact analysis

#### 6. Enhanced User Experience & Interaction
- Stateful multi-turn conversation interface
- Context-aware response generation
- Guidance suggestions based on conversation history
- Backward compatibility with simple conversation interface

#### 7. Design Validation & Prototyping Integration
- Test plan export (JSON, Markdown formats)
- Hardware-in-the-Loop (HIL) testing interface (stub)
- Field trial tracking and outcome recording
- Physical validation workflow support

#### 8. Advanced Security & Privacy/Threat Modeling
- STRIDE methodology threat identification
- Risk score calculation (severity × likelihood)
- Automatic mitigation suggestions
- Integration with risk management system
- Security category breakdown (Spoofing, Tampering, etc.)

#### 9. Large-Scale/Global Scalability Planning
- Workload-based capacity planning
- Multi-region deployment recommendations
- High availability architecture design
- Cost estimation for different deployment scales
- Auto-scaling policy recommendations (planned)

## Architecture

Nomimi uses a modular pipeline architecture:

- **Core Pipeline** (`main_pipeline.py`): Orchestrates all modules and aggregates results
- **Capability Modules**: Independent modules for each of the nine capabilities
- **Web Interface** (`app.py`): Flask-based dashboard for visualization
- **Design Engine**: SpaceshipDesign, MetaOptimizer, SimulationEngine
- **Supporting Modules**: Knowledge integration, requirements management, trade studies, risk management, etc.

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

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

## Usage

### Running the Dashboard

Start the Flask web server:
```bash
python app.py
```

Then visit http://localhost:5000 in your web browser to see the dashboard with all nine capability sections populated with example data.

### Running Tests

Execute the test suite:
```bash
pytest -q
```

For more verbose output:
```bash
pytest -v
```

### Using Individual Modules

Each capability module can be used independently:

```python
from data_integration import DataIngestor, DataPipeline
from optimization_engine import OptimizationEngine
from threat_modeling import ThreatModel

# Data integration example
ingestor = DataIngestor()
data = ingestor.load_csv("path/to/data.csv")
pipeline = DataPipeline()
normalized = pipeline.normalize(data)

# Optimization example
optimizer = OptimizationEngine()
results = optimizer.optimize(design, objectives=["cost", "risk", "efficiency"])

# Threat modeling example
threats = ThreatModel()
threats.add_threat("T001", "S", "Unauthorized access", severity=8, likelihood=0.3)
```

## Project Structure

```
Nomimi/
├── app.py                      # Flask web application
├── main_pipeline.py            # Main orchestration pipeline
├── requirements.txt            # Python dependencies
├── SETUP_CHECKLIST.md         # Setup and running guide
├── README.md                   # This file
│
├── templates/
│   └── index.html             # Dashboard template
│
├── static/
│   └── style.css              # Dashboard styling
│
├── tests/
│   └── test_capabilities.py   # Test suite
│
├── Core Modules:
├── spaceship_design.py
├── simulation_engine.py
├── meta_optimizer.py
├── base_layer.py
│
├── Supporting Modules:
├── knowledge_integration.py
├── requirements_management.py
├── trade_study.py
├── risk_management.py
├── collaboration.py
├── visualization.py
├── regulatory_compliance.py
├── supply_chain.py
├── security_privacy.py
├── feedback_user_interaction.py
├── deployment_scalability.py
│
└── New Capability Modules:
    ├── data_integration.py
    ├── human_factors.py
    ├── novelty_manager.py
    ├── optimization_engine.py
    ├── dependency_graph.py
    ├── ux_conversation.py
    ├── validation_integration.py
    ├── threat_modeling.py
    └── scalability_planner.py
```

## Development

### Code Organization

- Each capability module follows a consistent pattern with classes that have `get_summary()` methods
- Modules include docstrings and TODO comments indicating extension points
- Stub implementations are clearly marked for features requiring external services
- No breaking changes to existing functionality

### Testing

The test suite (`tests/test_capabilities.py`) includes:
- Unit tests for each new capability module
- Integration test for the main pipeline
- Validation that all expected result keys are present

### Contributing

When adding new features:
1. Follow the existing code style (simple classes, clear method signatures)
2. Add docstrings with TODO comments for future enhancements
3. Update tests to cover new functionality
4. Keep stub implementations for features requiring external dependencies
5. Ensure backward compatibility with existing code

## Future Enhancements

See TODO comments in each module for planned improvements, including:
- Real MQTT/WebSocket connections for live data
- Full NSGA-II genetic algorithm implementation
- LLM integration for conversational interface
- Production-ready threat modeling with CVE integration
- Cloud provider API integration for accurate cost estimates
- Machine learning-based capacity planning

## License

See repository for license information.

## Contact

For questions or support, please open an issue on the GitHub repository.
