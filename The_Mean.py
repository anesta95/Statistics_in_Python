import pandas as pd
import statistics as stat
from numpy.random import randint, seed
import matplotlib.pyplot as plt
#INTRODUCTION
#Throughout this course we'll learn to summarize the distribution of a variable
#with a single value. Depending on the particular characteristics of a distribution,
#we'll see that we can summarize it using the mean, the weighted mean, the median, or the mode.

#We'll also learn to measure the variability in a distribution.
#If we have a distribution A with the values [3, 3, 3, 3], and a distribution B
#with [30, 1, 15, 43], we can clearly see that there's much more variability
#(diversity) in B. We'll learn to quantify variability using measures like
#variance and standard deviation.

#Once we understand the measures of variability, we can then learn how to locate
#a value in a distribution, and determine how it compares to other values.
#For instance, when we analyze salaries, we might want to find out whether a
#salary of $75000 is common or extreme inside a company.
#We'll learn to answer this question with precision using a z-score.

#In this first mission, we'll have a detailed discussion about the mean.
#We already learned briefly about the mean in the previous courses of the data
#science path, but here we discuss the concept again to give the explanations
#much more depth.

#2. THE MEAN

#Let's say we want to summarize the distribution below with a single value that
#is representative of the distribution as a whole.

#[0,1,4,7,8,10]

#Intuitively, we need to take into account equally every single value in the distribution
#if we want to find a good summary value that's representative of the entire distribution.
#We could try to sum all the values in the distribution, and then divide the total by the number of values we added —
#this way we'll manage to take into account equally every value in the distribution:

#0 + 1 + 4 + 7 + 8 + 10 / 6 = 30 / 6 = 5

#When we compute the summary value of a distribution in this way,
#we call the value the arithmetic mean, or the mean. For our distribution above,
#the mean is 5.

#We have good reasons to consider 5 a representative value for the distribution above.
#First, notice that 5 is right at the center of the distribution's range,
#which is 0 - 10 (0 is the minimum value in the distribution, and 10 is the maximum value)

#Also, each value is fairly close to the mean. The nearest value to the mean is 4,
#which is just 1 unit away from the mean, while the farthest values are 0 and 10,
#located 5 units away from the mean.

#Although the distance for each individual value varies,
#the sum of the distances of the values that are below the mean is equal to the sum
#of the distances of the values that are above the mean:

#TASKS

distribution = [0,2,3,3,3,4,13]

#We assigned a few values to the distribution variable in the code editor.

#Compute the mean of this distribution and assign the result to a variable named mean.
mean = stat.mean(distribution)
print(mean)
#Find out whether the value of the mean is at the center of the distribution's range (0 - 13).
#If it is, assign True to a variable named center, otherwise assign False.
center = (mean == 6.5)
print(center)
#Check whether the sum of the distances of the values that are below the mean is
#equal to the sum of the distances of the values that are above the mean.

#Measure the distance of each value from the mean.
#You can ignore potential values that are equal to the mean because the distances will be 0 for these cases.

#Sum up the distances of the values that are above the mean,
#and then sum up separately the distances of the values that are below the mean.

#Compare the results of the two sums — if they are equal,
#assign True to a variable named equal_distances, otherwise assign False.
above_mean = []
below_mean = []
for num in distribution:
    if num < mean:
        below_mean.append((mean - num))
    elif num > mean:
        above_mean.append((num - mean))
    else:
        pass

sum_above = sum(above_mean)
sum_below = sum(below_mean)
print(sum_above)
print(sum_below)
equal_distances = (sum_above == sum_below)
print(equal_distances)

#3. THE MEAN AS A BALANCE POINT

#In the last exercise, we observed from the distribution [0,2,3,3,3,4,13] that
#the mean 4 is not in the center of the 0 - 13 range interval

#As a consequence, we should avoid thinking of the mean as being the center of a distribution's range.
#In some cases, the mean will be equivalent to the center of the distribution's range,
#but we've just seen that this doesn't hold true for all distributions.

