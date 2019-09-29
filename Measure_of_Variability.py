import pandas as pd
import statistics as stat
from math import sqrt
import matplotlib.pyplot as plt
from numpy import std, var
houses = pd.read_csv('AmesHousing_1.txt', sep = '\t', index_col='Order')
#1. THE RANGE
#So far we've focused entirely on summarizing distributions using the mean,
#the weighted mean, the median, and the mode. An interesting distribution property
#we haven't yet discussed is variability.

#Consider, for instance, these two distributions of numerical values:
#A = [4, 4, 4, 4]
#B = [0, 8, 0, 8]

#The values of the distribution A don't vary -- each value is 4. The values in
#distribution B show some variability -- they are not all identical,
#and the values can either by 8 or 0.  If we were to quantify variability,
#we could assign a value of 0 to A to indicate that it has no variability.
#But what variability value should we assign to distribution B?

#We need a measure to summarize the variability of these two distributions.
#The summary metrics we've learned so far don't tell us anything about variability.
#The mean, the median, and the mode of distribution A are all 4, and
#distribution B has a mean and a median of 4, and no mode.
#If we were to judge variability based on these values,
#we'd probably have to conclude that the variabilities of the two distributions are equal, which is wrong.

#One intuitive way to measure the variability of a distribution is to find the
#difference between the maximum and the minimum value. Both the maximum and the
#minimum of distribution A is 4, so the variability of distribution A is 0:

#max(A) - min(A) = 4 - 4 = 0

#We call this measure of variability the range. So the range of distribution A
#is 0. The range of distribution B is 8:

#max(B) - min(B) = 8 - 0 = 8

#In more general terms, the range of distribution X, where X can be any distribtion
#of real numbers, is:

#range(x) = max(x) - min(x)

#We'll continue in the mission with the data set on house prices we used for the
#last three missions. Here's a short extract from the data set to help you recollect its structure:

print(houses.head())

#TASKS
#Write a function that takes in an array of numerical values and returns the range of that array.

def GetRange(array):
    return (max(array) - min(array))

#Using the function you wrote, measure the range of the SalePrice variable for each year of sales.
#You can find the year of sale in the Yr Sold column.

#Store the measures in a dictionary named range_by_year.
#The keys should be the individual years, and the dictionary values should be the ranges.
#This is how the dictionary should look like: {2010: 598868, 2009: 575100, 2008: 601900,...}.

range_by_year = {}
for year in houses['Yr Sold'].unique():
    data_by_year = houses[houses['Yr Sold'] == year]
    range_by_year[year] = GetRange(data_by_year['SalePrice'])

print(range_by_year)

#Using the measures of variability you got, asses the truth value of the following sentences:
#1. Prices had the greatest variability in 2008.
#If you consider this sentence true, assign the boolean True to a variable named one, otherwise assign False.
one = False
#Prices variability had a peak in 2007, then the variability started to decrease until 2010
#when there was a short increase in variability compared to the previous year (2009).
#If you consider this sentence true, assign the boolean True to a variable named two, otherwise assign False.
two = True

#2. THE AVERAGE DISTANCE
#The problem with the range is that it considers only two values in the distribution —
#the minimum and the maximum value. Consider this distribution C:

#C = [1, 1, 1, 1, 1, 1, 1, 1, 1, 21]

#We can see there's not much variability in distribution C - we have nine values of 1,
#and a single value of 21. Intuitively, we'd expect the variability of distribution C
#to be greater than 0 because there is some variability after all, but not much greater than 0
#(remember from the last screen that a distribution whose values don't vary should ideally have a variability of 0).

#Despite our expectations, the range indicates that the variability of distribution C is 20.
#max(C) - min(C) = 21 - 1 = 20

#This is signficantly greater than 0 and doesn't seem like a reasonable measure of variability for distribution C.
#The root of the problem is that the range considers only the two extreme values,
#and this makes it extremely sensitive to outliers. To get a more balanced measure of variability for distribution C,
#we need to take into account each value in the distribution.

#To take into account each value when measuring variability we could:

#1. Take a reference value, and measure the distance of each value in the distribution
#from that reference value.

#We can take the mean of the distribution as a reference value.
#Then, we measure the distance between each value in the distribution and the mean.


