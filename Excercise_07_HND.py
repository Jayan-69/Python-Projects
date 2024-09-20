print("-----Working with dictionaries-----")
print()

details = {'name' : 'Sachintha',
           'contact' : '0784657070',
           'workplace' : 'Esoft Gampaha',
           'working years' : 3,
           'age' : 123.45}

print(details)
print(type(details))

print("Name is ", details['name'])
print("Contact number is ", details['contact'])

details['name'] = 'ABC'
details['contact'] = "0763487290"
print(details)
