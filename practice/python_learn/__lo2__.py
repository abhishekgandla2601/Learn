'''
logical operators = evaluate multiple conditions (or, and, not)
                    or = at least one conditon must be True
                    and = both conditons must be True
                    not = inverts the condition (not, Fals, not True)
'''
temp = 30
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is hot outsuide")
    print("It is sunny")
elif temp <= 0 and is_sunny:
    print("It is could outside")
    print("It is sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside")
    print("It is sunny")
