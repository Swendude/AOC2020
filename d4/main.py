import re
# Deel 1
# with open('input.txt','r') as inpf:
#     inp = inpf.read()

# required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', ]
# valid = 0
# for passport_txt in str(inp).split("\n\n"):
#     found = []
#     for prop in passport_txt.replace("\n"," ").split(" "):
#         if prop.split(":")[0] in required:
#             found.append(prop)
#     if len(found) == len(required):
#         valid += 1

# print(valid)

# Deel 2


def validate_range(text, max_num, min_num,):
    if text.isdigit():
        num = int(text)
        return max_num >= num >= min_num
    else:
        return False


def validate_hgt(text):
    unit = value[-2:]
    if unit == 'cm':
        return validate_range(value[:-2], 193, 150)
    elif unit == 'in':
        return validate_range(value[:-2], 76, 59)
    else:
        return False

def validate_hcl(text):
    pattern = re.compile(r'^#([a-f0-9]){6}$')
    match = re.match(pattern, text)
    if not match:
        return False
    return True


def validate_ecl(text):
    return text in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def validate_pid(text):
    pattern = re.compile(r'^[0-9]{9}$')
    match = re.match(pattern, text)
    if not match:
        return False

    return True


with open('input.txt', 'r') as inpf:
    inp = inpf.read()

required_validators = {'byr': lambda x: validate_range(x,  2002, 1920),
                       'iyr': lambda x: validate_range(x, 2020, 2010),
                       'eyr': lambda x: validate_range(x, 2030, 2020),
                       'hgt': validate_hgt,
                       'ecl': validate_ecl,
                       'hcl': validate_hcl,
                       'pid': validate_pid
                       }
valids = 0

for passport_txt in str(inp).split("\n\n"):
    keys = []
    valid = []
    invalids = []
    pp_d = {}
    for prop in passport_txt.replace("\n", " ").split(" "):
        key, val = prop.split(":")
        pp_d[key] = val
    if 'cid' in pp_d:
        pp_d.pop('cid')
    
    if pp_d.keys() != required_validators.keys():
        continue
    else:
        for key,value in pp_d.items():
            # print(value)
            # print(required_validators[key](value))
            pp_d[key] = required_validators[key](value)
        if all(pp_d.values()):
            valids += 1
        

print(valids)