#We should think of the mean as being the value located at that particular point
#in the distribution where the total distance of the values below the mean is the
#same as the total distance of the values that are above the mean.
#In our last exercise, we saw that this holds true for the distribution [0,2,3,3,3,4,13].

#In fact, this is true for the distribution of any variable measured on an interval or ratio scale.

#To give students a better intuition for this property of the mean, it's common in the
#literature to describe the mean as the balance point of a lever.

#If the total distances above and below the mean were equivalent to the forces exerted
#by the weights on the rod of the lever, then there would be the same amount of force
#exerted on each side of the mean. This will make the rod stay in perfect equilibrium

#Now that we've seen that the total distances below the mean equal the total
#distances above the mean, we'll do a sanity check of this rule by measuring
#the distances for 5000 different distributions in the exercise below.

#Generate 5000 different distributions, measure the total distances above and below the mean,
#and check whether they are equal. For each of the 5000 iterations of a for loop:

#Set a seed using the seed() function from numpy.random.
#For the first iteration, the seed number should be 0, for the second iteration it should be 1,
#for the third it should be 2, and so on.

#Generate randomly a distribution of integers using the randint() function from
#numpy.random. Pass the right arguments to randint() such that each distribution will:
#Have 10 values.
#The values can range from 0 to 1000.

#Compute the mean of the distribution.

#Measure the total distance above and below the mean.
#Round off each distance to 1 decimal place using the round() function.
#This will prevent rounding errors at the 13th or 14th decimal place.

#Compare the two sums.
#If they are equal, then increment a variable named equal_distances with 1.
#You'll need to define equal_distances outside the loop with a value of 0.

#At the end equal_distances should have a value of 5000.
#This will confirm that for each of the 5000 distributions the total distance
#of the values above the mean is equal to the total distance of the values below the mean.

equal_distances = 0

for i in range(5000):
    seed(i)
    distribution = randint(0, 1000, 10)
    distribution_mean = sum(distribution) / len(distribution)

    above_mean = []
    below_mean = []
    for num in distribution:
        if num == distribution_mean:
            continue
        if num < distribution_mean:
            below_mean.append((distribution_mean - num))
        if num > distribution_mean:
            above_mean.append((num - distribution_mean))

    sum_above = round(sum(above_mean),1)
    sum_below = round(sum(below_mean),1)
    if (sum_above == sum_below):
        equal_distances += 1

print(equal_distances)

#4. DEFINING THE MEAN ALGEBRAICALLY

#A very useful property of the mean is that it can be defined algebraically in a simple way.
#This is how we can define the mean for any population of N values
#(N is the number of values in the population):

#population mean = x1 + x2 ... + xN / N

#By convention, the mean of a population is denoted with the Greek letter mew (pronounced "mew").
#So we rewrite the formula above:

#mew = x1 + x2 ... + xN / N

#Let's say the distribution [0,2,3,3,3,4,13] represents a population.
#The distribution has 7 values, so N = 7. Let's plug the values into the formula above:

#Above, we computed the mean for a population.
#When we compute the mean for a sample, we need to use a slightly different notation to
#indicate that we're computing the mean for a sample and not for a population.
#Instead of mew, we denote the sample mean using x-bar (pronounced "x-bar"),
#and we use n instead of N to denote the number of values in the sample.
#This is how we could define the sample mean algebraically:

#x-bar = x1 + x2 ... xn / n

#Let's say we sample three values from the distribution used above and end up with
#the sample [2,3,4]. Let's plug the values into the sample mean formula:

#x-bar = 2 + 3 + 4 / 3 = 9/3 = 3

#Alternative notation exists for the sample mean.
#Besides x-bar, the sample mean is denoted in other statistics resources with M, X-bar
#(uppercase X-bar), or x-bar(n).
#Throughout our statistics courses, we use the symbol x-bar to refer to the sample mean.

