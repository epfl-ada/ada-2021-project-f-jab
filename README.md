# Moviez - ADA project

## Abstract

```A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?```


## Research Questions

```A list of research questions you would like to address during the project.```

In this project we aim at addressing the following 4-5 main points. Each of them has 1-2 research questions (RQ) that we aim at answering:

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

1) **IMDb movies extensive dataset** that is publicly available on Kaggle. The dataset consists of movie data ranging from 1874-2027.


## Methods

RQ1: Simply linear regression?

RQ2.1: 	- Afinn sentiment lexicon with smoothing over time (moving average)
		- Create a comparison metric between IMDB rating and sentiment in quote
		- Simple linear regression? (important: same modeling as first RQ about Box Office/quotes relation!)

RQ2.2



RQ4: Look at movie plots and actors of a movie and relate this to the above RQ's. Maybe use latent analysis like PCA and reduce dimensionality to 2D for visual (simple) inspection.
	


Eventually implement this as a fun interactive feature!
- WhoSaidIt! - Interactive setting of speaker/movie relation. By entering a quote or statement about a movie, a speaker who is most likely to have said it will be returned.
	

## Proposed timeline

## Organization within the team
```A list of internal milestones up until project Milestone 3.```

## Questions for TAs 
```(optional) Add here any questions you have for us related to the proposed project.```
