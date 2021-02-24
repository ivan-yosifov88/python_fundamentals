year = int(input())
while True:
    year += 1
    new_year = ""
    # for nums in str(year):
    #     if nums not in new_year:
    #         new_year += nums
    # if len(str(year)) == len(new_year):
    #     print(new_year)
    #     break
    for nums in str(year):
        new_year += nums
        counter = 0
        num_check = ""
        for num in (nums, len(str(year))):
            num_check += num
            if new_year in num:
                counter += 1
                if counter == 2:
                    break