#Tasks
#Indicate whether the following sentences are true or false.
#We use the symbol mew to denote both the population and the sample mean. Assign True or False to a variable named one.

#If a population has 8 values, then n = 8. Assign True or False to a variable named two.

#x-bar is a symbol used as an alternative to M, X-bar or x-bar(n) to denote the population mean.
#Assign True or False to a variable named three.

one = False
two = False
three = False

#5. AN ALTERNATIVE DEFINITION
#X = [x1, x2, x3]

#You should think of SIGMA(N) i = 1 in terms of a for loop, where the iteration variable is i. This means:
#that i will take a different value for each iteration. i = 1 defines the starting
#value of the loop, which is 1. For every new iteration, the previous value of i is incremented by 1.
#The iteration stops when i = N. For our distribution X above, N =3, so we'll have three iterations of the loop:

#For the first iteration, i = 1. The i in xi will become 1, so we'll have x1.
#For the second iteration, i = 2. The i in xi will become 2, so we'll have x2.
#For the third iteration, i = 3. The i in xi will become 3, so we'll have x3.
#At this point the iterations stops because i = N

#This is one way we could code in Python a similar logic:

#distribution = [x_1, x_2, x_3]

#i = 1
#N = 3
#sum_of_the_distribution = 0

#for _ in range(N):
    #sum_of_the_distribution += distribution[i - 1] We subtract 1 because Python lists use zero-based indexing
    #i += 1

#While this is merely notation, it's important to understand it because we'll use
#it repeatedly as we move forward,
#and it'll also help you understand other statistics resources. T
#o sum up, these are the ways we can define the population mean algebraically

#For the sample mean, there's just a slight change in notation. mew becomes x-bar, and N becomes n:

#TASKS
#Write a function that behaves just like SUM(N) i=1 xi / N
#The function takes in an array of numbers and returns its mean value.
#Inside the function, write a for loop to iterate over the values in the array and sum them up.
#We can use sum() to compute the sum of an array without using a for loop, but for learning
#purposes we advise you to use a for loop just to understand better how SUM(N) i=1 xi / N works.

def GetPopMean(array):
    summed_array = 0
    for num in array:
        summed_array += num
    PopMean = summed_array / len(array)
    return PopMean

#Use the function you wrote to compute the mean of the three distributions we already
#defined in the code editor:

#For the distribution in distribution_1 assing the mean to a variable named mean_1.
#For the distribution in distribution_2 assign the mean to a variable named mean_2.
#For the distribution in distribution_3 assign the mean to a variable named mean_3.

distribution_1 = [42, 24, 32, 11]
distribution_2 = [102, 32, 74, 15, 38, 45, 22]
distribution_3 = [3, 12, 7, 2, 15, 1, 21]

mean_1 = GetPopMean(distribution_1)
print(mean_1)
mean_2 = GetPopMean(distribution_2)
print(mean_2)
mean_3 = GetPopMean(distribution_3)
print(mean_3)

#6. INTRODUCING THE DATA
#So far we've discussed a few theoretical aspects about the mean and
#used a few simple distributions (like [2,4,6])
#to make the explanations easier to grasp. At this point,
#we introduce a real-world data set to discuss the mean in the context of large
#and real-world distributions.

#We'll be working with a data set that describes characteristics of houses sold
#between 2006 and 2010 in the city of Ames (located in the American state of Iowa).
#There are 2930 rows in the data set, and each row describes a house.
#For each house there are 82 characteristics described, which means there are 82 columns in the data set.

#TASKS

#The data set is stored in a file named AmesHousing_1.txt. Read the file as a pandas DataFrame, and store it in a variable named houses.

#The values in each row are tab-separated, which means AmesHousing_1.txt is a TSV (tab-separated value) file.
#This is different from a CSV (comma-separated values) file, where the values are separated by commas, not by tab a tab character.
#Use the pd.read_table() function or pd.read_csv(sep = '\t') to read in the data set.

houses = pd.read_csv('AmesHousing_1.txt', sep = '\t')

