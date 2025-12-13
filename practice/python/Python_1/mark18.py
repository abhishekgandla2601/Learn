#match case statements

# in c and c++ we have switch case statements

x = int(input("Enter the value of x:"))

match x:
    case 0:
        print('x is Zero')
    case 4:
        print('Case is 4')
    case _ if x <10:
        print("x is < 10")
    
    case _: #default case
        print('default case')
        print(x)
        

'''
A match statement will compate a given variabe's
value to different shaoes, also referred t as the pattern.
The main idea is to keep on comparing the variable with all the 
present patterns until it fits into one.


The match case consists of three main entities:

1.The match keyword.
2.One or more case Clauses.
3.Expression for each case

The case clause consists of a pattern to be
matched to the variable, a condition to be evaluated if the pattern matches,
and a set of statements to be executed if the pattern matches.
'''