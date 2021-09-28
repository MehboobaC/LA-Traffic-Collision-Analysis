# LA-Traffic-Collision-Analysis


Road accidents are one of the most relevant causes of injuries and death worldwide, and therefore, they constitute a significant field of research on the use of advanced algorithms and techniques to analyze and predict traffic accidents and determine the most relevant elements that contribute to road accidents.

## DATASET
The dataset here reflects traffic collision incidents in the City of Los Angeles dating back to 2010. This data is obtained from a traffic collision data set maintained by the city of Los Angeles. While it doesn’t directly measure traffic, it measures a closely-related proxy. 
 This data is transcribed from original paper traffic reports, so it’s very likely that there are errors. The data begins in January 2010 and is updated weekly. In this particular project,data used is from January 2010 - January 2021, which ends up being ~551K rows. Each row corresponds to a collision. The data set contains 18 columns which includes dates (reported, occurred), time, area details, crime code, MO code, victim details (age, sex, descent) and location details. 

Find the dataset [here](https://data.lacity.org/Public-Safety/Traffic-Collision-Data-from-2010-to-Present/d5tf-ez2w) or [download](https://data.lacity.org/api/views/d5tf-ez2w/rows.csv) directly.


## OBJECTIVE
The purpose of the project is to do exploratory data analysis in Tableau and predict the number of collisions that will occur per month based on time series analysis. The predictive analysis with the time series models is implemented using python for the traffic collision data set. The process of modeling, as well as results, are interpreted using root mean square error and AIC value. The major contribution of this project is to give a clear view of how the traffic collision data set can be used to generate a more secure mobility environment, and ultimately, save lives.

