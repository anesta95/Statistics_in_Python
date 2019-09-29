#!/home/anesta95/.virtualenvs/Stats/bin/python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare
import re

# Jeopardy is a popular TV show in the US where participants answer questions to win money.
# It's been running for a few decades, and is a major force in popular culture.

# Let's say you want to compete on Jeopardy, and you're looking for any edge you can get to win.
# In this project, you'll work with a dataset of Jeopardy questions to figure out
# some patterns in the questions that could help you win.

# The dataset is named jeopardy.csv, and contains 20000 rows from the beginning of
# a full dataset of Jeopardy questions.

# As you can see, each row in the dataset represents a single question on a single
# episode of Jeopardy. Here are explanations of each column:

# Show Number -- the Jeopardy episode number of the show this question was in.
# Air Date -- the date the episode aired.
# Round -- the round of Jeopardy that the question was asked in.
#     Jeopardy has several rounds as each episode progresses.
# Category -- the category of the question.
# Value -- the number of dollars answering the question correctly is worth.
# Question -- the text of the question.
# Answer -- the text of the answer.

# TASKS
# Read the dataset into a Dataframe called jeopardy using Pandas.
# Print out the first 5 rows of jeopardy.
# Print out the columns of jeopardy using jeopardy.columns.
# Some of the column names have spaces in front.
#     Remove the spaces in each item in jeopardy.columns.
#     Assign the result back to jeopardy.columns to fix the column names in jeopardy.
# Make sure you pay close attention to the format of each column.

jeopardy = pd.read_csv('JEOPARDY_CSV.csv')
print(jeopardy.head())
print(jeopardy.columns)

StrippedJeopardyColumns = []
for item in jeopardy.columns:
    item = item.strip()
    StrippedJeopardyColumns.append(item)

jeopardy.columns = StrippedJeopardyColumns

print(jeopardy.columns)

# 2. NORMALIZING TEXT
# Before you can start doing analysis on the Jeopardy questions,
# you need to normalize all of the text columns (the Question and Answer columns).
# We covered normalization before, but the idea is to ensure that you lowercase words
# and remove punctuation so Don't and don't aren't considered to be different words when you compare them.

# TASKS
# Write a function to normalize questions and answers. It should:
# Take in a string.
# Convert the string to lowercase.
# Remove all punctuation in the string.
# Return the string.
# Normalize the Question column.
# Use the Pandas Series.apply method to apply the function to each item in the Question column.
# Assign the result to the clean_question column.
# Normalize the Answer column.
# Use the Pandas Series.apply method to apply the function to each item in the Answer column.
# Assign the result to the clean_answer column.

jeopardy['Answer'] = jeopardy['Answer'].astype(str)
print(jeopardy.dtypes)


def normalize_text(text):
    if text.isdecimal():
        pass
    else:
        text = text.lower()
        text = re.sub("[^A-Za-z0-9\s]", "", text)
    return text

jeopardy["clean_question"] = jeopardy["Question"].apply(normalize_text)
jeopardy["clean_answer"] = jeopardy["Answer"].apply(normalize_text)
print(jeopardy["clean_question"].head())
print(jeopardy["clean_answer"].head())

# 3. NORMALIZING COLUMNS
# Write a function to normalize dollar values. It should:
# Take in a string.
# Remove any punctuation in the string.
# Convert the string to an integer.
# If the conversion has an error, assign 0 instead.
# Return the integer.
# Normalize the Value column.
# Use the Pandas Series.apply method to apply the function to each item in the Value column.
# Assign the result to the clean_value column.
# Use the pandas.to_datetime function to convert the Air Date column to a datetime column.

def normalize_values(text):
    text = re.sub("[A-Za-z0-9\s]", "", text)
    try:
        text = int(text)
    except Exception:
        text = 0
    return text


jeopardy["clean_value"] = jeopardy["Value"].apply(normalize_values)
jeopardy["Air Date"] = pd.to_datetime(jeopardy["Air Date"])

