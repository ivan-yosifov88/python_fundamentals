version_list = input().split(".")
version_number = "".join(version_list)
new_version = str(int(version_number) + 1)
print(".".join(new_version))