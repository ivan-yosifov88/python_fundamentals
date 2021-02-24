# user_line = input().split(", ")
#
# for user in user_line:
#     if not (3 <= len(user) <= 16):
#         continue
#
#     is_valid = True
#
#     for char in user:
#         if not (char.isalnum() or char == "-" or char == "_"):
#             is_valid = False
#             break
#     if user.isspace():
#         continue
#     if not is_valid:
#         continue
#     print(user)
def user_validation(user_name):
    if not (3 <= len(user_name) <= 16):
        return False
    for name in user_name:
        if not (name.isalnum() or name == "-" or name == "_"):
            return False
    if user_name.isspace():
        return False
    return True


user_line = input().split(", ")

for user in user_line:
    validator = user_validation(user)
    if validator:
        print(user)