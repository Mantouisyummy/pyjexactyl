from pyjexactyl import Jexactyl

api = Jexactyl(url="https://panel.bunnyhost.top/", api_key="ptla_EGVyuMVv7lSJ4PZNH2ikzOtJNYXfIcsihzLqcfaR1fn")

users = api.users.list_users()

for page in users:
    for user in page:
        print(user)