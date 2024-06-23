"""
The class handling the iteration of the  Elementary Cellular Automata (ECA)
the ECA follows a set of known rules there are 256 rules 
"""
import numpy as np

class ECA: 
    def __init__(self, state, rule=220):
        self.state = state.astype(np.uint0)
        binary = bin(rule)[2:]
        while len(binary)<8: # pad to 8 bits
            binary = "0" + binary
        self.rules = { # calculate the rule table
            "000" : binary[7],
            "001" : binary[6],
            "010" : binary[5],
            "011" : binary[4],
            "100" : binary[3],
            "101" : binary[2],
            "110" : binary[1],
            "111" : binary[0]
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