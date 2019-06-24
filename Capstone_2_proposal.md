# Analyzing and Clustering/Predicting “Fad” Diets Sentiment

## Project Description
Sentiment analysis of “fad” diet tweets using NLP. The diets studied are: 'keto','whole30','glutenfree','mediterraneandiet','lowfat', 'atkins', 'paleo', 'celeryjuice'.

## Approach and Data Sources
I am collecting data using the Twitter developer API by streaming tweets containing selected diets as keywords. This is the same approach as Capstone #1 but I have been collecting more data for Capstone #2.

My initial thought which launched this project was to be able to determine which fad diet is most effective. This, of course, is complicated. Taking a step back, my broad goal is to provide insight about each diet.

Step 1: I can conduct NLP in several ways:
Apply NLP techniques learned during lecture
re-use WIT.ai as I did in Capstone #1. Look into Fasttext (from facebook).
During break week I played around using AWS which leverages S3, EC2 and Amazon Kinesis Firehouse and AWS Lambda to perform sentiment analysis all on AWS. However, I’m not sure if this is permissible and in the confines of the capstone requirements since everything is done through AWS. (Hamid/Flora, [please provide your thoughts on this!) (https://aws.amazon.com/blogs/machine-learning/build-a-social-media-dashboard-using-machine-learning-and-bi-services/)

Step 2: Machine Learning:
Base goal: Do unsupervised learning. Cluster groups based on tweets. Use unsupervised neural networks using auto-encoder, latent dirichlet allocation (LDA)
Stretch goal: Combine twitter data aggregated to the county or state level and add as a feature to predict an outcome like cardiovascular disease. This question will answer: Does a county or state’s sentiment (average of sentiment score?) of tweets regarding fad diets improve prediction. Basically I would add sentiment as a feature in CDC data and see if it improves prediction.
-Or-
What about this!: Map tweets by location (counties) to census data and predict the fad diet popularity and sentiment for a county even if we don't have tweets coming from that county. The practical application is being able to identify which diets are popular in a given area. This can help with with grocery store purchases and marketing.

## Purpose
My background is in nutrition and nutrition research. When I bring this up one of the first questions I always get is, “What do you think about <insert fad diet>. One limitation of traditional nutrition research is that they take a big investment in money and time, involve human subjects, and also can’t keep up with trends.

Measuring sentiment on social media is the next frontier of guiding research. From a public health perspective, we can invest dollars into diets that are making a big impact or showing signs of promise or use sentiment as a predictor. From a marketing perspective, companies can glean insights on what consumers are interested in.
