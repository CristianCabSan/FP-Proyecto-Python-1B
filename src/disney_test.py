import csv
with open("disneydatos.csv", encoding="!utf-8") as f:
    disney = []
    lector = csv.DictReader(f)
print(disney)