keyauthapp = api(
    name = "Nightmare-Remade",
    ownerid = "a8IXKWR4OX",
    secret = "e598dd522e146ff5a7112a2eded49f05e0613412f0cd9072a4ad53dd7e3cbb88",
    version = "1.0",
    hash_to_check = getchecksum()
)

print(f"""
App data:
Number of users: {keyauthapp.app_data.numUsers}
Number of online users: {keyauthapp.app_data.onlineUsers}
Number of keys: {keyauthapp.app_data.numKeys}
Application Version: {keyauthapp.app_data.app_ver}
Customer panel link: {keyauthapp.app_data.customer_panel}
""")

print(f"Current Session Validation Status: {keyauthapp.check()}")

key = input('Enter your license: ')
keyauthapp.license(key)
