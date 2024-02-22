
def fibonachi(x,flag = False):
    a,b = 0,1
    match flag:
        case True:
            while a<=x:
                print(a,end=', ')
                a,b = b,a+b 
            print()
        case False:
            for index in range(x):
                print(a,end=', ')
                a,b = b,a+b
            print()
        case _:
            raise ValueError("Argomunt is incorrect")

fibonachi(10)
fibonachi(2000,True)