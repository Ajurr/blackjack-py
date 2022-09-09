'''
 * File name: Blackjack.py

* Author: Hayden Hardaway

* Email Address: hayden.hardaway1@gmail.com

* Description: A Blackjack game with completely original code.

* Last changed: 4/29/2019
'''
import random
import locale as lc
import csv
import Instructions
import CardArt
import sys
import os
import time
lc.setlocale(lc.LC_ALL, "us")
FILENAME = "players1.csv"
newDeck = {'suit': ('Spades','Clubs','Diamonds','Hearts'), 'rank': ('Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King')}
dealer = []
player1 = []
deck = []
money = 1000
player1Value = 0
dealerValue = 0

#shuffles the deck and returns it as deck
def shuffleDeck():
    for s in newDeck['suit']:
        for r in newDeck['rank']:
            deck.append(r+' of '+s)
    
    random.shuffle(deck)
    return(deck)

#takes a hand list and deals a single card from the deck
def deal(hand):
    hand.append(deck.pop(0))
    return hand

#takes a hand list, calculates its pip values, and returns the value
def calculateValue(hand):
    isItAce = False
    value = 0
    if hand == dealer:
        for i in range(len(hand)):
            if hand[i].split()[0] in ('Jack' , 'Queen' , 'King' , '10'):
                value += 10
            elif hand[i].split()[0] in ('2','3','4','5','6','7','8','9'):
                value += int(hand[i].split()[0])
            elif hand[i].split()[0] == 'Ace':
                isItAce = True
                while True:
                    if (value + 11) >= 17 and (value + 11) <= 21:
                        value += 11
                        break
                    elif value <= 10:
                        value += 11
                        break
                    else:
                        value += 1
                        break
            
    else:
        for i in range(len(hand)):
            if hand[i].split()[0] in ('Jack' , 'Queen' , 'King' , '10'):
                value += 10
            elif hand[i].split()[0] in ('2','3','4','5','6','7','8','9'):
                value += int(hand[i].split()[0])
            elif hand[i].split()[0] == 'Ace':
                #print ("\n"+ hand[i]), don't need this anymore
                isItAce = True
                while True:                 #changed to mimic dealer
                    if (value + 11) <= 21:  #ace value is automated
                        value += 11        
                        break
                    elif value <= 10:
                        value += 11
                        break
                    else:
                        value += 1
                        break
                    

    if isItAce==True and value > 21:  #fixed problem of having an Ace in first two cards assigned a value of 11
        value = value - 11 +1         #Now the Ace will revert to 1, instead of causing a bust
    return value
#bet function, tracks how much the player wishes to bet before each hand is dealt
def betF(play,players):
    bet = 0
    global money
    money = float(play[2])
    if money == 0:
        lost(play,players)
    print("You have",moneyConvert(float(play[2])),"dollars")
    while True:
        try:
            bet = input("How much do you want to bet? (between 2 and 500)\n>")
            if bet == "exit":
                sys.exit()
            elif float(bet) > 500 or float(bet) < 2:
                print("Can't bet under $2 or over $500.")
            elif float(bet) <= float(play[2]):
                money -= float(bet)
                play.pop(2)
                play.append(money)
                writePlayers(players)
                return float(bet)
            elif float(bet) > money:
                print("Can't bet more than you have.")
        except ValueError:
            print("Enter a valid bet.")
            continue

#function to quickly convert an int to currency
def moneyConvert(x):
    return lc.currency(x, grouping=True)

#checks if the player wins, loses, or draws
def winLose(money, bet,play,players):
    global player1Value 
    global dealerValue
         
    if player1Value > 21:
        print("\nBUST!\n")
        print("You lost",moneyConvert(bet),"dollars")
        print(moneyConvert(float(play[2])))
    elif dealerValue > 21:
        money += (bet*1.5)
        play.pop(2)
        play.append(money)
        writePlayers(players)
        print("\nDEALER BUST!\n")
        print("You won",moneyConvert(bet/2),"dollars")
        print(moneyConvert(float(play[2])))

    elif player1Value == 21 and dealerValue == 21:
        money += bet
        play.pop(2)
        play.append(money)
        writePlayers(players)
        print("\nDealer and player blackjack, draw! Your bet is returned.\n")
        print(moneyConvert(float(play[2])))

    elif dealerValue == 21:
        print("\nDealer Blackjack!\n")
        print("You lost",moneyConvert(bet),"dollars")
        print(moneyConvert(float(play[2])))

    elif player1Value == 21:
        money += (bet*1.5)
        play.pop(2)
        play.append(money)
        writePlayers(players)
        #print("\nBLACKJACK!\n")
        print("You won",moneyConvert(bet/2),"dollars")
        print(moneyConvert(float(play[2])))

    elif player1Value < dealerValue:
        print("You lost",moneyConvert(bet),"dollars")
        print(moneyConvert(float(play[2])))

    elif player1Value > dealerValue:
        money += (bet*1.5)
        play.pop(2)
        play.append(money)
        writePlayers(players)
        print("You won",moneyConvert(bet/2),"dollars")
        print(moneyConvert(float(play[2])))

    elif player1Value == dealerValue:
        money += bet
        play.pop(2)
        play.append(money)
        writePlayers(players)
        print("Draw, your bet is returned.")
        print(moneyConvert(float(play[2])))

    return money

