list_1 = [1, 'Prachi']
list_2 = [3, 4, 5]

#Using +
joined_list = list_1 + list_2
print(joined_list)

#Using *
joined_list = [*list_1, *list_2]
print(joined_list)

#Using values
joined_list = list(set(list_1 + list_2))
print(joined_list)

#Using extend()
list_2.extend(list_1)
print(list_2)
