list_num = [1, 2, 3, 4, 5 ]

list_num = list_num + [6, 7, 8, 9, 10]

list_num.append([40, 50, 70, 80, 100])
list_num.extend([200, 300])

list_num += [90, 91, 92, 93, 94, 95]
print(list_num)

print(list_num)

new_num = [11, 12, 13, 14, 15]


fruits = ["apple", "banana"]
new_fruits = ["mango", "malta"]

all_fruits = [fruit for fruit in fruits] + [item for item in new_fruits]
print(all_fruits)
fruits[len(fruits):] = ["mango", "malta"]



print(fruits)
for num in new_num:
    list_num += [num]
    print(list_num)