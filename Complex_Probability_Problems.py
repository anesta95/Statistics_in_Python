# 1. COMPLEX PROBABILITY PROBLEMS
# With the concepts and techniques we've learned so far, we're now able to calculate empirical and
# theoretical probabilities for many kinds of events associated with any random experiment.
# There are, however, a few probability problems we cannot yet properly tackle using what we've learned:

# 1. What is the probability that it takes three flips or more for a coin to land heads up?
# 2. What is the probability of a coin landing heads up 18 times in a row?
# 3. What is the probability of getting at least one 6 in four throws of a single six-sided die?
# 4. What is the probability of getting at least one double-six in 24 throws of two six-sided dice?
# 5. What is the probability of getting four aces in a row when drawing cards from a standard 52-card deck?

# In this mission, we're going to develop new techniques that will help us answer all five questions — and many others.

# For now, let's solve a few probability problems as a quick warm-up for the next screen.
# For the exercises below, you'll need to use the addition rule:

# P(A U B) = P(A) + P(B) - P(A ∩ B)

# We'll  also need this formula to compute empirical probabilities:

# P(E) = number of times event E happened / number of times we repeated the experiment

# TASKS
# An advertisement company runs a quick test and
# shows two ads on the same web page (ad "A" and ad "B") to 100 users.
# At the end of the trial, they found:

# 12 users clicked on ad "A"
# 17 users clicked on ad "B"
# 3 users clicked on both ad "A" and ad "B"

# Find:

# The empirical probability that a user clicks on ad "A." Assign your result to p_a.
# The empirical probability that a user clicks on ad "B." Assign your result to p_b.
# The empirical probability that a user clicks on both ad "A" and ad "B."

# Assign your result to p_a_and_b.

# The probability that a user clicks on either ad "A" or ad "B."
# Assign your result to p_a_or_b.
# For this exercise, keep in mind a user can click on both ads,
# so the events are not mutually exclusive — use the addition rule.

p_a = 12/100
p_b = 17/100
p_a_and_b = 3/100
p_a_or_b = ((p_a + p_b) - (p_a_and_b))


# 2. OPPOSITE EVENTS
# In the previous mission, we learned the probability of any event ranges between 0 and 1:
# 0 <= P(Event) <= 1

# Impossible        Probable        Certain
#     0                 0.5             1
#A coin lands       A coin lands    A coin lands
#on something       on tails        on heads or
#other than                         tails
#heads or tails

# We also saw the probability of an event that contains all the outcomes of the sample space is 1
# (recall from the previous mission that a sample space is the set of all possible outcomes of a random experiment;
# the sample space is denoted by the Greek letter Ω -- read "omega"):

# P(Ω) = 1

# For instance, getting a number less than 7 when rolling a six-sided die
# (we'll call this event "A") corresponds to all the outcomes in the sample space, so:

# A = {1, 2, 3, 4, 5, 6}
# Ω = {1, 2, 3, 4, 5, 6}

# P(A) = number of successful outcomes / total number of outcomes = 6/6 = 1 = P(Ω)

# Now consider the two events below, which we're going to call "B" and "non-B":

# Getting a 2 when rolling a fair six-sided die (event B)
# Not getting a 2 when rolling a fair six-sided die (event non-B)

# Events B and non-B correspond to the following outcomes:

# B = {2}
# non-B = {1, 3, 4, 5, 6}

# When we throw the die, it's certain we'll get either a 2 (B) or a different number
# (non-B). This means the event "B or non-B" (B U non-B) is certain, and it has
# a probability of 1.

# Below, we use the addition rule to calculate P(B U non-B)
# (using set notation, remember we write "B or non-B" as B U non-B;
# B and non-B are also mutually exclusive events, which means they can't happen simultaneously —
# we can't get both a 2 and another number when we roll the die):

# P(B U non-B) = P(B) + P(non-B) = 1/6 + 5/6 = 6/6 = 1

# More generally, for any random experiment either event "E" or "non-E" will happen,
# so the event "E or non-E" is certain and has a probability of 1:

# P(E U non-E) = P(E) + P(non-E) = 1

