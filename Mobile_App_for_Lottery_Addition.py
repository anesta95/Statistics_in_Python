import pandas as pd
# A medical institute that aims to prevent and treat gambling addictions wants to 
# build a dedicated mobile app to help lottery addicts better estimate their chances of winning. 
# The institute has a team of engineers that will build the app, 
# but they need us to create the logical core of the app and calculate probabilities.

# For the first version of the app, they want us to focus on the 6/49 lottery and 
# build functions that enable users to answer questions like:

# What is the probability of winning the big prize with a single ticket?
# What is the probability of winning the big prize if we play 40 different tickets (or any other number)?
# What is the probability of having at least five (or four, or three, or two) winning numbers on a single ticket?

# The institute also wants us to consider historical data coming from the national 
# 6/49 lottery game in Canada. The data set has data for 3,665 drawings, 
# dating from 1982 to 2018 (we'll come back to this).


# On the first screen, we saw our goal is to write code that can enable users to 
# answer probability questions about playing the lottery. Throughout the project, 
# we'll need to calculate repeatedly probabilities and combinations. 
# As a consequence, we'll start by writing two functions that we'll use often:

# A function that calculates factorials; and
# A function that calculates combinations.
# To calculate factorials, this is the formula we learned we need to use:
    
# n! = n * (n-1) * (n-2) * ... * 2 * 1

# In the 6/49 lottery, six numbers are drawn from a set of 49 numbers that range from 1 to 49. 
# The drawing is done without replacement, which means once a number is drawn, it's not put back in the set.

# To find the number of combinations when we're sampling without replacement and 
# taking only k objects from a group of n objects, we can use the formula:
    
# nCk = (n-over-k) = n! / k!(n - k)!

# Now let's start coding the two functions. 

# TASKS
# Write a function named factorial() which takes as input a number n and 
# computes the factorial of that number n. Remember that we already coded this function in the last mission.

# Write a function named combinations() which takes in two inputs (n and k) and 
# outputs the number of combinations when we're taking only k objects from a group of n objects. 
# Remember that we already coded this function in the last mission.

def factorial(num):
    final_product = 1
    for i in range(num, 0, -1):
        final_product *= i
    return (final_product)
    
def combinations(n, k):
    numerator = factorial(n)
    denominator = factorial(k) * (factorial(n - k))
    return (numerator / denominator)
    
# 3. ONE-TICKET PROBABILITY
# On the previous screen, we focused on writing factorial() and combinations(), 
# two core functions that we're going to need repeatedly moving forward. 
# On this screen, we focus on writing a function that calculates the probability of winning the big prize.

# In the 6/49 lottery, six numbers are drawn from a set of 49 numbers that range from 1 to 49. 
# A player wins the big prize if the six numbers on their tickets match all the six numbers drawn. 
# If a player has a ticket with the numbers {13, 22, 24, 27, 42, 44}, 
# he only wins the big prize if the numbers drawn are {13, 22, 24, 27, 42, 44}. If only one number differs, he doesn't win.

# For the first version of the app, we want players to be able to calculate the probability 
# of winning the big prize with the various numbers they play on a single ticket 
# (for each ticket a player chooses six numbers out of 49). 
# So, we'll start by building a function that calculates the probability of winning the big prize for any given ticket.

# We discussed with the engineering team of the medical institute, 
# and they told us we need to be aware of the following details when we write the function:
    
# Inside the app, the user inputs six different numbers from 1 to 49.

# Under the hood, the six numbers will come as a Python list, 
# which will serve as the single input to our function.

# The engineering team wants the function to print the probability value in a friendly way — 
# in a way that people without any probability training are able to understand.

# Let's try to write this function!

# TASKS
# Write a function named one_ticket_probability(), 
# which takes in a list of six unique numbers and 
# prints the probability of winning in a way that's easy to understand.

# Start by calculating the total number of possible outcomes — 
# this is total number of combinations for a six-number lottery ticket. 
# There are 49 possible numbers, and six numbers are sampled without replacement. 
# Use the combinations() function you wrote in the previous screen.

# The user inputs just one combination, which means the number of successful outcomes is 1.

# Use the number of successful outcomes and 
# the total number of possible outcomes to calculate the probability for one ticket.

# The function should print the probability in a way that's easy to understand. 
# It's up to you what you choose, but here are a few suggestions:
    
# Print the probability as a percentage.

# Use the str.format() method to make the printed message more personalized with respect to what the user inputs.
# Test your function using a few inputs.

# Add some context for your readers to explain what you did in this step and why.

def one_ticket_probability(list):
    c = combinations(49, 6)
    probability = ((len(list) / len(list)) / c) * 100
    print('''Your entry of {} has a {:.7f}% chance of winning. In other words
you have a 1 in {:,} chance of winning'''.format(list, probability, c))
    
one_ticket_probability([1, 2, 3, 4, 5, 6])
one_ticket_probability([1, 49, 2 ,48, 3, 47])

#4. HISTORICAL DATA CHECK FOR CANADA LOTTERY
# On the previous screen, we wrote a function that can tell users what is the 
# probability of winning the big prize with a single ticket. 
# For the first version of the app, however, users should also be able to compare 
# their ticket against the historical lottery data in Canada and determine whether 
# they would have ever won by now.

