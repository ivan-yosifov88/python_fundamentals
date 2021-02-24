command = input()

is_no_need_to_sleep = True
counter = 0
while not command == "END":
    event = command
    if event.isupper():
        if event.lower() == "coding" or event.lower() == "cat" or event.lower() == "dog" or event.lower() == "movie":
            counter += 2
    elif event == "coding" or event == "cat" or event == "dog" or event == "movie":
        counter += 1
    # if counter >= 5:
    #     print("You need extra sleep")
    #     is_no_need_to_sleep = False
    #     break
    command = input()
if counter > 5:
    print("You need extra sleep")
else:
    print(counter)

