#!/bin/python3
import tweepy
import keys
import openai

#get necessary OpenAI api key from keys.py file. Key must be defined in keys.py
# WARNING: You must have an OpenAI account and an API key to run this program. 

openai.api_key = (keys.openaiAPI_Key)

#This model uses the latest text-davinci-003 model but you can change it to any available text models by changing the model= section to your desired model
#The default prompt can be changed to anything of your liking by replacing the default prompt with your prompt inside the quotes.
#Try playing around in the openai playground to get the perfect prompt for you!
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=('Generate a tweet that is deep and inspirational'),
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
  )

#Extract the text answer from the openai api response list
tweetext = (response["choices"][0]["text"])

#Tweepy Twitter api authentication (make sure all keys required are defined in keys.py file and that keys.py is in same location as the aitweet.py file)
def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)

    return tweepy.API(auth)

#Update the twitter status by sending the openAI text response to tweepy api update_status, then print a confirmation message
def tweet(api: tweepy.API, message: str):
    api.update_status(tweetext)

    print('Tweeted successfully!')

tweet(api(), tweetext)
