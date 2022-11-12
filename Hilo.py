import random

"""Hilo by Angela Murray"""

def main():
    """Hilo is a game in which the player guesses if the next card 
    drawn by the dealer will be higher or lower than the previous one. 
    Points are won or lost based on whether or not the player guessed correctly."""
 
    playAgain = 'y'
    score = 300 #starting, default value of score

    # loop for if game is continued
    while playAgain == 'y' and score  > 0:
        cardIs = Card.currentCard()
        guess2 = guess()
        nextCard = Card.nextCard()     
        compare = Card.compareHilo(nextCard, guess2, cardIs)
        currPoint = Points.calcPoints(compare)
        score += currPoint
        # print(f'Your score is: {score}')  #--having print score here allowed a negetive number to be shown
        # this breaks the loop without asking 'play again?'
        if score > 0:       
            print(f'Your score is: {score}')
            playAgain = input('Play again? [y/n] ')
            print('')
        else:
            print(f'Your score is: 0') #this prevents a negetive number from being shown as the score
            print(f'\nLife is not a matter of holding good cards,\nbut sometimes, playing a poor hand well.')
            print(f'      - Jack London -')
def guess():
    """player guesses if the next one will be higher or lower """
    guess1= input('Higher or lower? [h/l] ')
    return guess1



class Card:
    """chooses cards and compares the values"""


    def currentCard():
        """Displays current random card      
        """
        cards = random.randint(1, 13)
        print (f'The current card is: {cards}')
        cardIs = cards
        return cardIs


    def nextCard():
        """display next random card"""
        cards2 = random.randint(1, 13)
        print (f'The next card was: {cards2}')
        nextCard = cards2
        return nextCard


    def compareHilo(nextCard, guess2, cardIs):
        """Compare current card, next card and guess of higher or lower was right. 
        Args: 
            nextCard (random card), guess2 (input from user), cardIs (currentCard)

        """
        if cardIs > nextCard and guess2 == 'l':
            return True
        elif cardIs < nextCard and guess2 == 'l':
            return False
        elif cardIs > nextCard and guess2 == 'h':
            return False
        elif cardIs < nextCard and guess2 == 'h':
            return True



class Points:
    """Sets and calculate points in the game"""
  
  
    def calcPoints(compare):
        """
        correct guess = +100 pts
        wrong guess = -75 pts

        Args: 
            compare: Card.compareHilo(nextCard, guess2, cardIs)
        """
        correctGuess = 100
        wrongGuess = -75

        if compare is True:
            return correctGuess

        else: 
            return wrongGuess


if __name__ == "__main__":
    main()