print("let's start the game")
print("yah rha apka sawal")
qu=["Q.1 what is the capital of india?",
"Q.2 what is the national bird of india?",
"Q.3 what is the national flower of india?",
"Q.4 what is the national animal of india?"]
op=[["new delhi","mumbai","bhopal","banglore"],
["duck","crow","peocock","swan"],
["rose","lotus","sunflower","hibiscus"],
["lion","elephant","dog","tiger"]]
sol=[1,3,2,4]
anslist=[
    ["1.new delhi","2.mumbai"],
["2.crow","3.peocock"],
["1.rose","2.lotus"],
["1.lion","4.tiger"]]
i=0
count=0
price=0
while i<len(qu):
    print(qu[i])
    j=i
    sno=0
    while (sno<len(op[i])):
        a=op[j][sno]
        print(sno+1,a)
        sno+=1
    if count==0:     
        lifeline=input("do u want lifeline:-yes/no : ")
        if lifeline=="yes":
            count+=1
            print("select your option") 
            se=0
            b=i
            while se<len(anslist[i]):
                c=anslist[b][se]
                se+=1
                print(c)
            ans=int(input("choose your answer : ")) 
            if ans==sol[i]:
                price+=1000
                print("your answer is correct, and your winning price is",price)
                print("congratulations")
                print("your next que is:")
            else:
                print("your answer is wrong")
                break  
        else:
            ans1=int(input("plz enter your answer : "))
            if ans1==sol[i]:
                price+=1000
                print("your answer is correct, and your winning price",price) 
                print("congratulations")
            else:
                print("your answer is wrong")
                break
    else:
        ans2=int(input("enter your answer: "))
        if ans2==sol[i]:
            price+=1000
            print("your answer is correct and your winning price is",price)
            print("congratulations")
            print("your next que is:-")   
        else:
            print(" your answer is wrong") 
            break   
    i+=1