import pandas as pd
from scipy.stats import percentileofscore
wnba = pd.read_csv('wnba.csv')
#1. SIMPLIFYING DATA
#Previously, we focused on the details around collecting data, on understanding
#its structure and how it's measured. Collecting data is just the starting point in a data analysis workflow.
#We rarely collect data just for the sake of collecting it.
#We collect data to analyze it, and we analyze it for different purposes:

    #To describe phenomena in the world (science)
    #To make better decisions (industries)
    #To improve systems (engineering)
    #To describe different aspects of our society (data journalism)

#Step 1: Collecting Data
#Step 2: Analyzing data
#Step 3: Making use of the analysis

#Our capacity to understand a data set just by looking at it in a table format is limited,
#and it decreases dramatically as the size of the data set increases.
#To be able to analyze data, we need to find ways to simplify it.

#The WNBA data set we've been working with has 143 rows and 32 columns.
#This might not seem like much compared to other data sets,
#but it's still extremely difficult to find any patterns just by eyeballing the data set in a table format.
#With 32 columns, even five rows would take us a couple of minutes to analyze:

print(wnba.head())

#One way to simplify this data set is to select a variable, count how many times each unique value occurs,
#and represent the frequencies (the number of times a unique value occurs) in a table.
#This is how such a table looks for the POS (player position) variable:

print(wnba['Pos'].value_counts())

#Because 60 of the players in our data set play as guards, the frequency for guards is 60.
#Because 33 of the players are forwards, the frequency for forwards is 33, and so on.

#With the table above, we simplified the POS variable by transforming it to a comprehensible format.
#Instead of having to deal with analyzing 143 values (the length of the POS variable),
#now we only have five values to analyze.
#We can make a few conclusions now that would have been difficult and time consuming to
#reach at just by looking at the list of 143 values:

#We can see how the frequencies are distributed:
    #Almost half of the players play as guards.
    #Most of the players are either guards, forwards or centers.
    #Very few players have combined positions (like guard/forward or forward/center).
#We can make comparisons with ease:
    #There are roughly two times more guards than forwards.
    #There are slightly less centers that forwards; etc.

#Because the table above shows how frequencies are distributed, it's often called
#a frequency distribution table, or, shorter, frequency table or frequency distribution.
#Throughout this mission, our focus will be on learning the details behind this form of simplifying data.

#Tasks:
#Try to get a sense for how difficult it is to analyze the basketball data set in its original form.
#Read in the basketball data set (the name of the CSV file is wnba.csv) using pd.read_csv().
#Using DataFrame.shape, find the number of rows and columns of the data set.
print(wnba.shape)



#2. FREQUENCY DISTRIBUTION TABLES
#A frequency distribution table has two columns. One column records the unique
#values of a variable, and the other the frequency of each unique value.

#To generate a frequency distribution table using Python,
#we can use the Series.value_counts() method.
#Let's try it on the Pos column, which describes the position on the court of each individual.

print(wnba['Pos'].value_counts())

#Tasks
#Using the Series.value_counts() method, generate frequency distribution tables for the following columns:
freq_distro_pos = wnba['Pos'].value_counts()
freq_distro_height = wnba['Height'].value_counts()
print(freq_distro_height)

#3. Sorting Frequency Distribution Tables
#As you might have noticed, pandas sorts the tables by default in the descending order of the frequencies.
#Let's consider again the frequency distribution table for the Pos variable, which is measured on a nominal scale:

print(wnba['Pos'].value_counts())

#This default is harmless for variables measured on a nominal scale because the unique values,
#although different, have no direction (we can't say, for instance, that centers are greater or lower than guards).
#The default actually helps because we can immediately see which values have the
#greatest or lowest frequencies, we can make comparisons easily, etc.


#                               Nominal     Ordinal     Interval    Ratio
#We can tell whether two         YES         YES          YES        YES
#individuals are different

#We can tell the direction
#of the difference               NO          YES          YES        YES

#We can tell the size            NO          YES          YES        YES
#of the difference

#We can tell the size            NO          NO           YES        YES
#of the difference

#We can measure                  NO         YES           YES        YES
#quantitative variables

#We can measure                  YES        NO            NO         NO
#qualitative variables

#For variables measured on ordinal, interval, or ratio scales, this default makes
#the analysis of the tables more difficult because the unique values have direction
#(some uniques values are greater or lower than others).
#Let's consider the table for the Height variable, which is measured on a ratio scale:

