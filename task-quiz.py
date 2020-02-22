q1=input("Name the three primary colours according to the colour order? ").lower()
q2=input("Who banned art in mordern germany in the 30's? ").lower()
q3=input("What was Leonardo da Vinci's most famous painting? ").lower()
q4=input("Name Paulo Coelho most famous book? ").lower()
q5=input("How many paintings did vincent van gogh sell? ").lower()
k=0
i=True
while True:
    if(q1=="red blue yellow"):
        k=k+1
    else:
        k=k+0
    if(q2=="hitler"):
        k=k+1
    else:
        k=k+0
    if(q3=="mona lisa"):
        k=k+1
    else:
        k=k+0
    if(q4=="the alchemist"):
        k=k+1
    else:
        k=k+0
    if(q5=="900"):
        k=k+1
    else:
        k=k+0
    print("You have scored",k,"out of 5")
    q6=input("Press q to exit game, press enter to take the quiz again: ")
    if(q6=='q'):
        break
    else:
       k=0 
       q1=input("Name the three primary colours? ").lower()
       q2=input("Name the famous ballet Russian dancer who changed the face of modern ballet? ").lower()
       q3=input("What was Leonardo da Vinci's most famous painting? ").lower()
       q4=input("Name Paulo Coelho most famous book? ").lower()
       q5=input("How many paintings did vincent van gogh sell? ").lower()
