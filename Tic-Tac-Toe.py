def sum( a,b,c ):
   return a + b + c

def printboard(xside,zside):
    zero = ("X" if xside[0] else ("O" if zside[0] else 0))
    one = ("X" if xside[1] else ("O" if zside[1] else 1))
    two = ("X" if xside[2] else ("O" if zside[2] else 2))
    three = ("X" if xside[3] else ("O" if zside[3] else 3))
    four = ("X" if xside[4] else ("O" if zside[4] else 4))
    five = ("X" if xside[5] else ("O" if zside[5] else 5))
    six = ("X" if xside[6] else ("O" if zside[6] else 6))
    seven = ("X" if xside[7] else ("O" if zside[7] else 7))
    eight = ("X" if xside[8] else ("O" if zside[8] else 8))
    print(f"{zero} | {one} | {two}")
    print(f"--|---|--")
    print(f"{three} | {four} | {five}")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight}")


def checkwins(xside,zside):
    wins = [[0,1,2], [3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
    for win in wins:
       if (sum(xside[win[0]], + xside[win[1]], + xside[win[2]]) == 3):
            print("X won the match")
            return 1
       if (sum(zside[win[0]], + zside[win[1]], + zside[win[2]]) == 3):
          print("O won the match")
          return 0
    return -1
   


xside = [0,0,0,0,0,0,0,0,0]
zside = [0,0,0,0,0,0,0,0,0]
Turn = 1 # if turn = 1 then x turn , when turn =  0 then 0 turn
print("Welcome to TicTacToe Game")
while(True):
    printboard(xside,zside)
    if (Turn == 1):
        print("X's Chance")
        value = int(input("Please a value : "))
        xside[value] = 1
    else:
        print("0's Chnace")
        value = int(input("Please a value : "))
        zside[value] = 1
    demo = checkwins(xside,zside)
    if (demo != -1):
        print("Match Over")
        break
        
    Turn = 1 - Turn 


