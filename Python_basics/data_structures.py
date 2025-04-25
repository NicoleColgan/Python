tuple = ([1,2,3], False)
print(tuple)
# tuple[0] = 1 #not allowed

set = {4,1,1,1,2,3,2}
set.add(10)
#set theory
other_set={1, 123}
print(set.difference(other_set))
#create sets out of lists (cast)
my_list=[1,2,3]
#set_out_of_list = set(my_list)
#print(set_out_of_list)

#dictionaries
my_dict = {1: 1, 2: 100, 3: 1000}
fruit_dict = {
    'apple': 'round red fruit',
    'orange': 'orange circle fruit'
}
print(my_dict[2])
print(fruit_dict['apple'])
# add to it
fruit_dict['kiwi'] = 'green small fruit'
print(fruit_dict['kiwi'])
#update value
fruit_dict['kiwi'] = 'green seeded small fruit'
# different types of values
fruit_dict['veg_fruit'] = ['avo', 'tomatoe']
print(fruit_dict)