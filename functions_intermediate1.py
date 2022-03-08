# 1
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30

#2
def iterate_list_of_dictionaries(input_list_of_dictionaries):
    for dict in input_list_of_dictionaries:
        print(f"first_name - {dict['first_name']}, last_name - {dict['last_name']}")

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

#3
def iterate_list_of_dictionaries_by_key(key_name, input_list_of_dictionaries):
    for dict in input_list_of_dictionaries:
        print(dict[key_name])

#4
def print_dictionary_list_values(input_dictionary):
    for key_name in input_dictionary:
        print('--------------------')
        print(len(input_dictionary[key_name]), key_name.upper())
        for element in input_dictionary[key_name]:
            print(element)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

iterate_list_of_dictionaries(students)
iterate_list_of_dictionaries_by_key('last_name', students)
print_dictionary_list_values(dojo)