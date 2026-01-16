import pandas as pd
df = pd.read_csv("pandas-works\\ipl-casestudy\\ipl_data.csv")

print(df.shape)
print(df.columns)
print(df.info())

df["match_id"].fillna(567,inplace=True) 
df["season"].fillna(df["season"].mode()[0],inplace=True)                
df["city"].fillna(df["city"].mode()[0],inplace=True)
df["team1"].fillna(df["team1"].mode()[0],inplace=True)
df["team2"].fillna(df["team2"].mode()[0],inplace=True)
df["winning_team"].fillna("unknown",inplace=True)
df["player_of_match"].fillna("unknown",inplace=True)
df["venue"].fillna(df["venue"].mode()[0],inplace=True)
df["runs_scored"].fillna(df["runs_scored"].mean(),inplace=True)
df["wickets"].fillna(df["wickets"].mean(),inplace=True)

#print(df.isnull().sum())

#season count and max
print(df["season"].value_counts())
print("max matched season:",df["season"].value_counts().idxmax())

#winning score count and max
print(df["winning_team"].value_counts())
print("most game won team:",df["winning_team"].value_counts().idxmax())

#avg runs per seasons
print(df.groupby("season")["runs_scored"].mean())

#venue wise match count and avg runs
print(df["venue"].value_counts())
print(df.groupby("venue")["runs_scored"].mean())

#city wise run count and avg runs
print(df["city"].value_counts())
print(df.groupby("city")["runs_scored"].mean())

#team with hihest avg run
print(df.groupby("winning_team")["runs_scored"].mean().idxmax())

#top 3 matched venue
#print(df["venue"].value_counts().head(3))
top=df["venue"].value_counts()
print(top.sort_values(ascending=False).head(3))