#2. Find the mean of the distances.
#We first need to sum up all the distances.
#Then we need to divide the total by the number of distances.


#By measuring the distance of each value relative to a reference point and
#then taking the mean of the distances, we practically measure how much the
#values of a distribution vary on average with respect to that reference point.

#It's also very easy to define algebraically this method for any population of values
#[x1, x2, ..., xN] with mean mew:

#average distance = distanceof(x1 - mew) + (x2 - mew) + ... + (xN - mew) / N

#We'll continue discussing about this method in the next screen, but now let's use the
#formula above to measure the variability of distribution C:

#TASKS
C = [1,1,1,1,1,1,1,1,1,21]
#Write a function that takes in a numerical array and returns the average distance
#(as explained above). Inside the function's defition:

#Compute the mean of the array.
#Initialize an empty list.
#Loop through the values of the array. For each iteration:
#Compute the distance between the current value and the mean. Use value - mean every time, as indicated by the formula.
#Append the distance to the list we initialized before the loop.
#At the end of the loop, the list should contain all the distances.
#Return the mean of the list.

def GetAvgDist(array):
    MeanArray = (sum(array) / len(array))
    DistList = []
    for num in array:
        Dist = (num - MeanArray)
        DistList.append(Dist)
    return (sum(DistList) / len(DistList))

#Compute the average distance for distribution C using the function you wrote,
#and assign the result to a variable named avg_distance.

avg_distance = GetAvgDist(C)
print(avg_distance)

#3. MEAN ABSOLUTE DEVIATION
#In the last exercise the average distance was 0.
#This is because the mean is the balance point of the distribution and,
#as we've learned, the total distance of the values that are above the mean is
#the same as the total distance of the values below the mean. The mean mew of the
#distribution C is 3, so we have:

'''
        Values that are                         Value that are
        below the mean                          above the mean
        --------------                          ---------------
    Xi - mew      Distance                      Xi - mew      Distance
    1 - 3            -2                         21 - 3          18
    1 - 3            -2                                     --------
    1 - 3            -2                                     Total = 18
    1 - 3            -2
    1 - 3            -2
    1 - 3            -2
    1 - 3            -2
    1 - 3            -2
    1 - 3            -2
                   ------
                   Total = -18
                   '''

#Plugging the distances into the formula we used in the previous screen will
#make the numerator amount to 0, which in turn will make the average distance 0:

#average distance = -18 + 18 / 10 = 0 / 10 = 0

#To solve this problem, we can take the absolute value of each distance, and then sum up the absolute values.
#The absolute value (also called modulus) of a number is the positive version of that number,
#regardless of its sign. For instance, the absolute value of -7 is +7,
#and the absolute value of +7 is +7. In mathematical notation we write:

#|-7| = +7
#|+7| = +7

#We'll update the formula used previously to reflect the fact the we're summing up the absolute distances instead:

#mean absolute distance = |x1 - mew| + |x2 - mew| + ... + |xN - mew| / N

#We call this measure of variability mean absolute distance.
#In statistical jargon, however, the distance of a value from the mean is called deviation.
#So the mean absolute distance is more commonly known as mean absolute deviation or average absolute deviation.

#Let's take the mean absolute deviation of distribution C and see whether this metric does better than the range.
#Remember that the range is 20, but we expect a smaller value (which is greater than 0 at the same time).

#TASKS
#Write a function that takes in a numerical array and returns the mean absolute deviation. Inside the function:

#Compute the mean of the array.
#Loop through the values of the array. For each iteration:
#Compute the absolute distance (deviation). You can use the abs() function.
#Append the absolute distance to a list.
#Return the mean of the list containing all the absolute distances.

#Compute the mean absolute deviation of distribution , and assign the result to a variable named mad.

#Is the result considerably less than 20 but greater than 0, as we expected?


def GetAbsDev(array):
    MeanArray = (sum(array) / len(array))
    AbsDistList = []
    for num in array:
        AbsDist = abs(num - MeanArray)
        AbsDistList.append(AbsDist)
    return (sum(AbsDistList) / len(AbsDistList))

print(GetAbsDev(C))


