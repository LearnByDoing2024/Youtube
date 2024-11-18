# AutoGen Command Line Code Executor Demo

This project demonstrates the implementation and usage of AutoGen's Command Line Code Executor functionality, showcasing how to execute Python code programmatically using AutoGen's powerful automation capabilities.

## Project Overview

The project illustrates:
1. Basic command line code execution
2. Integration with AutoGen agents
3. Automated code generation and execution
4. Interactive coding demonstrations

## Features

### Basic Code Execution
- Local command line code execution setup
- Temporary directory management
- Code block execution with output capture
- Error handling and execution status reporting

### Agent Integration
- ConversableAgent implementation
- Code execution configuration
- Agent-based code generation
- Interactive chat capabilities

### Example Applications
- Fibonacci number calculation
- Basic Python script execution
- Output capture and display
- Temporary file management

## Technical Implementation

### Dependencies
```python
pip install pyautogen
```

### Core Components
1. **LocalCommandLineCodeExecutor**
   - Manages code execution environment
   - Handles file I/O operations
   - Provides execution status and output

2. **ConversableAgent**
   - Facilitates code generation
   - Manages execution flow
   - Handles user interactions

### Code Examples

#### Basic Execution
```python
from pathlib import Path
from autogen.coding import CodeBlock, LocalCommandLineCodeExecutor

work_dir = Path("coding")
executor = LocalCommandLineCodeExecutor(work_dir=work_dir)
```

#### Agent Setup
```python
from autogen import ConversableAgent

code_executor_agent = ConversableAgent(
    "code_executor_agent",
    llm_config=False,
    code_execution_config={"executor": executor},
    human_input_mode="ALWAYS"
)
```

## Usage

1. Install required dependencies
2. Set up the execution environment
3. Configure the code executor
4. Run example demonstrations

## Security Considerations
- Code execution is performed in isolated environments
- Temporary directories are used for file operations
- Human verification option for code execution
- Timeout settings for execution control

## Contributing
Feel free to contribute by:
- Reporting issues
- Suggesting improvements
- Adding new examples
- Enhancing documentation

## License
This project is part of the YouTube tutorial series by Learn By Doing with Steven.

## Acknowledgments
- AutoGen development team
- Python community
- Contributors and users
