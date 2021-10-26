import csv

with open(".\data\disney.csv", encoding="!utf-8") as f:
    disney = []
    next(f)
    for disney in f:

        #movie_title, release_date, genre, mpaa_rating, total_gross, inflation_adjusted_gross = disney.split(",")
        #total_gross = int(total_gross)
       # inflation_adjusted_gross = int(inflation_adjusted_gross)
        print(disney)
       # disney.append((movie_title, release_date, genre, mpaa_rating, total_gross, inflation_adjusted_gross))
print(disney)