# plotter.py
# Written by Gen Blaine
# Started Oct. 15, 2024
# This file takes a csv with opinion polling for elections. The program then uses LOESS filtering to produce estimates
# over time. 
import sys
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd
from colour import Color
import random
import numpy as np

# taken from https://stackoverflow.com/questions/42876366/check-if-a-string-defines-a-color
# but I added a 'u' because I am not a fatass American.
def check_colour(colour):
    try:
        # Converting 'deep sky blue' to 'deepskyblue'
        colour = colour.replace(" ", "")
        Color(colour)
        # if everything goes fine then return True
        return True
    except ValueError: # The color code was not found
        return False
    
def generate_random_colour(given_colours):
    r = random.random() 
    b = random.random() 
    g = random.random() 
    
    colour = (r, g, b)
    if (colour in given_colours):
        return generate_random_colour(given_colours)
    else:
        return colour

def main():
    filename1 = sys.argv[1]
    poll_data = pd.read_csv(filename1, sep=',', header=0, index_col=0)
    loess_smoothed = {}
    
    poll_data = poll_data.sort_index()
    parties = list(poll_data)

    # find the length of the dataframe to determine what the frac should be
    # and the size of the horizontal on the matplotlib
    number_of_rows = len(poll_data.index)
    if (number_of_rows <= 40): # very small dataset
        frac=0.35
        x=9
        y=5
    elif (number_of_rows <= 100): # fairly small dataset
        frac=0.175
        x=12
        y=7
    elif (number_of_rows <= 200): # pretty big dataset
        frac=0.1
        x=16
        y=10
    else: # very big dataset
        frac=0.075
        x=20
        y=13

    
    for party in parties:
        # Convert non-numeric values to 0
        poll_data[party] = pd.to_numeric(poll_data[party], errors='coerce').fillna(0)

        loess_smoothed[party] = sm.nonparametric.lowess(
            poll_data[party],
            poll_data.index,
            frac=frac,
            delta=0.0,
            is_sorted=True,
            missing='drop',
            return_sorted=True
        )

    colours=[]
    random.seed(10)

    j = 2
    while (j < len(sys.argv)):
        colour = sys.argv[j].lower()
        if check_colour(colour) == True:
            colours.append(colour)
        else:
            colours.append(generate_random_colour(colours))
        j += 1

    # generate colours for parties/candidates which were not given a colour in the command line
    while ((j-2) < len(parties)):
        colours.append(generate_random_colour(colours))
        j += 1

    # convert from excel date system to one that pandas can work with
    poll_data['timestamp'] = pd.to_datetime(poll_data.index, origin='1899-12-30', unit='D')

    i = 0
    plt.figure(figsize=(x, y))

    # Plot each party with its corresponding colour
    for party in parties:
        colour = colours[i]
        plt.plot(
            poll_data['timestamp'].values, 
            poll_data[party].to_numpy(),
            '.',
            alpha=0.5,
            label=party,
            color=colour
        )
        plt.plot(
            poll_data['timestamp'].values,
            loess_smoothed[party][:, 1],
            '-',
            color=colour
        )
        i += 1

    plt.xlabel('Date')
    plt.ylabel('Polling Data')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=len(parties))
    plt.title('Polling Data with LOWESS Smoothing')

    # find out whether the input came from the input directory
    if filename1[0:6] == "input/":
        filename = filename1[6:-4]
    else:
        filename = filename1[0:-4]
    plt.savefig('output/'+filename+'.png')


if __name__ == '__main__':
    main()