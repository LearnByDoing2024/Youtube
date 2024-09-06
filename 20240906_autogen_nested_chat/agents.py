import autogen
from config import get_llm_config

# Define the inner agents used in group chats
def create_inner_agents():
    llm_config = get_llm_config("Inner-Agent-Config")  # Ensure this key exists or fallback is handled

    inner_assistant = autogen.AssistantAgent(
        "Inner-assistant",
        llm_config=llm_config,
        is_termination_msg=lambda x: x.get("content", "").find("TERMINATE") >= 0,
    )

    inner_code_interpreter = autogen.UserProxyAgent(
        "Inner-code-interpreter",
        human_input_mode="NEVER",
        code_execution_config={
            "work_dir": "coding",
            "use_docker": False,
        },
        default_auto_reply="",
        is_termination_msg=lambda x: x.get("content", "").find("TERMINATE") >= 0,
    )

    return inner_assistant, inner_code_interpreter

def create_graphics_agents():
    llm_config = get_llm_config("Graphics-Agent-Config")

    price_graph_agent = autogen.AssistantAgent(
        name="PriceGraphAgent",
        llm_config=llm_config,
        system_message="""
        Your task is to generate a line chart displaying stock price trends over a given period.
        """,
    )

    financials_graph_agent = autogen.AssistantAgent(
        name="FinancialsGraphAgent",
        llm_config=llm_config,
        system_message="""
        Your task is to generate a bar chart displaying key financial metrics such as revenue, net income, and EBITDA.
        """,
    )

    peer_compare_graph_agent = autogen.AssistantAgent(
        name="PeerCompareGraphAgent",
        llm_config=llm_config,
        system_message="""
        Your task is to generate a comparative bar chart showing key financial metrics of the company against its peers.
        """,
    )

    return price_graph_agent, financials_graph_agent, peer_compare_graph_agent

def create_groupchat_manager(inner_assistant, inner_code_interpreter):
    groupchat = autogen.GroupChat(
        agents=[inner_assistant, inner_code_interpreter],
        messages=[],
        speaker_selection_method="round_robin",
        allow_repeat_speaker=False,
        max_round=8,
    )

    manager = autogen.GroupChatManager(
        groupchat=groupchat,
        is_termination_msg=lambda x: x.get("content", "").find("TERMINATE") >= 0,
        llm_config=get_llm_config("Manager-Config"),  # Make sure this config is defined or fallback
        code_execution_config={
            "work_dir": "coding",
            "use_docker": False,
        },
    )
    return manager

# Define the outer agents used in the main task
def create_outer_agents():
    llm_config = get_llm_config("Outer-Agent-Config")  # General fallback or defined key

    assistant_1 = autogen.AssistantAgent(
        name="Assistant_1",
        llm_config=llm_config,
    )

    assistant_2 = autogen.AssistantAgent(
        name="Assistant_2",
        llm_config=llm_config,
    )

    writer = autogen.AssistantAgent(
        name="Writer",
        llm_config=llm_config,
        system_message="""
        You are a professional writer, known for
        your insightful and engaging articles.
        You transform complex concepts into compelling narratives.
        """,
    )

    reviewer = autogen.AssistantAgent(
        name="Reviewer",
        llm_config=llm_config,
        system_message="""
        You are a compliance reviewer, known for your thoroughness and commitment to standards.
        Your task is to scrutinize content for any harmful elements or regulatory violations, ensuring
        all materials align with required guidelines.
        """,
    )

    user = autogen.UserProxyAgent(
        name="User",
        human_input_mode="NEVER",
        is_termination_msg=lambda x: x.get("content", "").find("TERMINATE") >= 0,
        code_execution_config={
            "last_n_messages": 1,
            "work_dir": "tasks",
            "use_docker": False,
        }
    )

    return assistant_1, assistant_2, writer, reviewer, user
