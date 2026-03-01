import os
from dotenv import load_dotenv , dotenv_values
load_dotenv()
import requests
from config import NEWS_API_KEY
URL = "https://newsapi.org/v2/top-headlines"


# def get_news():
parameters = {
    "category" : "technology",
    "language" : "en",
    "pageSize" : 5,
    "apiKey" : os.getenv("NEWS_API_KEY"),
}
# proxies = {
#     "http": f"http://{os.getenv('LDAP_USRNAME')}:{os.getenv('LDAP_PASSWD')}@192.168.10.87:8080",
#     "https": f"https://{os.getenv('LDAP_USRNAME')}:{os.getenv('LDAP_PASSWD')}@192.168.10.87:8080",
# }
# headers = {
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
#     }
def fetch_news_as_msg():
    try:
        news_response = requests.get(url=URL,params=parameters)
        news_response.raise_for_status()
        news_data = news_response.json()
        req_news_data = news_data['articles'][0:2]
        return req_news_data
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred {e}")
