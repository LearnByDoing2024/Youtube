# AutoGen Code Executor Demo

This project demonstrates the usage of AutoGen's code execution capabilities, specifically focusing on the `LocalCommandLineCodeExecutor` for running Python code blocks.

## Overview

The demo showcases how to:
1. Set up a local code executor with AutoGen
2. Create a code executor agent
3. Execute Python code blocks that generate visualizations
4. Handle temporary file management

## Project Components

### Files
- `20240501 autogen code executor.ipynb`: Main Jupyter notebook containing the demo
- `scatter.png`: Generated scatter plot from the code execution
- `README.md`: Project documentation

### Key Features
- Local command line code execution
- Temporary directory management
- Matplotlib visualization generation
- AutoGen agent configuration

## Technical Implementation

### Dependencies
```python
pip install autogen matplotlib numpy
```

### Code Structure
1. **Setup Code Executor**
   ```python
   import tempfile
   from autogen import ConversableAgent
   from autogen.coding import LocalCommandLineCodeExecutor
   ```

2. **Configure Executor**
   - Uses temporary directory for code files
   - 10-second timeout for executions
   - Local command line execution environment

3. **Agent Configuration**
   - ConversableAgent with code execution capabilities
   - LLM disabled for demonstration
   - Human input mode set to "ALWAYS" for safety

## Usage Example

The notebook demonstrates executing a code block that:
1. Generates random data using NumPy
2. Creates a scatter plot using Matplotlib
3. Saves the plot as 'scatter.png'

## Output

The execution produces:
- A scatter plot visualization (`scatter.png`)
- Execution status and output messages
- Temporary file management information

## Security Considerations
- Code execution is performed in a temporary directory
- Timeout limits prevent infinite loops
- Human input verification for safety

## Contributing
Feel free to contribute to this project by:
- Submitting issues
- Proposing new features
- Creating pull requests

## License
This project is part of the YouTube tutorial series by Learn By Doing with Steven.
