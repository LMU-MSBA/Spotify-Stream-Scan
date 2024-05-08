# Spotify Stream Scan - Nearest Neighbors Reccomended System

## Model Description

We developed a K-Nearest Neighbors model in Python that takes an Artist's genres as an input and outputs the five closest artists that fall into all of those same genres. We also provide the popularity score of each of these artists to quantify the popularity of each artist that falls into each of the specified genres on the Spotify platform. The intended use of this model is for Spotify Talent Agents to use for prospective talent when aiming to identify which current popular artists on Spotify this new popular artists should be promoted with, based on music style and genre similarities.

## Input Features

The model uses over 550 genres that are one-hot encoded to determine Nearest Neighbors. Each artist has a row in the data frame used to train the model, and for each of the 550 genres, a 1 will indicate if the artist has an album in that genre, and a 0 indicates that the artist does not have an album in that genre.

## Model Output

Upon generating the new predictions data frame, the model calls `kneighbors()`, which will output a list of the five most similar artists to the new artist (based on genre similarities), sorted by popularity score.

## Model Performance

We used the **distance** measurement from the `kneighbors()` function to determine the mean distance to the Nearest Neighbor. While it's on the higher side (0.6), out of 0 to 1, we could improve our model in the future by reducin the number of genres, to make classification a little easier.

## Using the Model

When generating a new prediction, the user can create a new data frame that indicates which genre the new artist falls into:

```python

prediction_df = pd.DataFrame(columns = model_df.columns)
prediction_df.loc[0] = [0] * len(prediction_df.columns)

prediction_df['pop'] = 1
prediction_df['r&b'] = 1
prediction_df['rap'] = 1

prediction_df

```

In this particular example, we generated a data frame to represent an artist that falls into the pop, rap, and r&b categories.

This was the resulting output:

    Artist_Name  Popularity
893     Beyoncé          92
990         SZA          91
599     Cardi B          81
78      Kehlani          73
322     Normani          67