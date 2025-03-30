janes_followers = {}

while True:
    part_command = input()
    if part_command == "Log out":
        break
    parts = part_command.split(": ")
    command = parts[0]
    username = parts[1]
    if command == "New follower":
        if username in janes_followers:
            continue
        else:
            janes_followers[username]=[0,0]
    elif command == "Like":
        count = int(parts[2])
        if username not in janes_followers:
            janes_followers[username]=[count,0]
        else:
            janes_followers[username][0] += count
    elif command == "Comment":
        if username not in janes_followers:
            janes_followers[username]=[0,1]
        else:
            janes_followers[username][1] += 1
    elif command == "Blocked":
        if username not in janes_followers:
            print(f"{username} doesn't exist.")
        else:
            del janes_followers[username]

print(f"{len(janes_followers)} followers")
for users, like_comment in janes_followers.items():
    print(f"{users}: {like_comment[0] + like_comment[1]}")