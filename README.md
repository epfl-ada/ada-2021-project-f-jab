# Quotes'N'Movies - ADA project (F-JAB)

*OBS: Our milestone3 (final hand-in) is located in the `main.ipynb`-notebook. The `data`-folder used for the project as well as webscraping, filtering of Quotebank, preprocessing and exploratory investigations are located in the `exploratory`-folder. The same holds for plotly plots used on the webpage.*

Data story: https://albertkjoller.github.io/QuotesNMovies/ 

*OBS: We emphasize that the design principle for the data story has been to built a webpage that is understandable to a wide-ranging target group, including both data scientists and grandmothers. All the research backing up our statements are found in the `main.ipynb` or the exploratory investigations.*

*OBS: Our milestone3 is located in the "main.ipynb". Everything in exploratory is data or just that, exploratory notebooks.*
*Our data story can be found via this link: https://albertkjoller.github.io/QuotesNMovies/*

## Abstract

This study aims to investigate the correlation between quotes about movies made by people in news articles, movie IMDB rating and movie box office revenue. Furthermore, we intend to investigate whether some quotes may correlate with daily box office revenue. The quotebank dataset gives us a unique opportunity to investigate this correlation and to speculate how certain quotes may influence the sale of tickets for certain movies. We intend to do a semantic analysis on the quotes and investigate whether the old saying “bad publicity is good publicity” is indeed true. Will opinions of movie critics influence the daily box office revenue or will it not have any influence at all?

This study will hopefully lay the groundwork for further research into how quotes in news articles may influence the actions of the average person or even the other way around. This study will only investigate correlation and not causation.


## Research Questions

We aim at addressing the following 5 main points with provided research questions (RQ):

1) RQ1: Relation between Box Office sales and number of quotes of a movie

	1.1. Linear regression between total number of quotes on a movie and domestic box office revenue

	3.2. Observational study with propensity score matching
	
2) RQ2: An Investigation into Time Series Box Office and Quotes in a Few Movies

	2.1. Initial analysis and Kolmogorov-Smirnov test

	4.2. Checking correlation and Granger causality
	
3) RQ3: Sentiment analysis in quotes about movies over time

	3.1 Sentiment and Box Office

	5.2. Sentiment and IMDb - (WIP)

4) RQ4: Searching for a bias in the data

	4.1. Are quotes in Quotebank regarding movies biased?

	6.2. Bias in Internet Movie Database ratings

5) RQ5: The effect of COVID on media coverage of movies

	5.1. Calculate mean number of quotes on movies between 2015-2019 on a daily basis, calculate confidence intervals (bootstrapping), compare with 2020 data

	7.2. Use regression for comparison of the mean number of quotes across movies in covid and non-covid period, use t-test for comparison of means

## Proposed additional datasets

To be able to answer our research questions we need at least the following two sources:

1) **IMDb movies extensive dataset** from Kaggle (https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset). The data consists of 4 sub-datasets of movie data ranging from 1874-2027 from the IMDb webpage for movies with more than 100 reviews. We use the `movies.csv` and `ratings.csv` data files for analyses in which we can access movie titles, year of release, genre, language, IMDb ratings and age and gender of the voters, also whether the voter is American. We could use RottenTomatoes dataset (referred to at Kaggle) for critics ratings.

2) **Box Office dataset** from BoxOfficeMojo (by IMDb). We've been webscraping and created our own `.csv`-files. By accessing the webpage of a given movie (e.g. Star Wars: https://www.boxofficemojo.com/release/rl3305145857/?ref_=bo_gr_rls) we create a `csv`-file using `BeautifulSoup` containing info such as daily gross from domestic (U.S) movie theater for the full broadcasting period, distributor of the movie and number of theaters where it aired. (see `time_series_box_office_scraping-ipynb`).

3) **WikiData** - this relational database is used for mapping additional information to the Quotebank data. We will use it to deal with speakers (such as searching for their quote-ID's and mapping gender information to the quotes.


Since the Box Office data is domestic from the U.S. and since we have access to determining whether IMDb ratings are from U.S or non U.S. voters, we will restrict ourselves to look at movie data with all relevant domestic attributes are restricted to the U.S..


## Methods
The repository has all auxiliary scripts and notebook in the `exploratory` directory. The final story is told in `milestone3.ipynb`.

We filter the Quotebank data to match the top 10 movies per year based on box office revenue (`Quotebank_filter.ipynb`).  For the analysis of sentiments and box office, we decided to use top 10 movies per year. We tried filtering on top 50 movies and visualized the accumulated number of quotes per movies. We observed that after our chosen threshold (top 10) there were significantly less than 500 quotes/movie/year, meaning approximately 1-2 quotes per day per movie, which would make our time series analysis biased. 

We run the Quotebank data through cleaning and preprocessing (`Quotebank_preprocess.ipynb`). We do an exploration of sentiment analysis approaches in `Quotebank_sentiment.ipynb`. Also, we explore the quotes and the IMDb dataset (`IMDb_investigation.ipynb`). The Box Office data is scraped from the web (`BoxOffice_webscrape.ipynb`) and reformatted to a data frame in `BoxOffice_preprocess.ipynb`. It is investigated in `BoxOffice_investigation.ipynb`. 

For subtasks (RQs) we did the following investigations:

RQ1:
- Linear regression between total number of quotes on a movie and domestic box office revenue.
- Checking correlation between distribution of quotes over time and box office time series data.
- Observational study with propensity score matching: calculate propensity score with logistic regression, based on movie attributes on IMDb data on few quote vs many quote movies and compare the results with box office data.

RQ2:
- Pick similarly budgeted movies released close to each other, investigate how distribution of quotes and box office data evolves over time.
- Fit Vector Autoregression models to time series of box office and number of movies, do time series analysis and apply Granger causality test to determine casual effects.

RQ3:
- Apply different sentiment scores (with various complexity) to the data and investigate the better approach (AFINN, VADER (lexicons) and BERT (transformer))
- Analyse time series by using a smoothness filter or moving average on the sentiment. Visualize accumulated sentiment score across time. 
- Sentiment of quote related to domestic box office revenue: similarly to RQ1.
- Create comparison metric between IMDb rating and sentiment in quote and do linear regression to see if there's a mapping.
- Fit Vector Autoregression models to time series of box office and daily sentiment score, do time series analysis and apply Granger causality test to determine casual effects

RQ4:
- Extract genders from Wikidata and investigate BERT score distributions of movies, check if there are biased movies 
- Search for IMDb rating bias with linear regression, t-test for comparison of male and female votes, check influence of generations on movie ratings


RQ5:
-  Calculate mean number of quotes on movies between 2015-2019 on a daily basis, calculate confidence intervals (bootstrapping), compare with 2020 data
-  Use regression for comparison of the mean number of quotes across movies in covid and non-covid period, use t-test for comparison of means.

## Organization within the team

- Albert: Preprocessing of quotes and Box Office, sentiment analysis, investigation of RQ3, Preparing Data Story website.
- Felix: Webscraping of Box Office data, Investigation of RQ2, Preparing Data Story website.
- Julian: Filtering of Quotebank, investigation of RQ4, Loading and Processing of wikidata parquet files
- Benedek: Investigation of RQ1 and RQ3, Researched Time Series Analysis Methods for RQ2 & RQ3.