# Using a little algebra, we arrive at the following notation:

# P(E) = 1 - P(non-E)

# On the next screen, we'll explain in detail how the formula above helps us answer
# the first of the five questions we posed in the introduction:
# what is the probability that it takes three flips or more for a coin to land heads up?
# We'll now stop for a few exercises.

# TASKS
# A company that develops a time-tracking tool sells two kinds of subscription:
# basic and premium. When a new user tries the product, there's a 0.2 probability
# the user buys the basic subscription and 0.15 he buys premium. Find:

# The probability that a new user doesn't buy a basic subscription
# (you'll need to use the P(E) = 1 - P(non-E) formula). Assign your result to p_non_basic.

# The probability that a new user doesn't buy a premium subscription.
# Assign your result to p_non_premium.

# The probability that a user buys either basic or premium.
# Assign your result to p_subscription
# (assume buying basic and buying premium are mutually exclusive).

# The probability that a new user doesn't buy a subscription.
# Assign your result to p_non_subscription.

p_non_basic = 0.8
p_non_premium = 0.85
p_subscription = 0.35
p_non_subscription = 0.65

# 3. EXAMPLE WALK-THROUGH
# We'll now build on what we learned in the previous screen and find the probability
# that it takes three flips or more for a coin to land heads up — we're going to call this event "A."

# Event A (it takes three flips or more for a coin to land heads up) corresponds to the following outcomes,
# where each number represents the number of flips it takes until we first get heads up
# (number three, for example, says "the coin first landed heads up on the third flip"):

# A = {3, 4, 5, 6, ..., 100, 101, ...}

#Notice event A contains an infinite number of outcomes.
# When we flip the coin, we could get heads up on the first flip, or the second,
# or the third, the fourth, the fifth and so forth — in principle, we could never get heads up.

#The opposite of event A (it takes less than three flips for the coin to land heads up),
# which we'll call "non-A", has only two outcomes :

#non-A = {1, 2}

# In this random experiment, either A or non-A will happen, so:

# P(A U non-A) = P(A) + P(non-A) = 1

# We're interested in finding P(A) which is:

# P(A) 1 = P(non-A)

# We can find P(A) indirectly by first finding P(non-A), and then substituting in the equation above.

# Recall event A happens if it takes three flips or more for a coin to land heads up.
# If we flip a coin twice and it lands heads up at least once, it means event non-A happens.

#This means finding P(non-A) is equivalent to finding the probability that a coin flipped
# twice lands heads up at least once. If we flip a coin twice, these are all the outcomes we can get:
# {HH, HT, TH, TT} — "H" stands for heads, "T" for tails, and "HT" means "heads on the first flip, and tails on the second one."

'''
First Flip      Second flip         Combined Outcomes
    H               H                       HH
    H               T                       HT
    T               H                       TH
    TT              TT                      TT
'''

# Only the outcomes {HH, HT, TH} are successful with respect to the event non-A (the coin lands
# heads up at least once in two flips). There are four possible outcomes, which means:

# P(non-A) = number of successful outcomes/total number of possible outcomes = 3/4 = 0.75

#Now that we know P(non-A), we can find P(A),
#the probability that it takes three flips or more for a coin to land heads up:

# P(A) = 1 - P(non-A)
# P(A) = 1 - 0.75 = 0.25

# Let's now do a similar exercise to solidify our knowledge.

# TASKS
# Find the probability that it takes four flips or more for a coin to land heads up
# (let's call this event "B").

# Begin with finding the probability of the event non-B,
# which is equivalent to finding the probability that we'll get at least one
# heads if we flip a coin three times. Assign your result to p_non_b.

# Now use p_non_b to find the probability of B. Assign your result to p_b.
# Check the hint if you have difficulties solving this exercise.

p_non_b = 7/8
p_b = 1 - p_non_b

# 4. SET COMPLEMENTS
# On this screen, we introduce some set notation — otherwise things may get
# confusing when you read other resources on probability. In the previous two screens, we saw:

# P(E U non-E) = P(E) + P(non-E) = 1

