current_users = ["JACK", "mike", "Sarah", "Rick", "omar"]
current_users = [user.lower() for user in current_users]

print(current_users)

new_users = ["peter", "jack", "Emma", "RICK"]

for new_user in new_users:
    if new_user.lower() not in current_users:
        print(f"Username Available: {new_user}")
    elif new_user.lower() in current_users:
        print("Username is already taken")
    else:
        print("data error")