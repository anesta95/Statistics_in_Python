#!/home/anesta95/.virtualenvs/Stats/bin/python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from  numpy import arange

#1. IS FANDANGO STILL INFLATING RATINGS?
#In October 2015, a data journalist named Walt Hickey analyzed movie ratings data
#and found strong evidence to suggest that Fandango's rating system was biased and
#dishonest (Fandango is an online movie ratings aggregator).

#Fandango displays a 5-star rating system on their website,
#where the minimum rating is 0 stars and the maximum is 5 stars.

#Hickey found that there's a significant discrepancy between the number of stars
#displayed to users and the actual rating,
#which he was able to find in the HTML of the page. He was able to find that:

#The actual rating was almost always rounded up to the nearest half-star.
#For instance, a 4.1 movie would be rounded off to 4.5 stars, not to 4 stars, as you may expect.

#In the case of 8% of the ratings analyzed, the rounding up was done to the nearest whole star.
#For instance, a 4.5 rating would be rounded off to 5 stars.

#For one movie rating, the rounding off was completely bizarre:
#from a rating of 4 in the HTML of the page to a displayed rating of 5 stars.

#The two distributions above are displayed using a simple line plot,
#which is also a valid way to show the shape of a distribution.
#The variable being examined is movie rating, and for each unique rating we can
#see its relative frequency (percentage) on the y-axis of the graph.
#When an analysis report is intended for large audiences,
#relative frequencies (especially percentages) are preferred over absolute frequencies.

#Both distributions above are strongly left skewed, suggesting that movie ratings
#on Fandango are generally high or very high. We can see there's no rating under
#2 stars in the sample Hickey analyzed. The distribution of displayed ratings
#is clearly shifted to the right compared to the actual rating distribution,
#suggesting strongly that Fandango inflates the ratings under the hood.

#Fandango's officials replied that the biased rounding off was caused by a bug
#in their system rather than being intentional, and they promised to fix the bug
#as soon as possible. Presumably, this has already happened,
#although we can't tell for sure since the actual rating value doesn't seem to be
#displayed anymore in the pages' HTML.

#In this project, we'll analyze more recent movie ratings
#data to determine whether there has been any change in Fandango's rating system
#after Hickey's analysis.

#2. UNDERSTANDING THE DATA
#One of the best ways to figure out whether there has been any change in Fandango's
#rating system after Hickey's analysis is to compare the system's characteristics
#previous and after the analysis. Fortunately, we have ready-made data for both these periods of time:

#Walt Hickey made the data he analyzed publicly available on GitHub.
#We'll use the data he collected to analyze the characteristics of Fandango's
#rating system previous to his analysis.

#One of Dataquest's team members collected movie ratings data for movies released in 2016 and 2017.
#The data is publicly available on GitHub and we'll use it to analyze the rating system's
#characteristics after Hickey's analysis.

#TASKS

#Read in and explore briefly the two data sets (fandango_score_comparison.csv and movie_ratings_16_17.csv)
#to understand their structure.
#You can find the documentation of both data sets in the GitHub repositories we linked to above.

#Isolate the columns that offer information about Fandango's ratings in separate variables
#so we have just the data we're interested in more readily available for later use.

#For the data set with ratings previous to Hickey's analysis, select the following columns:
#'FILM', 'Fandango_Stars', 'Fandango_Ratingvalue', 'Fandango_votes', 'Fandango_Difference'.

#For the other data set, select the the following columns: 'movie', 'year', 'fandango'.

#Define the population of interest for our goal —
#remember that our goal is to determine whether there has been any
#change in Fandango's rating system after Hickey's analysis.

#By reading the README.md files of the two repositories, figure out
#whether the two samples are representative for the population we're trying to describe.