# Consider the event "getting a 2 when rolling a fair six-sided die,"
# which we'll call "B." Event B corresponds to the set B = {2}

# The event non-B is the opposite of B, and it corresponds to non-B = {1, 3, 4, 5, 6}.
# In set theory, the opposite of a set is called its complement.
# For instance, the opposite of set B is B©,
# where the "C" in the superscript stands for "complement."

# B = {2}
# B© = non-B = {1, 3, 4, 5, 6}

# We can now rewrite the first equation of this screen using set notation:
# P(E U E©) = P(E) + P(E©) = 1


# While this is mere notation, this is what you'll encounter in most probability resources —
# learning it will help you navigate other resources easier. We'll now do a quick
# exercise and begin to tackle the next question on the following screen:
# what is the probability of a coin landing heads up 18 times in a row?

# TASKS
# An advertisement company monitors the activity for a specific ad and shows it
# repeatedly to the same users (so a single user sees the ad multiple times).
# Regardless of the number of times the ad is shown to a user,
# the probability that the user clicks on the ad is 0.5. Find:

# The probability that a user doesn't click on the ad.
# Assign your answer to p_non_click.

# The probability that it takes two times or less for an user to click on the ad.
# Assign your answer to p_two_or_less.

# The probability that it takes three times or more for an user to click on the ad.
# Assign your answer to p_three_or_more.

p_non_click = 0.5
p_two_or_less = 1 - 0.25
p_three_or_more = 0.25

# 5. THE MULTIPLICATION RULE
# Over the next two screens, we're going to learn a new technique that will allow
# us to find the probability of a coin landing heads up 18 times in a row.
# We begin by finding the probability of a coin landing heads up two times in a row.

# If we flip a coin twice, these are all the outcomes we can get
# ("H" stands for heads, "T" for tails, and "HT" means "heads on the first flip,
# and tails on the second flip"):

# {HH, HT, TH, TT}
'''
First Flip      Second flip         Combined Outcomes
    H               H                       HH
    H               T                       HT
    T               H                       TH
    TT              TT                      TT
'''
# From all the possible outcomes, only one outcome (HH) is successful with respect
# to the event where the coin lands heads up two times in a row.
# We'll abbreviate this event "HH", so:

# P(HH) = number of successful outcomes/total number of possible outcomes = 1/4 = 0.25

# This approach works fine when we're dealing with only two flips,
# but things become much more complicated for 18 flips.
# For two flips, we have four possible outcomes (HH, HT, TH, and TT),
# but for 18 flips we have 262,144 possible outcomes
# (we'll learn how to calculate this ourselves in the next mission).
# Let's now look at a different approach of finding P(HH).

# Finding P(HH) means finding the probability that the coin lands heads up on the first flip
# (we'll call this event H1), and the coin lands heads up on the second flip
# (we'll call this event H2). So we want to find P(H1 and H2), or, using set notation, P(H1 ∩ H2).

# To find P(H1 ∩ H2), we can use a new rule called the multiplication rule of probability
# and multiply P(H1) by P(H2):

# P(H1 ∩ H2) = P(H1) x P(H2)

# Assuming the coin is fair, P(H1) = 0.5 and P(H2) = 0.5, so:

# P(H1 ∩ H2) = 0.5 x 0.5 = 0.25

# This is the same result we got from our previous approach.
# In more general terms, the multiplication rule says that for two events
# E1 and E2, the probability that both event E1 AND E2 happen can by found by
# multiplying the probability of E1 by the probability of E2:

# P(E1 ∩ E2) = P(E1) x P(E2)

# We'll continue the discussion in the next screen, where we'll also see the
# multiplication rule is a bit more nuanced. We'll also use the multiplication
# rule to find the probability of a coin landing heads up 18 times in a row.

# TASKS
# For rolling a fair six-sided die, find:

# The probability of getting a 6 two times in a row.
# Assign your result to p_6_6.

# The probability of getting a 3 on the first throw and a 2 on the second throw.
# Assign your result to p_3_2.

# The probability of getting an even number on both throws.
# Assign your result to p_even_even.

