import openai
from config import apikey
chatStr = ""


def chat(prompt):
    global chatStr
    openai.api_key = apikey
    chatStr += f"Zain: {prompt}\nFriday: "

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    chatStr += f"{response['choices'][0]['text']}"
    return response['choices'][0]['text']