#In the previous screen we transformed the distances to absolute values to avoid
#having the sum of distances amount to 0 in the numerator. Another way to solve
#this problem is to square each distance and then find the mean of all the squared distances:

#mean squared distance = (x1 - mew)^2 + (x2 - mew) + ... +(xN - mew)^2 / N

#This measure of variability is sometimes called mean squared distance or
#mean squared deviation (remember that "distance" and "deviation" are
#synonymous in this context). However, it's more commonly known as variance.


#Squaring the distances or taking their absolute values ensure that we get a
#variability value that is greater than 0 for all distributions that show some
#variability. Notice, however, that variance and mean absolute deviation will
#still be 0 for distributions that show no variability.

#Consider distribution D = [2, 2, 2], which has a variance and a mean absolute deviation of 0:

#variance = (2 - 2)^2 + (2 - 2)^2 + (2 - 2)^2 / 3 = 0^2 + 0^2 + 0^2 / 3 = 0

#mean absolute deviation = |2 - 2| + |2 + 2| + |2 + 2| / 3 = 0 + 0 + 0 /3 = 0

#In the previous exercise, we got a mean absolute deviation of 3.6 for our distribution
#C = [1,1,1,1,1,1,1,1,1,21]. A value of 3.6 fitted well our expectations because
#we had expected a variability value greater than 0, but signficantly less than 20.
#Let's see how well variance does with measuring the variability of distribution C.

#TASKS
#Write a function that takes in a numerical array and returns the variance of that array. Inside the function:
#Compute the mean of the array.
#Loop through the values of the array. For each iteration:
#Compute the squared distance (squared deviation).
#Append the squared distance to a list.
#Return the mean of the list of squared distances.

#Compute the variance of distribution C, and assign the result to a variable named variance_C.
#Is the result considerably less than 20 but greater than 0, as we expected?

def GetVariance(array):
    MeanArray = (sum(array) / len(array))
    SqrDistList = []
    for num in array:
        SqrDist = ((num - MeanArray) ** 2)
        SqrDistList.append(SqrDist)
    return (sum(SqrDistList) / len(SqrDistList))

variance_C = GetVariance(C)
print(variance_C)

#5. STANDARD DEVIATION
#In the previous exercise, we got a variance of 36 for distribution C = [1,1,1,1,1,1,1,1,1,21],
#which was much more than we had expected. This high variability value is the direct result of
#the squaring process, which makes most distances much bigger than they actually are.

#Squaring the distances also has the drawback of squaring the units of measurement.
#Let's consider this small sample from the Bedroom AbvGr variable
#(which describes the number of bedrooms in a house):

#[0,7,8]

#For computational purposes, and sometimes for simplicity,
#we tend to leave out the units of measurement in practice,
#but theoretically we should write out the units of measurement:
#[0 bedrooms, 7 bedrooms, 8 bedrooms]

#The units of measurement are subject to algebraic operations,
#so the variance of the sample above will be
#(for formatting purposes, we'll abbreviate "bedrooms" with "b"):

#variance = (0b - 5b)^2 + (7b - 5b)^2 + (8b -5b)^2 / 3
#variance = 25b^2 + 4b^2 + 9b^2 / 3 = 38b^2 / 3 = 12.6b^2

#The variance of this distribution is 12.6(rep) bedrooms^2,
#which is very counterintuitive (12.6(rep) is the abbrevation for 12.666...666.. —.  infinitely repeating).
#To solve this problem and also reduce the variability value, we can take the square root of variance.

#sqrt(variance) = sqrt(12.6(rep)^2) = 3.6 bedrooms

#The square root of variance is called the standard deviation (remember that "deviation"
#is synonymous with "distance")

#Notice that the standard deviation is simply the square root of variance:

#standard deviation = sqrt(variance)

#Let's return to our distribution C = [1,1,1,1,1,1,1,1,1,21],
#and see how well standard deviation does on measuring its variability.

#TASKS
#Write a function that takes in a numerical array and returns the standard deviation
#of that array. Inside the function:

#Compute the mean of the array.
#Loop through the values of the array. For each iteration:
#Compute the squared distance (squared deviation).
#Append the squared distance to a list.
#Compute the mean of the list of squared distances — this is the variance.
#Return the square root of the variance.


