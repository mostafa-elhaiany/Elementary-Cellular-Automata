"""
The class handling the iteration of the  Elementary Cellular Automata (ECA)
the ECA follows a set of knows rules hardcoded into the class 
"""
import numpy as np

class ECA: 
    def __init__(self, state):
        self.state = state.astype(np.uint0)
        self.rules = {
            "000" : 0,
            "001" : 1,
            "010" : 1,
            "011" : 1,
            "100" : 0,
            "101" : 1,
            "110" : 1,
            "111" : 0
        }

    def update(self):
        """
        For each row the rule calculates the next stop based on a context of 3 values 
        """
        new_state = np.zeros_like(self.state)
        size = len(new_state)
        for i in range(size):
            left = self.state[(i-1)%size]
            cur = self.state[i]
            right = self.state[(i+1)%size]
            binary = f"{left}{cur}{right}"
            out = self.rules[binary]
            new_state[i] = out
        self.state = new_state
        return self.state