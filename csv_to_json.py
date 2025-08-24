import pandas as pd
import json

#Lee el archivo"csv"
df = pd.read_csv('movies_initial.csv')

#guarda el dataframe como json
df.to_json('movies.json', orient='records')

with open('movies.json','r') as file:
    movies = json.load(file)

for i in range(100):
    movie= movies
    print(movie)
    break