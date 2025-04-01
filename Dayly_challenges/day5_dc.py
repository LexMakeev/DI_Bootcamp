keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

for item in zip(keys, values):
    print(item)

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
 
for name, age in family.items():
    if age < 3:
        print(f"{name} has to pay 0")
    elif age >= 3 and age <=12:
        print(f"{name} has to pay 10")
    elif age > 12:
        print(f"{name} has to pay 15")
 