print(wnba['Height'].value_counts())

#Because the Height variable has direction, we might be interested to find:
    #How many players are under 170 cm?
    #How many players are very tall (over 185)?
    #Are there any players below 160 cm?

#It's time-consuming to answer these questions using the table above.
#The solution is to sort the table ourselves.

#wnba['Height'].value_counts() returns a Series object with the measures of height as indices.
#This allows us to sort the table by index using the Series.sort_index() method:

print(wnba['Height'].value_counts().sort_index())

#We can also sort the table by index in a descending order using:
print(wnba['Height'].value_counts().sort_index(ascending = False))

#Tasks
#Generate a frequency distribution table for the Age variable,
#which is measured on a ratio scale, and sort the table by unique values.

    #Sort the table by unique values in an ascending order,
    #and assign the result to a variable named age_ascending.
age_ascending = wnba['Age'].value_counts().sort_index()
    #Sort the table by unique values in a descending order,
    #and assign the result to a variable named age_descending.
age_descending = wnba['Age'].value_counts().sort_index(ascending = False)
#Using the variable inspector, analyze one of the frequency distribution tables
#and brainstorm questions that might be interesting to answer here.
print(age_ascending)
print(age_descending)
    #How many players are under 20?
#0
    #How many players are 30 or over?
#38

#4. SORTING TABLES FOR ORDINAL VARIABLES

#The sorting techniques learned in the previous screen can't be used for ordinal
#scales where the measurement is done using words.
#We don't have a variable measured on an ordinal scale in our data set,
#but let's use the PTS variable and the conventions below to create one and see
#why the techniques we learned don't work:

#   Condition	       Label
#points <= 20	very few points
#20 < points <= 80	few points
#80 < points <= 150	many points
#points > 150	a lot of points


#We name the new column PTS_ordinal_scale.
#Below is a short extract from our data set containing the new column:

#print(wnba[['Name', 'PTS', 'PTS_ordinal_scale']].head())

#	Name	        PTS	PTS_ordinal_scale
#0	Aerial Powers	93	many points
#1	Alana Beard	217	a lot of points
#2	Alex Bentley	218	a lot of points
#3	Alex Montgomery	188	a lot of points
#4	Alexis Jones	50	few points

#We want to sort the labels in an ascending or descending order,
#but using Series.sort_index() doesn't work because the method can't infer
#quantities from words like "few points".
#Series.sort_index() can only order the index alphabetically in an ascending or descending order:

#print(wnba['PTS_ordinal_scale'].value_counts().sort_index())

#The solution is to do selection by index label.
#The output of wnba['PTS_ordinal_scale'].value_counts() is a Series object with
#the labels as indices. This means we can select by indices to reorder in any way we like:

#print(wnba['PTS_ordinal_scale'].value_counts()[['very few points', 'few points',
#'many points', 'a lot of points']])

#This approach can be time-consuming because it involves more typing than is ideal.
#We can use iloc[] instead to reorder by position:

#print(wnba['PTS_ordinal_scale'].value_counts().iloc[[3, 1, 2, 0]])


def make_pts_ordinal(row):
    if row['PTS'] <= 20:
        return 'very few points'
    if (20 < row['PTS'] <=  80):
        return 'few points'
    if (80 < row['PTS'] <=  150):
        return 'many, but below average'
    if (150 < row['PTS'] <= 300):
        return 'average number of points'
    if (300 < row['PTS'] <=  450):
        return 'more than average'
    else:
        return 'much more than average'

wnba['PTS_ordinal_scale'] = wnba.apply(make_pts_ordinal, axis = 1)

#Tasks
#Generate a frequency distribution table for the transformed PTS_ordinal_scale column.
#Order the table by unique values in a descending order (not alphabetically).
#Assign the result to a variable named pts_ordinal_desc.

pts_ordinal_desc = wnba['PTS_ordinal_scale'].value_counts().iloc[[4, 3, 0,
2, 1, 5]]

print(pts_ordinal_desc)

#5. PROPORTIONS AND PERCENTAGES
#When we analyze distributions, we're often interested in answering questions about
#proportions and percentages. For instance, we may want to answer the following questions
#about the distribution of the POS (player position) variable:

#What proportion of players are guards?
#What percentage of players are centers?
#What percentage of players have mixed positions?

