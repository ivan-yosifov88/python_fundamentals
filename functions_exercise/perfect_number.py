def perfect_number(num):
    sum_checker = 0
    for number in range(1, num):
        if num % number == 0:
            sum_checker += number
    if sum_checker == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())

perfect_number(number)