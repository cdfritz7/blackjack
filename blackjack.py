from random import shuffle
import time

class Cards:
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    values = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def __repr__(self):
        return self.values[self.value]+' of '+self.suits[self.suit]
    
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Cards(i,j))
        shuffle(self.cards)
    
    def draw_card(self):
        if(len(self.cards) == 0):
            return
        return self.cards.pop()
    
class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.total = 0
        self.card = None
        self.draws = 0
        
class Game:
    def __init__(self):
        self.deck = Deck()
        self.name = input("What is the player's name? ")
        self.player = Player(self.name)
        self.winnings = 0
          
    def drawAgain(self):                #used to prompt user to draw another card
        inp = input("Will you draw another card? (y/n) ")
        if(inp == 'y'):
            return True
        elif(inp == 'n'):
            return False
        else:
            print("Invalid input")
            self.drawAgain()
    
    def findValue(self, playerHand):    #creates array of all possible number values a hand can have
        values = [0]
        for i in playerHand:
            if(i.value == 14):
                x = len(values)
                for j in range(x):
                    values.append(values[j]+1)
                for j in range(x):
                    values[j] = (values[j]+11)
            elif((i.value<14) & (i.value>10)):
                for j in range(len(values)):
                    values[j]+=10
            else:
                for j in range(len(values)):
                    values[j]+=i.value
        return values
    
    def bust(self, values):             #used to see if a hand has gone bust
        for i in values:
            if(i<=21):
                return False
        return True
    
    def has17lessthan22(self, values):  #sees if the dealer's hand has a value greater than 17 but less than 22
        for i in values:
            if((i>=17)&(i<=21)):
                return True
        return False
    
    def highestValue(self, values):    #finds highest element in values under 22
        highest = 0
        for i in values:
            if((i > highest) & (i < 22)):
                highest = i
        return highest   
    
    def play_game(self):
        cards = self.deck.cards
        print("Lets play some black jack, {}!".format(self.name))
        quit1 = None
        playerwon = 3
        playerScore = 0
        dealerScore = 0
        playerHand = []
        dealerHand = []
        while len(cards)>=4 and quit1 != 'q':
            while(True):
                quit1 = input('Press q to quit, press any other key to play ')
                if(quit1 == 'q'):
                    break
                dealerHand = []
                playerHand = []
                dealerHand.append(self.deck.draw_card())
                dealerHand.append(self.deck.draw_card())
                playerHand.append(self.deck.draw_card())
                playerHand.append(self.deck.draw_card())
                print("The Dealer's face up card is the {}".format(dealerHand[0]))
                print("Your cards are the {} and the {}".format(playerHand[0], playerHand[1]))
                while(self.drawAgain()):
                    print("You draw a card...")
                    time.sleep(1)
                    playerHand.append(self.deck.draw_card())
                    print("Your cards are now the "+', '.join(str(e) for e in playerHand))
                    if(self.bust(self.findValue(playerHand))):
                        print("You have gone over 21 pardner...")
                        playerwon = 0
                        break
                if(playerwon == 0):
                    break
                print("Alright, time to see the Dealer's hand...")
                time.sleep(1)
                print("The Dealer has a {} and a {}".format(dealerHand[0], dealerHand[1]))
                while((not self.has17lessthan22(self.findValue(dealerHand)))&(not self.bust(self.findValue(dealerHand)))):
                    print("The Dealer draws a card...")
                    time.sleep(1.5)
                    dealerHand.append(self.deck.draw_card())
                    print("The Dealer now has the "+", ".join(str(e) for e in dealerHand))
                    time.sleep(1)
                if(self.bust(self.findValue(dealerHand))):
                    print("The Dealer busted..")
                    playerwon = 1
                    break
                dealerHigh = self.highestValue(self.findValue(dealerHand))
                playerHigh = self.highestValue(self.findValue(playerHand)) 
                if(dealerHigh > playerHigh):
                    playerwon = 0
                    break
                if(dealerHigh < playerHigh):
                    playerwon = 1
                    break
                if((playerHigh == 21) & (dealerHigh == 21) & (len(dealerHand) != 2) & (len(playerHand) == 2)):
                    playerwon = 1
                    break
                if((playerHigh == 21) & (dealerHigh == 21) & (len(dealerHand)== 2) & (len(playerHand) != 2)):
                    playerwon = 0
                    break
                playerwon = 2  #sets playerwon to 2 for a tie
                break
            if(playerwon == 0):
                print("The Dealer won this round\n")
                dealerScore +=1
            elif(playerwon == 1):
                print("You won this round!\n")
                playerScore +=1
            elif(playerwon == 2):
                print("It was a tie my friend\n")
            playerwon = 3
        print("Game Over, Final Score: Dealer - {}  {} - {}".format(dealerScore, self.name, playerScore))    
            
            
            
game1 = Game()
game1.play_game()
                