# Moviez - ADA project

## Abstract

```A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?```


## Research Questions

```A list of research questions you would like to address during the project.```

We aim at addressing the following 3-4 main points with provided research questions (RQ):

1) Relation between Box Office sales and number of quotes of a movie.
	- RQ1: *Is there a tendency between number of sold tickets and the 'hype' about a movie as it appears in the news paper media?*
	
2) Sentiment analysis in quotes about movies over time. Additionaly relate sentiment to Box Office sales and see if positive/negative media coverage affect the sale of tickets.
	- RQ: *Does the media/quoters opinion on a certain movie affect the amount of sold tickets?*
	- RQ: *Does the sentiment seen in quotes relate to the rating on IMDB?*
	
3) Analyze interdependencies between movies.
	- RQ: *How does the premiere dates and "public" opinion on a movie and its sales interfere with the sales of another movie and its premiere data?*

4) (Maybe:) Interpret if there is a bias in the data
	- RQ: *Is there a bias within the quotes and sentiment or rating of a movie and the gender, ethnicity, etc.?*
	

## Proposed additional datasets

```List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible.```

To be able to answer our research questions we need at least two additional datasets: one that contains information about movies, their release date and IMDb ratings 
and a second one containing information about box office sales. So far we've found the following two sources, that suits our needs:

1) **IMDb movies extensive dataset** that is publicly available on Kaggle (https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset). The data consist of 4 sub-datasets of movie data ranging from 1874-2027 scraped from the IMDb webpage for movies with more than 100 revies. As a first thought, we are interested in using the `movies.csv` and `ratings.csv` data files for analyses in which we can access movie titles, year of release, genre, language as well as the IMDb ratings and information about age and gender of the voters. One of the attributes further describes whether the voter is American or not, which becomes important when linking the data with our second dataset. As the Quotebank data we are provided with ranges from 2015 to 2020 we will restrict the IMDb data in this period as well, meaning a significant decrease in size of the IMDb dataset. Eventually, we could use the RottenTomatoes dataset (referred to at the Kaggle page) for more valid rating of a movie is provided as the critics ratings are encountered as well.


2) **Box Office dataset** from Box Office Mojo (by IMDb). No current self-containing data files exists so we've been webscraping and created our own `.csv`-files. By accessing the webpage of a given movie (i.a. Star Wars: https://www.boxofficemojo.com/release/rl3305145857/?ref_=bo_gr_rls) we create a `csv`-file using `BeautifulSoup` containing info such as daily gross from domestic (U.S) movie theater for the full broadcasting period, distributor of the movie and number of theaters where it aired. Some dates hold additional information of whether cinemas were affected by COVID, holidays, etc. that might come in handy for further analyses. The size of the data grows linearly with the amount of desired movies to be investigated, which might restrict us to focusing on determined movies, like the Top 10 in terms of gross within a given period.


Since the Box Office data is domestic from the U.S. and since we have access to determining whether IMDb ratings are from U.S or non U.S. voters, we will restrict ourselves to look at movie data with all relevant domestic attributes are restricted to the U.S..

## Methods

General: filter Quotebank data based on certain conditions (i.e. movie title included in quote, etc.). For subtasks (research questions) we will have to further filter the data. We prefer doing this in several steps to not lose data that is compatible with the conditions of one subtask even though it is not compatible with another subtask.



RQ1: Simply linear regression?

RQ2.1: 	
- Afinn sentiment lexicon with smoothing over time (moving average)
- Create a comparison metric between IMDB rating and sentiment in quote
- Simple linear regression? (important: same modeling as first RQ about Box Office/quotes relation!)

RQ2.2



RQ4: Look at movie plots and actors of a movie and relate this to the above RQ's. Maybe use latent analysis like PCA and reduce dimensionality to 2D for visual (simple) inspection.
	


Eventually implement this as a fun interactive feature!
- WhoSaidIt! - Interactive setting of speaker/movie relation. By entering a quote or statement about a movie, a speaker who is most likely to have said it will be returned.
	

## Proposed timeline

- Descriptive statistics before hand-in of Milestone 2

## Organization within the team
```A list of internal milestones up until project Milestone 3.```

## Questions for TAs 
```(optional) Add here any questions you have for us related to the proposed project.```