# The probability of getting a 1 on the first throw and an even number on the second throw.
# Assign your result to p_1_even.

p_6_6 = (1/6)**2
p_3_2 = (1/6)**2
p_even_even = 0.25
p_1_even = (1/6) * (1/2)

# 6. INDEPENDENT EVENTS
# On the previous screen, we learned to use the multiplication rule to find P(E1 ∩ E2):
# P(E1 ∩ E2) = P(E1) x P(E2)

# The multiplication rule, however, is a bit more nuanced, and
# it doesn't work for all kinds of events — at least not in this form.
# Consider the following two events, which are associated with flipping a fair coin:

# H1: the coin lands heads up on the first flip
# H2: the coin lands heads up on the second flip

# Taken individually, P(H1) = 0.5 and P(H2) = 0.5. If event H1 happens (the coin lands heads up),
# P(H2) keeps the same value (0.5) -- the fact that we get heads up on the first flip
# doesn't influence in any way the probability of getting heads up on the second flip.

# Events that don't influence each other's probability are called independent events.
# If H1 happens, P(H2) stays the same, so H1 and H2 are independent.
# The multiplication rule we learned only works for independent events.

# Consider now the following two events, which are associated with rolling a fair six-sided die:

# A: we get a number less than 4; event A corresponds to the outcomes {1, 2, 3}
# B: we get an even number; event B corresponds to the outcomes {2, 4, 6}

# Taken individually, P(A) = 3/6 and P(A) = 3/6.
# However, if event A happens, then we know for sure the outcome is some number
# from the set associated with A: {1, 2, 3}. If we know event A happened and the
# die showed a number less than 4, then what's the probability of B? Still 3/6?

# Event B (getting an even number) corresponds to the outcomes {2, 4, 6}.
# We know for sure we got one of the numbers {1, 2, 3} — because we know event A happened.
# Only 2 is an even number in {1, 2, 3}, so event B can only happen in this case if the die showed a 2 —
# because event B only happens if the die shows an even number ({2, 4, 6}).
# There are three possible outcomes ({1, 2, 3}) and only one successful outcome ({2}), so P(B) becomes:

# P(B) = number of successful outcomes / total number of possible outcomes = 1/3

# We can conclude that if event A happens, the probability of event B changes.
# If event B happened, this will also change the probability of A.
# Events A and B influence each other's probability, so they are not independent.

# The multiplication rule we learned doesn't work for events that are not independent.
# In a future course, we'll learn conditional probability and
# introduce a revised multiplication rule which also work for non-independent events.
# We'll also get a chance to derive the multiplication rule and understand why it works.

# So far, we've used the multiplication rule to calculate the probability of two independent events.
# The rule, however, works for any number of events —
# what we need to do is multiply together the probability of all the events:

# P(E1 ∩ E2 ∩ E3 ∩ ... ∩ En) = P(E1) x P(E2) x P(E3) x ... x P(En)

# For instance, this is how we find the probability that a coin lands heads up four times in a row:

# P(H1 ∩ H2 ∩ H3 ∩ H4) = P(H1) x P(H2) x P(H3) x ... x P(En)
#                      = 0.5 x 0.5 x 0.5 x 0.5
#                      = 0.0625

# Let's now answer our initial question and a few other that can be solved in the same way.

# TASKS
# Find the probability of:
# Getting heads up 18 times in a row when flipping a fair coin.
# Assign your answer to p_18h.

# Getting a six three times in a row when throwing a fair six-sided die.
# Assign your answer to p_666.

# Not getting any six when throwing a fair six-sided die four times.
# Assign your answer to p_not_6.

p_18h = (0.5) ** 18
p_666 = (1/6) **3
p_not_6 = (5/6)**4

#7. COMBINING FORMULAS
# Previously in this mission, we learned that:
# P(E) = 1 - P(E©)

# We also learned to use the multiplication rule for any number of independent events:
# P(E1 ∩ E2 ∩ E3 ∩ ... ∩ En) = P(E1) x P(E2) x P(E3) x ... x P(En)

# We can combine these two rules to solve two of the probability problems we posed in the beginning:

