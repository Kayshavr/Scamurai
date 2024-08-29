from openai import OpenAI
import os

def chat_with_gpt(prompt):

    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model="gpt-3.5-turbo",
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input ("You: ")
        if user_input. lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print ("Chatbot: ", response)