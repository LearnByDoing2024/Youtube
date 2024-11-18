# AutoGen Research Group Chat with RAG Integration

An advanced implementation showcasing AutoGen's group chat capabilities combined with Retrieval-Augmented Generation (RAG) for complex business scenarios. This project demonstrates how multiple AI agents can collaborate to solve sophisticated business problems like internal auditing and AML policy creation.

## Video Tutorial
Coming soon...

## Key Features
- Multi-agent group chat implementation using AutoGen
- RAG integration for enhanced knowledge retrieval
- Specialized business agents (CCO, Internal Auditor, Operations Manager)
- Scenario-based simulations
- Comprehensive policy generation capabilities
- Customizable agent interactions and behaviors

## Implemented Agents

### Core Agents
- **CCO (Chief Compliance Officer)**: Handles compliance-related queries and policy development
- **Internal Auditor**: Manages audit procedures and policy validation
- **Operations Manager**: Oversees operational implementation
- **Chat Manager**: Coordinates communication between agents

### Agent Capabilities
- Policy creation and validation
- Scenario simulation
- Risk assessment
- Compliance verification
- Process documentation

## Use Cases Demonstrated

### 1. AML Policy Development
- Comprehensive AML policy creation
- Risk sector identification
- Internal controls establishment
- Compliance monitoring procedures

### 2. Internal Audit Framework
- Policy development
- Procedure documentation
- Scenario-based validation
- Effectiveness assessment

## Technical Implementation

### Files Structure
- `20240517 autogen research agent sample.ipynb`: Main implementation notebook
- `20240517 autogen research agent sample.md`: Documentation and examples
- `20240516 internal audit debugger.ipynb`: Debugging and testing notebook
- `20240516 md.md` & `20240516 md1.md`: Additional documentation

### Configuration Options
- Customizable speaker selection methods
- Flexible agent transition rules
- History management
- Introduction protocols

## Usage

1. Configure Agent Settings:
```python
config = {
    "speaker_selection_method": "auto",
    "allow_repeat_speaker": True,
    "send_introductions": True
}
```

2. Initialize Group Chat:
```python
group_chat = GroupChat(
    agents=[cco, internal_auditor, operations_manager],
    manager=chat_manager,
    config=config
)
```

3. Run Simulations:
```python
chat_manager.initiate_chat(
    message="Create an internal audit policy for transaction monitoring"
)
```

## Advanced Features

### Speaker Selection
- Auto-selection based on context
- Rule-based transitions
- Customizable selection templates

### History Management
- Clear history functionality
- Message context preservation
- Conversation flow control

### RAG Integration
- Enhanced knowledge retrieval
- Context-aware responses
- Dynamic information updates

## Documentation
- Detailed implementation guides
- Agent interaction patterns
- Configuration options
- Best practices and examples

## Contributing
Contributions welcome in:
- Additional agent roles
- New use case implementations
- Enhanced RAG capabilities
- Documentation improvements

## License
This project is open source and available under the MIT License.
