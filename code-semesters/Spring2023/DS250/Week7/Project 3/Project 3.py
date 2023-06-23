#%%
import sqlite3
import pandas as pd
import altair as alt

#%% Connect to the SQLite database
con = sqlite3.connect('lahmansbaseballdb.sqlite')

#%% GRAND QUESTION 1
query_grand_q1 = """
SELECT DISTINCT salaries.playerID, collegeplaying.schoolID, salaries.salary, salaries.yearID, salaries.teamID
FROM salaries
    JOIN collegeplaying ON salaries.playerID = collegeplaying.playerID
WHERE collegeplaying.schoolID = 'idbyuid'
ORDER BY salaries.salary DESC
"""

df_grand_q1 = pd.read_sql_query(query_grand_q1, con)

print(df_grand_q1.to_markdown())


# GRAND QUESTION 2

#%% PART A: Calculate the batting average for each player in 2016 with at least 1 at-bat
query_grand_q2_part_a = '''
SELECT playerID, yearID, CAST(H AS FLOAT) / AB AS batting_average
FROM batting
WHERE yearID = 2019 AND AB >= 1
ORDER BY batting_average DESC, playerID ASC
LIMIT 5
'''

df_grand_q2_part_a = pd.read_sql_query(query_grand_q2_part_a, con)

print(df_grand_q2_part_a.to_markdown())


#%% PART B: Calculate the batting average for each player in 2016 with at least 10 at-bats
query_grand_q2_part_b = '''
SELECT playerID, yearID, CAST(H AS FLOAT) / AB AS batting_average
FROM batting
WHERE yearID = 2019 AND AB >= 10
ORDER BY batting_average DESC, playerID ASC
LIMIT 5
'''

df_grand_q2_part_b = pd.read_sql_query(query_grand_q2_part_b, con)

print(df_grand_q2_part_b.to_markdown())


#%% PART C: Calculate the career batting average for players with at least 100 at-bats
query_grand_q2_part_c = '''
SELECT playerID, AVG(CAST(H AS FLOAT) / AB) AS career_batting_average
FROM batting
GROUP BY playerID
HAVING SUM(AB) >= 100
ORDER BY career_batting_average DESC
LIMIT 5
'''

df_grand_q2_part_c = pd.read_sql_query(query_grand_q2_part_c, con)

print(df_grand_q2_part_c.to_markdown())


#%% GRAND QUESTION 3
# SQL query to compare two baseball teams based on average salary
query_grand_q3 = '''
SELECT teamID, AVG(salary) AS avg_salary
FROM salaries
WHERE teamID IN ('NYA', 'TEX')
GROUP BY teamID
'''

df_grand_q3 = pd.read_sql_query(query_grand_q3, con)

print(df_grand_q3.to_markdown())

# Create an Altair bar chart to visualize the comparison
chart = alt.Chart(df_grand_q3).mark_bar().properties(
    title='Average Salary per Player'
).encode(
    x=alt.X('avg_salary', axis=alt.Axis(title="Average Salary")),
    y=alt.Y('teamID', axis=alt.Axis(title='Team'))
)

# Display the chart
chart

# %%
