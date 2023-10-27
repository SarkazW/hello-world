import random
nr = random.randint(0,20)
print(nr)
print("Ghiceste: ")
my=int(input())
print(my)

while my!=nr:
    if my> nr:
        print("Mai mic")
    else:
        print("Mai mare")
    print("Ghiceste: ")
    my=int(input())
    
print("Corect!!! Numarul este", my,"!")