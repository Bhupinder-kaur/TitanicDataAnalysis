# TitanicDataAnalysis
Titanic Dataset Analysis and Visualization 🚢📊
This project demonstrates an end-to-end data cleaning, preprocessing, and exploratory data analysis (EDA) on the Titanic dataset, including feature engineering and visualizations.

Key Steps:
Data Cleaning:

Removed unnecessary columns (Name, Ticket, Fare, Cabin) to simplify the analysis.
Handled missing values in the Age column by filling:
Survived passengers' missing age values with the mean age of survivors.
Non-survived passengers' missing age values with the mean age of non-survivors.
Feature Engineering:

Converted the Sex column into a numerical Gender column (1 for male, 0 for female).
Encoded the Embarked column into numerical values (1 for S, 2 for Q, 3 for C).
Visualizations:

Gender Distribution Pie Chart: A pie chart showing the distribution of males and females aboard the Titanic.
Survival Distribution by Gender: A pie chart illustrating the proportion of males and females who survived and did not survive the Titanic disaster.
Visualizations:
Gender Distribution:
Displays the proportion of males and females on the Titanic using a pie chart.
Survival by Gender:
Visualizes the survival rates of males and females using a segmented pie chart showing "Survived" and "Not Survived" for each gender.
Technologies Used:
Python: Core programming language.
Pandas: Data manipulation and cleaning.
NumPy: Numerical operations.
Matplotlib: Data visualization.
This project provides insights into how gender and embarkation location influenced survival on the Titanic. 🎯 Check out the code for more details on data processing and visualization!
