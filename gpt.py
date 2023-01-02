import os
import openai

from dotenv import load_dotenv 

def config():
  load_dotenv()

config()

openai.api_key = os.getenv("OPENAI_API_KEY")



def captionMaker(name, location, labels, dishName):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt= f"""Write 1 caption for an Instagram post. Restaurant name and other details have been provided. Also use relevant hastags. 
    Name: {name}
    Location: {location}
    Dish name: {dishName}
    Labels: {labels}""", 
    temperature=1,
    max_tokens=250,
    top_p=1,
    frequency_penalty=2,
    presence_penalty=2
  )
  return response.choices[0].text