def contain_func(key, word):
    if word in key:
        print(f"{key} contains {word}")
    else:
        print("Substring not found!")


def flip_func(key, comm, start_i, end_i):
    if comm == "Upper":
        result = key[start_i:end_i].upper()
    elif comm == "Lower":
        result = key[start_i:end_i].lower()
    key = key[:start_i] + result + key[end_i:]
    print(key)

    return key


def slice_func(key, start_i, end_i):
    key = key[:start_i] + key[end_i:]
    print(key)
    return key


activation_key = input()
data = input()

while not data == "Generate":
    command = data.split(">>>")[0]
    if command == "Contains":
        substring = data.split(">>>")[1]
        contain_func(activation_key, substring)
    elif command == "Flip":
        new_command, start, end = data.split(">>>")[1:4]
        start = int(start)
        end = int(end)
        activation_key = flip_func(activation_key, new_command, start, end)
    elif command == "Slice":
        start, end = data.split(">>>")[1:3]
        start = int(start)
        end = int(end)
        activation_key = slice_func(activation_key, start, end)

    data = input()
print(f"Your activation key is: {activation_key}")