'''
Created on Apr 28, 2019

@author: Hayden Hardaway
'''

def art(hand):
    value = "0"
    suit = "n" #♥♦♣♠
    
    cardList = []
    
    for i in range(len(hand)):
        card = hand[i].split()
        suit = card[2]
        if suit == "Spades":
            suit = "♠"
        elif suit == "Clubs":
            suit = "♣"
        elif suit == "Diamonds":
            suit = "♦"
        elif suit == "Hearts":
            suit = "♥"
        
        value = card[0]
        #cardList.append("┌─────────┐\n│░"+value+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░░░░░░░░│\n│░░░░░░░░░│\n│░░░░░░░░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+value+"░│\n└─────────┘")
        if value == "Ace":
            cardList.append("┌─────────┐\n│░"+"A"+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░░░░░░░░│\n│░░░░"+"A"+"░░░░│\n│░░░░░░░░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+"A"+"░│\n└─────────┘")  
        if value == "2":
            cardList.append("┌─────────┐\n│░"+value+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░░░"+suit+"░░░░│\n│░░░░░░░░░│\n│░░░░"+suit+"░░░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+value+"░│\n└─────────┘")
        if value == "3":
            cardList.append("┌─────────┐\n│░"+value+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░░░"+suit+"░░░░│\n│░░░░"+suit+"░░░░│\n│░░░░"+suit+"░░░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+value+"░│\n└─────────┘")
        if value == "4":
            cardList.append("┌─────────┐\n│░"+value+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░"+suit+"░░░"+suit+"░░│\n│░░░░░░░░░│\n│░░"+suit+"░░░"+suit+"░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+value+"░│\n└─────────┘")
        if value == "5":
            cardList.append("┌─────────┐\n│░"+value+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░"+suit+"░░░"+suit+"░░│\n│░░░░"+suit+"░░░░│\n│░░"+suit+"░░░"+suit+"░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+value+"░│\n└─────────┘")
        if value == "6":
            cardList.append("┌─────────┐\n│░"+value+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░"+suit+"░░░"+suit+"░░│\n│░░"+suit+"░░░"+suit+"░░│\n│░░"+suit+"░░░"+suit+"░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+value+"░│\n└─────────┘")
        if value == "7":
            cardList.append("┌─────────┐\n│░"+value+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░"+suit+"░"+suit+"░"+suit+"░░│\n│░░"+suit+"░░░"+suit+"░░│\n│░░"+suit+"░░░"+suit+"░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+value+"░│\n└─────────┘")
        if value == "8":
            cardList.append("┌─────────┐\n│░"+value+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░"+suit+"░"+suit+"░"+suit+"░░│\n│░░"+suit+"░░░"+suit+"░░│\n│░░"+suit+"░"+suit+"░"+suit+"░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+value+"░│\n└─────────┘")
        if value == "9":
            cardList.append("┌─────────┐\n│░"+value+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░"+suit+"░"+suit+"░"+suit+"░░│\n│░░"+suit+"░"+suit+"░"+suit+"░░│\n│░░"+suit+"░"+suit+"░"+suit+"░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+value+"░│\n└─────────┘")
        if value == "10":
            cardList.append("┌─────────┐\n│░"+value+"░░░░░░│\n│░"+suit+"░░"+suit+"░░░░│\n│░░"+suit+"░"+suit+"░"+suit+"░░│\n│░░"+suit+"░"+suit+"░"+suit+"░░│\n│░░"+suit+"░"+suit+"░"+suit+"░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░"+value+"░│\n└─────────┘")
        if value == "Jack":
            cardList.append("┌─────────┐\n│░"+"J"+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░░░░░░░░│\n│░░░░"+"J"+"░░░░│\n│░░░░░░░░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+"J"+"░│\n└─────────┘")  
        if value == "Queen":
            cardList.append("┌─────────┐\n│░"+"Q"+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░░░░░░░░│\n│░░░░"+"Q"+"░░░░│\n│░░░░░░░░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+"Q"+"░│\n└─────────┘")  
        if value == "King":
            cardList.append("┌─────────┐\n│░"+"K"+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░░░░░░░░│\n│░░░░"+"K"+"░░░░│\n│░░░░░░░░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+"K"+"░│\n└─────────┘")  
              
    for i in range(len(cardList)):
        cardList[i] = cardList[i].split("\n")
    
    for i in range(9):
        print()
        for j in range(len(cardList)):
            print(cardList[j][i], end = "")