#With the help of the documentation and by exploring the data set yourself,
#assess the truth value of the following sentences:

#This data set has variables measured on every scale of measurement:
#nominal, ordinal, interval and ratio.
#(If you think this is true, assign the boolean True to the variable one, otherwise assign False.)

print(houses.info())
one = True
#The SalePrice column is continuous and measured on an interval scale.
#(If you think this is true, assign the boolean True to the variable two, otherwise assign False.)

print(houses['SalePrice'].head())
two = False

#In the paper he published here, professor Dean DeCock wrote
#"The initial Excel file contained 113 variables describing 3970 property sales
#that had occurred in Ames, Iowa between 2006 an 2010".
#If we wanted to measure the mean sale prices for all the houses sold between 2006 and 2010
#in Ames, Iowa, the data stored in the AmesHousing_1.txt would be a sample.
#(If you think the last sentence is true, assign the boolean True to the variable three, otherwise assign False.)

three = True

#7. MEAN HOUSE PRICES
#Let's say we're interested to analyze the distribution of the sale prices of the houses.
#We can get a good overview about this distribution using the Series.describe() method:

print(houses['SalePrice'].describe())

#We an see that the distribution has a large range: the minimum sale price is $12789 while the maximum is $755000.
#Among this diversity of prices, we can see that the mean (or the "balance point") of this distribution is approximately $180796.
#The mean gives us a sense about the typical sale price in this distribution of 2930 prices.

#If we want to compute only the mean, it's more convenient to use the Series.mean() method:
print(houses['SalePrice'].mean())


#TASKS
#Use the function you wrote in step 5 to compute the mean of the SalePrice distribution.
#Assign the result to a variable named function_mean.

function_mean = GetPopMean(houses['SalePrice'])
print(function_mean)
#Use Series.mean() to compute the mean of the SalePrice distribution.
#Assign the result to a variable named pandas_mean.
pandas_mean = houses['SalePrice'].mean()

means_are_equal = (function_mean == pandas_mean)
print(means_are_equal)

#ESTIMATING THE POPULATION MEAN
#In practice, we almost always work with samples. But most of the times we're not
#interested in answering questions about samples -- we want to answer questions about populations.

#A lot of the questions we want to answer in practice can be reduced to finding the mean of a population:

#What is the mean amount of money our customers spent last year on our website?

#What is the mean amount of time customers spent daily the first week after the promotion we ran?
#How does that compare to the mean amount of time spent daily in the week before the promotion?

#What is the mean sale price of a house in Ames, Iowa for the period 2006-2010?

#When we only have a sample but want to find the mean in the population,
#the best we can do is to compute the sample mean x-bar and hope it's a good estimate for the population mean mew.
#When estimating the population mean mew using the sample mean x-bar, there are three possible scenarios:

#The sample mean x-bar overestimates the population mean mew. This means that x-bar > mew.
#The sample mean x-bar underestimates the population mean mew. This means that x-bar < mew.
#The sample mean x-bar is equal to the population mean mew. This means that x-bar = mew.

#When x-bar > mew and x-bar < mew, sampling errors occur.
#Remember that sampling error is given by the difference between a population's parameter and a sample's statistic.
#Mew is a parameter, and x-bar is a statistic, so the sampling error is given by

#sampling error = mew = x-bar

#Our aim is to reduce the sampling error.
#Two important factors that influence the sampling error are:

#Sample representativity — the more representative a sample is, the closer x-bar will be to mew.
#Sample size — the larger the sample, the more chances we have to get a representative sample. By consequence, this means less sampling error.

#This emphasizes once more the importance of the sampling process,
#where we should try our best to get a representative sample.

#In the exercise below, we'll try to visualize on a scatter plot how the sampling error
#changes as we increase the sample size. Just to prove a point, we'll assume that our
#data set describes all the houses sold in Ames, Iowa between 2006 and 2010.

#TASKS

