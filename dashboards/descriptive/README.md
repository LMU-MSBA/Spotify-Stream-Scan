# Spotify Discovery Dashboard

## Purpose

Our Discovery Dashboard is targeted towards Spotify's talent managers who are seeking out new artists to promote on Spotify's music streaming platform. 

The Discover Dashboard aims to identify where talent managers should focus their efforts when choosing certain artists to promote to users. A variety of visualizations allows the Dashboard user or observer to quickly and easily identify trends present in the data.

Our dashboard will primarily be used for decision making in the **Talent Acquisition Process** at Spotify, since talent managers can identify and monitor what types of artists and genres are most popular at the moment.

The Discover Dashboards empowers our talent managers in their decision making process on who they should focus efforts on in promotions by giving them access to information that is indicative of success, in terms of Popularity among Spotify users.

## Access

[Click here](https://public.tableau.com/app/profile/shaye.o.beirne/viz/SpotifyDiscoveryDashboard/SpotifyDiscoveryDashboard#1) to view the Spotify Discovery Dashboard

## Data Source

We utilized the [Spotify API](https://developer.spotify.com/documentation/web-api) to gain access to information from the Spotify platform, such as Artist Information, Genres, and Album Information.

## Key Metrics

Our Dashboard focuses primarily on each Artist's [Popularity Score](https://developer.spotify.com/documentation/web-api/reference/get-an-artist), which quanitifies an artist's popularity on the Spotify Platform. The score is calculated from the popularity of all of the artist's tracks on a scale from 0-100, with 100 being the most popular. Our dashboard also uses Follower count as a supporting KPI, which is also indicative of popularity on of the Spotify platform.

## How to Use the Dashboard

The Spotify Discovery Dashboard consists of five main visualizations:

- **Volume of Artists by Genre**: This packed bubbles plot allows the user to visualize the volume of artists present on the Spotify platform, grouped by Genre. While there are many genres of music available on Spotify, we chose to display the Top 10 Genres by volume of artists.
- **Top 20 Artists by Popularity**: This table lists the Top 20 artists across our 10 most popular genres by Popularity score. Some of these artists fall under multiple genres.
- **Relationship Between Popularity and Followers**: This scatterplot visualizes the positive, exponential relationship between Popularity Score on Spotify and Follower Count on Spotify
- **Average Followers by Genre**: This bar plot displays the average number of followers, grouped by genre.
- **Distribution of Popularity by Genre**: This series of boxplots displays the distribution of Follower counts for artists, grouped by genre. This allows the user to easily identify outliers of follower counts among genres.

## How to Refresh the Data

We are in the process of connecting the Spotify Discovery Dashboard to our ETL pipeline, which will allow the user to refresh the dashboard and view current, up-to-date data in real time.
