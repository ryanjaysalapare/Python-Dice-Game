# I, Ryan Jay Salapare, Student Number 000823653, certify that all code submitted is my own work; 
# that I have not copied it from any other source. I also certify that I have not allowed
# my work to be copied by others.

#   project.py

def numRolls( getRandomNumber ):
    #This function will help us to get random numbers from a dice.
    #We will use a range of 1-6 since dices have numbers ranging from 1-6
    import random
    
    numRolls = []
    for n in range(dices):
        numRolls.append(random.randint(1,6))
    return numRolls

def pattern1( numOfSides, randomNumbers ):
    #This function will check if number of sides meets criteria.
    #If number of sides is greater than 4, then we check if the pattern matches
    #to get a bonus factor
    
    bonusFactor = []
    if sides >= 4:
        numTemp = randomNums[0]
        for i in randomNums:
            if numTemp != i:
                bonusFactor  = 0
                print("Pattern 1 not matched in your roll ... {0} some dice are different"\
                .format(randomNums))
                break
        else:
            bonusFactor = 10
            print("Pattern 1 matched in your roll ... {0} all dice have the same value"\
            .format(randomNums))
    else:
        bonusFactor = 0
        print("Pattern 1 not matched ... sides is less than or equal to 4".format(sides))
         
    return bonusFactor
     
def pattern2( maximumScore, sumRolls ):
    #This function will check if the maximum score of the player is greater than or equal to 20.
    #If maximum score is True, then we check if the pattern matches to get 
    #a bonus factor
    
    bonusFactor = []
    if maximumScore >= 20:
        for i in range(2, sumOfRolls):
            if sumOfRolls % i == 0:
                bonusFactor = 0
                print("Pattern 2 not matched ... {0} is not a prime number!"\
                .format(sumOfRolls))
                break
        else:
            bonusFactor = 15
            print("Pattern 2 matched ... {0} is a prime number!"\
            .format(sumOfRolls))
    else:
        bonusFactor = 0
        print("Pattern 2 not matched ... your maximum score [{0}] is not greater than or equal to 20"\
        .format(maximumScore))
    
    return bonusFactor

def pattern3( dices, averageOfRolls, randomNumbers, average ):
    #This function will check if number of dices is greater than or equal to 5.
    #If dices >= 5, check if half of the random dices are greater than or equal
    #to the average.
    
    bonusFactor = []
    if dices >= 5:
        counter = 0
        for i in randomNums:
            if i >= roundedAverage:
                counter += 1

        if counter >= roundedAverage:
            bonusFactor = 5
            print("Pattern 3 matched! More than half of {0} are greater than or equal to the average of {1}."\
            .format(randomNums,roundedAverage))
        else:
            bonusFactor = 0
            print("Pattern 3 not matched! Less than half of {0} are greater than or equal to the average of {1}."\
            .format(randomNums,roundedAverage))
    else:
        bonusFactor = 0
        print("Pattern 3 does not apply since there are less than 5 dices.")

    return bonusFactor

def pattern4( dices, sides, randomNumbers ):
    #This function will check if number of dices is greater than or equal to 4 and if number of sides is greater
    #than the number of dices.
    #If condition is met, check if all the numbers have different values

    bonusFactor = []
    if dices >= 4 and sides > dices:
        for randomNums[0] in randomNums[1::]:
            bonusFactor = 0
            print("Pattern 4 not matched! Some of the values in {0} match!".format(randomNums))
            break
        else:
            bonusFactor = 8
            print("Pattern 4 matched! All of the dice are different values {0}".format(randomNums))    
    else:
        bonusFactor = 0
        print("Pattern 4 does not apply, either sides <=4 or # sides <= # dice.")
    
    return bonusFactor

def bonusFactor( one, two, three, four ):
    #This function will get us the total amount of bonus factors that the player got.
    #If the player didn't matched any patterns, then a Pattern 5 will apply
    #which gives the player a bonus factor of 1
    
    bonusFactor = []
    bonusFactors = (patternOne,patternTwo,patternThree,patternFour)
    sumOfBonus = sum(bonusFactors)
    
    anyGame = True
    if anyGame:
        if sumOfBonus == 0:
            sumOfBonus = 1
            print("Since none of the other patterns were matched, pattern 5 is matched!")
        else:
            print("Since you matched a pattern, pattern 5 is not matched!")
    else:
        pass
        
    return sumOfBonus

#======================================MAIN LINE OF CODE========================================

print("\nCOMP 10001 - W2020 Final Project by Ryan Jay Salapare, Student number\
 000823653\nWelcome to my dice game, good luck!\n")

