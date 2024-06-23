# Elementary-Cellular-Automata
A pygame visualization of Elementary Cellular Automata

# overview 
In mathematics and computability theory, an elementary cellular automaton is a one-dimensional cellular automaton where there are two possible states (labeled 0 and 1) and the rule to determine the state of a cell in the next generation depends only on the current state of the cell and its two immediate neighbors. 

# ECA
There are $8 = 2^3$ possible configurations for a cell and its two immediate neighbors. 
The rule defining the cellular automaton must specify the resulting state for each of these possibilities.

The rules can be found [here](https://en.wikipedia.org/wiki/Elementary_cellular_automaton#Single_1_histories)

# Installation

### Prerequisites
- Python 3.x

1. Clone the repository
2. Navigate to the project directory

### Installing Required Libraries

This program uses Pygame and Numpy. If you haven't installed Pygame or Numpy yet, you can install them using pip. Open your terminal and run the following command:

```sh
pip install pygame numpy
```

### Running the simulation

To run the simulation, run `main.py`
```sh
python main.py
```

# Configuration
In `config.py` there are options to customize things
