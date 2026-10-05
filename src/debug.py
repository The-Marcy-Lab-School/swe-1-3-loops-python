def broken_loop(start, end):
    result = ""
    for i in range(start, end, 2):
        result += str(i)
    return result


def broken_nested():
    result = ""
    for i in range(2):
        for i in range(10):
            result += f"-{i}{i}"
    return result[1:]
