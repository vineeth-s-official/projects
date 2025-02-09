# ODD OR EVEN 

import random
def playgame():
    compchoice1=random.randint(1,6)
    compchoice2=['bat','bowl']
    userchoice1=input("odd or even:--")
    userchoice2=int(input("enter a number(1-6):--"))
    e=userchoice2+compchoice1
    userscore=0
    compscore=0
    print('computer entered',compchoice1)
    if e%2!=0:
        a='odd'
    else:
        a='even'
    print(a)
    if a==userchoice1:
        print("user has won the toss")
        g=input('choose to bat or bowl:--')
    elif a!=userchoice1:
        print("computer has won the toss")
        h=random.choice(compchoice2)
        print('computer has choosed to',h)

    if a==userchoice1:
        while True:
            if g=='bat':
                print("user is batting and computer is bowling")
                l=int(input("enter a number(1-6) :--"))
                i=random.randint(1,6)
                print('computer entered',i)
                if i==l:
                    print("out")
                    print('user score=',userscore)
                    print('target score for computer=',userscore+1)
                    break
                else:
                    userscore+=l
                    print('user score=',userscore)
            elif g=='bowl':
                print("user is bowling and computer is batting")
                l=int(input("enter a number(1-6):--"))
                i=random.randint(1,6)
                print('computer entered',i)
                if l==i:
                    print("out")
                    print('computer score=',compscore)
                    print('target score for user =',compscore+1)
                    break
                else:
                    compscore+=i
                    print('computer score=',compscore)
                    
                    

        while True:                
            if g=='bat':
                print("user is bowling and computer is batting")
                l=int(input("enter a number:--"))
                i=random.randint(1,6)
                print('computer entered',i)
                if l==i:
                    print("out")
                    print('computer score=',compscore)
                    break
                elif l!=i:
                    compscore+=i
                    print(compscore)
                    
            
            elif g=='bowl':
                print("user is batting and computer is bowling")
                l=int(input("enter a number:--"))
                i=random.randint(1,6)
                print('computer entered',i)
                if l==i:
                    print("out")
                    print('user score=',userscore)
                    break
                elif l!=i:
                    userscore+=l
                    print('user score=',userscore)
                    
    if a!=userchoice1:
        
        while True:
            if h=='bat':
                print("computer is batting and user is bowling")
                l=int(input("enter a number:--"))
                i=random.randint(1,6)
                print('computer entered',i)
                if i==l:
                    print("out")
                    print('computer score=',compscore)
                    print('target score for user =',compscore+1)
                    break
                else:
                    compscore+=i
                    print('computer score=',compscore)
            elif h=='bowl':
                print("computer is bowling and user is batting")
                l=int(input("enter a number"))
                i=random.randint(1,6)
                print('computer entered',i)
                if l==i:
                    print("out")
                    print('user score=',userscore)
                    print('target score for computer=',userscore+1)
                    break
                else:
                    userscore+=l
                    print('user score=',userscore) 
    
        while True:
            if h=='bowl':
                print("computer is batting and user is bowling")
                l=int(input("enter a number:--"))
                i=random.randint(1,6)
                print('computer entered',i)
                if i==l:
                    print("out")
                    print('computer score=',compscore)
                    break
                elif i!=l:
                    compscore+=i
                    print('computer score=',compscore)
                    if compscore>userscore:
                        break
                    

            elif h=='bat':
                print("computer is bowling and user is batting")
                l=int(input("enter a number"))
                i=random.randint(1,6)
                print('computer entered',i)
                if l==i:
                    print("out")
                    print('user score=',userscore)
                    break
                elif l!=i:
                    userscore+=l
                    print('user score=',userscore)
                              
    if compscore>userscore:   
        print(f'computer wins with a lead of {compscore-userscore}')
    elif userscore>compscore:
        print(f'user wins with a lead of {userscore-compscore}')
    else:
        print(f' its a tie with user and computer having a score of {userscore}') 
            

playgame()    


            
            

        
            


            
            


        




    

    






    
    
