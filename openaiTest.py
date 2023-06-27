import openai
from config import apikey #create a config file and add your api key there.
import os

def AI(prompt):
    openai.api_key = apikey
    text = f"openAI response for Prompt: {prompt} \n************************\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text += response["choices"][0]["text"]

    if not os.path.exists("openAI"):
        os.mkdir("openAI")
    with open(f"openAI/{''.join(prompt.split('AI')[1:]).strip()}.txt", "w") as f:
        f.write(text)
        f.close()

# ---------------------------------------------------------------------------------------

'''
{
  "id": "cmpl-7UzpGSyms2RctUAWVcoW3OQ4KrBYu",
  "object": "text_completion",
  "created": 1687621854,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "\n\nTo: [Supervisor's Name]\n\nFrom: [Your Name]\n\nSubject: Request for Sick Leave\n\nDate: [date]\n\nI am writing to request a sick leave of absence from my position.\n\nI am suffering from [illness], which requires that I take some time away from work to allow me to recover. My doctor has recommended that I take [time frame] off of work to rest and recuperate.\n\nI understand that this absence may cause disruption, and I am willing to work with you to make sure that my work is covered while I am off. I am confident that I will be able to return to work feeling refreshed and ready to resume my job.\n\nThank you for your understanding. I will look forward to hearing from you regarding my sick leave request.\n\nSincerely,\n\n[Your Name]",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 6,
    "completion_tokens": 182,
    "total_tokens": 188
  }
}
'''
