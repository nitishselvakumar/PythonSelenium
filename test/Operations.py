def emp_details(**details):
    return details


d = emp_details(id=100, name='bala', email="bala@gmail.com")
print(d)

for i in d.items():
    print(i)
