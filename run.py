from cardsmodule import *
from adt import *

#Global
payCards = {'A' : 4, 'K' : 3,'Q' : 2,'J' : 1}


def showGreeting():
    h,s,d,c = [u"\u2665",u"\u2660",u"\u2666",u"\u2663"]
    print("********************************************************")
    print("*                                          Welcome to Strip Me                                             *")
    print("*Rules of the game: Check the Docs                                                               *")
    print("*Game Play:                                                                                                      *")
    print("*-player 0: The Computer                                                                                 *")
    print("*-player 1: you                                                                                                   *")
    print("*-enter: play the top card and place on discard pile                                     *")
    print("*-q: quit                                                                                                             *")
    print("*                                               {}{}Enjoy!{}{}                                                     *".format(h,s,d,c))
    print("********************************************************")

def isPayCard(card):
    if not card:
        return False
    return card[1] in payCards.keys()

def getCardRate(card):
    if isPayCard(card):
        return payCards[card[1]]
    return 0

def fillHand(queue, cards):
    for i in cards:
        enqueue(queue,i)
    return queue

def prepPlayers():
    hands = deal(shuffle(100, new_Deck()),52//2,2)[0]
    p1 = hands[0]
    p2 = hands[1]
    p1 = fillHand(newQueue(), p1)
    p2 = fillHand(newQueue(), p2)
    return [p1,p2]

def printCard(card):
    icon = getSuitIcon(card[0])
    print(icon)

def placeCard(hand, stack):
    push(stack, queueFront(hand))
    hand = dequeue(hand)
    return (hand, stack)

def playCard(p, hands, stack):
    card = queueFront(hands[p])
    print('Player {}'.format(p))
    printCardToString(card)
    return placeCard(hands[p], stack)

def takePayment(hand, stack):
    for i in range(len(stackContents(stack))):
        enqueue(hand,stackTop(stack))
        pop(stack)
    return (hand, stack)

def play(card, hand, player,):
    pass


def stripMe():
    try:
        showGreeting()
        p0, p1 = prepPlayers()
        pile = newStack()
        t = 1
        end = False
        op = input("(Press 'Enter' to begin Playing or 'q' to quit) >> ")
        card = None
        while(op != 'q'):
            if emptyQueue(p0):
                print("Player {} Won! \nPress 'Enter' to start a new game or 'q' to quit".format(1))
                end = True
            elif emptyQueue(p1):
                print("Player {} Won! \nPress 'Enter' to start a new game or 'q' to quit".format(0))
                end = True
            else:
                if(isPayCard(card)):
                    value = getCardRate(card)
                    while(value > 0):
                        value -= 1
                        card = queueFront(p1)
                        playCard(t,[p0,p1],pile)
                        if(isPayCard(card)):
                            break
                    if(value <= 0 and not isPayCard(card)):
                        print("Player 0 took Payment ")
                        takePayment(p0,pile)
                else:
                    card = queueFront(p1)
                    playCard(t,[p0,p1],pile)
                t = 0
                
                if(isPayCard(card)):
                    value = getCardRate(card)
                    while(value > 0):
                        value -= 1
                        card = queueFront(p0)
                        playCard(t,[p0,p1],pile)
                        if(isPayCard(card)):
                            break
                    if(value <= 0 and not isPayCard(card)):
                        print("Player 1 took Payment ")
                        takePayment(p1,pile)
                else:
                    card = queueFront(p0)
                    playCard(t,[p0,p1],pile)
                t = 1
            op = input(">> ")
            if end and op != 'q':
                print("")
                print("")
                print("New game started")
                p0, p1 = prepPlayers()
                pile = newStack()
                t = 1
                end = False
        if op == 'q' and not end:
            print("BOO!! You forfeited")
        print("Thanks for playing :)")
    except KeyboardInterrupt:
        print("")
        print("Game Terminated!")
    except IndexError:
        pass
    except TypeError:
        pass


def printCardToString(card):
    print('*********')
    print("*{}{}\t*".format(card[1],getSuitIcon(card[0])))
    print("*\t*")
    print("*           {}{}*".format(card[1],getSuitIcon(card[0])))
    print('*********')

if __name__ == '__main__':
    stripMe()

