import pandas as pd
from pathlib import Path

#this is the dir 
base = Path(__file__).parent
root = base.parent
csv_path = root / "raw" / "netflix_titles.csv"
output_dir = root / "output"


df = pd.read_csv(csv_path)

# Separate Movies and TV Shows
df_movies = df[df["type"] == "Movie"].copy()
df_series = df[df["type"] == "TV Show"].copy()

# Drop rows with missing title or type
df_movies = df_movies.dropna(subset=['title', 'type'])
df_series = df_series.dropna(subset=['title', 'type'])

# Fill missing values for selected columns
fill_columns = ['director', 'cast', 'country', 'date_added',
                'release_year', 'rating', 'duration', 'listed_in', 'description']

for column in fill_columns:
    df_movies[column] = df_movies[column].fillna('Unknown')
    df_series[column] = df_series[column].fillna('Unknown')

# Format titles
df_movies['title'] = df_movies['title'].str.strip().str.title()
df_series['title'] = df_series['title'].str.strip().str.title()

# Convert 'date_added' to datetime
df_movies['date_added'] = pd.to_datetime(df_movies['date_added'], errors='coerce')
df_series['date_added'] = pd.to_datetime(df_series['date_added'], errors='coerce')

# Extract duration values
df_movies['duration_min'] = df_movies['duration'].str.extract(r'(\d+)').astype(float)
df_series['duration_season'] = df_series['duration'].str.extract(r'(\d+)').astype(float)

# Define a function to validate ratings
def check_if_valid(rating):
    valid_ratings = [
        'G', 'PG', 'PG-13', 'R', 'NC-17',
        'TV-Y', 'TV-Y7', 'TV-Y7-FV', 'TV-G', 'TV-PG', 'TV-14', 'TV-MA',
        'NR', 'UR', 'Not Rated'
    ]
    if isinstance(rating, str) and rating in valid_ratings:
        return rating
    else:
        return "Unknown"

# Apply the rating validator
df_movies['rating'] = df_movies['rating'].apply(check_if_valid)
df_series['rating'] = df_series['rating'].apply(check_if_valid)

# Preview results
print("Movies Sample:")
print(df_movies.head(10))

print("\nTV Shows Sample:")
print(df_series.head(10))

movies_filename = output_dir / "movies_clean.csv"
series_filename = output_dir / "series_clean.csv"

df_movies.to_csv(movies_filename, index=False)
df_series.to_csv(series_filename, index=False)