sides = int(input("\nEnter # of faces [2,20]: "))
while sides < 2 or sides > 20:
    print("Im sorry, that isn't a valid positive integer, please try again.")
    sides = int(input("Enter # of faces [2,20]: "))

dices = int(input("\nEnter # of dices [3,6]: "))
while dices < 3 or dices > 6:
    print("Im sorry, that isn't a valid positive integer, please try again.")
    dices = int(input("Enter # of dices [3,6]: "))

score = []
turns = 1
loop = 0

#LOOP THE GAME
while loop < turns:
    #EXECUTE FUNCTION numRolls
    randomNums = numRolls(dices)
    sumOfRolls = sum(randomNums)
    averageOfRolls = sumOfRolls / dices
    roundedAverage = round(averageOfRolls)
    print("\nYou have rolled:", randomNums)
    print("These die sum to {0} and have an average rounded value of {1}".\
           format(sumOfRolls, roundedAverage))

    #GETTING THE MAXIMUM SCORE AND AVERAGE
    maximumScore = sides * dices
    percentage  = sumOfRolls / maximumScore

    #CALLING THE FUNCTIONS of the patterns(One to Four)
    patternOne = pattern1(sides,randomNums)
    patternTwo= pattern2(maximumScore,sumOfRolls)
    patternThree = pattern3(dices,averageOfRolls,roundedAverage,randomNums)
    patternFour = pattern4(dices,sides,randomNums)

    #CALLING THE FUNCTION bonusFactor
    bonus = bonusFactor(patternOne,patternTwo,patternThree,patternFour)
    
    #CALCULATING SCORES
    print("Your bonus factor is", bonus)
    studentMod = 823653 % 500
    rawScore = (bonus + studentMod)
    score.append(rawScore)
    print("These dice are worth {0} points.".format(rawScore))
    
    #GET AVERAGE SCORE FOR ALL THE TURNS MADE
    averageScore = sum(score) // turns
    
   
    #ASK THE PLAYER IF THEY WANT TO REROLL ANY DICE
    decision = input("\nDo you want to reroll any dice? ['yes', 'no'] ")
    while decision.upper() != "YES" and decision.upper() != "NO":
        print("I'm sorry, the choices are ['yes', 'no'] . Please pick one of them.")
        decision = input("Do you want to reroll any dice? ['yes', 'no'] ")
        
    subNums = []
    reroll = 1
    #VALIDATING REROLLED DICES
    if decision.upper() == "YES":
        for i in randomNums:
            option = input("Reroll die {0} (was {1}) ['y','n'] ".format(reroll,i))
            while option.upper() != "Y" and option.upper() != "N":
                print("I'm sorry, the choices are ['y', 'n'] . Please pick one of them.")
                option = input("Reroll die {0} (was {1}) ['y','n'] ".format(reroll,i))
            import random
            if option.upper() == "Y":
                reroll += 1
                subNums = randomNums
                subNums.remove(i)
                subNums.insert(i,random.randint(1,6))
            if option.upper() == "N":
                reroll += 1

    #ASKING THE PLAYER AGAIN IF THEY ARE SURE OF THEIR PREVIOUS DECISIONS
    finalCheck = input("Are you sure? ['yes', 'no'] ")
    while finalCheck.upper() != "YES" and finalCheck.upper() != "NO":
        print("I'm sorry, the choices are ['yes', 'no'] . Please pick one of them.")
        finalCheck = input("Are you sure? ['yes', 'no'] ")
    if finalCheck.upper() == "YES":
        print(subNums)
        pass
    if finalCheck.upper() == "NO": 
        subNums = randomNums
        print(subNums)
        
    #VALIDATING REROLLED DICES
    if decision.upper() == "NO":
        print("Your score of {0} on turn {1} was average compared to other turns today."\
        .format(averageScore,turns))
    loop += 1
    
    #ASK THE PLAYER IF THEY WANT TO PLAY AGAIN 
    anotherTurn = input("Do you want to play another turn? ['y', 'n'] ")
    while anotherTurn.upper() != "Y" and anotherTurn.upper() != "N":
        print("I'm sorry, the choices are ['y', 'n'] . Please pick one of them.")
        anotherTurn = input("Do you want to play another turn? ['y', 'n'] ")
        
    if anotherTurn.upper() == "Y":
        turns += 1
    if anotherTurn.upper() == "N":
        loop += 1 
        print("Your played {0} turns today with an average score of {1} points."\
        .format(turns,averageScore))
      
        
        