def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put",voltage, "volts through it. ")
    print("-- Lovely plummage, the", type)
    print("-- It's",state,"!")
    
    parrot(1000)                                            # 1 positional argument
    parrot(voltage=1000)                                    # 1 keyword argument
    parrot(voltage=10000, action='VOOOOOM')                 # 2 keyword arguments 
    parrot(action='VOOOM', voltage=100000)                  # 2 keyword arguments
    parrot('a million', 'bereft of life','jump')            # 3 positional arguments 
    parrot('a thousand', state='pushing up the daisies')    # 1 positonal, 1 keyword 
    
    '''
    The following calls are invalid
    parrot()                        # required string missing
    parrot(voltage=5.0, 'dead')     # non-keyword argument after a keyword argument
    parrot(100, voltage=1000)       # duplicate value for the same argument
    parrot(actor='John Cleese')     # unknown keyword argument    
    '''
    
    
    
    def cheeseshop(kind, *arguments, **keywords):  # * is tuple, ** is dictionary
        print(f"-- Do you have any {kind} ?")
        print(f"-- I'm sorry, we're all out of {kind}.")
        for arg in arguments:
            print(arg)
        print("-"*40)
        for kw,val in keywords.items():
            print(f"{kw} : {val}")
            
    cheeseshop("Limburger", "It's very runny, sir", "It's really very, VERY runny, sir", 
               shopkeeper="Michael", client="John", sketch="Cheese Shop Sketch")