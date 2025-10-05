Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import math
... 
... def calculate_lottery_probability(total_numbers, numbers_to_match, draws):
...     """
...     Calculate the probability of winning a lottery.
... 
...     :param total_numbers: Total number of balls or numbers in the lottery.
...     :param numbers_to_match: Number of balls or numbers you need to match to win.
...     :param draws: Number of draws or tickets purchased.
...     :return: Probability of winning.
...     """
...     # Calculate the total number of combinations possible
...     total_combinations = math.comb(total_numbers, numbers_to_match)
... 
...     # Calculate the probability of winning in a single draw
...     probability_single_draw = 1 / total_combinations
... 
...     # Calculate the probability of winning in multiple draws
...     probability_multiple_draws = 1 - math.pow((1 - probability_single_draw), draws)
... 
...     return probability_multiple_draws
... 
... # Example usage:
... total_numbers = 49  # Total numbers in the lottery
... numbers_to_match = 6  # Numbers you need to match to win
... draws = 1  # Number of draws or tickets
... 
... probability = calculate_lottery_probability(total_numbers, numbers_to_match, draws)
... print(f"The probability of winning the lottery is: {probability:.20f}")
SyntaxError: multiple statements found while compiling a single statement