#Determine whether the sampling is random or not —
#did all the movies have an equal chance to be included in the two samples?
Fandango_Hickey = pd.read_csv('fandango_score_comparison.csv')
Fandango_Prev = Fandango_Hickey[['FILM', 'Fandango_Stars',
'Fandango_Ratingvalue', 'Fandango_votes', 'Fandango_Difference']]
Fandango_DQ = pd.read_csv('movie_ratings_16_17.csv')
Fandango_Post = Fandango_DQ[['movie', 'year', 'fandango']]

print(Fandango_Prev.head())
print(Fandango_Post.head())
#Useful information can also be found in Hickey's article.

#3. CHANGING THE GOAL OF OUR ANALYSIS
#In the last exercise, you should have concluded that the sampling processes were not random,
#and the resulting samples are very unlikely to be representative of the population we're interested in describing.

#Setbacks like these are common in practical data analysis —
#you spend time to collect data only to find out that you haven't found exactly what you need.
#The worst thing you could do is to abandon the research altogether and
#start looking again for something new and perfect.
#Instead, it's much better to carry on and try to come up with creative workarounds that are good enough.

#At this point, we have at least two alternatives: either we collect new data,
#either we change the goal of our analysis by placing some limitations on it.

#Tweaking our goal seems a much faster choice compared to collecting new data.
#Also, it's quasi-impossible to collect a new sample previous to Hickey's analysis at this moment in time.

#TASKS
#Change slightly the current goal of our analysis such that:

#The population of interest changes and the samples we currently work with become representative.

#The new goal is still a fairly good proxy for our initial goal,
#which was to determine whether there has been any change
#in Fandango's rating system after Hickey's analysis.

#This is not a one-solution-only exercise, so don't be afraid to experiment with new ideas.

#4. ISOLATING THE SAMPLES WE NEED
#In our solution notebook we changed our goal to finding out whether there's any
#difference between Fandango's ratings for popular movies in 2015 and Fandango's
#ratings for popular movies in 2016.
#With this new research goal, we have two populations of interest:

#All Fandango's ratings for popular movies released in 2015.
#All Fandango's ratings for popular movies released in 2016.
#We need to be clear about what counts as popular movies.
#We'll use Hickey's benchmark of 30 fan ratings and count a movie as popular
#only if it has 30 fan ratings or more on Fandango's website.

#The term "popular" is vague and we need to define it with precision before continuing.
#We'll use Hickey's benchmark of 30 fan ratings and consider a movie as "popular"
#only if it has 30 fan ratings or more on Fandango's website.

#Check if both samples contain popular movies — that is,
#check whether all (or at least most) sample points are movies with over 30 fan
#ratings on Fandango's website.

#For the first dataset, the number of 2015 files that have less than 30 Fandango_votes

print(sum(Fandango_Prev['Fandango_votes'] < 30))
#There are none, awesome!

#One of the data sets doesn't provide information about the number of fan ratings,
#and this raises representativity issues once again.

#Find a quick way to check whether this sample contains enough popular movies as to be representative.
#I am going to take a random sample of 10 of the movies from the new dataset
#and see what proportion of them have over 30 fan votes.

print(Fandango_Post.sample(10, random_state = 1))
#Fan Votes for Random Sample of 2016 movies
#Mechanic: Resurrection: 25563
#Warcraft: 63206
#Max Steel: 6802
#Me Before You: 30449
#Fantastic Beasts and Where to Find Them: 87391
#Cell: 3772
#Genius: 2871
#A Hologram for the King: 10180
#Captain America: Civil War 178805

#All movies qualify!

#If you explore the data sets enough, you'll notice that some movies were not
#released in 2015 and 2016. We need to isolate only the sample points that belong to our populations of interest.

#Isolate the movies released in 2015 in a separate data set.
#Isolate the movies released in 2016 in another separate data set.
#These are the data sets we'll use next to perform our analysis.

#For Fandango_Prev we have to extract the year from the film column

Fandango_Prev['Year'] = Fandango_Prev['FILM'].str[-5:-1]
print(Fandango_Prev.head(2))
print(Fandango_Prev['Year'].value_counts())
Fandango_2015 = Fandango_Prev[Fandango_Prev['Year'] == '2015'].copy()
print(Fandango_2015.head())
Fandango_2015['Year'] = pd.to_numeric(Fandango_2015['Year'], errors='coerce')