#It's very difficult to answer these questions precisely just by looking at the frequencies:

#G      60
#F      33
#C      25
#G/F    13
#F/C    12
#Name: Pos, dtype: int64

#We can see that almost half of the players are guards, but we need more granularity
#to answer the first question above. For that, we can transform frequencies to proportions.

#The proportion of each player position quantifies how many players play in a certain
#position relative to the total number of players.
#There are 60 guards and 143 players overall (including guards) so the proportion of guards is
#60/143.

#In practical data analysis, it's much more common to express the fraction as a
#decimal between 0 and 1.
#So we'd say that  0.42 (the result of 60/143) of the players are guards.

#DIVIDE frequencies by TOTAL to get PROPORITONS.

#In pandas, we can compute all the proportions at once by dividing each frequency
#by the total number of players:

print(wnba['Pos'].value_counts() / len(wnba))

#G      0.419580
#F      0.230769
#C      0.174825
#G/F    0.090909
#F/C    0.083916
#Name: Pos, dtype: float64

#It's slightly faster though to use Series.value_counts() with the normalize parameter set to True:

print(wnba['Pos'].value_counts(normalize = True))

#G      0.419580
#F      0.230769
#C      0.174825
#G/F    0.090909
#F/C    0.083916
#Name: Pos, dtype: float64

#To find percentages, we just have to multiply the proportions by 100:

print(wnba['Pos'].value_counts(normalize = True) * 100)

#G      41.958042
#F      23.076923
#C      17.482517
#G/F     9.090909
#F/C     8.391608
#Name: Pos, dtype: float64

#COUNTING players by position --> DIVIDE frequencies by total length of dataset
#to get PROPORTIONS --> MULTIPLY proportions by 100 to get percentages.

#Because proportions and percentages are relative to the total number of instances in some set of data,
#they are called RELATIVE FREQUENCIES.
#In contrast, the frequencies we've been working with so far are called ABSOLUTE
#FREQUENCIES because they are absolute counts and don't relate to the total number of instances.

#Tasks:
#Answer the following questions about the Age variable:
percentages = wnba['Age'].value_counts(normalize = True).sort_index() * 100
#What proportion of players are 25 years old? Assign your answer to a variable named proportion_25.
proportion_25 = percentages[25]/100
print(proportion_25)
#What percentage of players are 30 years old? Assign your answer to a variable named percentage_30.
percentage_30 = percentages[30]
print(percentage_30)
#What percentage of players are 30 years or older? Assign your answer to a variable named percentage_over_30.
percentage_over_30 = percentages.loc[30:].sum()
print(percentage_over_30)
#What percentage of players are 23 years or younger? Assign your answer to a variable named percentage_below_23.
percentage_below_23 = percentages.loc[:23].sum()
print(percentage_below_23)

#6. PERCENTILES AND PERCENTILE RANKS
#In the previous exercise, we found that the percentage of players aged 23 years
#or younger is 19% (rounded to the nearest integer).
#This percentage is also called a percentile rank.

#A percentile rank of a value x in a frequency distribution is given by the percentage
#of values that are equal or less than x. In our last exercise, x = 23,
#and the fact that 23 has a percentile rank of 19% means that 19% of the values
#are equal to or less than 23.

#In this context, the value of 23 is called the 19th percentile.
#If a value x is the 19th percentile, it means that 19% of all the values in the
#distribution are equal to or less than x.

#When we're trying to answer questions similar to "What percentage of players are 23 years or younger?", we're trying to find percentile ranks.
#In our previous exercise, our answer to this question was 18.881%.
#We can arrive at the same answer a bit faster using the percentileofscore(a, score, kind='weak') function from scipy.stats:

#from scipy.stats import percentileofscore
#print(percentileofscore(a = wnba['Age'], score = 23, kind = 'weak'))

#We need to use kind = 'weak' to indicate that we want to find the percentage of
#values that are equal to or less than the value we specify in the score parameter.

#Another question we had was what percentage of players are 30 years or older.
#We can answer this question too using percentile ranks.
#First we need to find the percentage of values equal to or less than 29 years (the percentile rank of 29).
#The rest of the values must be 30 years or more.

#In our exercise the answer we found was 26.573%.
#This is what we get using the technique we've just learned:

#print(100 - percentileofscore(wnba['Age'], 29, kind = 'weak'))