def GetStdDev(array):
    MeanArray = stat.mean(array)
    SqrDistList = []
    for num in array:
        SqrDist = ((num - MeanArray) ** 2)
        SqrDistList.append(SqrDist)
    variance = stat.mean(SqrDistList)
    return (sqrt(variance))

standard_deviation_C = GetStdDev(C)
print(standard_deviation_C)

#6. AVERAGE VARIABILITY AROUND THE MEAN
#In practice, standard deviation is perhaps the most used measure of variability.
#Let's try to get a better understanding of it by measuring the variability of the
#SalePrice variable in our data set. We'll use the GetStdDev() function
#we wrote for the previous exercise:

print(GetStdDev(houses['SalePrice']))

#Standard deviation tells us how much the values in a distribution vary (on average)
#around the mean of that distribution. The mean of the SalePrice variable is approximately $180,796:

print(houses['SalePrice'].mean())
#The mean tells us that the average price of a house is roughly $180,796,
#but this doesn't mean that each house (or most of them) costs exactly $180,796.
#One house could cost $120,000, another $240,000, and it could be that no house
#actually costs exactly $180,796. The standard deviation gives us a picture about this
#variability around the mean sale price. So, on average, sale prices vary by roughly $79,873
#above and below a mean of $180,796.

#Below, we'll try to visualize this variability around the mean by:

#Generating a histogram for the distribution of the SalePrice variable.
#Using vertical lines to mark the mean and the average deviations above and below the mean.

mean = houses['SalePrice'].mean()
st_dev = GetStdDev(houses['SalePrice'])
houses['SalePrice'].plot.hist()
plt.axvline(mean, color = 'Black', label = 'Mean')
plt.axvline(mean - st_dev, color = 'Red', label = 'Below')
plt.axvline(mean + st_dev, color = 'Violet', label = 'Above')
#plt.savefig("Sales_Price_Histogram_with_Std_Devs.png")
plt.close()

#Notice in the histogram that prices can vary around the mean much more or much less than $79,873.
#Some outliers around $700,000 are more than $500,000 above the mean and a couple of houses around
#$30,000 are more than $150,000 below the mean. The standard deviation doesn't set boundaries for
#the values in a distribution: the prices can go above and below the mean more than $79,873.

#TASKS
#The standard deviation of the SalePrice variable should give us a picture about the diversity of prices on the real estate market.
#Find the year with the greatest variability of prices and assign the answer as an integer to the variable greatest_variability.
#Find the year with the lowest variability of prices and assign the answer as an integer to the variable lowest_variability.
#Use the function you wrote in the previous screen to measure the standard deviation of each year.
#You can find information about the years of sale in the Yr Sold column.
#There are many ways you can solve this exercise. If you get stuck, you can check the hint or the solution code.

var_by_year = {}
for year in houses['Yr Sold'].unique():
    data_by_year = houses[houses['Yr Sold'] == year]
    var_by_year[year] = GetStdDev(data_by_year['SalePrice'])

print(var_by_year)
greatest_variability = max(var_by_year, key = var_by_year.get)
lowest_variability = min(var_by_year, key = var_by_year.get)
print(greatest_variability)
print(lowest_variability)

#7. A MEASURE OF SPREAD
#Another way to understand standard deviation is as a measure of spread in a distribution —
#values in a distribution can be more or less spread. We took four random samples of 50 sample
#points each from the SalePrice distribution, and plotted their histograms to visualize the spread for each sample:

#According to our visual estimates, sample 2 has the biggest spread,
#while the other three samples have a similar spread,
#with sample 3 seemingly having the lowest spread.
#The standard deviations of these four distributions fit our visual estimates fairly well:

for i in range(1,5):
    sample = houses['SalePrice'].sample(50, random_state = i)
    # we used the same random states for the samples in the graph above
    st_dev = GetStdDev(sample)
    print('Sample ' + str(i) + ': ' + str(st_dev))

#TASKS
#We took two samples of 50 sample points each from the distribution of the Year Built variable.
#Examine the graph below, and estimate visually which sample has a bigger spread.

