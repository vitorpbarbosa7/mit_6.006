u = 65
n = 4

c = 1 + ((u + 1).bit_length() // n.bit_length())

# digits = []
# high = u

# for j in range(c):
#     high, low = divmod(high, n)
#     digits.append(low)

# digits.reverse()

# print(digits)