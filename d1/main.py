with open('input.txt', 'r') as inp:
    cleaned = list(map(lambda r: int(r.strip()), list(inp)))
    for first in cleaned:
        for second in cleaned:
            for third in cleaned:
                if first + second + third == 2020:
                    print(first * second * third)
    