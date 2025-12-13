'''
logical operators = evaluate multiple conditions (or, and, not)
                    or = at least one conditon must be True
                    and = both conditons must be True
                    not = inverts the condition (not, Fals, not True)
'''

temp = 20

is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")

else:
    print("The outdoor event is still scheduled")
