# Climate Analysis and Exploration

## Project Overview

In this project, I worked on climate analysis and data exploration of a climate database. The technologies I used include Python, SQLAlchemy ORM queries, Pandas, and Matplotlib.

## Data Analysis

I started by setting up the database using SQLAlchemy and reflected the existing database into a new model. I then saved references to each table and created a session link from Python to the database.

I performed various analyses on the data:

1. **Precipitation Analysis:** I designed a query to retrieve the last 12 months of precipitation data and plotted the results. I also calculated the summary statistics for the precipitation data.

2. **Station Analysis:** I calculated the total number of stations in the dataset. I then found the most active stations and listed them along with their observation counts in descending order. For the most active station, I calculated the lowest, highest, and average temperature. I also queried the last 12 months of temperature observation data for this station and plotted the results as a histogram.

## Flask API

After completing the initial analysis, I designed a Flask API based on the queries I developed. I created routes for:

- The home page (`/`)
- Precipitation data (`/api/v1.0/precipitation`)
- List of stations (`/api/v1.0/stations`)
- Temperature observations for the previous year (`/api/v1.0/tobs`)
- Temperature statistics for a given start or start-end range (`/api/v1.0/temp/start/end`)

Each route returns a JSON representation of the data.

## Conclusion

This project allowed me to apply data engineering skills to set up a database, data analysis skills to explore it, and web development skills to make the data available via an API. It was a great experience to see how these different aspects tie together in a full-stack application. I look forward to applying these skills to future projects.