#Compute the mean of the SalePrice variable.
#We'll assume that the data we have is a population relative to the question
#"What's the mean sale price of a house in Ames, Iowa for the period 2006-2010?"

#For each iteration of a for loop that iterates 101 times:

#Sample the SalePrice distribution using the Series.sample() method.

#For the first iteration, the random_state parameter is 0, for the second iteration is 1, for the third is 2, and so on.

#For the first iteration, the sample size is 5.

#The last sample size is 2905 (which is close to 2930, the population's size).

#To achieve that, you'll need to increment the sample size by 29 for every new iteration.
#Note that you'll first have to define the sample size with a value of 5 outside the loop.

#Compute the sample mean.
#Compute the sampling error. For answer checking purposes, use parameter - statistic, not statistic - parameter.
sample_size = 5
sample_sizes = []
sampling_errors = []
for i in range(101):
    sample = houses['SalePrice'].sample(sample_size, random_state = i)
    sample_mean = sample.mean()
    sampling_error = pandas_mean - sample_mean #(parameter defined above - statistic)
    sampling_errors.append(sampling_error)
    sample_sizes.append(sample_size)
    sample_size += 29

plt.scatter(sample_sizes, sampling_errors)
plt.axhline(0)
plt.axvline(2930)
plt.xlabel("Sample size")
plt.ylabel("Sampling error")
#plt.savefig("Sampling size v Sampling error.png")
plt.close()
#ESTIMATES FROM LOW-SIZED SAMPLES
#We've seen in the previous exercise that the general tendency for the sampling error
#is to decrease as the sample size increases. This tendency, however, has exceptions.
#For instance, there are cases where small sample sizes (100-500 sample points)
#gave us better estimates for the population mean mew than large sample sizes (2500 sample points or more) did.

#For any given sample size, we can have many combinations of values.
#For instance, for a sample size of 3, we can have many possible combinations of sale prices:
#[220000, 143000, 281000], [123600, 209500, 202665], [287000, 142500, 440000], etc.
#Most of the samples of size 3 will give a good estimate of the population mean mew.
#To prove this point, in the code below we will:

#Measure the mean for 10000 samples of size 3.
#Use a histogram to visualize the distribution of the sample means.
#Draw a vertical line corresponding to the population mean.


means = []
for i in range(10000):
    sample = houses['SalePrice'].sample(3, random_state = i)
    means.append(sample.mean())

plt.hist(means)
plt.axvline(houses['SalePrice'].mean())
#plt.savefig("Histogram_of_10000_samples_size_3.png")
plt.close()
#We can see that most sample means cluster around the population mean.
#This means that when we take a sample of size 3 and compute x-bar,
#we have fairly good chances to get a good estimate for the population mean mew.
#This explains what we've seen in the scatter plot above, where we got good estimates from low-sized samples.

#It's also worth noting that the mean of the 10000 sample means we measured is very close to the population mean mew:

print(sum(means) / len(means))
print(houses['SalePrice'].mean())

#TASKS
#Take 10000 samples of sample size 100 from the population of sale prices and
#measure the mean of each sample. For each of the 10000 iterations of a for loop:

#Use Series.sample() to take a sample of size 100 from the SalePrice variable.
#The random_state parameter is 0 for the first iteration, 1 for the second iteration,
#2 for the third iteration, and so on.

#Compute the mean of the sample.
SampleMeans = []
for i in range(10000):
    sample = houses['SalePrice'].sample(100, random_state = i)
    sample_mean = sample.mean()
    SampleMeans.append(sample_mean)

#Use plt.hist() to generate a histogram to visualize the distribution of sample means.

#Draw a vertical line for the population mean.
#Label the x-axis "Sample mean".
#Label the y-axis "Frequency".
#Set the range of the x-axis to (0,500000).
#This is the same range as the histogram we built above has.
#Can you observe any obvious difference between the two histograms now that we've increased the sample size?

