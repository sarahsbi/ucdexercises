import pandas as pd

netflix_data= pd.read_csv("netflix_titles.csv")

drop_duplicates= netflix_data.drop_duplicates(subset=['type'])
print(netflix_data.shape,drop_duplicates.shape)

