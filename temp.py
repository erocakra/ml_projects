user = api.me()
print(user.screen_name)
print(user.followers_count)
count = 0
for friend in user.friends():
    print(friend.screen_name)
    count += 1
print(count)
print("===================")
