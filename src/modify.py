def while_to_for():
    i = 0
    while i < 5:
        print(i)
        i += 1


def continue_guard_clause():
    for i in range(1, 5):
        # Add a guard clause to skip 2 and 3
        print("Sure glad this isn't 2 or 3")
        print(i)
