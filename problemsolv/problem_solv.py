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

list_num.append([20, 30, 40, 50, 60])
list_num.insert(2, 200)
print(list_num)

new_item = [6, 7, 8, 9]

for item in new_item:
    list_num +=  [item]
    print(list_num)
    
    



list_collection = ["shirt", "pant"]

new_collection = ["T-shirt", "Trawzer"]

all_products = list_collection + new_collection
print(all_products)


all_products = [produc for produc in list_collection] + [product for product in new_collection]

print(all_products)