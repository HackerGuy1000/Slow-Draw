import os,openai,random
import requests  # request img from web
import shutil  # save img locally

def generatePrompt():
    

    openai.api_key= os.getenv("OPEN_API_KEY")

    text = "Here is a list of simple 10 pixel art ideas that are seperated new lines in no numerical order"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"user","content":text}
        ],
        temperature=1,
        max_tokens=50

    )
    ideas = completion.choices[0].message["content"].split("\n")
    prompt = ideas[random.randint(0,len(ideas)-1)]
    return prompt
def generateImage(game):
    print("generating image")
    file_name = "generatedImg.png"

    openai.api_key = os.getenv("OPEN_API_KEY")

    response = openai.Image.create(
        prompt=game+" as 64 bit pixel art",
        n=1,
        size="1024x1024")
    image_url = response['data'][0]['url']
    res = requests.get(image_url, stream=True)

    if res.status_code == 200:
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ', file_name)
    else:
        print('Image Couldn\'t be retrieved')

    print(image_url)
