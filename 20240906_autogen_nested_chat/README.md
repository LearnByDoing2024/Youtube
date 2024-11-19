# AutoGen Nested Chat Implementation

This project demonstrates advanced nested chat implementations using Microsoft's AutoGen framework, as shown in [this tutorial video](https://youtu.be/eEwkQTaRCDs).

## Overview
This project showcases:
- Implementation of nested conversations between multiple AI agents
- Complex problem-solving through agent collaboration
- Dynamic task delegation and management
- Advanced AutoGen framework features

## Features
- 🤖 Multiple AI agent interactions
- 🔄 Nested conversation flows
- 📝 Task breakdown and delegation
- 🎯 Goal-oriented problem solving
- 🔍 Context awareness between agents
- 📊 Structured conversation management

## Key Components
1. Agent Types:
   - Assistant Agent: Primary problem solver
   - Code Expert: Handles code-related tasks
   - Planner: Manages task breakdown
   - Reviewer: Validates solutions
   
2. Conversation Patterns:
   - Sequential discussions
   - Nested problem-solving
   - Parallel agent interactions
   - Context preservation

## Prerequisites
- Python 3.8+
- Required packages:
  ```bash
  pip install pyautogen
  pip install openai
  ```
- OpenAI API key or compatible LLM setup

## Setup Instructions
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure your API keys in `config.json`
4. Run the example:
   ```bash
   python main.py
   ```

## Usage Examples
1. Basic Nested Chat:
   ```python
   python examples/basic_nested_chat.py
   ```
2. Multi-Agent Problem Solving:
   ```python
   python examples/multi_agent_solving.py
   ```

## Configuration
- Agent configuration in `config.json`
- Conversation flow settings
- Model parameters
- Logging preferences

## Best Practices
- Define clear agent roles
- Structure conversations properly
- Handle context effectively
- Implement proper error handling
- Monitor agent interactions

## Troubleshooting
Common issues and solutions:
- API authentication errors
- Agent communication timeouts
- Context management issues
- Memory limitations

## Contributing
We welcome contributions:
- Bug reports
- Feature requests
- Documentation improvements
- Code contributions

## License
This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

Copyright 2024 Steven Wang

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
