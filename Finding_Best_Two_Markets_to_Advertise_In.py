#!/home/anesta95/.virtualenvs/Stats/bin/python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#1. FINDING THE BEST TWO MARKETS TO ADVERTISE IN
#We've come a long way in this course and learned:

#How to summarize distributions using the mean, the median, and the mode.

#How to measure the variability of a distribution using the range,
#the mean absolute deviation, the variance, and the standard deviation.

#How to locate any value in a distribution using z-scores.

#To make learning smoother and more efficient,
#we learned about each of these topics in isolation.
#In this guided project, we make one step further and learn to combine some of
#these skills to perform practical data analysis.
#Moreover, we'll also make use of what we learned in the first course.

#Let's assume that we're working for an an e-learning company that offers courses on
#programming. Most of our courses are on web and mobile development,
#but we also cover many other domains, like data science, game development, etc.
#We want to promote our product and we'd like to invest some money in advertisement.
#Our goal in this project is to find out the two best markets to advertise our product in.

#TASKS
#To help readers gain context into your project, use the first Markdown cell of the notebook to:

#Add a title.
#Write a short introduction where you explain readers in no more than two paragraphs:
#What the project is about.
#What your goal is in this project.
#The title and the introduction are tentative at this point,
#so don't spend too much time here — you can come back at the end of your work to refine them.

#2. UNDERSTANDING THE DATA
#To reach our goal, we could organize surveys for a couple of different markets
#to find out which would the best choices for advertising.
#This is very costly, however, and it's a good call to explore cheaper options first.

#We can try to search existing data that might be relevant for our purpose.
#One good candidate is the data from freeCodeCamp's 2017 New Coder Survey.
#freeCodeCamp is a free e-learning platform that offers courses on web development.
#Because they run a popular Medium publication (over 400,000 followers),
#their survey attracted new coders with varying interests (not only web development),
#which is ideal for the purpose of our analysis.

#TASKS
#Read in the '2017-fCC-New-Coders-Survey-Data.csv' file and explore briefly the data set.

#Look for number of rows and columns.
#Print the first five rows.
#Try to find relevant columns for the purpose of our analysis.
#Try to understand what each column describes.

survey = pd.read_csv('2017-fCC-New-Coders-Survey-Data.csv', encoding = 'latin-1')
print(survey.head())
print(survey.info())
print(survey.shape)

#You'll notice that most column names are self-explanatory,
#but it seems that we don't have a clear documentation explaining each column name.
#However, you can find more information in the raw-data folder of the repository we
#mentioned above — you can find the initial survey questions, and from there it should
#be easy to infer what each column describes.

#Once you're done with this initial exploration, add some context for readers and discuss:

#Why you're using a ready-made data set instead of organizing a survey.
#Because it is data from potential users we are trying to survey/attract and it is
#not very costly to do the analysis.

#What's this data set about.
#Survey responses from freeCodeCamp users about what products/languages/services
#they want to code in and use.

#Where can this data set be downloaded.
#Download at https://github.com/freeCodeCamp/2017-new-coder-survey

#3. CHECKING FOR SAMPLE REPRESENTATIVITY
#As we mentioned earlier, most of the courses we offer are on web and mobile development,
#but we also cover many other domains, like data science, game development, etc.
#For the purpose of our analysis, we want to answer questions about a population
#of new coders that are interested in the subjects we teach. We'd like to know:

#Where are these new coders located.
#What are the locations with the greatest number of new coders.
#How much money new coders are willing to spend on learning.

#Before starting to analyze the sample data we have,
#we need to clarify whether it's representative for our population
#of interest and it has the right categories of people for our purpose.

#TASKS
#Figure out whether the sample we have is representative for our population of interest.

#The JobRoleInterest column describes for every participant the role(s) they'd be interested in working.
#Generate a frequency distribution table for this column. Take percentages instead of absolute frequencies.
#Analyze the table.

#Are people interested in only one subject or they can be interested in more than one subject?
#If most people are interested in more than one subject, is this sample still representative?
#The focus of our courses is on web and mobile development.
#How many people are interested in at least one of these two subjects?

