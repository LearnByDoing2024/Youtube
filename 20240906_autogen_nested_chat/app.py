
import streamlit as st
from config import available_models
from agents import create_inner_agents, create_graphics_agents, create_groupchat_manager, create_outer_agents
from workflow import initiate_nested_chat, initiate_graphical_chats

# Predefined tasks
predefined_tasks = [
    "On which days in 2024 was Microsoft Stock higher than $400? Comment on the stock performance. Make a pleasant joke about it.",
    "analyze amazon past month stock price, financial standing, show relevant graphs, news, and give investment suggestion",
    "Pick 10 tech stocks and analyze their performance in the past year, analyze financial standings, show graphics, give investment suggestion report.",
    "Randomly pick 10 tech stocks and analyze their performance in the past year, analyze financial standings, show graphics, hypothetically suggest what should have been done to achieve max portfolio return."
]

# Initialize Streamlit app
st.title('Streamlit Chatbot App')

# Add a note about the types of tasks the app can handle
st.markdown("""
**Note:** This app can handle the following types of tasks:
- Financial analysis, such as stock performance commentary and key financial metrics visualization.
- Generating financial graphs like price trends, financial comparisons, and peer analysis.
- Creating written content, such as articles, summaries, or jokes based on data or concepts.
- Custom tasks defined by the user.
""")

# Sidebar for Model Selection and Task Input
with st.sidebar:
    st.header("Configuration")
    
    selected_model_name = st.selectbox(
        'Select a model:',
        list(available_models.keys()),
        key='model'
    )

    task_type = st.selectbox(
        'Select a task or input your own:',
        predefined_tasks + ["Input your own task"],
        key='task_type'
    )

    if task_type == "Input your own task":
        task = st.text_area('Please input your custom task here:', key='custom_task')
    else:
        task = task_type

# Initialize session state for conversation history, summary, and HTML output
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

if 'summary' not in st.session_state:
    st.session_state.summary = ""

if 'html_output' not in st.session_state:
    st.session_state.html_output = ""

# Create inner agents
inner_assistant, inner_code_interpreter = create_inner_agents()
price_graph_agent, financials_graph_agent, peer_compare_graph_agent = create_graphics_agents()

# Create group chat manager
manager = create_groupchat_manager(inner_assistant, inner_code_interpreter)

# Create outer agents
assistant_1, assistant_2, writer, reviewer, user = create_outer_agents()

# Start conversation
if st.button('Start Conversation'):
    # Generate textual summary and conversation
    try:
        res_textual = initiate_nested_chat(assistant_1, manager, writer, reviewer, user, task)
    except Exception as e:
        st.error(f"Error during nested chat: {str(e)}")
        res_textual = None

    # Generate graphics
    try:
        res_graphics = initiate_graphical_chats(price_graph_agent, financials_graph_agent, peer_compare_graph_agent, user, task)
    except Exception as e:
        st.error(f"Error during graphical chat: {str(e)}")
        res_graphics = None

    # Process textual results
    if res_textual:
        for res in res_textual:
            if hasattr(res, 'conversation') and res.conversation:
                st.session_state.conversation_history.extend(res.conversation)

            if hasattr(res, 'summary') and res.summary:
                st.session_state.summary = res.summary

            if hasattr(res, 'html_output') and res.html_output:
                st.session_state.html_output = res.html_output

        st.subheader('Summary')
        if st.session_state.summary:
            st.write(st.session_state.summary)

    # Display financial visualizations
    st.subheader('Financial Visualizations')
    if res_graphics and hasattr(res_graphics, 'conversation'):
        for message in res_graphics.conversation:
            if 'graph' in message['content']:
                st.image(message['content']['graph'])  # Assuming the graph is returned as an image

    # Display conversation history
    st.subheader('Conversation History')
    if st.session_state.conversation_history:
        for i, message in enumerate(st.session_state.conversation_history):
            st.markdown(f"**Turn {i+1}:**")
            st.write(message['content'])

# Option to clear conversation history
if st.button('Clear Conversation History'):
    st.session_state.conversation_history = []
    st.session_state.summary = ""
    st.session_state.html_output = ""
    st.success("Conversation history cleared.")
