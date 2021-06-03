# read any thing from user or internet

from win32com.client import Dispatch
import requests
import json


def speak(str):

    speak = Dispatch('SAPI.SpVoice')
    speak.Speak(str)

if __name__ == '__main__' :
    speak("Good Morning Sir")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=534e78adcd2a4725b9a501e53f262235"
    news = requests.get(url).text       # req the content as text format(converts it into text format)
    news_dict = json.loads(news)             # converts into python object(parsed the object)
    # print(news_dict["articles"])
    arts = news_dict["articles"]
    # print(type(arts))
    # print(arts)
    for art_lst in arts:
         if art_lst["source"]["name"] in "NDTV News":            # print the news only from NDTV News
             speak(art_lst["description"])
             speak("Moving on to the next news.")

    print("Thanks for Listing")