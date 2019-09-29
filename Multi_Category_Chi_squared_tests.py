#!/home/anesta95/.virtualenvs/Stats/bin/python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare
from scipy.stats import chi2_contingency
# 1. MULTIPLE CATEGORIES
income = pd.read_csv('income.csv')
# In the last mission, we looked at the gender frequencies of people included in a
# data set on US income. The dataset consists of 32561 rows, and here are the first few:

print(income.head())

# Each row represents a single person who was counted in the 1990 US Census,
# and contains information about their income and demograpics.
# Here are some of the relevant columns:

# age -- how old the person is
# workclass -- the type of sector the person is employed in.
# race -- the race of the person.
# sex -- the gender of the person, either Male or Female.
# high_income -- if the person makes more the 50k or not.

# In the last mission, we calculated a chi-squared value indicating how the
# observed frequencies in a single categorical column, such as sex,
# varied from the US population as a whole.

# In this mission, we'll look how to make this same technique applicable to cross tables,
# that show how two categorical columns interact.
# For instance, here's a table showing the relationship between sex and high_income:

'''
                             Sex
                Male        Female      Totals
        >50k    6662        1179        7841
Income <=50k    15128       9592        24720
        Totals  21790       10771       32561
'''

# On looking at this diagram, you might see a pattern between sex and high_income.
# But it's hard to immediately quantify that pattern, and tell if it's significant.
# We can apply the chi-squared test (also known as the chi-squared test of association)
# to figure out if there's a statistically significant correlation between two categorical columns.

# 2. CALCULATING EXPECTED VALUES
# In the single category chi-squared test, we find expected values from other data sets,
# and then compare with our own observed values. In a multiple category chi-squared test,
# we calculate expected values across our whole dataset.
# We'll illustrate this by converting our chart from last screen into proportions:

'''
                             Sex
                Male        Female      Totals
        >50k    .205        .036        .241
Income <=50k    .465        .294        .759
        Totals  .67         .33           1
'''

# Each cell represents the proportion of people in the data set that fall into the specified categories.

# 20.5% of Males in the whole data set earn >50k in income.
# 33% of the whole dataset is Female
# 75.9% of the whole dataset earns <=50k.

# We can use our total proportions to calculate expected values.
# 24.1% of all people in income earn >50k, and 33% of all people in income are Female,
# so we'd expect the proportion of people who are female and earn >50k to be 0.241 * 0.33,
# which is 0.07953. We have this expectation based on the proportions of Females and
# >50k earners across the whole dataset. Instead, we see that the observed proportion is 0.036,
# which indicates that there may be some correlation between the sex and high_income columns.

# We can convert our expected proportion to an expected value by multiplying by 32561,
# the total number of rows in the data set, which gives us 32561 * 0.07953, or 2589.6.

# Using the expected proportions in the table above,
# calculate the expected values for each of the 4 cells in the table.

# Calculate the expected value for Males who earn >50k, and assign to males_over50k.
# Calculate the expected value for Males who earn <=50k, and assign to males_under50k.
# Calculate the expected value for Females who earn >50k, and assign to females_over50k.
# Calculate the expected value for Females who earn <=50k, and assign to females_under50k.

males_over50k = 32561 * (.67 * .241)
males_under50k = 32561 * (.67 * .759)
females_over50k = 32561 * (.33 * .241)
females_under50k = 32561 * (.33 * .759)

# 3. CALCULATING CHI-SQUARED
# In the last screen, you should have ended up with a table like this:

'''
                        Sex
                Male        Female
        >50k    5257.6      2589.6
Income
        <=50k   16558.2     8155.6
'''

# Now that we have our expected values,
# we can calculate the chi-squared value by using the same principle from the previous mission.
# Here are the steps:

# Subtract the expected value from the observed value.
# Square the difference.
# Divide the squared difference by the expected value.
# Repeat for all the observed and expected values and add up the values.

# Here's the formula:

#SumOf((Observed - Expected)**2) / expected)

# Here's a table of our observed values for reference:
'''
                        Sex
                Male        Female
        >50k    6662        1179
Income
        <=50k   15128       9592
'''


# TASKS
# Compute the chi-squared value for the observed values above and the expected values above.
# Assign the result to chisq_gender_income.

diffs = []
observed = [6662, 15128, 1179, 9592]
expected = [5257.6, 16558.2, 2589.6, 8155.6]
for i, obs in enumerate(observed):
    exp = expected[i]
    diff = (obs - exp) ** 2 / exp
    diffs.append(diff)

chisq_gender_income = sum(diffs)

print(chisq_gender_income)

