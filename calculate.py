def calculate(values, expression, logicgates):    
    for i in range(0, len(logicgates)):
        expression = expression.replace(logicgates[i], str(values[i]))
    return (int(eval(expression)))


    
   