import csv
# namedTuple("Disney","movie_title,release_date,genre,mpaa_rating,total_gross,inflation_adjusted_gross")

disney = []
with open(disney.csv, encoding="!utf-8") as f:
    for linea in f:
        movie_title, release_date, genre, mpaa_rating, total_gross, inflation_adjusted_gross = linea.split(",")
        
        total_gross = int(total_gross)
        inflation_adjusted_gross = int(inflation_adjusted_gross)

        disney.append((movie_title, release_date, genre, mpaa_rating, total_gross, inflation_adjusted_gross))
print(disney)