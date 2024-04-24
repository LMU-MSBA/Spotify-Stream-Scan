# Spotify Talent Insights Dashboard
## Purpose
The purpose of this dashboard is to aid talent managers during the artist acquisition phase by providing insights into artist popularity and genre trends. It's designed to streamline the decision-making process

## Access
To explore the dashboard, __

## Data Sources
After automating the ETL (Extract, Transform, Load) processes, we consolidate our data into an AWS data warehouse. This integrated data is then connected to Tableau for visualization and analysis, which includes up-to-date Artist Information, Genres, and Album Information.

## Key Metrics
The dashboard prominently features the Popularity Average Score as its primary metric, which rates an artist's fame on a scale from 1 to 100, with 100 denoting the highest level of popularity. 

## How to use the dashboard
This Dashboard is designed during the artist acquisition phase by providing __five__ keys data visualizations:

* __Top 10 Artist by Average Popularity__
  * This bar chart ranks artists with the highest average popularity scores 
* __Lowest Artist Popularity Score__
  * This bar chart highlights artists with the lowest average popularity scores
* __Most Followed Genres__
  * The bubble chart visualizes music genres according to their follower count
* __Genres and Average Popularity__
  * The list orders music genres by average popularity score
* __Energy vs Loudness__
  *  A scatter plot positively correlating music features, energy and loudness, of songs

## How to refresh the data
The Spotify dashboard is connected to the data warehouse, enabling users to access and visualize updated streaming data in real time. This integration ensures that all stakeholders can monitor trends and user behavior.
