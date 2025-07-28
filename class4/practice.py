list_item = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


list_item.reverse()
print(list_item)

list_rev = list(reversed(list_item))
print(list_rev)

my_list = [1, 2, 3, 4, 5, 6, 7]

rev_list = []

for i in my_list:
    rev_list = [i] + rev_list
    print(rev_list)

    

list_len = len(list_item)
list_max = max(list_item)
print(list_max)

print(list_len)






my_list1 = [10, 20, 30, 40, 50, 60, 70]

rev_list1 = []

for i in my_list1:
    rev_list1 = [i] + rev_list1
    
    print(rev_list1)


my_list = [1, 2, 3, 4, 5]

rev_list = []

i = len(my_list) -1

while 0 <=i:
    rev_list.append(my_list[i])
    
    i -= 1
    
print(rev_list)


list_item = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

rev_list = []

for item in list_item:
    rev_list.append([item])
rev_list = rev_list[:: -1]
print(rev_list)

