from pretty_print import pretty_print_messages
from agents.supervisor_agent_scratch import supervisor

if __name__ == "__main__":

    # for chunk in research_agent.stream(
    #     {"messages": [{"role": "user", "content": "who is the mayor of NYC?"}]}
    # ):
    #     pretty_print_messages(chunk)

    # for chunk in math_agent.stream(
    #     {"messages": [{"role": "user", "content": "what's (3 + 5) x 7"}]}
    # ):
    #     pretty_print_messages(chunk)


    # # Display image of the architecture
    # with open("graph.png", "wb") as f:
    #     f.write(supervisor.get_graph().draw_mermaid_png())


    # for chunk in supervisor.stream(
    #     {
    #         "messages": [
    #             {
    #                 "role": "user",
    #                 "content": "find US and New York state GDP in 2024. what % of US GDP was New York state?",
    #             }
    #         ]
    #     },
    #     # subgraphs=True,
    # ):
    #     pretty_print_messages(chunk, last_message=True)
    #     pass 

    # final_message_history = chunk["supervisor"]["messages"]
    # for message in final_message_history:
    #     message.pretty_print()


    config = {
        "configurable": {
            "thread_id": "multi_turn_session_1"  # consistent thread ID for memory
        }
    }

    print("💬 Multi-turn conversation started. Type 'exit' to stop.")
    while True:
        user_input = input("👤 You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        result = supervisor.invoke({
            "messages": [{"role": "user", "content": user_input}]
        }, config=config)

        print("🤖 Agent:")
        for msg in result["messages"]:
            print(msg.content)




