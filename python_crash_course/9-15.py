from random import choice
series = [1,2,3,4,5,6,7,8,9,10, 'a', 'b', 'c', 'd', 'e']
"""
def winner_ticket_number(ticket_list):
    for i in range(4):
        print(choice(ticket_list), end='')
"""
def winner_ticket_number(ticket_list):
    i = 4
    ticket = []
    while(i != 0):
        ticket.append(choice(ticket_list))
        i = i - 1
    return ticket

my_ticket = [4,6,7,'d','e']
count = 0

for i in range(4):
    for j in range(4):
        if()
print('')