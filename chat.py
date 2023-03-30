import os,openai

openai.api_key= os.getenv("OPEN_API_KEY")

text = input("Write text to be completed: ")

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"user","content":text}
    ],
    temperature=0,
    max_tokens=50

)
print(text + completion.choices[0].message["content"])