print("hello! welcome to quiz program")
print("are u intrested in playng quiz game ")
a=input("enter yes or no")
score=0
if(a.lower() != "yes"):
    quit()
print("let's get started :)")
answer=input("CPU stands for ? ")
if(answer.lower()=='central processing unit'):
    print("Correct")
    score+=1
else:
    print("incorrect")
answer=input("RAM stands for ? ")
if(answer.lower()=='random access memory'):
    print("Correct")
    score+=1
else:
    print("incorrect")
answer=input("ROM stands for ? ")
if(answer.lower()=='read only memory'):
    print("Correct")
    score+=1
else:
    print("incorrect")
answer=input("AI stands for ? ")
if(answer.lower()=='artificial intelligence'):
    print("Correct")
    score+=1
else:
    print("incorrect")
print("your score out of 4 is",score)
print("you got",((score/4)*100),"precntage ")
a=((score/4)*100)
if(a!=100):
    print("you need to imporve")
else:
    print("woo hooo! keep learning/playing")