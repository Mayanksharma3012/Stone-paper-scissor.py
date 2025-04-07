'''stone, paper and scissor

stone = 0
paper = 1
scissor = -1

'''
def sps():
    print("choose one of this : ")
    print("stone\t\tpaper\t\tscissor")
    import random
    comp = random.choice([0, 1, -1])
    youstr = input("you choose :  ")
    compdict = { 0 : "stone", 1 : "paper", -1 : "scissor" }
    youdict = {"stone" : 0, "paper" : 1, "scissor" : -1 }
    you = youdict[youstr]

    print(f" you chose: {compdict[you]}\ncomputer chose: {compdict[comp]}")
    if(you == comp):
        print("its a draw")
        print("play again")
        sps()
    elif(you == 0 and comp == 1):
        print("you loose :(")
    elif(you == 1 and comp == 0):
        print("you win :)")
    elif(you == 1 and comp == -1):
        print("you loose :(")
    elif(you == -1 and comp == 1):
        print("you win :)")
    elif(you == -1 and comp == 0):
        print("you loose :(")
    elif(you == 0 and comp == -1):
        print("you win :)")
    else:
        print("somthing went wrong!!!")

    again = input("if you wanna play again entre 'again': \n")
    if(again == "again"):
        sps()
    else:
        print("E\tN\tD")

sps()