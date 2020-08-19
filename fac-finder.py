def fac_finder():
    import math
    while True: 
        p=input('stop or run=')
        
        if p=='stop':
            break
        
            
        elif p=='run':
            q=input('please enter the no.=')
            print(math.factorial(int(q)))
            
        else:
            print('give proper input')
