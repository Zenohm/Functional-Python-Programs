def dragon(iterations):
    directions = [False]
    app = directions.append
    for counter in range(iterations):
        gen = (not(directions[digit]) for digit in reversed(range(len(directions))))
        app(False)
        for elements in gen:
            app(elements)
    return directions

def bitwise_booleanize(data):
    return [1 if elem else 0 for elem in data]

def format_dragon(iterations):
    return ''.join(map(str,bitwise_booleanize(dragon(iterations))))

