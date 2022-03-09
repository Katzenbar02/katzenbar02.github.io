from game.display import Display
from game.hidden_word import Hidden_Word
from game.terminal_service import TerminalService

class Director:

    def __init__(self):
        """Initializes the Director class. Responsible for vairables to be used and pulls in other classes.
        creates two variables:
        self._score: responsible for losing logic. player starts at zero, incorrect guesses raises number. 
        self._guess: responsible for creating a slot for user input. 
        
        Initializes the Director Class
        
        Args:
            self (Director): an instance of Director.
        """
        self._hidden_word = Hidden_Word()
        self._is_playing = True
        self._display = Display()
        self._terminal_service = TerminalService()
        self._score = 0
        self._guess = ''
    
    def calculate_guess(self):
        """Proccesses variable gathered from get inputs. 
        
        Args:
            self (Director): an instance of Director.
        """
        self._display.create_word_banner(self._hidden_word._secret_word, self._guess)
        self._display.create_parachute(self._score)
        self._display.create_guy(self._score)

    def results(self):
        '''displays generated results

        Args:
            self (Director): an instance of Director.
        '''
        self._display.display_results()
         

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self.starting_info()

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def starting_info(self):
        self.results()

    def _get_inputs(self):
        """Gathers user input for guesed letter.
        Args:
            self (Director): an instance of Director.
        """
        self._guess = self._terminal_service.read_text("Guess a Letter? [a-z]: ")

    def _do_updates(self):
        """Runs calculate_guess and proccesses inputs 

        Args:
            self (Director): an instance of Director.
        """
        self.calculate_guess()
                

    def _do_outputs(self):
        """Displays the ressults at the end of round. Also determins endgame. 
        
        Args:
            self (Director): an instance of Director.
        """
        self.results()

        self._score = len(self._display._guessed_letters_display)
        game_over = 'GAME OVER!'
        win_screen = 'You WON!'
        reveal = 'The word was: ' + self._hidden_word._secret_word
        if self._score == 5:
           self._is_playing = False
           self.calculate_guess()
           self.results()
           self._terminal_service.write_text(game_over)
           self._terminal_service.write_text(reveal)

        elif "_" not in self._display._word_display:
            self._is_playing = False
            self._terminal_service.write_text(win_screen)
