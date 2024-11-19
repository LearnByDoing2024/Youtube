# AutoGen Research Group Chat with RAG Integration

An advanced implementation showcasing AutoGen's group chat capabilities combined with Retrieval-Augmented Generation (RAG) for complex business scenarios. This project demonstrates how multiple AI agents can collaborate to solve sophisticated business problems like internal auditing and AML policy creation. Watch the tutorial on [Learn By Doing with Steven YouTube Channel](https://youtu.be/your-video-id).

## Project Structure
```
├── 20240517 autogen research agent sample.ipynb  # Main implementation notebook
├── 20240517 autogen research agent sample.md     # Documentation and examples
├── 20240516 internal audit debugger.ipynb        # Debugging and testing notebook
├── 20240516 md.md                               # Additional documentation
└── 20240516 md1.md                              # Additional documentation
```

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

## Prerequisites
- Python 3.8+
- AutoGen library
- Basic understanding of RAG systems
- Knowledge of compliance frameworks

## Usage

1. Clone the repository:
```bash
git clone https://github.com/learnbydoingwithsteven/Youtube.git
cd "20240517 AUTOGEN RESEARCH GROUP CHAT AND RAG GROUP CHAT"
```

2. Configure Agent Settings:
```python
config = {
    "speaker_selection_method": "auto",
    "allow_repeat_speaker": True,
    "send_introductions": True
}
```

3. Initialize Group Chat:
```python
group_chat = GroupChat(
    agents=[cco, internal_auditor, operations_manager],
    manager=chat_manager,
    config=config
)
```

4. Run Simulations:
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

## Best Practices
- Regular agent behavior validation
- Comprehensive error handling
- Clear conversation boundaries
- Proper state management
- Performance optimization

## Contributing
We welcome contributions in:
- Additional agent roles
- New use case implementations
- Enhanced RAG capabilities
- Documentation improvements
- Testing and validation

## License
This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

Copyright 2024 Learn By Doing With Steven (YouTube Channel)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Acknowledgments
- AutoGen development team
- RAG framework contributors
- Open-source community
- All contributors and users