print(Fandango_Post['year'].value_counts())
Fandango_2016 = Fandango_Post[Fandango_Post['year'] == 2016].copy()
print(Fandango_2016.head())

#5. COMPARING DISTRIBUTION SHAPES FOR 2015 AND 2016
#After all these preliminary steps, we can now start analyzing the
#two samples we isolated before. Once again, our goal is to determine whether
#there's any difference between Fandango's ratings for popular movies in 2015
#and Fandango's ratings for popular movies in 2016.

#Generate two kernel density plots on the same figure for the distribution of
#movie ratings of each sample. Customize the graph such that:

#It has a title with an increased font size.
#It has labels for both the x and y-axis.
#It has a legend which explains which distribution is for 2015 and which is for 2016.
#The x-axis starts at 0 and ends at 5 because movie ratings on Fandango start at 0 and end at 5.
#The tick labels of the x-axis are: [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0].
#It has the fivethirtyeight style (this is optional).
#You can change to this style by using plt.style.use('fivethirtyeight').
#This line of code must be placed before the code that generates the kernel density plots.

plt.style.use('fivethirtyeight')

Fandango_2015['Fandango_Stars'].plot.kde(label = '2015', legend = True,
figsize = (8, 5.5))
Fandango_2016['fandango'].plot.kde(label = '2016', legend = True)
plt.title('''Comparing distribution shapes for Fandango's ratings
\n(2015 v. 2016)''', y = 1.07) #y parameter pads title upwards
plt.xlabel('Stars')
plt.xlim(0,5) #Because ratings start at 0 and end at 5
plt.xticks(arange(0,5.1,0.5))
#plt.savefig("Comparing_Fandango_Ratings_2015_2016.png")

#Analyze the two kernel density plots. Try to answer the following:

#What is the shape of each distribution?
#2016 is still left skewed but is much more normally distributed around
#a lower mean of 4.0 instead of 4.5 for 2015.

#If their shapes are similar, is there anything that clearly differentiates them?

#An interesting part of both distributions is that while 2016 is more
#normally distributed than 2015, they both that peaks around the .5
#rating marks (3.5, 4.0, 4.5, etc) which suggests they might still be rounding
#some of the ratings up or down.

#Can we see any evidence on the graph that suggests that there is indeed a change
#between Fandango's ratings for popular movies in 2015 and Fandango's ratings for
#popular movies in 2016?
#It does look like there has been a noticable change in most frequent
#ratings of the Fandango movies from the 2015 sample to the 2016 sample.

#Provided there's a difference, can we tell anything about the direction of the
#difference? In other words, were movies in 2016 rated lower or higher compared to 2015?
#It looks like the bulk average rating of 2016 movies was about .5 lower than in 2015.

#6. COMPARING RELATIVE FREQUENCIES
#The kernel density plots from the previous screen showed that there's a clear difference
#between the two distributions. They also provided us with information about the direction
#of the difference: movies in 2016 were rated slightly lower than those in 2015.

#While comparing the distributions with the help of the kernel density plots was a great start,
#we now need to analyze more granular information.

#TASKS
#Examine the frequency distribution tables of the two distributions

#The samples have different number of movies.
#Does it make sense to compare the two tables using absolute frequencies?

#If absolute frequencies are not useful here, would relative frequencies be of more help?
#If so, what would be better for readability — proportions or percentages?

#Analyze the two tables and try to answer the following questions:

#Is it still clear that there is a difference between the two distributions?
#What can you tell about the direction of the difference just from the tables?
#Is the direction still that clear anymore?

print('2015' + '\n' + '-' * 16) # To help us distinguish between the two tables immediately and
                                # avoid silly mistakes as we read to and fro
print(Fandango_2015['Fandango_Stars'].value_counts(normalize = True).sort_index() * 100)

