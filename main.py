from pretty_print import pretty_print_messages
from agents.supervisor_agent_v1 import supervisor

if __name__ == "__main__":

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

        print("🤖 Agent:")

        for chunk in supervisor.stream(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": user_input,
                    }
                ]
            },
            subgraphs=True,
        ):
            pretty_print_messages(chunk, last_message=True)



