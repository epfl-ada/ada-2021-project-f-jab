# Moviez - ADA project

## Abstract

This study aims to investigate the correlation between quotes about movies made by people in news articles, movie IMDB rating and movie box office revenue. Furthermore, we intend to investigate whether some quotes may correlate with daily box office revenue. The quotebank dataset gives us a unique opportunity to investigate this correlation and to speculate how certain quotes may influence the sale of tickets for certain movies. We intend to do a semantic analysis on the quotes and investigate whether the old saying “bad publicity is good publicity” is indeed true. Will opinions of movie critics influence the daily box office revenue or will it not have any influence at all?

This study will hopefully lay the groundwork for further research into how quotes in news articles may influence the actions of the average person or even the other way around. This study will only investigate correlation and not causation.


## Research Questions

We aim at addressing the following 4-5 main points with provided research questions (RQ):

1) Relation between Box Office sales and number of quotes of a movie.
	- RQ1: *Is there a tendency between number of sold tickets and the 'hype' about a movie as it appears in the news paper media?*
	
2) Sentiment analysis in quotes about movies over time. Additionaly relate sentiment to Box Office sales and see if positive/negative media coverage affect the sale of tickets.
	- RQ2.1: *Does the media/quoters opinion on a certain movie affect the amount of sold tickets?*
	- RQ2.2: *Does the sentiment seen in quotes relate to the rating on IMDB?*
	
3) Analyze interdependencies between movies.
	- RQ3: *How does the premiere dates and "public" opinion on a movie and its sales interfere with the sales of another movie and its premiere data?*

4) (Maybe:) Interpret if there is a bias in the data
	- RQ4: *Is there a bias within the quotes and sentiment or rating of a movie w.r.t gender, ethnicity, etc.?*

5) (Maybe:) Movies vs Series With the rise of Netflix, TV Series became an extremely popular source of entertainment
	- RQ5: *Are the most popular series or movies quoted more frequently on average, is the difference significant?*
	

## Proposed additional datasets

To be able to answer our research questions we need at least two additional datasets: one that contains information about movies, their release date and IMDb ratings and a second one containing information about (daily) box office sales. We've found the following two sources, that suit our needs:

1) **IMDb movies extensive dataset** that is publicly available on Kaggle (https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset). The data consist of 4 sub-datasets of movie data ranging from 1874-2027 scraped from the IMDb webpage for movies with more than 100 reviews. As a first thought, we are interested in using the `movies.csv` and `ratings.csv` data files for analyses in which we can access movie titles, year of release, genre, language as well as the IMDb ratings and information about age and gender of the voters. One of the attributes further describes whether the voter is American or not, which becomes important when linking the data with our second dataset. As the Quotebank data we are provided with ranges from 2015 to 2020 we will restrict the IMDb data in this period as well, meaning a significant decrease in size of the IMDb dataset. Eventually, we could use the RottenTomatoes dataset (referred to at the Kaggle page) for more valid rating of a movie is provided as the critics ratings are encountered as well.


2) **Box Office dataset** from Box Office Mojo (by IMDb). No current self-containing data files exists so we've been webscraping and created our own `.csv`-files. By accessing the webpage of a given movie (i.a. Star Wars: https://www.boxofficemojo.com/release/rl3305145857/?ref_=bo_gr_rls) we create a `csv`-file using `BeautifulSoup` containing info such as daily gross from domestic (U.S) movie theater for the full broadcasting period, distributor of the movie and number of theaters where it aired. Some dates hold additional information of whether cinemas were affected by COVID, holidays, etc. that might come in handy for further analyses. The size of the data grows linearly with the amount of desired movies to be investigated, which might restrict us to focusing on determined movies, like the Top 10 in terms of gross within a given period. For more specifics on the procedure, see `time_series_box_office_scraping-ipynb`.


3) **Google-Trends-API** If we need further insight into how the hype around a movie evolved over time, we can pull the historical, hourly distribution of Google Search Querys about the movie title from the Google-Trends-API via pytrends (https://pypi.org/project/pytrends).


Since the Box Office data is domestic from the U.S. and since we have access to determining whether IMDb ratings are from U.S or non U.S. voters, we will restrict ourselves to look at movie data with all relevant domestic attributes are restricted to the U.S..

## Methods

First, we filter the Quotebank data to match certain criteria. We look for substrings containing movie titles, restricting ourselves to the top 10 movies per year based on box office revenue. See `filter_quotes.ipynb` for more info. Next we run the Quotebank data through an extensive cleaning and preprocessing (`preprocessingQuotebank.ipynb`). We do a sentiment analysis on the quotes in `sentiment.ipynb`. Finally we explore the filtered quotes and the imdb dataset in `movies.ipynb`.

For subtasks (RQs) we will have to further filter the data. We prefer doing this in several steps to not lose data that is compatible with the conditions of one subtask even though it is not compatible with another subtask. We plan to do the following per subtask:

RQ1:
- Linear regression between the total number of quotes on a movie and domestic box office revenue.
- Checking correlation between the distribution of quotes over time and box office time series data.
- Propensity score matching: calculate propensity score with logistic regression, based on movie attributes on IMDb data on few quote vs many quote movies and compare the results with box office data.

RQ2:
- Assign sentiment scores using Afinn sentiment lexicon and analyse time series by using a smoothness filter or moving average.
- RQ2.1 of sentiment of quote related to domestic box office revenue will be done similarly to the linear regression in RQ1.
- Create a comparison metric between IMDB rating and sentiment in quote and do linear regression to see if there's a mapping between the two.

RQ3:
- Pick similar budget movies released close to each other and investigate how to distribution of quotes and the box office data evolves in time.
- Do Chi-square test of independence on the box office and quotes separatly.

RQ4:
- Do an observational study where a certain "bias"-parameter is investigated from matching i.a. actors or movies on the remaining available data. For instance we could investigate whether Thriller or Action differ in rating/sentiment score by mathcing based on distribution of number of quotes, etc.. 
- Ise latent analysis like PCA and reduce dimensionality to 2D for a simple visual inspection.

RQ5:
-  Calculate the mean number of quotes on movies and series on a daily basis and calculate confidence intervals with bootstrapping.
-  Use regression for comparison of the mean number of quotes across movies and series, use t-test for compariosn of means.


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