#function for the dealer's turn after initial deal
def dealerTurn():
    global dealerValue
    while True:
        print('\nDEALER\'S CARDS')
        CardArt.art(dealer)
        dealerValue = calculateValue(dealer)
        print(dealerValue)
        time.sleep(1)
        if dealerValue >= 17 and dealerValue < 21:
            print("\nDEALER STAND\n")
            break
        elif dealerValue == 21:
            break
        elif dealerValue <= 16:
            print("\nDEALER HIT")
            deal(dealer)
        else:
            break
    return dealer

#function for the player's turn after the initial deal
def playerTurn():
    global player1Value
    while True:
        player1Value = calculateValue(player1)  #added so you dont have to say hit or stand if you have Blackjack
        if player1Value == 21:
            print(player1Value)
            print("\nYou have Blackjack! Dealer's Turn.")
            break
        choice = input("\nHit or stand?\n>")
        if choice.lower() == "hit":
            deal(player1)
            print("\nPLAYER\'S CARDS")
            CardArt.art(player1)
            player1Value = calculateValue(player1)
            print(player1Value)
            if player1Value == 21:
                break
            elif player1Value > 21:
                break
        elif choice == "stand":
            player1Value = calculateValue(player1)
            print(player1Value)
            print("\nPLAYER STAND")
            break
        elif choice == "exit":
            sys.exit()
        else:
            print("Type hit or stand.") #clarification
    return player1

def menu(players):    #login for users to save money
    print("BLACKJACK\nLogin to play or Create an account")
    print("Type exit, to leave the game")
    player =[]
    while True:
        mOption = input("Login or Create?")
        mOption = mOption.lower()
        if mOption == "login":
            user = input("Enter full name: ").strip()
            passW = input("Enter password: ").strip()
            for i in range (len(players)):
                if user == players[i][0] and passW == players[i][1]:
                    print("Welcome back",user)
                    print()
                    os.system('cls')
                    return players[i]
            else:
                print("Try again")
                os.system("cls")
        elif mOption == "create":
            fullName= getFullName()
            print()
            player.append(fullName)
            password = getPass()
            player.append(password)
            player.append(money)
            players.append(player)
            writePlayers(players)
            print()
            print("Hi " + fullName + ", thanks for creating an account.")
            os.system('cls')
            return player
        elif mOption == "exit":
            sys.exit()
        else:
            print("Enter login or create")
def getFullName():
    while True:
        name = input("Enter full name: ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")
def getPass():
    while True:
        print("Password must be 8 characters or more with at least one digit and one uppercase letter.\n")
        password = input("Enter password: ").strip()
        digit = False
        capL = False
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                capL = True
        if digit == False or capL == False or len(password) < 8:
            continue
        else:
            return password

def writePlayers(players):   #stores data of player
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(players)
def readPlayers():
    players=[]
    with open(FILENAME,newline ="") as file:
        reader= csv.reader(file)
        for row in reader:
            players.append(row)
    return players

def instruc():  #prints instructions
    while True:
        iOption = input("If you want to read the instructions, type yes, if not type no.")
        iOption = iOption.lower()
        if iOption == "yes":
            print()
            Instructions.instructions()

            break
        elif iOption == "no":
            os.system('cls')
            break
        else:
            print("Type yes or no")

def lost(play,players):   #if user loses game,  
    print("You lost all your money!")
    while True:
        choice = input("Type Play again or exit")
        choice = choice.lower()
        if choice == "play again":
            play.pop(2)
            play.append(1000)
            writePlayers(players)
            return play
        elif choice == "exit":
            sys.exit()
        else:
            print("Please type one or the other.")

def main():
    #global variables may look confusing but it prevents spaghetti code
    global dealer
    global player1
    global money
    global player1Value
    global dealerValue
    players= readPlayers()
    play = menu(players)
    instruc()
    while True:
        bet = betF(play,players)
        deck = shuffleDeck()
        dealer = []
        player1 = []
        player1Value = 0
        dealerValue = 0
        print('\nDEALER\'S CARDS')
        for _ in range(2):
            deal(dealer)
        CardArt.dealerFirstTurn(dealer)
        print('\nPLAYER\'S CARDS')
        for _ in range(2):
            deal(player1)
        CardArt.art(player1)
        player1 = playerTurn()
        time.sleep(1)
        if player1Value > 21:
            money = winLose(money, bet,play,players)
        else:
            dealer = dealerTurn()
            time.sleep(1)
            money = winLose(money, bet,play,players)
        print()
    
if __name__ == "__main__":
    main()
