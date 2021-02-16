def emp_details(**details):
    return details


d = emp_details(id=123, name="bala", salary=56839.34)
print(d)

for i in d.items():
    print(i)
