def check (x):
    if x < 0:
        print('less')
    elif x > 0:
        print('more')
        check(42)
    elif x == 42 :
        print('x is 42')
        # check(42)
    else :
        print('else condition')  

y = check(42) 
  