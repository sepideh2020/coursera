product = "iphone and android phones"

lett_d = {}
for char in product:
    if char not in lett_d:
        lett_d[char] = 0
    lett_d[char] = lett_d[char] + 1

dic_keys = lett_d.keys()
max_value = list(lett_d.keys())[0]

for key in dic_keys:
    if lett_d[key] > lett_d[max_value]:
            max_value = key