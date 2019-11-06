houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house", "Ali baba"]

# Each function call represents an elf doing his work
def deliver_presents_recursively(houses):
    # Worker elf doing his work
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)

    # Manager elf doing his work
    else:
        mid = len(houses) // 2
        #print("len", mid)
        first_half = houses[:mid]
        #print("first half", first_half)
        second_half = houses[mid:]
        #print("second half", second_half)

        # Divides his work among two elves
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)


def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)


#deliver_presents_recursively(houses)
print(factorial_recursive(5))