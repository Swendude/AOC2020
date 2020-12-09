from itertools import combinations  

with open('input.txt', 'r') as f:
    lines = [int(line) for line in f]


def pairwise_sums(numbers):
    # Beware: monkey code below
    pairs = []
    for n in numbers:
        for m in numbers:
            pairs.append((n,m))
    pairs = set(pairs)

    return [p1 + p2 for (p1, p2) in pairs]

target = None

for i, n in enumerate(lines):
    if i >= 25:
        preamble = lines[i-25:i]
        if n in pairwise_sums(preamble):
            continue
        else:
            target = n
            print('Part 1:', n)
            break

def sublists(l): 
  # list to store all the sublists 
  sublist = [[]] 
  
  for i in range(len(l) + 1): 
    for j in range(i + 1, len(l) + 1): 
      sli = l[i:j]  # make a slice of the subarray 
      sublist.append(sli) #add it to the list of sublists
            
  return sublist 


ranges = sublists(lines)
for r in ranges:
    if len(r) > 1:
        if sum(r) == target:
            print('Part 2:', max(r) + min(r))
            break
