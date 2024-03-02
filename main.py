from itertools import product
from calculate import calculate
import re 
       
## ALTERE A EXPRESSÃO LOGICA ABAIXO, USE APENAS: 'AND' 'OR'  'NOT'.
## UTILIZE APENAS LETRAS PARA NOMEAR PORTAS LÓGICAS
## CHANGE THE LOGICAL EXPRESSION BELOW, JUST USE: 'AND' 'OR' 'NOT'.
## USE ONLY LETTERS TO NAME LOGIC GATES

expression = "A and B and C ou (not(A and B) and C and D)"

## NÃO ALTERAR A PARTIR DAQUI
## DO NOT CHANGE FROM HERE
def truthtable(expression):    
    logicgates = sorted(set(re.findall(r'\b[a-zA-Z]\b', expression)))
    qtylogicgates = len(logicgates)
    combinations = list(product([0,1], repeat = qtylogicgates))
    print("Truth Table:")
    print("|".join(logicgates)+'|X')
    for combination in combinations:     
        listcombination = list(combination)             
        X = calculate(listcombination, expression, logicgates )
        print("|".join(map(str, listcombination))+f'|{X}')
if __name__ == "__main__":
    truthtable(expression)        