# On this screen, we'll focus on exploring the historical data coming from the Canada 6/49 lottery. 

# The data set contains historical data for 3,665 drawings 
# (each row shows data for a single drawing), dating from 1982 to 2018. 
# For each drawing, we can find the six numbers drawn in the following six columns:

# NUMBER DRAWN 1
# NUMBER DRAWN 2
# NUMBER DRAWN 3
# NUMBER DRAWN 4
# NUMBER DRAWN 5
# NUMBER DRAWN 6
# Let's now write some code to open this data set and get familiar with its structure.

# Open the 649.csv file and save it as a pandas DataFrame.
# Print the number of rows and columns of this data set.
# Print the first and the last three rows and try to get familiar with the data set.

lottery = pd.read_csv('649.csv')
print(lottery.shape)
print(lottery.head(3))
print(lottery.tail(3))

# 5. FUNCTION FOR HISTORICAL DATA CHECK
# On the previous screen, we focused on opening and exploring the Canada lottery data set. 
# On this screen, we're going to write a function that will enable users to compare their ticket 
# against the historical lottery data in Canada and determine whether they would have ever won by now.

# The engineering team told us that we need to be aware of the following details:

# Inside the app, the user inputs six different numbers from 1 to 49.

# Under the hood, the six numbers will come as a Python list and serve as an input to our function.

# The engineering team wants us to write a function that prints:

# the number of times the combination selected occurred in the Canada data set; and
# the probability of winning the big prize in the next drawing with that combination.

# We'll now start working on writing this function. 
# Note there's more than one way to solve this problem, 
# so take the instructions below as suggestions.


# Extract all the winning six numbers from the historical data set as Python sets 
# (set is a data type in Python).

# Write a function named extract_numbers() that takes as input a row of the lottery dataframe and 
# returns a set containing all the six winning numbers. For the first row, for instance, 
# the function should return the set {3, 41, 11, 12, 43, 14}.

# Use extract_numbers() in combination with the DataFrame.apply() 
# method to extract all the winning numbers.

def extract_numbers(row):
    row = row[4:10]
    winning_numbers = set(row.values)
    return (winning_numbers)
    
winning_numbers = lottery.apply(extract_numbers, axis=1)
print(winning_numbers.head())

# Write a function named check_historical_occurence() that takes in two inputs: 
# a Python list containing the user numbers and a pandas Series containing sets 
# with the winning numbers (this is the Series you'll extract using the extract_numbers() function).

# Convert the user numbers list as a set using the set() function.

# Compare the set against the pandas Series that contains the sets with the winning numbers to find the number of matches — 
# a Series of Boolean values will be returned as a result of the comparison 
# (the value will be True each time there'll be a match).

# Print information about the number of times the combination inputted by the user occurred in the past.

# Print information (in an easy-to-understand way) 
# about the probability of winning the big prize in the next drawing with that combination.

# Test your function with a few inputs.

# Add some context for your readers to explain what you did in this step and why.
# REMEMBER:
winning_numbers = lottery.apply(extract_numbers, axis=1)

def check_historical_occurance(user_numbers, historical_numbers):
    user_number_set = set(user_numbers)
    reference_check = (user_number_set == historical_numbers)
    number_of_wins = reference_check.sum()
    if number_of_wins == 0:
        print('''The set of numbers {} has never won in the past. This does not
        mean it is more likely to occur now. Your chances of winning the big
        prize in the next drawing with the numbers {} is about 0.0000072%. In
        other words you have 1 in 13,983,816 chances to win.'''.format(
            str(user_numbers), str(user_numbers)))
    else:
        print('''The set of numbers {} has occured {} times. Your chances of 
        winning the big prize in the next drawing with the numbers {} is about
        0.0000072%. In other words you have 1 in 13,983,816 
        chances to win.'''.format(
            str(user_numbers), str(number_of_wins), str(user_numbers)))
    
    
test_input = [1, 2, 10, 40, 23, 36]
test_input_2 = [34, 14, 47, 21, 31, 5]
    
check_historical_occurance(test_input, winning_numbers)
check_historical_occurance(test_input_2, winning_numbers)

# 6. MULTI-TICKET PROBABILITY
# So far, we wrote two functions:

# one_ticket_probability() — calculates the probability of winning the big prize with a single ticket

# check_historical_occurrence() — checks whether a certain combination has occurred in the Canada lottery data set

# Lottery addicts usually play more than one ticket on a single drawing, 
# thinking that this might increase their chances of winning significantly. 
# Our purpose is to help them better estimate their chances of winning — 
# on this screen, we're going to write a function that will allow the users to 
# calculate the chances of winning for any number of different tickets.

# We've talked with the engineering team and they gave us the following information:

# The user will input the number of different tickets they want to play 
# (without inputting the specific combinations they intend to play).

# Our function will see an integer between 1 and 13,983,816 (the maximum number of different tickets).

# The function should print information about the probability of winning 
# the big prize depending on the number of different tickets played.

# Let's now start writing this function.