# What is the probability of getting at least one 6 in four throws of a single six-sided die?
# What is the probability of getting at least one double-six in 24 throws of two six-sided dice
# (the two dice are thrown simultaneously)?

# Let's begin with the first question and use "A" to refer to the event
# "getting at least one 6 in four throws of a single six-sided die".
# To find P(A), we can use the formula:

# P(A) = 1 - P(A©)

# Since event A is getting at least one 6 in four throws, event A© is not getting
#any 6 in four throws. So event A© is equivalent to getting any of the outcomes
# {1, 2, 3, 4, 5} four times in a row. For a single throw, the probability of
# getting any of the outcomes {1, 2, 3, 4, 5} is 5/6.
# Using the multiplication rule, the probability for four throws, is:

# P(A©) = 1 - P(A©)
# P(A©) = (5/6)**4 = 0.4823

# Now that we know P(A©), we can find P(A), which is the probability of getting
# at least one 6 in four throws:

# P(A) = 1 - (5/6)**4 = 0.5177

# The second question is left as an exercise (you can find the answer using an
# identical approach as we took above for the first question).
# On the next screen, we're going to answer our last question and
# find the probability of getting four aces in a row when drawing cards
# from a standard 52-card deck — we'll see this problem is a bit tricky.

# TASKS
# Find the probability of getting at least one double-six in 24 throws of two
# six-sided dice (the two dice are thrown simultaneously).
# Assign your answer to p_one_double_6.
# The table below shows all the outcomes of throwing two six-sided dice.

p_one_double_6 = 1 - (35/36) ** 24

# 8. SAMPLING WITH(OUT) REPLACEMENT
# On this screen, we're going to find the probability of getting four aces
# in a row when drawing cards from a standard 52-card deck.
# The deck has four aces and a total of 52 cards.

# Since there are four aces and 52 cards,
# the probability of drawing an ace if we draw a card is:

# P(Ace) = 4/52

# You might think that in order to find the probability of drawing four aces in a row
# (we'll call this event "AAAA"), all we need to do is multiply P(Ace) by itself four times:

# P(AAAA) = (4/52) ** 4 = 0.000035

# However, whether multiplying P(Ace) by itself four times is correct or not depends
# on an important detail: whether we put the cards we draw back in the deck.
# Let's first consider the case where we draw cards from the deck, but we don't put them back.

# As we saw before, for the first draw, P(Ace) = 4/52. Let's say we draw a card,
# which is an ace of diamonds, and don't put the card back in the deck.
# Because we don't put the ace of diamonds back, we now have a deck of 51 cards,
# where only three cards are aces.

# With 51 cards and three aces, the probability of getting an ace for the second draw is:
# P(Ace) = 3/51

# To find the probability of getting four aces in a row,
# we need to take into account at each step that the card is not put back in the deck:

# P(AAAA) = 4/52 x 3/51 x 2/50 x 1/49 = 0.00000369

# If we do put the cards back in the deck after drawing, then P(Ace) = 4/52 for every draw.
# In this case, it's correct to do:

# P(AAAA) = (4/52) ** 4 = 0.000035

# When we replace the cards after drawing, we say that we're sampling with replacement.
# When we don't put the cards back, we're sampling without replacement.
# In either case, the chances of getting four aces in a row are extremely low,
# so remember: never bet on getting four aces in a row.

# Let's now look at a similar exercise and wrap up this mission on the next screen.

# We're sampling without replacement from a standard 52-card deck. Find the probability of:

#Getting two kings in a row. Assign your answer to p_kk.

#Getting a seven of hearts, followed by a queen of diamonds. Assign your answer to p_7q.

#Getting a jack, followed by a queen of diamonds, followed by a king, followed by another jack.

#Assign your answer to p_jqkj. This one is a bit tricky, so pay attention to the details of the question.

p_kk = (4/52) * (3/51)
p_7q = (1/52) * (1/51)
p_jqkj = (4/52) * (1/51) * (4/50) * (3/49)

# 9. NEXT STEPS
# In the next mission, we'll solve even more complex probability problems
# using special counting techniques like permutations and combinations.


