# Analyzing the Popularity and Attitudes of “Fad” Diets.

## Project Description:
Analyzing tweets mentioning “fad” diets over Memorial Day weekend by assessing their popularity and analyzing sentiment. The diets studied are: keto, paleo, gluten-free, Whole30, low-fat, and Mediterranean.

## Motivation:
My background is in nutrition and nutrition research. When I bring this up one of the first questions I always get is, “What do you think about <insert fad diet>. One limitation of traditional nutrition research is that they take a big investment in money and time, involve human subjects, and also can’t keep up with trends.

Measuring sentiment on social media is the next frontier of guiding research. From a public health perspective, we can invest dollars into diets that are making a big impact or showing signs of promise. From a marketing perspective, companies can glean insights on what consumers are interested in.

## Pipeline and EDA:
Collect tweets filtering on diet keywords (i.e. “keto) and store as JSON in a text file (twitter_data.txt)
Read in the data as a Pandas DataFrame. Notice that there are “parent” and “child” variables (i.e. within ‘user’ there are sub-variables. Also note that ‘favorite_count’ and ‘retweet_count’ is 0! This is because tweets were collected as they streamed in. We will deal with this later.
Explore ‘user’ child variables. The top ‘location’ tweeted from is the US (n=302), London (135) and Seattle (125). Cool! RandySolares was the top tweeter, tweeting 122 times about keto over the weekend. How prolific! Very few tweets (398 out of 13,000) have place location. Maybe people are more aware of their privacy these days.
	![image](images/Top_locations.png)
![image](images/top_users.png)
Subset the data for only english tweets since I am not as well-versed with cultural and language differences pertaining to fad diets. Also, the sentiment analysis must be done in English. This takes the data from 13,000 to 9,953 tweets.
Perform more EDA. Plot the popularity of the diets. Keto is by far the most mentioned diet, followed by paleo, gluten-free and Whole-30. I would have thought Whole30 would have been higher because #Whole30 is an official hashtag and backed by a company.
I used “lost” as a keyword proxy for weight-loss (i.e. someone will say “I lost 30 lbs on keto) and “start” as a keyword proxy for starting a diet (i.e. “I started keto today). The trend of keto, followed by paleo, being the most popular persists. Interestingly, Whole30 was the next most popular over gluten-free. Maybe more people are starting Whole30 and losing weight with Whole30 compared to gluten-free which is not as “trendy”, sometimes medically necessary, and not generally for weight-loss.
![image](images/Popularity_of_fad_diets.png)
Next it is time to deal with retweets. These are indicated by the tweet starting with “RT”. Again, keto followed by paleo is the most retweeted. We want to remove retweets because we only want to analyze the sentiment on original tweets. This leaves us with 5,683 tweets.
Conduct sentiment analysis using Wit.AI (bought by Facebook).
Pip install Wit in the terminal.
Perform more cleaning. We want to deduplicate exact tweets (Note: I tested the analyzer with url’s and handles and these did not affect the score). Now there are 5,674 tweets.
Output a csv file containing only the ID and the tweet on each line with a header of “0, 1” ( tweet_diet_sentiment.csv). This is what we feed into the sentiment analyzer.
Run through the analyzer. The output is a confidence number (how confident the analyzer was assigning it a value) and a value (positive, negative, neutral). Output the results as a csv (outputs/tweet_diet_sentiment_result.csv)
Once we have confidence numbers and values for every tweet, time to do some more EDA! Looking at the number of positive, negative and neutral tweets, keto has the most tweets as expected.
	![image](images/keto_diet_sentiment.png)
But looking at the percentage, it appears that gluten-free has the greatest percentage of positive tweets. It also seems like people are very neutral about lowfat diet. Time for some hypothesis testing!
![image](images/Percent_Values_Tweets_by_Diet.png)

## Hypothesis Testing
### Hypothesis test 1
Since the Keto diet appears to be so popular, let’s test if positive tweets about the keto diet are more confidently positive. H0: Positive keto tweets are no more confidently positive than positive tweets about other diets. H1: Positive keto tweets are more confidently positive than positive tweets about other diets.
Scatter plot of confidence of positive keto tweets vs. other positive diet tweets. The mean confidence of other tweet are higher!
![image](images/images/Confidence_of_Pos_Keto.png)
Perform Welch’s T-Test
Welch Test Statistic: -3.65
Degrees of Freedom for Welch's Test: 2164.32
p-value for different average confidence: 0.00
p-value for positive Keto tweet confidence average greater than other diets: 1.000
Perform U-Test: p-value = 1.
Turn values into a binomial distribution and perform a two sample approximate test of population proportions.
Conclude - No difference! This is not surprising after examining the scatter plot

### Hypothesis test 2
From step 8 we noticed that gluten-free has the greatest percentage of positive tweets and no negative tweets. Let’s see if Gluten-Free tweets are more confidently positive than positive tweets about other diets. Following the same steps as Hypothesis Test 1, step 4, I get a p-value of < 0.001

###Hypothesis test 3
As part of the EDA process I noticed that negative tweets had lower confidence than positive tweets. I tested to see if there was a difference using Welch’s and p<.001. Positive tweets have a significantly higher mean confidence than negative tweets.
![image](images/Confidence_box_plots.png)
![image](images/Confidence_of_Pos.png)


## Conclusions
In terms of popularity, the Keto diet is by far the most mentioned diet over Memorial Day weekend. This is followed by paleo, gluten-free then Whole30. There were barely any mentions of the Mediterranean diet (considered a “gold-standard” of diets), and low-fat diets (whose time has may passed due to recent research refuting its benefits).

Positive tweets about keto were no more confidently positive than tweets about other diets. When people are tweeting positively about keto they may not be doing so more enthusiastically than other diets. This suggests that although keto is the most popular the enthusiasm is not greater than other diets. However, positive tweets about gluten-free diet is more enthusiastic. One explanation is that people on gluten-free diets do so to address a specific problem (i.e. an allergy to gluten) and the effect of going on this diet is more dramatic and reflected in the enthusiasm of the tweet.

Positive tweets are more confidently classified as positive than negative tweets. This may be a function of the Wit.AI analyzer being better at identifying positive tweets.

## Next Steps:
The tweets were collected over a very limited and specific time - over Memorial Day weekend. After filtering out retweets and non-english tweets, the sample was a quarter of the size. Clearly, to perform more meaningful analysis more tweets will need to be captured. This should be done using AWS and Spark to better learn these data science skills.  
Dealing with retweets by matching on “RT” took time and was clunky. Capturing tweets with retweet_count will be easier for next time.
I only looked at tweets but not extended tweets. I did not realize this until I was too far into the project.
I used Wit.ai as a “black-box.” To better understand the sentiment analysis I will need to understand the process and perhaps explore other tools. Wit.ai only returns one value (positive, neutral, negative) and a confidence value which measures how confident the designation is.  More robust output will give me more dimensions to analyze.
I intend on continuing to exploring this topic. I will need to refine the fad diets I am examining (i.e. maybe drop low fat and Mediterranean) and perhaps add celery juice, which has been getting a lot of buzz the last year. I also want to be able to use geo-location data (which my data didn’t capture) and relate this do county-level health outcomes from CDC, NHANES, or USDA data.