plt.hist(SampleMeans)
plt.xlim(0,500000)
plt.axvline(houses['SalePrice'].mean())
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
#plt.savefig("Histogram_of_10000_samples_size_100.png")
plt.close()

#10. VARIABILITY AROUND THE POPULATION MEAN
#In the previous exercise, we observed that with a sample size of 100 the sample
#means vary much less around the population mean than in the case of a sample size of 3.

#Generally, as we increase the sample size, there will be less and less variability around the population mean.
#If there's less variability, there are less chances to get a poor estimate for the population mean —
#the worst sample means we can get are fairly close to the population mean, which is good.

#11. THE SAMPLE MEAN AS AN UNBIASED ESTIMATOR
#If we took all the possible samples for a given sample size,
#we'd observe that the mean of the sample means will be equal to the population mean.
#Consider this small population of values:

#X = [0, 3, 6]

#The mean mew of this population is 0+3+6/3 = 3 . Now let's take every possible sample of size 2, and compute the mean for each sample:

#Sample             Mean
#[0, 3]             1.5
#[0, 6]             3
#[3, 0]             1.5
#[3, 6]             4.5
#[6, 0]             3
#[6, 3]             4.5

#Now let's find the mean of the sample means.
#We add up the means we got for each of the six samples above and divide by the number of samples:

#1.5 + 3 + 1.5 + 4.5 + 3 + 4.5 / 6 = 18 / 6 = 3

#The value we got is the same as the population mean mew.
#So on average the sample mean is equal to the population mean. T
#This is true for the distribution above and for any other distribution of real numbers.

#When a statistic is on average equal to the parameter it estimates,
#we call that statistic an unbiased estimator. In our case, the sample mean x-bar
#is an unbiased estimator for the population mean mew.

#This also holds true if we sample with replacement.
#When we do sampling with replacement, we sample one value, and then we put it back in the population,
#which means we can sample that value again. For instance, if we want a sample of size 2 from the population above,
#and we sample with replacement, this could happen:


#We extract one value randomly and get a 3.
#Because we sample with replacement, we put the value back in the population.
#We extract one more value and get a 3 again. We end up with this sample: [3, 3].

#Below we can see the samples of size 2 we can get when we sample with replacement
#from the population above. We also show the mean for each sample:

#Sample             Mean
#[0, 3]             1.5
#[0, 0]             0
#[3, 0]             1.5
#[3, 6]             4.5
#[3, 3]             3
#[6, 0]             3
#[6, 3]             4.5
#[6, 6]             6

#The mean of the sample means amounts to 3 again, and confirms that x-bar is an
#unbiased estimator for the population mean mew when we sample with replacement:

#1.5 + 3 + 0 + 1.5 + 4.5 + 3 + 3 + 4.5 + 6 / 9 = 27/9 = 3

#TASKS
#Check whether the population mean of the population [3, 7, 2] is equal to the
#mean of all the sample means of size 2 that we can get if we do sampling without replacement.

#Compute the mean for each sample.
#Compute the mean of all the sample means.
#Compare it with the population mean using the == operator,
#and assign the result of the comparison to a variable named unbiased.
population = [3, 7, 2]
samples_list = [[3, 7], [3, 2], [7, 3], [7, 2], [2, 3], [2, 7]]
ListOfMeans = []
for sample in samples_list:
    ListOfMeans.append(sum(sample) / len(sample))

MeanOfSampleMeans = sum(ListOfMeans) / len(ListOfMeans)

unbiased = (MeanOfSampleMeans == (sum(population) / len(population)))
print(unbiased)

#12. Next Steps
#In this mission, we explored in more depth the mean:

#We saw that the mean can be intuitively understood as the "balance point" of a distribution.

#We learned to distinguish conceptually between the sample and the population mean,
#and we saw that we use different notation for each case.

#We demonstrated with a few examples that the sample mean x-bar is an unbiased estimator for the population mean mew.

#In the next mission, we'll explore a few edge cases where it's either impossible to compute the mean,
#or it's possible but not theoretically sound.