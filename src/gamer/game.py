from typing import List

import numpy as np


class NormalFormGame:
    """
    Represents a normal form game using a payoff matrix.

    Attributes:
        payoff_matrix (np.ndarray): The payoff matrix for the game.
        num_players (int): The number of players in the game.
        num_strategies (List[int]): The number of strategies available to each player.
    """

    def __init__(self, payoff_matrix: np.ndarray):
        """
        Initializes a NormalFormGame with the given payoff matrix.

        Args:
            payoff_matrix (np.ndarray): The payoff matrix representing the game.
                It should be a 3-dimensional array where the first dimension represents the players,
                the second and third dimensions represent the strategies, and the values represent payoffs.
        """
        if not isinstance(payoff_matrix, np.ndarray):
            raise ValueError("Payoff matrix must be a numpy ndarray.")

        if payoff_matrix.ndim != 3:
            raise ValueError("Payoff matrix must be a 3-dimensional array.")

        self.payoff_matrix = payoff_matrix
        self.num_players = payoff_matrix.shape[0]
        self.num_strategies = list(payoff_matrix.shape[1:])

    def get_payoff_matrix(self) -> np.ndarray:
        """
        Returns the payoff matrix of the game.

        Returns:
            np.ndarray: The payoff matrix.
        """
        return self.payoff_matrix
