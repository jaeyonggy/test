from pretty_print import pretty_print_messages
from agents.supervisor_agent_scratch_description import supervisor_with_description
from langchain_core.messages import BaseMessage, AIMessage
from agents.car_info_agent import car_info_agent

if __name__ == "__main__":

    for chunk in car_info_agent.stream(
        {"messages": [{"role": "user", "content": "G80 가격이 얼마야?"}]}
    ):
        pretty_print_messages(chunk)

    # for chunk in math_agent.stream(
    #     {"messages": [{"role": "user", "content": "what's (3 + 5) x 7"}]}
    # ):
    #     pretty_print_messages(chunk)


    # # Display image of the architecture
    # with open("graph.png", "wb") as f:
    #     f.write(supervisor.get_graph().draw_mermaid_png())


    # for chunk in supervisor_with_description.stream(
    #     {
    #         "messages": [
    #             {
    #                 "role": "user",
    #                 "content": "find US and New York state GDP in 2024. what % of US GDP was New York state?",
    #             }
    #         ]
    #     },
    #     subgraphs=True,
    # ):
    #     pretty_print_messages(chunk, last_message=True)
    #     pass 

    # print(chunk)
    # final_message_history = chunk["supervisor"]["messages"]
    # for message in final_message_history:
    #     message.pretty_print()


    config = {
        "configurable": {
            "thread_id": "multi_turn_session_1"  # consistent thread ID for memory
        }
    }

    # print("💬 Multi-turn conversation started. Type 'exit' to stop.")
    # while True:
    #     user_input = input("👤 You: ")
    #     if user_input.lower() in ["exit", "quit"]:
    #         break

    #     result = supervisor_with_description.invoke({
    #         "messages": [{"role": "user", "content": user_input}]
    #     }, config=config)

    #     print("🤖 Agent:")
    #     for msg in result["messages"]:
    #         if isinstance(msg, AIMessage):
    #             print(msg.content)

    # print("💬 Multi-turn conversation started. Type 'exit' to stop.")

    # while True:
    #     user_input = input("👤 You: ")
    #     if user_input.lower() in ["exit", "quit"]:
    #         break

    #     print("🤖 Agent:")

    #     # Initialize a variable to store the final assistant message
    #     final_message = None

    #     # Stream the response from the graph
    #     for message_chunk, metadata in supervisor_with_description.stream(
    #         {
    #             "messages": [{"role": "user", "content": user_input}]
    #         },
    #         config=config,
    #         stream_mode="messages",  # Ensure this mode is set for message streaming
    #         # subgraphs=True  # Include if using subgraphs
    #     ):
    #         # Optionally, use pretty_print_messages to format the output
    #         # pretty_print_messages((message_chunk, metadata), last_message=True)

    #         # Display the content of the message chunk
    #         if message_chunk.content:
    #             print(message_chunk.content, end="", flush=True)

    #         # Store the final assistant message
    #         if isinstance(message_chunk, AIMessage):
    #             final_message = message_chunk

    #     # Optionally, print a newline after the assistant's response
    #     print()


    # print("💬 Multi-turn conversation started. Type 'exit' to stop.")

    # while True:
    #     user_input = input("👤 You: ")
    #     if user_input.lower() in ["exit", "quit"]:
    #         break

    #     print("🤖 Agent:")

    #     for chunk in supervisor_with_description.stream(
    #         {
    #             "messages": [
    #                 {
    #                     "role": "user",
    #                     "content": user_input,
    #                 }
    #             ]
    #         },
    #         subgraphs=True,
    #     ):
    #         pretty_print_messages(chunk, last_message=True)



