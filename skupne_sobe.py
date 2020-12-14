# Zaporedje stevil
x = 0
i = 0
while i < 1000:
    print(x)
    x = ((1664525 * x) + 1013904223) % (2 ** 32)
    i += 1

# Zaporedje sob
x = 0
i = 0
st = 0
while i < 1000:
    if x % 10 == 6:
        st += 1
    x = ((1664525 * x) + 1013904223) % (2 ** 32)
    i += 1
print('V sobi številka 6 je bila:', st)

# Srecanja
st_a = 0
st_b = 0
i = 0
st = 0
while i < 1000:
    if (st_a % 10) == (st_b % 10):
        st += 1
    st_a = ((1664525 * st_a) + 1013904223) % (2 ** 32)
    st_b = ((22695477 * st_b) + 1) % (2 ** 32)
    i += 1
print('Srečali sta se:', st)
