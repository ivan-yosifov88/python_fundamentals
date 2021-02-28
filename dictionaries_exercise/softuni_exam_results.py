data = input()

result = {}
submission = {}
while not data == "exam finished":
    if len(data.split("-")) > 2:
        username, language, points = data.split("-")
        points = int(points)
        if language not in submission:
            submission[language] = 0
        submission[language] += 1
        if username not in result:
            result[username] = []
        result[username].append(points)
    else:
        username, new_command = data.split("-")
        if username in result:
            result.pop(username)
    data = input()

print("Results:")

sorted_result = sorted(result.items(), key=lambda x: (-max(x[1]), x[0]))
for user, point in sorted_result:
    print(f"{user} | {max(point)}")
sorted_submission = sorted(submission.items(), key=lambda x: (-x[1], x[0]))

print("Submissions:")
for language, submits in sorted_submission:
    print(f"{language} - {submits}")


