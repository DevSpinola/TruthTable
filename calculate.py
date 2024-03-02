import sys
def calculate(values, expression, logicgates):    
    try:
        for i in range(0, len(logicgates)):
            expression = expression.replace(logicgates[i], str(values[i]))
        
        result = eval(expression)
        return int(result)
    except (SyntaxError, NameError) as e:
        print(f'Error evaluating the expression, Try again!\nRemember to use only "or/and/not"')        
        sys.exit(1)