def dealerFirstTurn(hand):
    value = "0"
    suit = "n" #♥♦♣♠
    
    cardList = []
    
    card = hand[1].split()
    suit = card[2]
    if suit == "Spades":
        suit = "♠"
    elif suit == "Clubs":
        suit = "♣"
    elif suit == "Diamonds":
        suit = "♦"
    elif suit == "Hearts":
        suit = "♥"
        
    value = card[0]
    cardList.append("┌─────────┐\n│░░░░░░░░░│\n│░░░░░░░░░│\n│░░░░░░░░░│\n│░░░░░░░░░│\n│░░░░░░░░░│\n│░░░░░░░░░│\n│░░░░░░░░░│\n└─────────┘")
    #cardList.append("┌─────────┐\n│░"+value+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░░░░░░░░│\n│░░░░░░░░░│\n│░░░░░░░░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+value+"░│\n└─────────┘")
    if value == "Ace":
        cardList.append("┌─────────┐\n│░"+"A"+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░░░░░░░░│\n│░░░░"+"A"+"░░░░│\n│░░░░░░░░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+"A"+"░│\n└─────────┘")  
    if value == "2":
        cardList.append("┌─────────┐\n│░"+value+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░░░"+suit+"░░░░│\n│░░░░░░░░░│\n│░░░░"+suit+"░░░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+value+"░│\n└─────────┘")
    if value == "3":
        cardList.append("┌─────────┐\n│░"+value+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░░░"+suit+"░░░░│\n│░░░░"+suit+"░░░░│\n│░░░░"+suit+"░░░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+value+"░│\n└─────────┘")
    if value == "4":
        cardList.append("┌─────────┐\n│░"+value+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░"+suit+"░░░"+suit+"░░│\n│░░░░░░░░░│\n│░░"+suit+"░░░"+suit+"░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+value+"░│\n└─────────┘")
    if value == "5":
        cardList.append("┌─────────┐\n│░"+value+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░"+suit+"░░░"+suit+"░░│\n│░░░░"+suit+"░░░░│\n│░░"+suit+"░░░"+suit+"░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+value+"░│\n└─────────┘")
    if value == "6":
        cardList.append("┌─────────┐\n│░"+value+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░"+suit+"░░░"+suit+"░░│\n│░░"+suit+"░░░"+suit+"░░│\n│░░"+suit+"░░░"+suit+"░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+value+"░│\n└─────────┘")
    if value == "7":
        cardList.append("┌─────────┐\n│░"+value+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░"+suit+"░"+suit+"░"+suit+"░░│\n│░░"+suit+"░░░"+suit+"░░│\n│░░"+suit+"░░░"+suit+"░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+value+"░│\n└─────────┘")
    if value == "8":
        cardList.append("┌─────────┐\n│░"+value+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░"+suit+"░"+suit+"░"+suit+"░░│\n│░░"+suit+"░░░"+suit+"░░│\n│░░"+suit+"░"+suit+"░"+suit+"░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+value+"░│\n└─────────┘")
    if value == "9":
        cardList.append("┌─────────┐\n│░"+value+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░"+suit+"░"+suit+"░"+suit+"░░│\n│░░"+suit+"░"+suit+"░"+suit+"░░│\n│░░"+suit+"░"+suit+"░"+suit+"░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+value+"░│\n└─────────┘")
    if value == "10":
        cardList.append("┌─────────┐\n│░"+value+"░░░░░░│\n│░"+suit+"░░"+suit+"░░░░│\n│░░"+suit+"░"+suit+"░"+suit+"░░│\n│░░"+suit+"░"+suit+"░"+suit+"░░│\n│░░"+suit+"░"+suit+"░"+suit+"░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░"+value+"░│\n└─────────┘")
    if value == "Jack":
        cardList.append("┌─────────┐\n│░"+"J"+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░░░░░░░░│\n│░░░░"+"J"+"░░░░│\n│░░░░░░░░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+"J"+"░│\n└─────────┘")  
    if value == "Queen":
        cardList.append("┌─────────┐\n│░"+"Q"+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░░░░░░░░│\n│░░░░"+"Q"+"░░░░│\n│░░░░░░░░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+"Q"+"░│\n└─────────┘")  
    if value == "King":
        cardList.append("┌─────────┐\n│░"+"K"+"░░░░░░░│\n│░"+suit+"░░░░░░░│\n│░░░░░░░░░│\n│░░░░"+"K"+"░░░░│\n│░░░░░░░░░│\n│░░░░░░░"+suit+"░│\n│░░░░░░░"+"K"+"░│\n└─────────┘")  
              
    for i in range(len(cardList)):
        cardList[i] = cardList[i].split("\n")
    
    for i in range(9):
        print()
        for j in range(len(cardList)):
            print(cardList[j][i], end = "")
    
    
#hand = ["Ace of Spades", "2 of Clubs", "3 of Diamonds", "4 of Hearts","5 of Spades", "6 of Clubs", "7 of Diamonds","8 of Hearts","9 of Spades","10 of Clubs","Jack of Diamonds","Queen of Hearts","King of Spades"]
#art(hand)
#hand = ["Ace of Spades", "2 of Clubs"]
#dealerFirstTurn(hand)
