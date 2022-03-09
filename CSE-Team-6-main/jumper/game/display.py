class Display:

    def __init__(self):
        self._parachute_display = [" ___ ","/___\ ", "\   /"," \ / "]
        self._guy_display = ["  O  "," /|\ "," / \ ","     ","^^^^^"]
        self._word_display = ["_","_","_","_","_"]
        self._guessed_letters_display = []

    def create_parachute(self,score):
        """Creates the correct parachute according to the score.
        
        Args:
            self (Display): displays the parachute
            score (Director): checks the score
        """

        parachute = [ " ___ ","/___\ ", "\   /"," \ / "]
        parachute_list = []
        for i in range(score , 4):
            parachute_list.append(parachute[i])
        self._parachute_display = parachute_list

    def create_guy(self,score):
        """Creates the correct parachute guy depending on score.
        
        Args:
            self (display): displays the parachute guy
            score (director): checks the score
        """
        if score != 5:
            guy = ["  O  "," /|\ "," / \ ","     ","^^^^^"]
            guy_list = []
            for i in range((len(guy)-1)):
                guy_list.append(guy[i])
            self._guy_display = guy_list
            
        if score == 5:
            game_over_guy = [" \ /  ","  |  ", " /x\ ", "^^^^^"]
            self._guy_display = game_over_guy

    def create_word_banner(self, word, guess):
        """Displays the in-progress word at the top of the parachute.
        
        Args:
            self (display): displays the outputs.
            word (hidden_word): pulls the random word
            guess (director): checks against the guess
        """
        if word.find(guess) != -1:
            for i in range(5):
                if guess == word[i-1]:
                    self._word_display[i-1] = guess
                i += 1
            
        else: 
            print("try again")
            self._guessed_letters_display.append(f'{guess}')
            

    def display_results(self):
        """Displays the endgame results.
        
        Args:
            self (display): displays the outputs.
        """
        print(*self._word_display)
        print(*self._parachute_display, sep="\n")
        print(*self._guy_display, sep="\n")
        print('Guessed Letters:')
        print(*self._guessed_letters_display, sep=", ")
        print()

# display = Display()
# score = 4
# guess = 's'
# word = 'Adult'
# display.create_word_banner(word, guess)
# display.create_parachute(score)
# display.create_guy()
# display.display_results()