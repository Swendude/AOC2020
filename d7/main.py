import pprint
from collections import defaultdict
import re
bags_can_contain = defaultdict(list)
bag_can_be_contained_by = defaultdict(list)

with open('input.txt') as f:
    for line in f:
        container, contents = line.split('contain')
        contents = re.findall(r'(\d+) ([a-z ]+) [bag|bags,. ]+', contents)
        container = re.match(r'([a-z ]+) bags', container).groups()[0]
        for content in contents:
            bags_can_contain[container].append(content)
            bag_can_be_contained_by[content[1]].append(container)

rows = [['shiny gold']]
parents_checked = set()
new_parents = True
while new_parents:
    new_row = []
    new_parents = False
    for bag in rows[-1]:
        if bag in bag_can_be_contained_by:
            new_row = new_row + list(bag_can_be_contained_by[bag])
            new_parents = True
    if new_row: rows.append(new_row)

flat = [b for r in rows[1:] for b in r]
print(len(set(flat)))