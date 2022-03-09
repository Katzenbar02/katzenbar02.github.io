from deck import Deck

#Die == Deck
#dice == card
#roll == deal

'''
The player starts the game with 300 points.
Individual cards are represented as a number from 1 to 13.
The current card is displayed.
The player guesses if the next one will be higher or lower.
The the next card is displayed.
The player earns 100 points if they guessed correctly.
The player loses 75 points if they guessed incorrectly.
If a player reaches 0 points the game is over.
If a player has more than 0 points they decide if they want to keep playing.
If a player decides not to play again the game is over.

The card is: #
Higher or lower? [h/l] x
Next card was: #
Your score is: ###
Play again? [y/n] x
'''

class Director:
    def __init__(self):
        self.deal = []
        self.is_playing = True
        #self.score = 0
        self.total_score = 75
        self.first_round = False
    #creates within a list two instances of deck class
        for i in range(2):
            deck = Deck()
            self.deal.append(deck)

    def start_game(self):
        while self.is_playing:
            self.play_game()
            self.do_outputs()
            self.play_again()
    
    def play_again(self):
        if self.total_score <= 0:
            print('Looks like you lost, thanks for playing!')
            exit()
        else:
            draw_card = input('Do you want to play again? [y/n]:')
            self.is_playing = (draw_card == 'y')
            self.first_round = (draw_card == 'y')

    
    def play_game(self):
        if not self.is_playing:
            return

        if self.first_round == False:
            hand = self.deal[0]
            hand.draw()
            print(f'The card is: {hand.card}')
            hand = hand.card

            top_card = self.deal[1]
            top_card.draw()
        
        elif self.first_round == True:
            hand = self.deal[0]
            print(f'The card is: {self.deal[0]}')
            top_card = self.deal[1]
            top_card.draw()

        hi_lo = input('Higher or lower? [h/l]: ')

            
        if hi_lo == 'h':
            if top_card.card <= hand:
                #self.score += -75
                self.total_score += -75

            if top_card.card > hand:
                #self.score += 100
                self.total_score += 100

        elif hi_lo == 'l':
            if top_card.card >= hand:
                #self.score += -75
                self.total_score += -75
            
            if top_card.card < hand:
                #self.score += 100
                self.total_score += 100

        print(f'The next card was: {top_card.card}')

        self.deal[0] = top_card.card

    
    def do_outputs(self):
        if not self.is_playing:
            return
        
        print(f'Your score is: {self.total_score}')
        self.is_playing == (self.total_score > 0)
        print('')

# director = Director()
# director.start_game()

