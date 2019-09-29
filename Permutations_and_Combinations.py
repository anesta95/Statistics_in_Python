    # 1. THE RULE OF PRODUCT
# So far in our course, we learned to calculate probabilities for all sorts of events.
# In this mission, we'll direct our focus not so much toward calculating probabilities,
# but toward calculating the number of outcomes associated with various random experiments.
# We'll learn some powerful counting techniques that will allow us to answer questions like:

# What is the probability of cracking a 4-digit PIN code using the code 8362?
# What is the probability of cracking a 6-digit PIN code using the code 348821?
# What is the probability of winning the big prize in a state lottery if we use the numbers
# (3, 20, 37, 44, 45, 49)?

# We begin with considering a composite experiment A1A2 made of two different experiments,
# which we denote by "A1" and "A2":

# A1: flipping a coin
# A2: throwing a six-sided die

# A1A2 means we flip a coin and throw a die and consider the outcomes of the two individual
# experiments together (the two individual experiments are flipping a coin and throwing a die).
# One of the possible outcomes of the composite experiment A1A2 is (H,1),
# which means the coin lands heads up and the die shows a 1.
# There are 12 possible outcomes associated with A1A2:

# Ω = {(H, 1), (H, 2), (H, 3), (H, 4), (H, 5), (H, 6), (T, 1), (T, 2), (T, 3), (T, 4), (T, 5), (T, 6)}

# When we flip the coin, there are two possible outcomes: heads or tails.
# Each of the two outcomes can be followed by six other outcomes,
# depending how the six-sided die lands. If there are two outcomes,
# and each of these two have six other corresponding outcomes,
# we can use multiplication to find the total number of outcomes:

# Number of outcomes = 2 x 6 = 12

# Generally, if we have an experiment E1 (like flipping a coin) with a outcomes,
# followed by an experiment E2 (like rolling a die) with b outcomes,
# then the total number of outcomes for the composite experiment E1E2
# can be found by multiplying a with b:

# Number of outcomes = a x b

# The formula above is known as the rule of product (or the multiplication principle).
# Note that this is different than the multiplication rule we learned in the previous mission.

# We'll use the rule of product throughout this mission to build more powerful counting techniques.
# For now, let's do a quick exercise.

# TASKS
# Consider the composite experiment E1E2, where E1 is rolling a fair six-sided die once,
# and E2 is rolling the same die again.
# One of the outcomes of E1E2 could be (1, 6), which means we get a 1 for the first roll
# and a 6 for the second one.

# 1. Use the rule of product to calculate the total number of outcomes.
# Assign your answer to n_outcomes.

# 2. Use n_outcomes to calculate the probability of getting a (6,6).
# Assign your answer to p_six_six. Check the hint if you have difficulties calculating this.

# 3. Use n_outcomes to calculate the probability of not getting a (5,5) and
# assign your answer to p_not_five_five.

n_outcomes = 36
p_six_six = 1 / n_outcomes
p_not_five_five = 35/n_outcomes

# 2. EXTENDED RULE OF PRODUCT
# On the previous screen, we learned that if we have an experiment E1
# (like flipping a coin) with a outcomes, followed by an experiment E2
# (like rolling a die) with b outcomes, then the total number of outcomes for the
# composite experiment E1E2 can be found by multiplying a with b (recall this is called the rule of product):

# Number of outcomes = a x b

# We can extend the rule of product for any number of experiments.
# For instance, consider the composite experiment E1E2E3, where:

# E1 is flipping a coin
# E2 is rolling a six-sided die
# E3 is flipping a coin (again, yes)

# We can extend the rule of product and multiply the outcomes of each experiment to get 24 outcomes:

# Number of outcomes = 2 x 6 x 2

# More generally, if we have an experiment E1 with a outcomes,
# followed by an experiment E2 with b outcomes, followed by an experiment En with z outcomes,
# the total number of outcomes for the composite experiment E1E2 ... En
# can be found by multiplying their individual outcomes:

# Number of outcomes = a x b x .. x z

# Let's now use this extended rule of product to calculate more outcomes and probabilities.

# TASKS
# We roll a fair six-sided die three times and then randomly draw a card from a standard 52-card deck.
# One of the outcomes could be (6, 6, 6, ace of diamonds),
# which means getting three 6's in a row when we roll the die,
# followed by drawing an ace of diamonds from the deck.