#Assign your answer to a variable named bigger_spread. If you think sample 1 has
#a bigger spread, assign the string 'sample 1' to bigger_spread, otherwise assign 'sample 2'.
bigger_spread = 'sample 2'
#Sanity check your visual estimate by computing and comparing the standard deviations of the two samples.

#You can see the two samples already saved in the code editor.

#Assign the standard deviation of sample 1 to a variable named st_dev1.
#Compute the standard deviation using the standard_deviation() function.

#Assign the standard deviation of sample 2 to a variable named st_dev2.
#Compute the standard deviation using the standard_deviation() function.
sample1 = houses['Year Built'].sample(50, random_state = 1)
sample2 = houses['Year Built'].sample(50, random_state = 2)

st_dev1 = GetStdDev(sample1)
print(st_dev1)
st_dev2 = GetStdDev(sample2)
print(st_dev2)

#8. THE SAMPLE STANDARD DEVIATION
#In practice, we generally work with samples,
#but most of the time we're not actually interested in describing the samples.
#Rather, we want to use the samples to make inferences about their corresponding populations.
#Let's find out whether the standard deviation of a sample is a good estimate for
#the standard deviation in the corresponding population.

#Notice in the Standard Deviation formula that we used the population mean mew,
#which means that if we wanted to compute the standard deviation of a sample, we'd have to know mew.
#In practice, mew is almost never known, and we can't find it from our sample either, but we can estimate mew using the sample mean xbar

#We update slightly the formula for the sample standard deviation by changing mew to xbar
#and N to n (remember that N describes the number of data points in a population,
#while n describes the number of data points in a sample):

#Now that we have a working formula, can we use it to reliably estimate the population standard deviation?
#One way we can check this is by sampling repeatedly a known population and
#see how the sample standard deviations compare on average to the population standard deviation.

#TASKS
#Let's consider the data we have for SalePrice a population and sample it 5000 times.
#For each of the 5000 iterations of a for loop:

#Sample 10 data points from the SalePrice variable using the Series.sample() method.
#The random_state of Series.sample() should be 0 for the first iteration,
#1 for the second iteration, 2 for the third, and so on.
#Compute the standard deviation of the sample using the standard_deviation() function.
#Append the standard deviation to a list that will eventually store all the 5000 sample standard deviations.

#Generate a histogram using plt.hist() to visualize the distribution of the 5000 sample standard deviations.

#Draw a vertical line using plt.axvline() to mark the population standard deviation.
#Examine the histogram and try to figure out whether most sample standard deviations cluster above
#or below the population standard deviation, or right at the center of it.
SampleStdDevs = []
for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state = i)
    StdDev = GetStdDev(sample)
    SampleStdDevs.append(StdDev)

plt.hist(SampleStdDevs)
plt.axvline(GetStdDev(houses['SalePrice']))
#plt.savefig('Distribution_Sample_Stdevs_SalePrice.png')
plt.close()

#9. BESSEL'S CORRECTION
#In the last exercise, we plotted the histogram of 5000 sample standard deviations and
#compared them against the population standard deviation.
#Notice that most sample standard deviations are clustered below the population standard deviation:

#This suggests that the sample standard deviation usually underestimates the population standard deviation.
#We can also see that the mean of the 5000 sample standard deviations is below the population standard deviation:

print(stat.mean(SampleStdDevs)) #SampleStdDevs - a list with all the 5000 st. deviations
print(GetStdDev(houses['SalePrice']))

#So we can say that the sample standard deviation underestimates on average the population standard deviation.
#Some sample standard deviations are lower than the population standard deviation,
#some are greater, some may even be equal to the population standard deviation,
#but on average the sample standard deviation is lower than the population standard deviation.

#We can get a good intuition for why the sample standard deviation underestimates if we think in terms of distribution spread.
#When we sample a population, it's generally more likely to get a sample with a spread that's lower than the population's spread.
#This generally translates to a lower standard deviation than in the population.

#Getting a sample with a higher standard deviation than in the population is possible,
#but this is less likely. This is mostly specific to samples with a high spread and no clusters.

#To correct the underestimation problem, we can try to slightly modify the sample
#standard deviation formula to return higher values. One way to do that is to decrease the value of the denominator.
#For instance, 12/6 = 2 in, the denominator is 6. If we decrease the value of the denominator, we get a greater result: 12/4 = 3.

