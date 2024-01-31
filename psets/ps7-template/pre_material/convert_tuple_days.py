
input = (13, 25, 14, 2, 9, 17, 16, 13, 10, 16)
n = 5
k = 2

def convert_prices(input, n, k):

    result = []
    for i in range(0, len(input), k):
        result.append(input[i:i+k])

    return result

result = convert_prices(input, n, k)
print(result)