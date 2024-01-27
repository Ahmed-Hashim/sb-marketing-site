import requests
import environ

env = environ.Env()
access = env("FB_TOKEN")
page_ID = env("PAGE_ID")


def uptofb(link, mes):
    post = f"https://graph.facebook.com/{page_ID}/photos?url={link}&message={mes}&access_token={access}"
    response = requests.post(post)
    print(response.json())
    return response.json()