# 4. FINDING STATISTICSAL SIGNIFICANCE
# Now that we've found our chi-squared value, 1520.0, we can use the same technique
# with the chi-squared sampling distribution from the last mission to find a p-value
# associated with the chi-squared value. The p-value will tell us whether the difference
# between the observed and expected values is statistically significant or not.

# Rather than construct a sampling distribution again manually,
# we'll use the scipy.stats.chisquare function that we covered in the last mission.

# If we had a table of expected values that looked like this:
'''
  5 | 5
----|----
 10 | 10
'''

# And a table of observed values that looked like this:

'''
 10 | 10
----|----
 5  | 5
'''

# We could find the chi-squared value and
# the p-value using the scipy.stats.chisquare function like this:

# import numpy as np
# from scipy.stats import chisquare

# observed = np.array([10, 10, 5, 5])
# expected = np.array([5, 5, 10, 10])
# chisquare_value, pvalue = chisquare(observed, expected)

# TASKS
# Here are our expected values from the last screen:

'''
                        Sex
                Male        Female
        >50k    5257.6      2589.6
Income
        <=50k   16558.2     8155.6
'''

# And here are our observed values:

'''
                        Sex
                Male        Female
        >50k    6662        1179
Income
        <=50k   15128       9592
'''

# Use the scipy.stats.chisquare function to find the chi-squared value
# and p-value for the above observed and expected counts.
# Assign the p-value to pvalue_gender_income.

observed = np.array([6662, 15128, 1179, 9592])
expected = np.array([5257.6, 16558.2, 2589.6, 8155.6])

chi_square_gender_income, pvalue_gender_income = chisquare(observed, expected)

print(pvalue_gender_income)

# 5. CROSS TABLES
# We can also scale up the chi-squared test to cases where each category contains
# more than two possibilities. We'll illustrate this with an example where we look at sex vs race.

# Before we can find the chi-squared value, we need to find the observed frequency counts.
# We can do this using the pandas.crosstab function.
# The crosstab function will print a table that shows frequency counts for two or more columns.
# Here's how you could use the pandas.crosstab function:

# import pandas

# table = pandas.crosstab(income["sex"], [income["high_income"]])
# print(table)

# The above code will print a table showing how many people from
# income fall into each category of sex and high_income.

# The second parameter passed into pandas.crosstab is actually a list --
# this parameter can contain more than one item.

# TASKS
# Use the pandas.crosstab function to print out a table comparing
# the sex column of income to the race column of income.

sex_by_race = pd.crosstab(income['sex'], [income['race']])
print(sex_by_race)

# 6. FINDING EXPECTED VALUES
# Now that we have the observed frequency counts, we can generate the expected values.
# We can use the scipy.stats.chi2_contingency function to do this.
# The function takes in a cross table of observed counts, and returns the chi-squared value,
# the p-value, the degrees of freedom, and the expected frequencies.
# Let's say we have the following observed counts:

'''
  5 | 5
----|----
 10 | 10
'''

# Here's how we could use the scipy.stats.chi2_contingency function:
# import numpy as np
# from scipy.stats import chi2_contingency
# observed = np.array([[5, 5], [10, 10]])

# chisq_value, pvalue, df, expected = chi2_contingency(observed)

# You can also directly pass the result of the pandas.crosstab function into the
# scipy.stats.chi2_contingency function, which makes it extremely easy to perform a chi-squared test.

# Use the scipy.stats.chi2_contingency function to calculate the p-value for the sex and race columns of income.
# Assign the result to pvalue_gender_race.

chisq_gr, pvalue_gender_race, df_gr, expected_gr = chi2_contingency(sex_by_race)
print(pvalue_gender_race)

# 7. CAVEATS
# Now that we've learned the chi-squared test, you should be able to figure out if
# the association between two columns of categorical data is statistically significant or not.
# There are a few caveats to using the chi-squared test that are important to cover, though:

# Finding that a result isn't significant doesn't mean that no association between the columns exists.
# For instance, if we found that the chi-squared test between the sex and race columns returned a p-value of .1,
# it wouldn't mean that there is no relationship between sex and race.
# It just means that there isn't a statistically significant relationship.

# Finding a statistically significant result doesn't imply anything about what the correlation is.
# For instance, finding that a chi-squared test between sex and race results in a p-value of .01
# doesn't mean that the dataset contains too many Females who are White (or too few).
# A statistically significant finding means that some evidence of a relationship between the variables exists,
# but needs to be investigated further.

# Chi-squared tests can only be applied in the case where each possibility within a category is independent.
# For instance, the Census counts individuals as either Male or Female, not both.

# Chi-squared tests are more valid when the numbers in each cell of the cross table are larger.
# So if each number is 100, great -- if each number is 1, you may need to gather more data.
