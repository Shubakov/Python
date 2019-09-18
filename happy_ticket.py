def is_happy_ticket(ticket):
    if len(ticket) % 2 == 1:
        return False
    first_half_numbers = ticket[:len(ticket) // 2]
    second_half_numbers = ticket[len(ticket) // 2:]
    return sum(map(int, list(first_half_numbers))) == sum(map(int, list(second_half_numbers)))


print(is_happy_ticket(''))