# 1. Use the extended rule of product to calculate the total number of outcomes.
# Assign your answer to total_outcomes.

# 2. Use total_outcomes to calculate the probability of getting (6, 6, 6, ace of diamonds) —
# three sixes in a row followed by an ace of diamonds. Assign your answer to p_666_ace_diamonds.

# 3. Use p_666_ace_diamonds to calculate the probability of getting anything but (6, 6, 6, ace of diamonds).
# Assign your answer to p_no_666_ace_diamonds.

total_outcomes = (6 ** 3) * 52
p_666_ace_diamonds = 1 / total_outcomes
p_no_666_ace_diamonds = 1 - p_666_ace_diamonds

# 3. EXAMPLE WALKTHROUGH
# On the previous screen, we learned to compute the number of outcomes for any composite experiment E1E2 ... En
# using the formula below (where a, b, and z represent the number of outcomes associated with the individual
# experiments that are part of the composite experiment E1E2 ... En):

# Number of outcomes = a * b * ... * z

# Let's say we're interested in finding the probability of cracking a 4-digit PIN code using the code 8362
# (we chose 8362 randomly). To calculate the probability, we can use the formula:

# P(E) = number of successful outcomes / total number of possible outcomes

# The code "8362" is the only successful outcome, so the formula above becomes:

# P(E) = 1/total number of possible outcomes

# To find the total number of possible outcomes, we need to find the total number of possible 4-digit PIN codes.
# One way to form a 4-digit code is to sample with replacement four times from the set {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} —
# recall sampling with replacement means randomly extracting an element from a group,
# and then putting the element back in the group.
# The process of forming a 4-digit code can be broken down to four experiments:

# E1, which has 10 possible outcomes: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# E2, which has 10 possible outcomes: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# E3, which has 10 possible outcomes: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# E4, which has 10 possible outcomes: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# A 4-digit code can be thought of as the result of the composite experiment E1E2E3E4.
# For instance, the code 5391 means the experiment:

# E1 ended in a 5.
# E2 ended in a 3.
# E3 ended in a 9.
# E4 ended in a 1.

# Finding the total number of possible 4-digit codes is equivalent to finding the total
# number of outcomes for the composite experiment E1E2E3E4,
# for which we can use the extended rule of product:

# Number of outcomes = 10 x 10 x 10 x 10 = 10,000

# We conclude we have 10,000 possible 4-digit PIN codes.
# This makes some intuitive sense, since 4-digit PIN codes vary between 0000 and 9999
# (this is like counting from 0 to 9999: 0000, 0001, 0002, ..., 9998, 9999).

# In the following exercise, we're going to find the probability of cracking a
# 4-digit PIN code using the code 8362.

# TASKS

# Find the probability of cracking a 4-digit PIN code using the code 8362.
# Assign your answer to p_crack_4.

# Find the probability of cracking a 6-digit PIN code using the code 348821.
# Assign your answer to p_crack_6.

p_crack_4 = 1 / (10 ** 4)
p_crack_6 = 1 / (10 ** 6)

# 4. PERMUTATIONS
# On the last screen, we used the extended rule of product and saw we have 10,000 possible 4-digit PIN codes:

# Number of outcomes = 10 * 10 * 10 * 10

# Each PIN code represents a certain arrangement where the order of the individual digits matters.
# Because order matters, the code 1289 is different than the code 9821,
# even though both codes are composed of the same four digits: 1, 2, 8 and 9.
# If the order of digits didn't matter, 1289 would be the same as 9821.

# More generally, a certain arrangement where the order of the individual elements matters is called a permutation.
# For instance, there are 10,000 possible permutations for a 4-digit PIN code
# (in other words, there are 10,000 digit arrangements where the order of the digits matters).

# Let's now turn our attention to another example,
# where we're interested in finding the total number of possible permutations
# for the numbers {5, 6, 7} — one possible permutation would be 567, another 657, and so on.

# However, this time we want to form the permutations by sampling without replacement.
# For instance, if we sample once without replacement from the set {5, 6, 7} and get a 5,
# we don't put the 5 back in the set, and only {6, 7} remains for the second round of sampling.

# To form a permutation like 567 or 657,
# we need to sample three times from the set {5, 6, 7}.
# Since we sample three times, we can break down the entire process into three experiments:

# E1, which has three possible outcomes: {5, 6, 7}
# E2, which has two possible outcomes left
# (because we sample without replacement we leave out the element we got at E1;
# if we get a 6 at E1, only {5, 7} is left for E2)
# E3, which has one possible outcome left

# Using the extended rule of product,
# we see we have a total of six outcomes for the composite experiment E1E2E3:

# Number of outcomes = 3 * 2 * 1

# This makes sense, since these are all the possible permutations (arrangements)
# of {5, 6, 7} when we sample without replacement: 567, 576, 657, 675, 756, 765.

# More generally, if there are n outcomes for the first experiment, (n-1) outcomes for the second,
# (n-2) for the third, ..., and only one outcome for the last experiment,
# then we can find the number of permutations using the formula:

# Permutations = n * (n-1) * (n-2) * ... * 2 * 1

# In mathematics, the expression n * (n-1) * (n-2) * ... * 2 * 1 is often abbreviated as n!

# For instance, if n = 5, then n! = 5 * 4 * 3 * 2 * 1. The expression n! is called a factorial
# and is read as "n factorial"

# For our case above with finding the total number of permutations for {5, 6, 7}, n = 3. To find
# the total number of permutations we use:

# n! = 3! = 3 * 2 * 1
# To summarize, when we sample with replacement, the number of permutations is given by the formula:

# Permutations = n!
# We're now going to do an exercise and resume the discussion about permutations on the next screen.

# TASKS

# Write a function named factorial() which takes as input a number n and computes
# the factorial of that number n. There's more than one way to code this function,
# so we'll leave this exercise open — check the hint section if you get stuck.

# Use the factorial() function to find the total number of permutations
# (arrangements where order matters) for the letters "a", "b", "j", "k", "x", "y"
# (the letters cannot be repeated — this is equivalent to sampling without replacement
# from the set {"a", "b", "j", "k", "x", "y"}. Assign your answer to permutations_1.

# Use the factorial() function to find the total number of permutations for the 52 cards
# of a standard 52-card deck. Assign your answer to permutations_2.

def factorial(num):
    final_product = 1
    for i in range(num, 0, -1):
        final_product *= i
    return (final_product)

permutations_1 = factorial(6)
permutations_2 = factorial(52)
print(permutations_1)
print(permutations_2)
# 5. In the last exercise, we calculated the number of permutations for the 52 cards
# of a standard 52-card deck. In practice, however, we're usually interested in
# finding the number of permutations for a limited number of cards.

# For instance, in Texas hold 'em, which is a variation of poker,
# players are interested in having a winning 5-card poker hand.
# To find the total number of possible permutations for a 5-card poker hand,
# we can start by considering we're sampling without replacement five times from a standard 52-card deck:

# E1 — we have 52 cards in the deck, so 52 outcomes are possible
# E2 — we have 51 cards left in the deck, so 51 outcomes are possible
# (because we sample with replacement, we don't put back in the deck the card we got at E1)
# E3 — we have 50 cards left in the deck, so 50 outcomes are possible
# E4 — we have 49 cards left in the deck, so 49 outcomes are possible
# E5 — we have 48 cards left in the deck, so 48 outcomes are possible

# We can use the extended rule of product to calculate the number of permutations for a 5-card poker hand:

# Permutations = 52 * 51 * 50 * 49 * 48 = 311,875,200

# Note that we can't use Permutations = n! formula to calculate the number of permutations
# for a 5-card poker hand because in our case n = 52, and that'd lead us to a wrong result

# Permutations = 52 * 51 * 50 * ... * 3 * 2 * 1

# More generally, when we have a group of n objects,
# but we're taking only k objects, the number of permutations (which we abbreviate as "P") is:

# nPk = n * (n - 1) * (n - 2) * ... * (n - k + 1)

# In our 5-card poker hadn example, n = 52, and k = 5 so:

# 52P5 = 52 * (52 - 1) * (52 - 2) * (52 - 3) * (52 - 5 + 1)
# 52P5 = 52 * 51 * 50 * 49 * 48
# 52P5 = 311,875,200

# We're now going to do a quick exercise, and then discuss more about the formula we just learned.