#In the next screen, we'll learn how to find quickly any percentile using pandas.
#For now, let's practice percentile ranks more.

#Tasks
#Import percentileofscore() from scipy.stats, and then use it to answer the following questions:
#Imported above

#What percentage of players played half the number of games or less in the 2016-2017 season
#(there are 34 games in the WNBA’s regular season)?
#Use the Games Played column to find the data you need,
#and assign your answer to a variable named percentile_rank_half_less.

percentile_rank_half_less = percentileofscore(wnba['Games Played'], 17,
kind = 'weak')
percentage_half_more = 100 - percentile_rank_half_less
print(percentile_rank_half_less)
print(percentage_half_more)

#7. FINDING PERCENTILES WITH PANDAS
#To find percentiles, we can use the Series.describe() method, which returns by
#default the 25th, the 50th, and the 75th percentiles:

print(wnba['Age'].describe())

#We are not interested here in the first three rows of the output
#(count, mean, and standard deviation).
#We can use iloc[] to isolate just the output we want:

print(wnba['Age'].describe().iloc[3:])

#The 25th, 50th, and 75th percentiles pandas returns by default are the scores
#that divide the distribution into four equal parts.

#The three percentiles that divide the distribution in four equal parts are also
#known as quartiles (from the Latin quartus which means four).
#There are three quartiles in the distribution of the Age variable:

#The first quartile (also called lower quartile) is 24
#(note that 24 is also the 25th percentile).
#The second quartile (also called the middle quartile) is 27
#(note that 27 is also the 50th percentile).
#And the third quartile (also called the upper quartile) is 30
#(note that 30 is also the 75th percentile).

#We may be interested to find the percentiles for percentages other than
#25%, 50%, or 75%. For that, we can use the percentiles parameter of Series.describe().
#This parameter requires us to pass the percentages we want as proportions between 0 and 1.

print(wnba['Age'].describe(percentiles = [.1, .15, .33, .5, .592, .85,
.9]).iloc[3:])

#Percentiles don't have a single standard definition, so don't be surprised if you
#get very similar (but not identical) values if you use different functions
#(especially if the functions come from different libraries).

#Tasks
#Use the Age variable along with Series.describe() to answer the following questions:

#What's the upper quartile of the Age variable? Assign your answer to a variable named age_upper_quartile.
#What's the middle quartile of the Age variable? Assign your answer to a variable named age_middle_quartile.
#What's the 95th percentile of the Age variable? Assign your answer to a variable named age_95th_percentile.
percentiles = wnba['Age'].describe(percentiles = [.5, .75, .95])
age_upper_quartile = percentiles['75%']
print(age_upper_quartile)
age_middle_quartile = percentiles['50%']
print(age_middle_quartile)
age_95th_quartile = percentiles['95%']
print(age_95th_quartile)
#Indicate the truth value of the following sentences:

#A percentile is a value of a variable, and it corresponds to a certain percentile
#rank in the distribution of that variable.
#(If you think this is true, assign True (boolean, not string) to a variable named question1, otherwise assign False.)
question1 = False
#A percentile rank is a numerical value from the distribution of a variable.
#(Assign True or False to question2.)
question2 = True
#The 25th percentile is the same thing as the lower quartile, and the upper quartile
#is the same thing as the third quartile. (Assign True or False to question3)
question3 = True

#8. GROUPED FREQUENCY DISTRIBUTION TABLES
#With frequency tables, we're trying to transform relatively large and incomprehensible
#amounts of data to a table format we can understand.
#However, not all frequency tables are straightforward:

print(wnba['Weight'].value_counts().sort_index())

#There's a lot of granularity in the table above, but for this reason it's not
#easy to find patterns. The table for the Weight variable is a relatively happy case -
#the frequency tables for variables like PTS, BMI, or MIN are even more daunting.

#There's a lot of granularity in the table above, but for this reason it's not easy to find patterns.
#The table for the Weight variable is a relatively happy case - the frequency tables for variables like
#PTS, BMI, or MIN are even more daunting.

#Fortunately, pandas can handle this process gracefully.
#We only need to make use of the bins parameter of Series.value_counts().
#We want ten equal intervals, so we need to specify bins = 10:

print(wnba['Weight'].value_counts(bins = 10).sort_index())