#We'll decrease by 1 the denominator in the sample standard deviation formula.

#This small correction we added to the sample standard deviation
#(dividing by n-1 instead of n) is called Bessel's correction.
#Let's implement Bessel's correction to our standard_deviation() function and repeat the
#steps in the last exercise to see if Bessel's correction adds any improvements.

#TASKS
#Modify the code we wrote in the previous exercise by implementing Bessel's correction, and generate the histogram again.
#If you want to challenge yourself, delete the display code and recode everything from scratch.
#Does it look like Bessel's correction added any improvement?

def standard_deviation(array):
    reference_point = sum(array) / len(array)

    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)

    variance = sum(distances) / (len(distances) - 1)

    return sqrt(variance)

st_devs = []

for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state = i)
    st_dev = standard_deviation(sample)
    st_devs.append(st_dev)

pop_stdev = standard_deviation(houses['SalePrice'])
plt.hist(st_devs)
plt.axvline(pop_stdev)
#plt.savefig('Sample_StdDevs_Bessel_Correction.png')
plt.close()

#10. STANDARD NOTATION
#It looks like Bessel's correction added some visible improvements and
#partially corrected the underestimation problem.

#The improvement brought by Bessel's correction is more obvious when we compare
#the average values of the two distributions above.
#The mean of the 5000 sample standard deviations without Bessel's correction is roughly 71304,
#while the mean standard deviation of the sample standard deviations having the correction is roughly 75161.
#This is significantly closer to the population standard deviation, which is approximately 79873.

#We could decrease the denominator more (dividing by n-2 maybe) to try improving the correction.
#However, we need a single mathematical definition for the sample standard deviation,
#and we have to choose between n, n-1, n-2, etc.
#Remember that in practice we don't know the population standard deviation,
#so we can't tell which correction would work best for each sample standard deviation.

#Statisticians agree that n-1 is the best choice for the sample standard deviation formula,
#and we'll explore a strong argument in support of this in the next screen.

#Now that we know what formulas to use for samples and populations,
#we introduce some standard notation that will help you understand other statistics resources.
#The population standard deviation is denoted with the Greek letter sigma

#Remember that the population standard deviation sigma is just the square root of the population variance.
#For this reason, the population variance is written as sigma^2
#(such that taking the square root of the variance sigma^2 results in the standard deviation sigma: sqrt(sigma^2)

#The sample standard deviation is simply denoted with s, while the sample variance is denoted with s^2
#(also notice Bessel's correction in the denominator):

#The main takeaway is that we need to use the s and s^2 formulae (with Bessel's correction) for samples.
#For populations, we can use the sigma or sigma^2 formulae (without Bessel's correction).

#TASKS
#We already sampled our data set and saved the sample in a variable named sample.
#Use the Series.std() method to compute the sample standard deviation for the SalePrice column.
#You can use the ddof parameter to choose between  and . Save the result to a variable named pandas_stdev.

#Use the numpy.std() function to compute the sample standard deviation for the SalePrice column.
#You can use the ddof parameter to choose between  and . Save the result to a variable named numpy_stdev.

#Compare pandas_stdev with numpy_stdev using the == operator.
#Assign the result of the comparison to a variable named equal_stdevs.

#Use the Series.var() method to compute the sample variance for the SalePrice column.
#Assign the result to pandas_var.

#Use the numpy.var() function to compute the sample variance for the SalePrice column.
#Assign the result to numpy_var.

#Compare pandas_var with numpy_var using the == operator.
#Assign the result of the comparison to a variable named equal_vars.

sample = houses.sample(100, random_state = 1)

pandas_stdev = sample['SalePrice'].std(ddof = 1)# default ddof = 1
numpy_stdev = std(sample['SalePrice'], ddof = 1)# default ddof = 0
equal_stdevs = (pandas_stdev == numpy_stdev)
pandas_var = sample['SalePrice'].var(ddof = 1)# default ddof = 1
numpy_var = var(sample['SalePrice'], ddof = 1)# default ddof = 0
equal_vars = (pandas_var == numpy_var)
print(equal_stdevs)
print(equal_vars)