# TASKS

def multi_ticket_probability(num_tickets_bought):
    unique_possible_combinations = combinations(49, 6)
    successful_outcomes = num_tickets_bought
    prob_of_winning = successful_outcomes / unique_possible_combinations
    percentage_form = 100 * prob_of_winning
    combinations_round = round(unique_possible_combinations / 
    successful_outcomes)
    print('''Your probability of winning by buying {:,} tickets is {:.7f}%. In 
    other words you have a 1 in {:,} chance to win.'''.format(
        num_tickets_bought, percentage_form, combinations_round))
    
test_inputs = [1, 10, 100, 10000, 1000000, 6991908, 13983816]

for num in test_inputs:
    print('------------------------')
    multi_ticket_probability(num)

# 7. LESS WINNING NUMBERS -- FUNCTION
# So far, we wrote three main functions:

# one_ticket_probability() — 
# calculates the probability of winning the big prize with a single ticket

# check_historical_occurrence() — 
# checks whether a certain combination has occurred in the Canada lottery data set

# multi_ticket_probability() — 
# calculates the probability for any number of tickets between 1 and 13,983,816

# On this screen, we're going to write one more function to allow the users to 
# calculate probabilities for two, three, four, or five winning numbers.

# For extra context, in most 6/49 lotteries there are smaller prizes if a player's 
# ticket match two, three, four, or five of the six numbers drawn. 
# As a consequence, the users might be interested in knowing the probability of 
# having two, three, four, or five winning numbers.

# These are the engineering details we'll need to be aware of:

# Inside the app, the user inputs:
# six different numbers from 1 to 49; and
# an integer between 2 and 5 that represents the number of winning numbers expected
# Our function prints information about the probability of 
# having the inputted number of winning numbers.

# To help you code this function, we'll guide you through calculating the probability 
# for having five winning numbers. For the sake of example, let's say a player chose 
# these six numbers on a ticket: (1, 2, 3, 4 ,5 ,6). Out of these six numbers, 
# we can form six five-number combinations:

# (1, 2, 3, 4, 5)
# (1, 2, 3, 4, 6)
# (1, 2, 3, 5, 6)
# (1, 2, 4, 5, 6)
# (1, 3, 4, 5, 6)
# (2, 3, 4, 5, 6)

# We can also find the total number of five-number combinations by calculating (6-over-5) ("6 choose 5"):

# 6C5 = (6-over-5) = 6!/5!(6 - 5)! = 6
# For each one of the six five-number combinations above, 
# there are 44 possible successful outcomes in a lottery drawing. 
# For the combination (1, 2, 3, 4, 5), for instance, there are 44 lottery outcomes 
# that would return a prize:

# (1, 2, 3, 4, 5, 6)
# (1, 2, 3, 4, 5, 7)
# ...
# (1, 2, 3, 4, 5, 30)
# (1, 2, 3, 4, 5, 31)
# ...
# (1, 2, 3, 4, 5, 49)

# Since there are six five-number combinations and each combination corresponds 
# to 44 successful outcomes, we need to multiply 6 by 44 to find the total 
# number of successful outcomes:

# 6 * 44 = 264

# Since there are 264 successful outcomes and there are 13,983,816 total possible outcomes 
# (the result of 49-over-6), the probability of having five winning numbers for a single lottery ticket is:

# P(5-winning numbers) = 264/(49-over-6) = 0.0000189

# Now let's try to code the function. To calculate the probabilities, 
# we tell the engineering team that the specific combination on the ticket is 
# irrelevant behind the scenes, and we only need the integer between 2 and 5 
# representing the number of winning numbers expected.

# TASKS

# Write a function named probability_less_6() which takes in an integer between 2 
# and 5 and prints information about the chances of winning depending on the value of that integer.

# First, calculate the number of successful outcomes given the value of the input. 
# We already covered how to calculate this when the input is 5 — when the input is lower, 
# we need to take the same approach (but be careful, the number of combinations will vary). 
# If you get stuck, try to sneak a look at the solution notebook.

# Second, calculate the number of total possible outcomes.

# Calculate the probability using the number of successful outcomes and the number of total possible outcomes.
# Display the probability value in a way that will be easy to understand for the user.
# Test your function on all possible inputs: 2, 3, 4, and 5.

# Add some context for your readers to explain what you did in this step and why.

def probability_less_6(num_correct_numbers):
        num_combs = combinations(6, num_correct_numbers)
        num_combs_remaining = combinations((49 - num_correct_numbers),
        (6 - num_correct_numbers))
        
        successful_outcomes = num_combs * num_combs_remaining
        n_combs_total = combinations(49, 6)
        
        probability = successful_outcomes / n_combs_total
        probability_percentage = probability * 100
        
        combinations_simplified = round(n_combs_total / successful_outcomes)
        
        print('''Your chances of having {} winning numbers with this ticket are 
        {:.6f}%. In other words, you have a 1 in {:,} chances to win.'''.format(
            str(num_correct_numbers), probability_percentage, int(
                combinations_simplified)))
            
            
for test_input in [2, 3, 4, 5]:
    print('----------------------')
    probability_less_6(test_input)