#(54.941, 60.8], (60.8, 66.6] or (107.2, 113.0] are number intervals.
#The ( character indicates that the starting point is not included, while the ]
#indicates that the endpoint is included. (54.941, 60.8] means that 54.941 isn't
#included in the interval, while 60.8 is.
#The interval (54.941, 60.8] contains all real numbers greater than 54.941 and less than or equal to 60.8.

#We can see above that there are 10 equal intervals, 5.8 each. The first interval,
#(54.941, 60.8] is confusing, and has to do with how pandas internals show the output.
#One way to understand this is to convert 54.941 to 1 decimal point, like all the other values are.
#Then the first interval becomes (54.9, 60.8]. 54.9 is not included,
#so you can think that the interval starts at the minimum value of the Weight variable, which is 55.

#Because we group values in a table to get a better sense of frequencies in the distribution,
#the table we generated above is also known as a grouped frequency distribution table.
#Each group (interval) in a grouped frequency distribution table is also known as a class interval.
#(107.2, 113.0], for instance, is a class interval.

#Using the grouped frequency distribution table we generated above for the Weight variable,
#we can find patterns easier in the distribution of values:

#Most players weigh somewhere between 70 and 90 kg.
#Very few players weigh over 100 kg.
#Very few players weigh under 60 kg; etc.

#Tasks
#Examine the frequency table for the PTS (total points) variable trying to find
#some patterns in the distribution of values. Then, generate a grouped frequency
#distribution table for the PTS variable with the following characteristics:

#The table has 10 class intervals.
#For each class interval, the table shows percentages instead of frequencies.
#The class intervals are sorted in descending order.

#Assign the table to a variable named grouped_freq_table,
#then print it and try again to find some patterns in the distribution of values.

print(wnba['PTS'].describe())

print(wnba['PTS'].value_counts(bins = 10, normalize = True).sort_index(ascending
= False) * 100)

#9. INFORMATION LOSS
#When we generate grouped frequency distribution tables, there's an inevitable
#information loss. Let's consider this table:

print(wnba['PTS'].value_counts(bins = 10))

#Looking at the first interval, we can see there are 30 players who scored
#between 2 and 60 points (2 is the minimum value in our data set,
#and points in basketball can only be integers).
#However, because we grouped the values, we lost more granular information like:

#How many players, if any, scored exactly 50 points?
#How many players scored under 10 points?
#How many players scored between 20 and 30 points, etc?

#To get back this granular information, we can increase the number of class intervals.
#However, if we do that, we end up again with a table that's lengthy and very difficult to analyze.

#On the other side, if we decrease the number of class intervals, we lose even more information:

print(wnba['PTS'].value_counts(bins = 5).sort_index())

#There are 54 players that scored between 2 and 118 points.
#We can get this information from the first table above too,
#but there's some extra information there: among these 54 players,
#30 scored between 2 and 60 points, and 24 scored between 61 and 118 points.
#We lost this information when we decreased the number of class intervals from 10 to 5.

#We can conclude there is a trade-off between the information in a table, and how comprehensible the table is.

#When we increase the number of class intervals, we can get more information,
#but the table becomes harder to analyze. When we decrease the number of class intervals,
#we get a boost in comprehensibility, but the amount of information in the table decreases.

#As a rule of thumb, 10 is a good number of class intervals to choose because it
#offers a good balance between information and comprehensibility.

#Generate a grouped frequency distribution for the MIN variable
#(minutes played during the season), and experiment with the number of class
#intervals to get a sense for what conclusions you can draw as you vary the
#number of class intervals. Try to experiment with the following numbers of class intervals:

print(wnba['PTS'].value_counts(bins = 1).sort_index())
print('----------')
print(wnba['PTS'].value_counts(bins = 2).sort_index())
print('----------')
print(wnba['PTS'].value_counts(bins = 3).sort_index())
print('----------')
print(wnba['PTS'].value_counts(bins = 5).sort_index())
print('----------')
print(wnba['PTS'].value_counts(bins = 10).sort_index())
print('----------')
print(wnba['PTS'].value_counts(bins = 15).sort_index())
print('----------')
print(wnba['PTS'].value_counts(bins = 20).sort_index())
print('----------')
print(wnba['PTS'].value_counts(bins = 40).sort_index())

#10. READABILITY FOR GROUPED FREQUENCY TABLES
#Pandas helps a lot when we need to explore quickly grouped frequency tables.
#However, the intervals pandas outputs are confusing at first sight:

print(wnba['PTS'].value_counts(bins = 5).sort_index())
#Imagine we'd have to publish the table above in a blog post or a scientific paper.
#The readers will have a hard time understanding the intervals we chose.
#They'll also be puzzled by the decimal numbers because points in basketball can only be integers.

#To fix this, we can define the intervals ourselves.
#For the table above, we can define six intervals of 100 points each,
#and then count how many values fit in each interval. We'd like to end with a table like this:

#(0,100]      49
#(100,200]    28
#(200,300]    32
#(300,400]    17
#(400,500]    10
#(500,600]     7

#Next, we show one way to code the intervals.
#We start with creating the intervals using the pd.interval_range() function:

#intervals = pd.interval_range(start = 0, end = 600, freq = 100)
#print(intervals)

#IntervalIndex([(0, 100], (100, 200], (200, 300], (300, 400], (400, 500], (500, 600]]
              #closed='right',
              #dtype='interval[int64]')

#Next, we create a new Series using the intervals as indices, and, for now, 0 as values:

#gr_freq_table = pd.Series([0,0,0,0,0,0], index = intervals)
#print(gr_freq_table)

#(0, 100]      0
#(100, 200]    0
#(200, 300]    0
#(300, 400]    0
#(400, 500]    0
#(500, 600]    0
#dtype: int64


#Next, we loop through the values of the PTS column, and for each value:
#We loop through the intervals we defined previously, and for each interval:
    #We check whether the current value from the PTS column belongs to that interval.
    #If the value doesn't belong to an interval, we continue the inner loop over the intervals.
    #If the value belongs to an interval:
        #We update the counting for that interval in gr_freq_table by adding 1.
        #We exit the inner loop over the intervals with break because
        #a value can belong to one interval only, and it makes no sense to continue the loop
        #(without using break, we'll get the same output but we'll do many redundant iterations).
#for value in wnba['PTS']:
    #for interval in intervals:
        #if value in interval:
            #gr_freq_table.loc[interval] += 1
            #break
#print(gr_freq_table)

#Now we do a quick sanity check of our work.
#There are 143 players in the data set, so the frequencies should add up to 143:

#print(gr_freq_table.sum())

#Note that we're not restricted by the minimum and maximum values of a variable when we define intervals.
#The minimum number of points is 2, and the maximum is 584, but our intervals range from 1 to 600.

#Using the techniques above, generate a grouped frequency table for the PTS variable.
#The table should have the following characteristics:

#There are 10 class intervals.
#The first class interval starts at 0 (not included).
#The last class interval ends at 600 (included).
#Each interval has a range of 60 points.

#Assign the table to a variable named gr_freq_table_10.

intervals = pd.interval_range(start = 0, end = 600, freq = 60)
gr_freq_table_10 = pd.Series([0 for i in range(10)], index = intervals)
for value in wnba['PTS']:
    for interval in intervals:
        if value in interval:
            gr_freq_table_10.loc[interval] += 1
            break

print(gr_freq_table_10)

#11. FREQUENCY TABLES AND CONTINUOUS VARIABLES
#Remember from the previous mission that a height of 175 cm is just an interval
#bounded by the real limits of 174.5 cm (lower real limit) and 175.5 (upper real limit).
#When we build frequency tables for continuous variables, we need to take into account that the values are intervals.

#The height of 175 cm has a frequency of 16 in the distribution of the Height variable:
print(wnba['Height'].value_counts()[175])

#This doesn't mean that there are 16 players that are all exactly 175 cm tall.
#It rather means that there are 16 players with a height that's somewhere between 174.5 cm and 175.5 cm.

#A similar reasoning applies when we read grouped frequency tables.
#If we had an interval of (180, 190] for a continuous variable, 180 and 190 are
#with 179.5 being the lower real limit of 180, and 190.5 the upper real limit of 190.

#Continuous variables affect as well the way we read percentiles.
#For instance, the 50th percentile (middle quartile) in the distribution of the Height variable is 185 cm:

print(wnba['Height'].describe().iloc[5])
#This means that 50% of the values are less than or equal to 185.5 cm
#(the upper limit of 185 cm), not equal to 185 cm.

#12. NEXT STEPS
#In this mission, we learned how to organize data in frequency and grouped frequency tables.
#Frequency tables allow us to transform large and incomprehensible amounts of data to a format we can understand.

#Next in the course, we'll learn how to visualize frequency tables using bar plots and histograms.