# Using the formula we just learned, calculate:
# The number of permutations for 3-card hand when we're drawing without replacement
# from a 52-card standard deck. Assign your answer to perm_3_52.

# The number of permutations for a 4-card hand when we're drawing without replacement
# from a 20-card deck. Assign your answer to perm_4_20.

# The number of permutations for 4-card hand when we're drawing without replacement
# from a 27-card deck. Assign your answer to perm_4_27.

perm_3_52 = (52 * 51 * 50)
perm_4_20 = (20 * 19 * 18 * 17)
perm_4_27 = (27 * 26 * 25 * 24)

# 6. PERMUTATIONS FORMULAS
# On the last screen, we learned to use the formula below to calculate permutations
# when we're sampling without replacement and taking only k objects from a group of n objects:

# nPk = n * (n - 1) * (n - 2) * ... * (n - k + 1)

# We applied the formula to calculate the number of permutations for a 5-card poker hand,
# and we saw that n = 52 and k = 5 for a 52-card standard deck, so:

# 52P5 = 52 * (52 - 1) * (52 - 2) * (52 - 3) * (52 - 5 + 1)
# 52P5 = 52 * 51 * 50 * 49 * 48
# 52P5 = 311,875,200

# When k is large, however, calculations tend to become a bit messy. If n = 52, and
# k = 20, then we'd have:

# 52P20 = 52 * 51 * 50 * 49 * 48 * ... * 35 * 34 * 33 * 32 * 31

# To make calculations neater, the formula is oftentimes written in terms of factorials:

# nPk = n! / (n - k)!

# If we use this formula for our 5-card example, we get the same result:

# 52P5 = 52!/(52 - 5)! = 52! / 47! = 311,875,200
# To see how this new formula is equivalent to the initial one,
# let's extend the numerator and the denominator:

# nPk = n!/(n - k)! =
# n * (n - 1) * ... * (n - k + 1) * (n - k) * ... * 2 * 1 / (n - k) * ...* 2 * 1

# If we cancel out the similar terms in the numerator and the denominator, we are left with the initial formula:
# nPk = n!/(n - k)! = n * (n - 1) * ... * (n - k + 1)

# Let's now write a function for this formula and find the answer to a probability problem.

# TASKS
# Write a function named permutation() which takes in two inputs (n and k) and
# outputs the number of permutations when we're taking only k objects from a group of n objects.
# To simplify your work, use the factorial() function we wrote on a previous screen.

# A password manager software generates 16-character passwords from a list of 127 characters
# (the list contains numbers, letters, or other symbols).
# Assume the sampling from the list is done randomly and without replacement,
# and find the probability of cracking a password generated by this software if
# we're using the password "@*AmgJ(UL3Yl726x", which has 16 characters. Assign your answer to p_crack_pass.

def permutation(n, k):
    final_product = 1
    for i in range(n, (n - k), -1):
        final_product *= i
    return (final_product)

p_crack_pass = 1 / (permutation(127, 16))
print(p_crack_pass)

#7. UNIQUE ARRANGEMENTS
# Previously, we mentioned players in Texas hold 'em are interested in having a
# winning 5-card poker hand. To find the number of permutations for a 5-card poker hand,
# we learned to use this formula:

# nPk = n!/(n-k)!
# 52P5 = 52! / (52-5)! = 311,875,200

# However, remember that a permutation is an arrangement of elements where order matters.
# The three 5-card hands we see below, for instance,
# have the same cards and yet are considered different permutations (arrangements) because order matters:

# 2S  6H  7C  10S 7D
# 7D  2S  10S 6H  7C
# 10S 7C  6H  7D  2S

# In a poker game, however, the order of cards is not important,
# so the three hands above would be considered identical.
# Consequently, we might be interested instead in ignoring the order and
# finding the number of unique card arrangements.

# To find the number of unique card arrangements,
# we begin with the observation that each unique 5-card arrangement has 5! = 120 permutations.

# In other words, the five cards of a unique hand can be ordered in 120 different ways.
# In the diagram above, we see just three out the 120 permutations of that unique hand.

# If each unique hand can be arranged in 5! = 120 ways and there are C total unique hands,
# then C * 5! gives us the total number of permutations of a 5-card hand:

# C * 5! = 52P5

# Now finding the number of unique 5-card hands means finding C in the equation above.
# Using a little algebra, we isolate C on the left side of the equal sign:

