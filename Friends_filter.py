from urllib.parse import urlencode

import requests

AUTHORIZER_URL = "https://oauth.vk.com/authorize"
APP_ID = "6259910"
VERSION = "5.69"

# auth_data = {
#     "client_id": APP_ID,
#     "redirect_uri": "https://oauth.vk.com/blank.html",
#     "display": "page",
#     "scope": "friends",
#     "response_type": "token",
#     "v": VERSION
# }

# print("?".join((AUTHORIZER_URL, urlencode(auth_data))))

TOKEN = ""


def get_my_friends_list():     # возвращает список id моих друзей
    params = {

        "access_token": TOKEN,
        "v": VERSION
    }
    response = requests.get("https://api.vk.com/method/friends.get", params)
    friends = response.json()["response"]["items"]
    return friends


def get_friends_of_my_friends(friends):  # ищет общих друзей среди моих друзей и возвращает список с их id

    my_friend_list = []

    for friend in friends:
        user = str(friend)
        params = {
            "user_id": user,
            "access_token": TOKEN,
            "v": VERSION
        }

        resp = requests.get("https://api.vk.com/method/friends.get", params)
        if friend == get_my_friends_list()[0]:
            my_friend_list = resp.json()["response"]["items"]
        try:
            my_friend_list1 = resp.json()["response"]["items"]  # в этой операции выдает ошибку, если не обрабатывать
        except Exception:
            continue
        my_friend_list = list(set(my_friend_list) & set(my_friend_list1))
    return my_friend_list

print(get_friends_of_my_friends(get_my_friends_list()))