print('2016' + '\n' + '-' * 16)
print(Fandango_2016['fandango'].value_counts(normalize = True).sort_index() * 100)

#In 2016, very high ratings (4.5 and 5 stars) had significantly lower percentages compared to 2015.
#In 2016, under 1% of the movies had a perfect rating of 5 stars,
#compared to 2015 when the percentage was close to 7%. Ratings of 4.5 were also more popular in 2015 —
#there were approximately 13% more movies rated with a 4.5 in 2015 compared to 2016.

#The minimum rating is also lower in 2016 — 2.5 instead of 3 stars, the minimum of 2015.
#There clearly is a difference between the two frequency distributions.

#For some other ratings, the percentage went up in 2016.
#There was a greater percentage of movies in 2016 that received 3.5 and 4 stars,
#compared to 2015. 3.5 and 4.0 are high ratings and this challenges the direction
#of the change we saw on the kernel density plots.

#7. DETERMINING THE DIRECTION OF THE CHANGE
#We confirmed with the two tables before that there is indeed a clear difference
#between the two distributions. However, the direction of the difference is not as
#clear as it was on the Kernel Density Plots.

#We'll take a couple of summary statistics
#(remember the distinction between sample statistics and population parameters)
#to get a more precise picture about the direction of the difference.
#We'll take each distribution of movie ratings and compute its mean, median, and mode,
#and then compare these statistics to determine what they tell about the direction of the difference.

#We've already learned a bit about these three summary metrics in the pandas course,
#and we'll learn more about them right in the next mission of the next course.
#For now, here are the pandas methods you can use to compute these summary metrics:

#Series.mean()
#Series.median()
#Series.mode()

#TASKS
#Compute the mean, median, and mode for each distribution.
mean_2015 = Fandango_2015['Fandango_Stars'].mean()
print(mean_2015)
median_2015 = Fandango_2015['Fandango_Stars'].median()
print(median_2015)
mode_2015 = Fandango_2015['Fandango_Stars'].mode()[0]
print(mode_2015)

mean_2016 = Fandango_2016['fandango'].mean()
print(mean_2016)
median_2016 = Fandango_2016['fandango'].median()
print(median_2016)
mode_2016 = Fandango_2016['fandango'].mode()[0]
print(mode_2016)

#Compare these metrics and determine what they tell about the direction of the difference.
#What's magnitude of the difference? Is there a big difference or just a slight difference?
summary = pd.DataFrame()
summary['2015'] = [mean_2015, median_2015, mode_2015]
summary['2016'] = [mean_2016, median_2016, mode_2016]
summary.index = ['mean', 'median', 'mode']
print(summary)

#Generate a grouped bar plot to show comparatively how the mean, median, and mode
#varied for 2015 and 2016. You should arrive at a graph that looks similar (not necessarily identical) to this:

plt.style.use('fivethirtyeight')
summary['2015'].plot.bar(color = '#0066FF', align = 'center', label = '2015',
width = .25)
summary['2016'].plot.bar(color = '#CC0000', align = 'edge', label = '2016',
width = .25, rot = 0, figsize = (8,5))

plt.title('Comparing summary statistics: 2015 vs 2016', y = 1.07)
plt.ylim(0,5.5)
plt.yticks(arange(0,5.1,.5))
plt.ylabel('Stars')
plt.legend(framealpha = 0, loc = 'upper center')
plt.savefig("Comparing_summary_stats_of_Fandango_ratings.png")

#The mean rating was lower in 2016 with approximately 0.2.
#This means a drop of almost 5% relative to the mean rating in 2015.

print((summary.loc['mean'][0] - summary.loc['mean'][1]) / summary.loc['mean'][0])

#While the median is the same for both distributions, the mode is lower in 2016 by 0.5.
#Coupled with what we saw for the mean, the direction of the change we saw on the kernel density plot is confirmed:
#on average, popular movies released in 2016 were rated slightly lower than popular movies released in 2015.