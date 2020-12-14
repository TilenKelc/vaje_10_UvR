
prepovedani = [
    (12, 18),
    (2, 5),
    (3, 8),
    (0, 4),
    (15, 19),
    (6, 9),
    (13, 17),
    (4, 8)
]

max_st = 0
for (_, max_i) in prepovedani:
    if max_st < max_i:
        max_st = max_i
print(max_st)

# -----------

i = 0
while i <= max_st:
    for (min_i, max_i) in prepovedani:
        if min_i <= i <= max_i:
            print(i, 'je vsebovan v ({}, {})'.format(min_i, max_i))
            break
    else:
        print(i, 'je dovoljeno')
    i += 1

# ------------

""" Dodatna naloga
prepovedani = [
    (12, 18),
    (2, 5),
    (3, 8),
    (0, 4),
    (15, 19),
    (6, 9),
    (13, 17),
    (4, 8),
    (9, 12)
]

max_st = 0
for (_, max_i) in prepovedani:
    if max_st < max_i:
        max_st = max_i
check = []
i = 0
while i <= max_st:
    for (min_i, max_i) in prepovedani:
        if min_i <= i <= max_i:
            check.append(True)
            break
    else:
        print(i, 'je dovoljeno')
        check.append(False)
        break
    i += 1
if False not in check:
    print(20)
"""
