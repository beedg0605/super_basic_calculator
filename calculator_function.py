def basic_calc(a,b,op):
    
    if(a.isnumeric() & b.isnumeric()):
        a=float(a)
        b=float(b)
        if(op == 'add' or op == '+'):
            output = a + b
        elif(op == 'subtract' or op == '-'):
            output = a - b
        elif(op == 'multiply' or op == '*'):
            output = a * b
        elif(op == 'divide' or op == '/'):
            output = a / b
        else:
            output = 'Invalid operation'
    else:
        output = 'Invalid number. Try again'
    
    return output