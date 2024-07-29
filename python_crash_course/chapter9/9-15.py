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

def check_ticket(played_ticket, winning_ticket):
    for element in played_ticket:
        if element not in winning_ticket:
            return False

def make_random_ticket(possibilities):
    """Return a random ticket from a set of possibilities."""
    ticket = []

    while len(ticket) < 4:
        pulled_item = choice(possibilities)
        if pulled_item not in ticket:
            ticket.append(pulled_item)

winning_ticket = winner_ticket_number(series)
my_ticket = [4,6,7,'d','e']
plays_count = 0
won = False
max_tries = 1000000

while not won:
    new_ticket = make_random_ticket(series)
    won = check_ticket(new_ticket, winning_ticket)
    plays_count += 1
    if plays_count >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")