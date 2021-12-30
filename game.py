import random

def nextPlayer(currentPlayer,playerList):
    x = playerList.index(currentPlayer)
    if x == len(playerList) - 1:
        return playerList[0]
    else:
        return playerList[x + 1]

def constructSolutionList(solutionWord):
    solutionList = []
    for i in range(0,len(solutionWord)):
        solutionList.append("_")
    return solutionList

def printSolutionList(solutionList):
    for i in range (0,(len(solutionList)) + (len(solutionList) + 3)):
        print("=",end="")
    print("\n| ",end="")
    for i in range(0,len(solutionList)):
        print(solutionList[i],end=" ")
    print("|\n",end="")
    for i in range (0,(len(solutionList)) + (len(solutionList) + 3)):
        print("=",end="")
    print("\n")

def printPlayerBank(playerList,playerBankList):
    for i in range(0,len(playerList)):
        print(playerList[i] + ": $" + str(playerBankList[i]),end="  ")
    print("\n")

def updateSolutionList(solutionList,guessList,solutionWord):
    for x in range(0,len(guessList)):
        for y in range(0,len(solutionWord)):
            if guessList[x] == solutionWord[y]:
                solutionList[y] = guessList[x]

wordFile = open("words_alpha.txt")
allWords = wordFile.read()
words = list(map(str, allWords.split('\n')))
wordFile.close()

wheelList = [100,100,150,200,250,250,300,350,400,450,450,500,500,550,600,650,700,700,750,800,850,900,"Lose a turn","Bankrupt"]
vowelList = ["A","E","I","O","U"]
consonantList = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]
guessList = []
solutionWord = "JOHNCENA"
solutionList = constructSolutionList(solutionWord)
print("Welcome to the Wheel of Fortune")
while True:
    print("Please enter a name for Player 1:",end="")
    playerOneName = input()
    if playerOneName.isalpha():
        break
    else:
        print("ERROR: Please enter a valid name for Player 1")
while True:
    print("Please enter a name for Player 2:",end="")
    playerTwoName = input()
    if playerTwoName.isalpha():
        break
    else:
        print("ERROR: Please enter a valid name for Player 2")
while True:
    print("Please enter a name for Player 3:",end="")
    playerThreeName = input()
    if playerThreeName.isalpha():
        break
    else:
        print("ERROR: Please enter a valid name for Player 3")

playerList =[playerOneName,playerTwoName,playerThreeName]
playerBankList = [0,0,0]

currentPlayer = random.choice(playerList)

print("The first player will be " + currentPlayer)

while(True):
    printPlayerBank(playerList,playerBankList)
    printSolutionList(solutionList)
    print(currentPlayer + ", what would you like to do?")
    print("""
=================
1. Spin the wheel
2. Guess the word
3. Buy a vowel
=================
    """)
    menuSelection = input("Enter a selection")
    if (not menuSelection.isnumeric()) or (int(menuSelection)) == 0:
        print("ERROR: Please enter a valid selection")

    elif int(menuSelection) == 1:
        wheelSpin =random.choice(wheelList)
        print(currentPlayer + " spun the wheel! It landed on " + str(wheelSpin))
        if wheelSpin == "Lose a turn":
            print("Oh no! " + currentPlayer + " lost a turn! Oh well...")
            currentPlayer = nextPlayer(currentPlayer,playerList)
            continue
        if wheelSpin == "Bankrupt":
            print("Big yikes! " + currentPlayer + " just went bankrupt...")
            playerBankList[playerList.index(currentPlayer)] = 0
            currentPlayer = nextPlayer(currentPlayer,playerList)
            continue  
        else:
            while(True):
                consonantGuess = input(currentPlayer + ", please guess a consonant: ")
                if (consonantGuess.isalpha()) and (len(consonantGuess) == 1):
                    if consonantGuess.upper() in consonantList:
                        if consonantGuess.upper() in guessList:
                            print("That consonant has already been guessed! Guess another...")
                            continue
                        else:
                            guessList.append(consonantGuess.upper())
                            if consonantGuess.upper() in solutionWord:
                                print("That consonant was in the word, congratulations!")
                                playerBankList[playerList.index(currentPlayer)] += (solutionWord.count(consonantGuess.upper())) * int(wheelSpin)
                                updateSolutionList(solutionList,guessList,solutionWord)
                                break
                            else:
                                print("Consonant not in the word... Sorry!")
                                currentPlayer = nextPlayer(currentPlayer,playerList)
                                break
                    else:
                        print("You entered a vowel!! Please enter a consonant!")
                        continue
                else:
                    print("ERROR: Please enter a valid input")
                    continue
        continue

    elif int(menuSelection) == 2:
        while(True):
            print("Please guess the word: ",end="")
            wordGuess = input()
            if wordGuess.isalpha():
                if list(wordGuess.upper()) == list(solutionWord.upper()):
                    print("Congrats! You guessed the word!")
                    break
            else:
                print("ERROR: Please enter a valid word")
                continue

