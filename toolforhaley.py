import openai
from gtts import gTTS
import os
from playsound import playsound

def main():
    language = 'en'
    openai.api_key = "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"
    # Set up the model and prompt
    model_engine = "text-davinci-003"
    print("Please give me a story prompt. For example, tell me to write a romantic fanfiction about Snape and the Naval Academy Women's Rugby Team.")
    prompt = input("Prompt: ")
    #prompt = "Write me a romantic fanfiction about Snape and the Naval Academy Women's Rugby Team."

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=1,
    )
    response = completion.choices[0].text
    print(response)
    myobj = gTTS(text=response, lang=language, slow=False, tld='co.uk')
    myobj.save("story.mp3")
    playsound("story.mp3")
    print("Saved story to 'story.mp3'")

if __name__ == "__main__":
    main()
