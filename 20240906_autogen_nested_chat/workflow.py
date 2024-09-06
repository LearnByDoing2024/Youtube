from datetime import datetime, timedelta

def writing_message(recipient, messages, sender, config):
    """
    Generates a message for the writer agent to polish the content into an engaging and well-formatted article or summary.
    """
    return f"Polish the content to make an engaging and nicely formatted blog post. \n\n {recipient.chat_messages_for_summary(sender)[-1]['content']}"

def generate_graphics_message(recipient, messages, sender, config):
    """
    Generates a message for the graphics agents to create a visual representation of the data provided.
    """
    return f"Generate a graphic for the data provided: \n\n {recipient.chat_messages_for_summary(sender)[-1]['content']}"

def initiate_graphical_chats(price_graph_agent, financials_graph_agent, peer_compare_graph_agent, user, task):
    graphical_chat_queue = [
        {"recipient": price_graph_agent, "message": generate_graphics_message, "summary_method": "last_msg", "max_turns": 1},
        {"recipient": financials_graph_agent, "message": generate_graphics_message, "summary_method": "last_msg", "max_turns": 1},
        {"recipient": peer_compare_graph_agent, "message": generate_graphics_message, "summary_method": "last_msg", "max_turns": 1},
    ]
    
    user.register_nested_chats(graphical_chat_queue, trigger=user)

    # Get current date and a range to ensure we're fetching recent data
    current_date = datetime.now()
    past_date = current_date - timedelta(days=365)  # last 1 year

    # Format the task to include date range
    task_with_dates = f"{task} between {past_date.strftime('%Y-%m-%d')} and {current_date.strftime('%Y-%m-%d')}"

    res = user.initiate_chat(recipient=price_graph_agent, message=task_with_dates, max_turns=1, summary_method="last_msg")
    return res

def initiate_nested_chat(assistant_1, manager, writer, reviewer, user, task):
    nested_chat_queue = [
        {"recipient": manager, "summary_method": "reflection_with_llm"},
        {"recipient": writer, "message": writing_message, "summary_method": "last_msg", "max_turns": 1},
        {"recipient": reviewer, "message": "Review the content provided.", "summary_method": "last_msg", "max_turns": 1},
        {"recipient": writer, "message": writing_message, "summary_method": "last_msg", "max_turns": 1},
    ]
    
    assistant_1.register_nested_chats(nested_chat_queue, trigger=user)

    # Get current date and a range to ensure we're fetching recent data
    current_date = datetime.now()
    past_date = current_date - timedelta(days=365)  # last 1 year

    # Format the task to include date range
    task_with_dates = f"{task} between {past_date.strftime('%Y-%m-%d')} and {current_date.strftime('%Y-%m-%d')}"

    res = user.initiate_chats([
        {"recipient": assistant_1, "message": task, "max_turns": 1, "summary_method": "last_msg"},
    ]) #change task to task with dates to impose a time range
    
    return res
