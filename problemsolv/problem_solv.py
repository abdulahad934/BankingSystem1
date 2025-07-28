list_fruits = []

list_fruits = list_fruits + ["apple", "Mango"]
print(list_fruits)

list_fruits2 = ["Banana"]

list_fruits2 += ["Mango", "Orange"]

list_item = ["car", "bike"]
new_item = ["toyota", "Bazaz"]

for item in new_item:
    list_item = list_item + [item]
    
    print(list_item)
print(list_fruits2)


list_num = [1, 2, 3, 4, 5]

new_item = [6, 7, 8, 9]

for item in new_item:
    list_num += [item]
    print(list_num)