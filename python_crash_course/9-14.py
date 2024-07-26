from random import choice
series = (1,2,3,4,5,6,7,8,9,10, 'a', 'b', 'c', 'd', 'e')

def winner_ticket_number(ticket_list):
    for i in range(4):
        print(choice(ticket_list))

winner_ticket_number(series)