print(jeopardy.dtypes)

# 4. ANSWERS IN QUESTIONS
# In order to figure out whether to study past questions,
# study general knowledge, or not study it all,
# it would be helpful to figure out two things:

# How often the answer is deducible from the question.
# How often new questions are repeats of older questions.

# You can answer the second question by seeing how often complex words (> 6 characters) reoccur.
# You can answer the first question by seeing how many times words in the
# answer also occur in the question. We'll work on the first question now, and come back to the second.

# TASKS
# Write a function that takes in a row in jeopardy, as a Series. It should:
# Split the clean_answer column around spaces and assign to the variable split_answer.

# Split the clean_question column around spaces and assign to the variable split_question.

# Create a variable called match_count, and set it to 0.

# If the is in split_answer, remove it using the remove method on lists.
# The is commonly found in answers and questions, but doesn't have any meaningful use in finding the answer.

# If the length of split_answer is 0, return 0. This prevents a division by zero error later.

# Loop through each item in split_answer, and see if it occurs in split_question.
# If it does, add 1 to match_count.

# Divide match_count by the length of split_answer, and return the result.

# Count how many times terms in clean_answer occur in clean_question.
# Use the Pandas DataFrame.apply method to apply the function to each row in jeopardy.

# Pass the axis=1 argument to apply the function across each row.

# Assign the result to the answer_in_question column.

# Find the mean of the answer_in_question column using the mean method on Series.

def count_matches(row):
    match_count = 0
    split_answer = row['clean_answer'].split(' ')
    split_question = row['clean_question'].split(' ')
    if "the" in split_answer:
        split_answer.remove("the")
    if len(split_answer) == 0:
        return 0
    for word in split_answer:
        if word in split_question:
            match_count += 1
    return (match_count / len(split_answer))

jeopardy['answer_in_question'] = jeopardy.apply(count_matches, axis=1)

print(jeopardy['answer_in_question'].mean())

# The answer only appears in the question about 6% of the time.
# This isn't a huge number, and means that we probably can't just hope that
# hearing a question will enable us to figure out the answer. We'll probably have to study.

# 5. RECYCLED QUESTIONS
# Let's say you want to investigate how often new questions are repeats of older ones.
# You can't completely answer this, because you only have about 10% of the full
# Jeopardy question dataset, but you can investigate it at least.

# To do this, you can:

# Sort jeopardy in order of ascending air date.

# Maintain a set called terms_used that will be empty initially.

# Iterate through each row of jeopardy.

# Split clean_question into words, remove any word shorter than 6 characters,

# and check if each word occurs in terms_used.

# If it does, increment a counter.

# Add each word to terms_used.

# This will enable you to check if the terms in questions have been used previously
# or not. Only looking at words greater than 6 characters enables you to
# filter out words like the and than, which are commonly used,
# but don't tell you a lot about a question.

question_overlap = []
terms_used = set()
jeopardy = jeopardy.sort_values("Air Date")

for i, row in jeopardy.iterrows():
    match_count = 0
    split_question = row['clean_question'].split(' ')
    split_question = [q for q in split_question if len(q) > 5]
    for word in split_question:
        if word in terms_used:
            match_count += 1
    for word in split_question:
        terms_used.add(word)
    if len(split_question) > 0:
        match_count /= len(split_question)
    question_overlap.append(match_count)

jeopardy["question_overlap"] = question_overlap
print(jeopardy["question_overlap"].mean())

# There is about 87% overlap between terms in new questions and terms in old questions.
# This only looks at a small set of questions, and it doesn't look at phrases,
# it looks at single terms. This makes it relatively insignificant,
# but it does mean that it's worth looking more into the recycling of questions.

# 6. LOW VALUE VS HIGH VALUE QUESTIONS
# Let's say you only want to study questions that pertain to high value
# questions instead of low value questions. This will help you earn more money when you're on Jeopardy.

# You can actually figure out which terms correspond to high-value questions
# using a chi-squared test. You'll first need to narrow down the questions into two categories:

