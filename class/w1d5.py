# DICTIONARIES
# rick_dict = {
#     'first name':'Rick',
#     'last name':'Sanchez'
# }
# print(rick_dict['first name'])
# print(rick_dict['last name'])

# shirts = [
#   {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'S',
#     'price': 20
#   },
#   {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'M',
#     'price': 25
#   },
#   {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'L',
#     'price': 30
#   },
# ]
# print(shirts)
# print(shirts[1],{'price'})

# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }
# print(sample_dict["class"]["student"]["marks"]["history"])
# print(sample_dict.get("history")) !(something isn't working)

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"

# }
# # keys_to_remove = ["name", "salary"]
# del sample_dict["name"]
# del sample_dict["salary"]
# print(sample_dict)

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"

# }
# keys_to_remove = ["name", "salary"]
# for key in keys_to_remove:
#     del sample_dict[key]
# print(sample_dict)

# DICTIONARIES AND LOOPS

# for i in range(1,10):
#     print(i)
#     if i == 9:
#         break(stops), continue(excludes), pass(placeholder, does nothing)
# print(i)

my_number = '1234'

my_list = [int(num) * 2 for num in my_number]
print(my_list)