#11. SAMPLE VARIANCE -- UNBIASED ESTIMATOR

#In the previous screen, we stated that statisticians agree that n - 1 is better
#than n or n-2 for computing the sample standard deviation s.
#An argument supporting this comes from the fact that the sample variance s^2
#(which uses n-1) is an unbiased estimator for the population variance sigma^2.
#Since standard deviation is just the square root of variance,
#it makes sense to use n-1 as well (although standard deviation is not an unbiased estimator, as we'll see).

#As we learned previously when we discussed the mean, we call a statistic an unbiased
#estimator when that statistic is equal on average to the parameter it estimates.
#Remember that the sample mean xbar is an unbiased estimator for the population mean mew
#no matter whether we sample with or without replacement. The sample variance s^2
#is an unbiased estimator for the population variance sigma^2 only when we sample
#with replacement. In the diagram below, we will:

#Take all possible samples of size n=2 from the population [0,3,6] with sigma=6.
#Compute the sample variance s^2 for each sample.
#Take the mean of all the sample variances s^2. You can see that the mean is 6,
#which is the same as the population variance sigma^2, which shows that the sample
#variance s^2 is an unbiased estimator for the population variance sigma^2.

'''
Sample          Sample variance (using n-1)
------          ---------------------------
[0, 3]                      4.5
[0, 6]                      18
[0, 0]                      0
[3, 0]                      4.5
[3, 6]                      4.5
[3, 3]                      0
[6, 0]                      18
[6, 3]                      4.5
[6, 6]                      0
                        --------
                        Mean sample
                        variance: 54/9 = 6
'''

#Although the sample variance s^2 is an unbiased estimator, and the sample
#standard deviation s is basically sqrt(s^2), the unbiasedness doesn't carry over
#(sigma is roughly 2.45 for the population [0, 3, 6]):

'''
Sample          Sample standard deviation (using n-1)
------          ---------------------------
[0, 3]                      2.12
[0, 6]                      4.24
[0, 0]                      0
[3, 0]                      2.12
[3, 6]                      2.12
[3, 3]                      0
[6, 0]                      4.24
[6, 3]                      2.12
[6, 6]                      0
                        --------
                        Mean sample
                        stddev: 1.89
'''

#In the exercise below, we'll see that the sample variance s^2 and the sample
#standard deviation s are biased when we sample without replacement.

#TASKS
#In the code editor, you can see all the possible samples of size n=2 for the population
#[0,3,6] when we sample without replacement.

population = [0, 3, 6]

samples = [[0,3], [0,6],
           [3,0], [3,6],
           [6,0], [6,3]]

#Compute the sample variance and sample standard deviation for each sample.
#Take the mean of all the sample variances.
#Compare the mean variance with the population variance
#(which you'll have to compute) using the == operator, and assign the result to a variable equal_var.

#If the sample variance is biased in this case, the result should be False.

#Take the mean of all the sample standard deviations.
#Compare the mean standard deviation with the population standard deviation using
#the == operator, and assign the result to equal_stdev.

#If the sample variance is biased in this case, the result should be False.
SampleStandardDeviations = []
SampleVariances = []

for sample in samples:
    StdDev = std(sample, ddof = 1)
    Variance = var(sample, ddof = 1)
    SampleStandardDeviations.append(StdDev)
    SampleVariances.append(Variance)

MeanSSD = stat.mean(SampleStandardDeviations)
MeanVar = stat.mean(SampleVariances)
Pop_Std = std(population)
Pop_Var = var(population)

equal_var = (MeanVar == Pop_Var)
equal_stdev = (MeanSSD == Pop_Std)
print(equal_var)
print(equal_stdev)


#In this mission, we learned how to measure the variability of a distribution using the range,
#the mean absolute deviation, the variance, and the standard deviation.
#These metrics are ideal for measuring the variability of distributions whose values are measured on an interval or ratio scale.

#Measuring variability for ordinal and nominal data is much harder because we can't
#quantify the differences between values. For this reason, little is written in the literature about measuring
#variability for ordinal and nominal data. If you want to dig more into this, you can start by reading this paper.

#Next in this course, we'll build on what we know about the mean and the standard deviation and learn about z-scores.