# Low value -- Any row where Value is less than 800.
# High value -- Any row where Value is greater than 800.

# You'll then be able to loop through each of the terms from the last screen, terms_used, and:

# Find the number of low value questions the word occurs in.

# Find the number of high value questions the word occurs in.

# Find the percentage of questions the word occurs in.

# Based on the percentage of questions the word occurs in, find expected counts.

# Compute the chi squared value based on the expected counts and
# the observed counts for high and low value questions.

# You can then find the words with the biggest differences in usage between high and
# low value questions, by selecting the words with the highest associated chi-squared values.
# Doing this for all of the words would take a very long time, so we'll just do it for a small sample now

# TASKS

# Create a function that takes in a row from a Dataframe, and:
# If the clean_value column is greater than 800, assign 1 to value.

# Otherwise, assign 0 to value.

# Return value.

# Determine which questions are high and low value.
# Use the Pandas DataFrame.apply method to apply the function to each row in jeopardy.

# Pass the axis=1 argument to apply the function across each row.

# Assign the result to the high_value column.

# Create a function that takes in a word, and:
# Assigns 0 to low_count.

# Assigns 0 to high_count.

# Loops through each row in jeopardy using the iterrows method.

# Split the clean_question column on the space character ().

# If the word is in the split question:
# If the high_value column is 1, add 1 to high_count.

# Else, add 1 to low_count.

# Returns high_count and low_count.
# You can return multiple values by separating them with a comma.

# Create an empty list called observed_expected.

# Convert terms_used into a list using the list function,
# and assign the first 5 elements to comparison_terms.

# Loop through each term in comparison_terms, and:
# Run the function on the term to get the high value and low value counts.

# Append the result of running the function (which will be a list) to observed_expected.

def value_determinator(row):
    if row["clean_value"] > 800:
        value = 1
    else:
        value = 0
    return (value)

jeopardy['high_value'] = jeopardy.apply(value_determinator, axis=1)

def count_word_high_low(word):
    low_count = 0
    high_count = 0
    for i, row in jeopardy.iterrows():
        split_question = row['clean_question'].split(' ')
        if word in split_question:
            if row['high_value'] == 1:
                high_count += 1
            else:
                low_count += 1
    return (high_count, low_count)

observed_expected = []
comparison_terms = list(terms_used)[0:20]

for word in comparison_terms:
    word_list = count_word_high_low(word)
    observed_expected.append(word_list)

print(observed_expected)

# 7. Applying the Chi-squared test
# Now that you've found the observed counts for a few terms,
# you can compute the expected counts and the chi-squared value.

# Find the number of rows in jeopardy where high_value is 1, and assign to high_value_count.

# Find the number of rows in jeopardy where high_value is 0, and assign to low_value_count.

# Create an empty list called chi_squared.

# Loop through each list in observed_expected.
# Add up both items in the list (high and low counts) to get the total count, and assign to total.
# Divide total by the number of rows in jeopardy to get the proportion across the dataset. Assign to total_prop.
# Multiply total_prop by high_value_count to get the expected term count for high value rows.
# Multiply total_prop by low_value_count to get the expected term count for low value rows.
# Use the scipy.stats.chisquare function to compute the chi-squared value and p-value given the expected and observed counts.
# Append the results to chi_squared.

# Look over the chi-squared values and the associated p-values.
# Are there any statistically significant results?

high_value_count = jeopardy[jeopardy['high_value'] == 1]
low_value_count = jeopardy[jeopardy['high_value'] == 0]

chi_squared = []

for list in observed_expected:
    total = sum(list)
    total_prop = total / jeopardy.shape[0]
    high_value_exp = total_prop * high_value_count
    low_value_exp = total_prop * low_value_count

    observed = np.array([list[0], list[1]])
    expected = np.array([high_value_exp, low_value_exp])
    chi_squared.append(chisquare(observed, expected))

print(chi_squared)




