# ada-2021-project-f-jab
ada-2021-project-f-jab created by GitHub Classroom


### Data story
RQ = Research Question

Relation between Box Office sales and number of quotes about a certain movie
	- RQ: "Is there a tendency between number of sold tickets and the 'hype' about a movie in the media?"
	- How: 
		○ Simple linear regression?

Analyze sentiment in quotes about movies over time
	- More: Relate sentiment to Box Office sales and see if quotes in media affect sales of tickets
	- RQ: "Does the media/quoters opinion on a certain movie affect the amount of sold tickets?"
	- RQ: "Does the sentiment seen in quotes relate to the rating on IMDB?"
	- How: 
		○ Afinn sentiment lexicon with smoothing over time (moving average)
		○ Create a comparison metric between IMDB rating and sentiment in quote
		○ Simple linear regression? (important: same modeling as first RQ about Box Office/quotes relation!)

Analyze interdependencies between movies
	- RQ: "How does the premiere dates and "public" opinion on a movie and its sales interfere with the sales of another movie and its premiere data?"
	- How: ?

WhoSaidIt! - Interactive setting of speaker/movie relation
	- What: by entering a quote or statement about a movie, a speaker who is most likely to have said it will be returned.
	- Why:
		○ Fun feature
		○ ?????

(Maybe:) Interpret if there is a bias in the data
	- RQ: "Is there a bias within the quotes and sentiment or rating of a movie and the gender/ethnicity/(anything else?)?"
	- How:
		○ Look at the plots and actors of a movie and relate this to the above RQ's.
