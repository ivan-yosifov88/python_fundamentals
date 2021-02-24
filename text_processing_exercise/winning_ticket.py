ticket_to_check = input().split(",")
ticket_to_check = [ticket.strip() for ticket in ticket_to_check]
winning_symbol = ['@', '#', '$', '^']
for ticket in ticket_to_check:
    left_part = ticket[:len(ticket)//2]
    right_part = ticket[len(ticket)//2:]
    if not len(ticket) == 20:
        print("invalid ticket")
        continue
    else:
        for symbol in winning_symbol:
            left = left_part.count(symbol)
            right = right_part.count(symbol)
            count = min(left, right)
            symbol_check = count * symbol
            if 6 <= count < 10 and symbol_check in left_part and symbol_check in right_part  :
                print(f'ticket "{ticket}" - {count}{symbol}')
                break
            elif left == right == 10:
                print(f'ticket "{ticket}" - {left}{symbol} Jackpot!')
                break
            else:
                continue
        else:
            print(f'ticket "{ticket}" - no match')

