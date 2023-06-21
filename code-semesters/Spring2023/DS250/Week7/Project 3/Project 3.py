#%%
import pandas as pd 
import altair as alt
import numpy as np
import sqlite3
#%%
import datadotworld as dw

# %%
# careful to list your path to the file.
sqlite_file = 'lahmansbaseballdb.sqlite'
con = sqlite3.connect(sqlite_file)

results = pd.read_sql_query( 
    'SELECT * FROM allstarfull LIMIT 5',
    con)

results

#%%
table = pd.read_sql_query(
    "SELECT * FROM sqlite_master WHERE type='table'",
    con)
print(table.filter(['name']))
print('\n\n')
# 8 is collegeplaying
print(table.sql[8])

#%%

# Execute the SQL query
batting_query = "SELECT * FROM batting LIMIT 2"
batting_results = pd.read_sql_query(batting_query, con)
print(batting_results)


#%%
query = "SELECT playerID, yearID, AB, H, ((H * 1.0) / AB) AS batting_average FROM batting WHERE playerID = 'addybo01' AND yearID = 1871"
results = pd.read_sql_query(query, con)

# Retrieve the batting average
batting_average = results['batting_average'].values[0]
print("Batting average for addybo01 in 1871:", batting_average)



# %%
qr = dw.query('sqlite_file', 'SELECT * FROM batting LIMIT 2')
results = qr.dataframe
print(results)

#%%
results = pd.read_sql_query(
    'SELECT s.playerID, c.schoolID, s.salary, s.yearID, s.teamID FROM collegeplaying AS c JOIN salaries AS s ON c.playerID = s.playerID JOIN people AS p ON p.playerID = c.playerID WHERE c.schoolID="BYU-Idaho" ORDER BY s.salary DESC',
    con)

results

# %%
results = pd.read_sql_query(
    "SELECT b.playerID, b.schoolID, s.salary, s.yearID, s.teamID \
    FROM collegeplaying AS b \
    INNER JOIN salaries AS s ON b.playerID = s.playerID \
    WHERE b.schoolID = 'BYU-Idaho'",
    con)

print(results)


# %%
baseball_byuIdaho = dw.query(sqlite_file,
    '''
    SELECT DISTINCT CollegePlaying.playerID,
        CollegePlaying.schoolID,
        Salaries.salary,
        Salaries.yearID,
        Salaries.teamID
    FROM CollegePlaying
        JOIN Salaries 
            ON CollegePlaying.playerID = Salaries.playerID
    WHERE CollegePlaying.schoolID = "idbyuid"
    ORDER BY Salaries.salary DESC
    '''
).dataframe

print(baseball_byuIdaho.to_markdown())
# %%
