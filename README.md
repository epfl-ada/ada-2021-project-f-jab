# Moviez - ADA project

*OBS: Our milestone3 is located in the "main.ipynb". Everything in exploratory is data or just that, exploratory notebooks.*

## Abstract

This study aims to investigate the correlation between quotes about movies made by people in news articles, movie IMDB rating and movie box office revenue. Furthermore, we intend to investigate whether some quotes may correlate with daily box office revenue. The quotebank dataset gives us a unique opportunity to investigate this correlation and to speculate how certain quotes may influence the sale of tickets for certain movies. We intend to do a semantic analysis on the quotes and investigate whether the old saying “bad publicity is good publicity” is indeed true. Will opinions of movie critics influence the daily box office revenue or will it not have any influence at all?

This study will hopefully lay the groundwork for further research into how quotes in news articles may influence the actions of the average person or even the other way around. This study will only investigate correlation and not causation.


## Research Questions

We aim at addressing the following 5 main points with provided research questions (RQ):

1) RQ1: Relation between Box Office sales and number of quotes of a movie
	1.1. Linear regression between total number of quotes on a movie and domestic box office revenue
	1.2. Observational study with propensity score matching
	
2) RQ2: An Investigation into Time Series Box Office and Quotes in a Few Movies
	2.1. Initial analysis and Kolmogorov-Smirnov test
	2.2. Checking correlation and Granger causality
	
3) RQ3: Sentiment analysis in quotes about movies over time
	3.1 Sentiment and Box Office
	3.2. Sentiment and IMDb - (WIP)

4) RQ4: Searching for a bias in the data
	4.1. Are quotes in Quotebank regarding movies biased?
	4.2. Bias in Internet Movie Database ratings

5) RQ5: The effect of COVID on media coverage of movies
	5.1. Calculate mean number of quotes on movies between 2015-2019 on a daily basis, calculate confidence intervals (bootstrapping), compare with 2020 data
	5.2. Use regression for comparison of the mean number of quotes across movies in covid and non-covid period, use t-test for comparison of means

## Proposed additional datasets

To be able to answer our research questions we need at least the following two sources:

1) **IMDb movies extensive dataset** from Kaggle (https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset). The data consists of 4 sub-datasets of movie data ranging from 1874-2027 from the IMDb webpage for movies with more than 100 reviews. We use the `movies.csv` and `ratings.csv` data files for analyses in which we can access movie titles, year of release, genre, language, IMDb ratings and age and gender of the voters, also whether the voter is American. We could use RottenTomatoes dataset (referred to at Kaggle) for critics ratings.

2) **Box Office dataset** from BoxOfficeMojo (by IMDb). We've been webscraping and created our own `.csv`-files. By accessing the webpage of a given movie (e.g. Star Wars: https://www.boxofficemojo.com/release/rl3305145857/?ref_=bo_gr_rls) we create a `csv`-file using `BeautifulSoup` containing info such as daily gross from domestic (U.S) movie theater for the full broadcasting period, distributor of the movie and number of theaters where it aired. (see `time_series_box_office_scraping-ipynb`).


3) **Google-Trends-API** If we need further insight into how the hype around a movie evolved over time, we can pull the historical, hourly distribution of Google Search Querys about the movie title from the Google-Trends-API via pytrends (https://pypi.org/project/pytrends).


Since the Box Office data is domestic from the U.S. and since we have access to determining whether IMDb ratings are from U.S or non U.S. voters, we will restrict ourselves to look at movie data with all relevant domestic attributes are restricted to the U.S..

## Methods

We filter the Quotebank data to match the top 10 movies per year based on box office revenue. (`filter_quotes.ipynb`). We run the Quotebank data through cleaning and preprocessing (`preprocessingQuotebank.ipynb`). We do a sentiment analysis in `sentiment.ipynb`. Finally we explore the quotes and the imdb dataset (`movies.ipynb`).

For subtasks (RQs) we plan to do the following:

RQ1:
- Linear regression between total number of quotes on a movie and domestic box office revenue.
- Checking correlation between distribution of quotes over time and box office time series data.
- Propensity score matching: calculate propensity score with logistic regression, based on movie attributes on IMDb data on few quote vs many quote movies and compare the results with box office data.

RQ2:
- Create a naive and simple sentiment model based on sentiment scores using Afinn sentiment lexicon and analyse time series by using a smoothness filter or moving average. Define a metric that normalizes the sentiment score with regards to the length of a quote.
- Find a more clever and complex sentiment prediction model that incorporates semantic relations between words in quotes.
- Sentiment of quote related to domestic box office revenue: similarly to RQ1.
- Create comparison metric between IMDB rating and sentiment in quote and do linear regression to see if there's a mapping.

RQ3:
- Pick similarly budgeted movies released close to each other, investigate how distribution of quotes and box office data evolves over time.
- Do Chi-square test of independence on the box office and quotes separatly.

RQ4:
- Do observational study where a certain "bias"-parameter is investigated from matching e.g. actors or movies on the remaining available data. (e.g. investigate whether Thriller and Action differ in rating) 
- Use latent analysis like PCA and reduce dimensionality to 2D for visual inspection.

RQ5:
-  Calculate mean number of quotes on movies between 2015-2019 on a daily basis, calculate confidence intervals (bootstrapping), compare with 2020 data
-  Use regression for comparison of the mean number of quotes across movies in covid and non-covid period, use t-test for comparison of means.


Eventually: implement "WhoSaidIt!" as a fun interactive feature (simply do a document search using some t.b.d. information retrieval method such as cosine distance.
	

## Proposed timeline

- Investigate RQ1 & RQ2 (by Nov 26)
- Investigate RQ3, RQ4 & RQ5 (by Dec 3)
- Discuss results and possible improvements (by Dec 5)
- Finalize notebook (by Dec 10)
- Create Jekyll website, present data story (by Dec 15)
- Check & submit (by Dec 17)


## Organization within the team

- Decide the main topic of our project, hypothesize and propose possible interesting questions 
- Find dataset on movies and their attributes
- Find box office time series data
- Build scraping pipeline for box office data
- Explore IMDb dataset, extract relevant movie titles in order to filter the Quotbank data
- Descriptive data analysis on IMDb dataset including plots
- Load the relevant quotes from Quotebank
- Explore the Quotes
- Find NLP model and try sentiment analysis on quotes, validate whether the model works

## Questions for TAs 

1) Related to RQ2.2 - is linear regression a suitable approach for comparing IMDb ratings to sentiment about movies?
