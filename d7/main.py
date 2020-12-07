import pprint

with open('input.txt') as f:
    inputs = [line for line in f]

bags_can_contain = {}

def contents_lists(text):
    result = []
    parts = text.split(',')
    for part in parts:
        cleaned = part.strip().replace('.', '')
        amount, _type = cleaned.split(" ")[0], ' '.join(cleaned.split(" ")[1:])
        result.append((amount, _type))
    return result

for inp in inputs:
    container, contents = inp.split('contain')
    bags_can_contain[container.strip()] = contents_lists(contents)

bag_can_be_contained_by = {}
for bag, containables in bags_can_contain.items():
    for amount, containable in containables:
        if containable in bag_can_be_contained_by:
            bag_can_be_contained_by[containable].add(bag)
        else:
            bag_can_be_contained_by[containable] = set([bag])

# targets = ['shiny gold bags']
# can_hold_me = set()
# ended = False
# i = 0
# while not ended:
#     if targets == []:
#         ended = True
#     new_targets = []
#     for target in targets:
#         if target in bag_can_be_contained_by:
#             parents = set(bag_can_be_contained_by[target])
#             can_hold_me = can_hold_me.union(set(zip([i * len(parents)], parents)))
#             new_targets = new_targets + list(parents)
#     targets = list(set(new_targets))
#     i += 1

# pprint.pprint(sorted(can_hold_me))
# print(len(can_hold_me))
# ended = False

#     if targets == []:
#         ended = True
#     for target in targets:
#             can_hold_me = can_hold_me.union(set(bag_can_be_contained_by[target]))
#     targets = list(set(new_targets))

# print(len(set(ends)))


# pprint.pprint(bags_can_contain['clear gray bags'])
pprint.pprint(bag_can_be_contained_by['shiny gold bags'])