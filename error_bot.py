import random
from reconchess import *
import numpy as np
import time

class ErrorBot(Player):
    def __init__(self):
        self._error_probability = np.random.uniform(low=0.0, high=.01)
        print("Error Probability: {0}".format(self._error_probability))

    def __possibly_error_out(self):
        if np.random.uniform() <= self._error_probability:
            raise Exception("****** Bot crash *******")

    def __delay(self, high, desc):
        delay_seconds = np.random.uniform(low=0.0, high=high)
        print("Delaying {0} by {1} seconds.".format(desc, delay_seconds))
        time.sleep(delay_seconds)

    def handle_game_start(self, color: Color, board: chess.Board, opponent_name: str):
        self.__possibly_error_out()
        self.__delay(5, "game start")

    def handle_opponent_move_result(self, captured_my_piece: bool, capture_square: Optional[Square]):
        self.__possibly_error_out()
        self.__delay(5, "handle move result")

    def choose_sense(self, sense_actions: List[Square], move_actions: List[chess.Move], seconds_left: float) -> \
            Optional[Square]:
        self.__possibly_error_out()
        self.__delay(5, "choose sense")
        return random.choice(sense_actions)

    def handle_sense_result(self, sense_result: List[Tuple[Square, Optional[chess.Piece]]]):
        self.__possibly_error_out()
        self.__delay(5, "handle move result")

    def choose_move(self, move_actions: List[chess.Move], seconds_left: float) -> Optional[chess.Move]:
        self.__possibly_error_out()
        self.__delay(5, "choose move")
        return random.choice(move_actions + [None])

    def handle_move_result(self, requested_move: Optional[chess.Move], taken_move: Optional[chess.Move],
                           captured_opponent_piece: bool, capture_square: Optional[Square]):
        self.__possibly_error_out()
        self.__delay(5, "handle move result")

    def handle_game_end(self, winner_color: Optional[Color], win_reason: Optional[WinReason],
                        game_history: GameHistory):
        self.__possibly_error_out()
        self.__delay(5, "handle game end")