# C (number of unique 5 card hands) = 52P5 (Number of permutations for a 5-card poker hand)/
# 5! (number of ways each unique hand can be arranged)

# We now extend 52P5 in the numerator and calculate C, the total number of unique 5-card hands:

# C = (52! / (52 - 5)!) / 5! = 2598960

# We can see the number of unique 5-card hands (2,598,960)
# is much lower than the number of permutations of all 5-card hands (311,875,200).
# Let's now do an exercise and use what we found to calculate some probabilities.
# We'll discuss more about unique arrangements on the next screen.

# TASKS
# Use the factorial() and permutation() functions to calculate the number of unique
# 5-card arrangements when drawing without replacement from a standard 52-card deck.
# Assign your answer to a variable named c.

# Calculate the probability of getting a 5-card hand with four aces and a seven of diamonds
# (assume we're drawing randomly and without replacement from the deck).
# Assign your answer to p_aces_7.

# For a state lottery, six numbers are drawn randomly and without replacement from
# an urn containing numbers from 1 to 49. Using the factorial() and the permutation()
# functions, find the total number of unique 6-number arrangements that could result.
# Assign your answer to c_lottery.

# Calculate the probability of winning the big prize for this state lottery provided you use the numbers
# (3, 20, 37, 44, 45, 49) — the big prize means the numbers match exactly those resulted from the official drawing.

# Assign your answer to p_big_prize.
# Print p_big_prize to see what are the chances of winning the big prize and
# think whether you'd recommend spending money on lottery to a close friend.

c = permutation(52, 5) / factorial(5)
p_aces_7 = 1 / c
c_lottery = permutation(49, 6) / factorial(6)
p_big_prize = 1 / c_lottery
print(p_aces_7)
print(p_big_prize)

# 8. COMBINATIONS
# On the previous screen, we made the observation that in a poker game the order in
# which the cards are arranged in a 5-card hand doesn't matter.
# We saw, for instance, that these three different arrangements would be considered
# identical in a poker game:

# 2S  6H  7C  10S 7D
# 7D  2S  10S 6H  7C
# 10S 7C  6H  7D  2S

# More generally, if the order of the elements in an arrangement doesn't matter,
# the arrangement is called a combination. Combinations are the opposite of permutations,
# where the order of the elements does matter. To sum it up, we have two kinds of arrangements:

# Arrangements where the order matters, which we call permutations.
# Arrangements where the order doesn't matter, which we call combinations.
# On the previous screen, we used this technique to calculate the number of combinations (number of unique 5 card hands):

# C = 52P5(Number of permutations for a 5-card poker hand) / 5! (number of ways each unique hand can be arranged) =
# 2,598,960

# We need to transform this technique into a general formula that we can use to
# calculate combinations for any kind of situation, not just 5-card poker hands.

# The notation 52P5 we used is a variation of the nPk, where n = 52 and k = 5.
# We'll replace 52P5 with nPk to make the formula more general (the 5! in the denominator also becomes k!):

# C = 52P5 / 5! ==> C = nPk / k!

# Now, we expand nPk in the numerator:

# C = nPk / k! = (n!/(n - k)!) / k!

# We simplify the fractions above using a little algebra:

# C = nPk/k! = (n!/(n-k)!)/k! = n! / k!(n - k)!

# Above we transformed (n!/(n-k)!)/k! to n! / k!(n - k)!, and the final formula
# that we can use moving forward is:

# C = n! / k!(n - k)!

# There's some specific notation for combinations: C is written as nCk.
# More often, however, nCk is written as (n-over-k), which we read as "n choose k".

# nCk = (n-over-k) = n!/k!(n-k)!

# If we wanted, for instance, to calculate the number of unique ways we can extract
# 10 books from a small library of 35 different books, we can calculate (35-over-10) ("35 choose 10"):

# (35-over-10) = 35C10 = 35!/10!(35-10)! = 183,579,396

# Let's now write a function for our formula above, solve a few probability problems, and wrap up this mission on the next screen.

def combinations(n, k):
    numerator = factorial(n)
    denominator = factorial(k) * (factorial(n-k))
    return (numerator / denominator)

c_18 = combinations(34, 18)
p_non_Y = 1 - (1 / c_18)

print(c_18)
print(p_non_Y)

