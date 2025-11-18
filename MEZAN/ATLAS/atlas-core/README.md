# ATLAS Core - Multi-Agent AI Research Orchestration System

**Version**: 0.1.0
**Status**: Week 1 Implementation Complete

---

## Overview

ATLAS Core is the main orchestration engine for the ATLAS multi-agent AI research system. It manages 40+ specialized research agents, implements dialectical workflows (thesis-antithesis-synthesis), and integrates with the Libria optimization solvers for intelligent task assignment and resource allocation.

## Features

### ✅ Week 1 Complete

- **ATLASEngine**: Main orchestration class
- **ResearchAgent Base Class**: Foundation for all research agents
- **8 Specialized Agents**:
  - SynthesisAgent
  - LiteratureReviewAgent
  - HypothesisGenerationAgent
  - CriticalAnalysisAgent
  - ValidationAgent
  - DataAnalysisAgent
  - MethodologyAgent
  - EthicsReviewAgent
- **Redis Blackboard**: Shared state management with Libria
- **Dialectical Workflows**: Thesis-antithesis-synthesis reasoning
- **Mock Libria Integration**: Development mode until Libria is ready
- **Test Suite**: Comprehensive unit tests
- **Demo Script**: Working example

## Quick Start

### Installation

```bash
cd atlas-core
pip install -e .
```

### Basic Usage

```python
from atlas_core.engine import ATLASEngine
from atlas_core.agents import create_agent

# Initialize ATLAS Engine
atlas = ATLASEngine(libria_enabled=False)

# Register agents
agent = create_agent(
    agent_type="synthesis",
    agent_id="agent_001",
    specialization="machine_learning",
    skill_level=0.85
)
atlas.register_agent(agent)

# Assign task
task = {
    "task_id": "task_001",
    "task_type": "synthesis",
    "complexity": 0.7
}
assigned_agent_id = atlas.assign_task(task)

# Execute dialectical workflow
result = atlas.execute_workflow(
    workflow_type="thesis_antithesis_synthesis",
    inputs={"topic": "neural_architecture_search"}
)
```

### Run Demo

```bash
cd atlas-core
python demo.py
```

### Run Tests

```bash
cd atlas-core
pytest tests/ -v
```

## Architecture

```
atlas-core/
├── atlas_core/
│   ├── __init__.py          # Package exports
│   ├── engine.py            # ATLASEngine main class
│   ├── agent.py             # ResearchAgent base class
│   ├── agents.py            # Concrete agent implementations
│   ├── blackboard.py        # Redis blackboard connector
│   └── libria_mock.py       # Mock LibriaRouter for development
├── tests/
│   ├── test_engine.py       # Engine tests
│   └── test_agents.py       # Agent tests
├── demo.py                  # Demo script
├── requirements.txt         # Dependencies
├── setup.py                 # Package setup
└── README.md               # This file
```

## Agent Types

### 1. SynthesisAgent
Synthesizes information from multiple sources and reconciles opposing viewpoints.

### 2. LiteratureReviewAgent
Reviews and summarizes relevant literature on a given topic.

### 3. HypothesisGenerationAgent
Generates testable research hypotheses based on input data.

### 4. CriticalAnalysisAgent
Provides critical analysis and challenges to hypotheses or arguments.

### 5. ValidationAgent
Validates research findings against established criteria.

### 6. DataAnalysisAgent
Analyzes data and produces statistical insights.

### 7. MethodologyAgent
Designs research methodologies and experimental protocols.

### 8. EthicsReviewAgent
Reviews ethical implications of research.

## Dialectical Workflows

### Thesis-Antithesis-Synthesis

Classic dialectical reasoning workflow:

1. **Thesis**: HypothesisGenerationAgent generates initial hypothesis
2. **Antithesis**: CriticalAnalysisAgent challenges with counter-arguments
3. **Synthesis**: SynthesisAgent reconciles into refined conclusion

```python
result = atlas.execute_workflow(
    workflow_type="thesis_antithesis_synthesis",
    inputs={"topic": "your_research_topic"}
)

# Access results
thesis = result["thesis"]
antithesis = result["antithesis"]
synthesis = result["synthesis"]
```

## Libria Integration

ATLAS integrates with Libria solvers for optimization:

- **QAPLibria**: Optimal agent-task assignment
- **FlowLibria**: Workflow routing with confidence
- **AllocLibria**: Resource allocation
- **GraphLibria**: Communication topology optimization
- **DualLibria**: Adversarial workflow validation
- **EvoLibria**: Agent architecture evolution

### Using Real Libria (Week 2+)

Once Libria integration is ready:

```python
# Enable Libria integration
atlas = ATLASEngine(libria_enabled=True)

# ATLAS will automatically use Libria solvers
assignment = atlas.assign_task(task)  # Uses QAPLibria
result = atlas.execute_workflow(...)  # Uses FlowLibria routing
```

## Redis Blackboard

ATLAS uses Redis for shared state with Libria:

### Connection

```python
from atlas_core.blackboard import ATLASBlackboard

blackboard = ATLASBlackboard("redis://localhost:6379/0")

# Test connection
if blackboard.ping():
    print("Connected to Redis")
```

### State Storage

Agent state is stored in Redis with keys:
- `atlas:agent:{agent_id}:type` - Agent type
- `atlas:agent:{agent_id}:skill_level` - Skill level
- `atlas:agent:{agent_id}:workload` - Current workload
- `atlas:agent:{agent_id}:history` - Execution history
- `atlas:agent:{agent_id}:connections` - Communication connections

## Development

### Adding New Agent Types

1. Create agent class inheriting from `ResearchAgent`
2. Implement `execute(task)` method
3. Add to agent factory in `agents.py`

Example:

```python
class CustomAgent(ResearchAgent):
    def execute(self, task: Dict) -> Dict:
        # Your implementation
        return {
            "result": "...",
            "quality": 0.85
        }

# Add to factory
def create_agent(agent_type: str, ...):
    agent_classes = {
        ...
        "custom": CustomAgent,
    }
```

### Running Tests

```bash
# All tests
pytest tests/ -v

# Specific test file
pytest tests/test_engine.py -v

# With coverage
pytest tests/ --cov=atlas_core --cov-report=html
```

## Week 2 Roadmap

- [ ] Implement workflow.py module for advanced workflows
- [ ] Add multi-perspective analysis workflow
- [ ] Integrate real LibriaRouter from Libria instance
- [ ] Test agent-task assignment via QAPLibria
- [ ] Test workflow routing via FlowLibria
- [ ] Expand to 20+ agents
- [ ] Add quality gates
- [ ] Performance benchmarking

## Integration with Libria

ATLAS and Libria are developed in parallel:

- **ATLAS** (this package): Multi-agent orchestration
- **Libria** (separate package): Optimization solvers
- **Integration**: Via LibriaRouter in `libria-integration/`

See `ATLAS_LIBRIA_INTEGRATION_SPEC.md` for complete integration details.

## Dependencies

- redis >= 4.0.0
- numpy >= 1.21.0
- pandas >= 1.3.0
- pytest >= 7.0.0
- anthropic >= 0.18.0
- openai >= 1.0.0
- pydantic >= 2.0.0

## License

MIT License - See LICENSE file

## Contributors

ATLAS Team - meshal@berkeley.edu

---

**Status**: Week 1 implementation complete! Ready for Week 2 integration with Libria.
