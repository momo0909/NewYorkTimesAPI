from Project2_Flask import main_functions
import requests


def request_key():
    api_dict = main_functions.read_from_file("Project2_Flask/JSON_Files/api_key.json")
    return api_dict['key']


def request_newly_api(section):
    url1 = "https://api.nytimes.com/svc/news/v3/content/all/" + section + ".json?api-key=" + request_key()

    response1 = requests.get(url1).json()  # serializes the url
    return response1


def best_Sellers(genre):
    url2= "https://api.nytimes.com/svc/books/v3/lists/current/"+ genre +".json?api-key=" + request_key()

    response2 = requests.get(url2).json()
    return response2