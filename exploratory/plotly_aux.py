import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm.notebook import tqdm
import plotly.express as px
import plotly.io as pio


#inspiration taken from this approach: https://towardsdatascience.com/how-to-produce-an-animated-bar-plot-in-plotly-using-python-2b5b360492f8


def wrangleData(df, time_attribute='year-month'):
    #Creating numerical movie keys
    keys = [i for i in range(df['movie'].unique().__len__())]

    # create sub-dataframes for each movie sorted by the time index
    all_dataframes = {}
    for i, movie in zip(keys, df['movie'].sort_values().unique()):
        df_temp = df[df['movie'] == movie].sort_values(time_attribute, ascending=True)
        all_dataframes[i] = df_temp
    
    # concatenating all sub-dataframes to a single dataframe
    concat_df = []
    for i in all_dataframes:
        concat_df.append(all_dataframes[i])

    df_wrangled = pd.concat(concat_df)
    
    return df_wrangled


def createPlotDF(df_all, attribute, y_label, dataset='boxOffice', time_attribute='year-month', N_samples=10, replace=True):
    """ takes as input; a dataframe, the attribute, time-attribute we investigate name we wish to investigate as well as
    number of movies in the subsample and whether it should be done with replacement or not.
    
    return as a dataframe containing (sorted) movie title for all time indeces (i.e. year-month) as well as 
    the mean sentiment related to that movie in that time slot. This mean score is forced to zero if no quotes
    about a movie in the given time-index are found.
    """
    
    # selecting sub-sample if 'N_samples' argument is passed
    if N_samples == None:
        df_sample = df_all
    else:
        selected_movies = df_all['movie'].sample(N_samples, replace=replace).values.tolist()
        df_sample = df_all[df_all['movie'].isin(selected_movies)]
    
    df_plot = {}
    i = 0
    
    # creating data frame for visualization
    for movie in tqdm(df_sample.movie.unique()):
        acc_mean = 0
        for time_idx in df_sample[time_attribute].sort_values().unique():
            # checking whether movie/time-index pair exists in dataframe
            condition = np.logical_and(df_sample[time_attribute] == time_idx, df_sample['movie'] == movie)

            if condition.sum() == 0: # if movie and time-index does not occur together
                acc_mean += 0 
                
            else: # when movie and time-index occur together, mean the specified scores from that time-index
                if dataset == 'Quotebank': # multiplies daily sentiment by number of Occurences of the quote.
                    acc_mean += (df_sample[condition][attribute] * df_sample[condition]['numOccurrences']).sum()
                else:
                    acc_mean += df_sample[condition][attribute].sum()
            
            # add values to dataframe for plotting
            df_plot[i] = [time_idx, movie, acc_mean]
            i += 1
    
    # creating dataframe and specifying column names
    df_plot = pd.DataFrame(df_plot).T
    df_plot.columns = [time_attribute, 'movie', f'Accumulated {y_label}']

    return df_plot, df_sample


def animatedBarPlot(df_plot, y_label, title, time_attribute='year-month', speed=0.2, save_fig=True):
    """ 
    speed must be between 0 and 1 where 1 is not included.
    """

    # finds lower and upper bound of plotly plot
    upper = df_plot[f'Accumulated {y_label}'].max()
    lower = df_plot[f'Accumulated {y_label}'].min()
    range_x = [np.round(lower + 0.05*lower), np.round(upper + 0.05*upper)]

    # makes the plotly object
    fig = px.bar(df_plot,
                 x=f'Accumulated {y_label}',
                 y='movie',
                 orientation='h',
                 animation_frame=time_attribute,
                 color="movie",
                 animation_group="movie",
                 range_x=range_x,
                 title=title)

    # changes the speed
    fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = (1-speed) * 1000
    fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = (1-speed) * 1000
    fig.update_yaxes(categoryorder="total ascending") # found command for ascending here: https://community.plotly.com/t/plotly-express-histogram-any-way-to-sort-bar-by-value/23905/2
    #fig.update_yaxes(automargin=False)
    fig.update_layout(showlegend=False)
    
    fig.show()

    if save_fig:
        filename = f"{y_label} - {time_attribute} - {len(df_plot.movie.unique())}"
        plot_dir = os.getcwd() + os.sep + 'plotlyplots'
        pio.renderers.default = 'browser'
        pio.show(fig)
        fig.write_html(rf"{plot_dir}{os.sep}{filename}.html")

        print(f"saved html version of plot to: {plot_dir}")
        
    return fig
