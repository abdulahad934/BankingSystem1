from itertools import chain


My_list = [1, 2, 3, 4, 5, 6]

new_list = [7, 8, 9, 10, 11, 12]

c = list(chain(My_list, new_list))

My_list = [*My_list, *new_list]

all_list = [item for item in My_list] + [nitem for nitem in new_list]
print(all_list)


My_list.append(new_list)
print(My_list)

new1_list = []

for item in new_list:
    My_list.append(item)
print(My_list)


new1_list = My_list + new_list

print(new1_list)



for item in My_list:
    

My_list += new_list
print(My_list)

My_list.extend(new_list)

print(My_list)