print(survey['JobRoleInterest'].value_counts(normalize = True) * 100)
#It looks like most people (~75%) are interested in more than one position

freq_table = pd.DataFrame(
    survey['JobRoleInterest'].value_counts(normalize = True) * 100)

print(type(freq_table))
freq_table['Title'] = freq_table.index
print(freq_table['Title'].head())
freq_table = freq_table.reset_index(drop=True)

print(freq_table.head())

our_roles_percentage = 0
other_roles_percentage = 0
our_roles = ['Web Developer', 'Mobile Developer',
                'Data Scientist', 'Game Developer']
freq_table_dict = dict(zip(freq_table['Title'], freq_table['JobRoleInterest']))

for job, percent in freq_table_dict.items():
    if any(x in job for x in our_roles):
        our_roles_percentage += percent
    else:
        other_roles_percentage += percent

print(our_roles_percentage)
print(other_roles_percentage)

labels = 'Our Roles', 'Other Roles'
pcts = [our_roles_percentage, other_roles_percentage]
colors = ['lightskyblue', 'lightcoral']
explode = (0.1, 0)  # explode 1st slice

# Plot
plt.pie(pcts, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
#plt.savefig('Pie_Chart_of_Our_Role_Interest.png')
plt.close()

#4. NEW CODERS - LOCATION AND DENSITIES
#Now that we found out that the sample has the right categories of people for our purpose,
#we can begin analyzing it. We can start with finding out where these new coders are located,
#and what are the densities (how many coderes there are) for each location.

#The data set provides information about the location of each participant at a country level.
#The CountryCitizen variable describes the country of origin for each participant,
#and the CountryLive variable describes what country each participants lives in
#(which may be different than the origin country).

#For our analysis, we'll work with the CountryLive variable because we're interested
#where people actually live at the moment when we run the ads.
#In other words, we're interested where people are located, not where they were born.

#Because the data set provides information at a country level,
#we can think of each country as an individual market.
#This means we can frame our goal as finding the two best countries to advertise in.

#One indicator of a good market is the number of potential customers —
#the more potential customers in a market, the better.
#If our ads manage to convince 10% of the 5000 potential customers in market A
#to buy our product, then this is better than convincing 100% of the 30 potential customers in market B.

#TASKS

#To make sure you're working with a representative sample,
#drop all the rows where participants didn't answer what role they are interested in.
#Where a participant didn't respond, we can't know for sure what their interests are,
#so it's better if we leave out this category of participants.

survey = survey.dropna(subset=['JobRoleInterest'])

#Generate a frequency table for the CountryLive variable.
#Generate both absolute and relative frequencies.
#Analyze the results.
#Based on the results, what are the two markets you'd choose for advertisement?
#Can we stop the analysis here, or we need to go more in depth?

print(survey['CountryLive'].value_counts())
countrylive_freq_table = pd.DataFrame(
    survey['CountryLive'].value_counts(normalize = True) * 100)

print(countrylive_freq_table)
countryfrom_freq_table = pd.DataFrame(
    survey['CountryCitizen'].value_counts(normalize = True) * 100)
print(countryfrom_freq_table)
#I would advertise in the US and India

#5. SPEND MONEY FOR LEARNING
#Previously, we found useful information about the location of new coders,
#and what are the countries where new coders live,
#but we need to go more in depth with our analysis before taking a decision.
#We can continue by figuring out how much money new coders are actually willing
#to spend on learning. Advertising within markets where most people are only
#willing to learn for free is extremely unlikely to be profitable for us.

#The MoneyForLearning column describes in American dollars the amount of money
#spent by participants from the moment they started coding until the moment they
#completed the survey. Our company sells subscriptions at a price of $59 per month,
#and for this reason we're interested in finding out how much money each student
#spends per month.

#It also seems like a good idea to narrow down our analysis to only four countries:
#the US, India, the United Kingdom, and Canada. Two reasons for this decision are:

#These are the countries having the highest absolute frequencies in our sample,
#which means we have a decent amount of data for each.

#Our courses are written in English, and English is an official language in all
#these four countries.
#The more people that know English, the better our chances to target the right people with our ads.

#TASKS
#Create a new column that describes the amount of money a student has spent per month
#(at the moment they completed the survey).

#You'll need to divide the MoneyForLearning column to the MonthsProgramming column.
#Some students answered that they had been learning to code for 0 months
#(it might be that they had just started when they completed the survey).
#To avoid dividing by 0, replace all the values of 0 with 1.

#Find out how many null values there are in the new column
#(the column describing the amount of money students spend per month).

#Keep only the rows that don't have a null value for the new column.

#Remove also any rows that have null values in the CountryLive column.

#Group the remaining data by the CountryLive column and
#find out how much money a student spends on average each month in the US, India, the United Kingdom and Canada.

#You can use the DataFrame.groupby() method.

#As a summary metric, we recommend choosing the mean to take into account all values in the distributions.
#You can also compute the median or the mode to see how they compare with the mean.

#Analyze the results. Is there anything in the results that looks off?

survey = survey.dropna(subset=['MonthsProgramming'])

survey = survey.dropna(subset=['CountryLive'])
survey['MonthsProgramming'].replace(0,1, inplace = True)



survey['MoneyPerMonth'] = (survey['MoneyForLearning']
/ survey['MonthsProgramming'])
survey = survey.dropna(subset=['MoneyPerMonth'])
print(survey['MoneyPerMonth'].head())


print(survey.groupby(['CountryLive'])['MoneyPerMonth'].count())
MeanMoneyPerMonth = survey.groupby(['CountryLive'])['MoneyPerMonth'].mean()

print(MeanMoneyPerMonth.loc[['Canada', 'United Kingdom', 'India',
'United States of America']])

#6. DEALING WITH EXTREME OUTLIERS
#In the last exercise, you should have arrived at the following mean values:

'''
CountryLive
United States of America    227.997996
India                       135.100982
United Kingdom               45.534443
Canada                      113.510961
Name: money_per_month, dtype: float64
'''
#The results for the United Kingdom and Canada are surprisingly low
#relative to the values we see for India. If we considered a few socio-economical metrics
#(like GDP per capita), we'd intuitively expect people in the UK and Canada to
#spend more on learning than people in India.

#It might be that we don't have have enough representative data for the United Kingdom,
#Canada, and India, or we have some outliers (maybe coming from wrong survey answers)
#making the mean too big for India, or too low for the UK and Canada.
#Or it might be that the results are correct.

#TASKS
#Generate four box plots on the same figure to visualize for each country
#(the US, India, the United Kingdom, Canada) the distribution of the variable
#that describes how much money each participant had spent per month.

#Can you spot extreme outliers for India, Canada or the United Kingdom?
#If not, what extreme outliers can you spot?
#Eliminate the extreme outliers.

#Recompute the mean values, just like we did in the previous screen:
#group the data by the CountryLive column, and then find out how much money a
#student spends on average each month in the US, India, the United Kingdom and Canada.

#If the mean values still look off, look more for extreme outliers.
#For instance, you can find a couple of persons in India who spend $5000 per month.
#Isolate these respondents and examine their answers to other questions in the
#survey to figure out whether these big expenses with learning are justified —
#you can try to find out whether they attended any bootcamp, which might justify the large amount of money spent.
#If you find more extreme outliers, remove them, and recompute the mean values.
#Is it clear enough at this point what are the two best countries to choose for advertisement?

only_four = survey[survey['CountryLive'].str.contains(
    'India|United Kingdom|Canada|United States of America')]

sns.boxplot(x="CountryLive", y="MoneyPerMonth", data = only_four)
#plt.savefig("Top_4_Countries_Average_Monthly_TechEd_Spending.png")
plt.close()

print(only_four.groupby(['CountryLive'])['MoneyPerMonth'].describe())
#Taking out extreme US outlier
survey = survey[survey['MoneyPerMonth'] < 20000]


# Recompute mean sum of money spent by students each month
countries_mean = survey.groupby('CountryLive').mean()
print(countries_mean['MoneyPerMonth'][['United States of America',
                            'India', 'United Kingdom',
                            'Canada']])

#Replotting
only_four = survey[survey['CountryLive'].str.contains(
    'India|United Kingdom|Canada|United States of America')]

sns.boxplot(x="CountryLive", y="MoneyPerMonth", data = only_four)
plt.title('Money Spent Per Month Per Country\n(Distributions)',
         fontsize = 16)
plt.ylabel('Money per month (US dollars)')
plt.xlabel('Country')
plt.xticks(range(4), ['US', 'UK', 'India', 'Canada']) # avoids tick labels overlap
#plt.savefig("Top_4_Countries_Average_Monthly_TechEd_Spending_minus_outlier.png")
plt.close()

#Inspect India outliers

india_outliers = only_four[
    (only_four['CountryLive'] == 'India') &
    (only_four['MoneyPerMonth'] >= 2500)]
print(india_outliers)
#None attended bootcamp, probably put in spending as university tuition.

only_four = only_four.drop(india_outliers.index) #using row labels

#Now let's look at more US outliers
us_outliers = only_four[
    (only_four['CountryLive'] == 'United States of America') &
    (only_four['MoneyPerMonth'] >= 6000)]
print(us_outliers)

# Remove the respondents who didn't attendent a bootcamp
no_bootcamp = only_four[
    (only_four['CountryLive'] == 'United States of America') &
    (only_four['MoneyPerMonth'] >= 6000) &
    (only_four['AttendedBootcamp'] == 0)
]

only_four = only_four.drop(no_bootcamp.index)


# Remove the respondents that had been programming for less than 3 months
less_than_3_months = only_four[
    (only_four['CountryLive'] == 'United States of America') &
    (only_four['MoneyPerMonth'] >= 6000) &
    (only_four['MonthsProgramming'] <= 3)
]

only_four = only_four.drop(less_than_3_months.index)

#Now looking at Canadian outliers
canada_outliers = only_four[
    (only_four['CountryLive'] == 'Canada') &
    (only_four['MoneyPerMonth'] > 4500)]
print(canada_outliers)

#No extreme outliers

# Recompute mean sum of money spent by students each month
print(only_four.groupby('CountryLive').mean()['MoneyPerMonth'])

# Visualize the distributions one more time
sns.boxplot(y = 'MoneyPerMonth', x = 'CountryLive',
            data = only_four)
plt.title('Money Spent Per Month Per Country\n(Distributions)',
          fontsize = 16)
plt.ylabel('Money per month (US dollars)')
plt.xlabel('Country')
plt.xticks(range(4), ['US', 'UK', 'India', 'Canada']) # avoids tick labels overlap
#plt.savefig('Top_4_Mean_Monthly_TechEd_Spending_no_outliers.png')
plt.close()

#7. CHOOSING THE TWO BEST MARKETS
#After eliminating the extreme outliers, we found the following mean values:
'''
CountryLive
Canada                       93.065400
India                        65.758763
United Kingdom               45.534443
United States of America    142.654608
Name: money_per_month, dtype: float64
'''

#There's not only one solution in this case, and you might have found solid
#arguments to take different decisions with respect to eliminating some of the outliers.
#You can see the decision we took in the solution notebook.

#Considering the results we've found so far, one country we should definitely
#advertise in is the US. There are a lot of new coders living there and they are
#willing to pay a good amount of money each month.

#We need to choose one more market though.

#TASKS
#Try to choose the second market to advertise in.

#Remember that we sell subscriptions at a price of $59 per month.
#Make sure you also consider the number of potential customers in each country.
#Based on all of the results you've found so far, brainstorm a couple of possible decisions.

#Does it make sense to advertise in more then two countries?
#Does it make sense to split the advertising budget unequally
#(e.g.: spend 70% to advertise in the US and 30% to advertise in India)?
#Does it make sense to advertise only in the US?
#If we had a marketing team in our company, would it be better to just send them
#our results and let them use their domain knowledge to take the best decision?

#Although people spend more money on average in Canada than they do in India,
#let's see if the market is larger in India
# Frequency table for the 'CountryLive' column
print(only_four['CountryLive'].value_counts(normalize = True) * 100)

#It seems like there might be more coders ready to learn in India, possibly
#putting more advertising dollars there could pay off.

#Probably best to let our marketing/ad team decide how they want to split the ad
#money between the four countries, if they even decide splitting would be adventageous.
