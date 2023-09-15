def basic_calc(a,b,op):
    
    if(a.isnumeric() & b.isnumeric()):
        a=float(a)
        b=float(b)
        if(op == 'Addition' ):
            output = a + b
        elif(op == 'Subtraction' ):
            output = a - b
        elif(op == 'Multiplication' ):
            output = a * b
        elif(op == 'Division' ):
            output = a / b
        else:
            output = 'Invalid operation'
    else:
        output = 'Invalid number. Try again'
    
    return output