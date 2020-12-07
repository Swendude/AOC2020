import re

valids = 0
input_pattern = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]+)')
with open('input.txt', 'r') as inp:
    for line in inp:
        match = re.match(input_pattern, line)
        
        pw = match.group(4)
        print(match.group(3))
        if (pw[int(match.group(1)) - 1] == match.group(3)) != (pw[int(match.group(2)) - 1] == match.group(3)):
            valids += 1
        
print(valids)