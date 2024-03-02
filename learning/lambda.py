people = [
    {"name": "Harry", "house": "New York"},
    {"name": "Stella", "house": "Tokyo"},
    {"name": "Adam", "house": "Olso"}
]

# def f(person):
#     return person["name"]

people.sort(key=lambda person: person["name"])

print(people)

movies = [
    {"title": "Green Book", "year": 2018},
    {"title": "The Shape of Water", "year": 2017},
    {"title": "Moonlight", "year": 2016},
    {"title": "Spotlight", "year": 2015},
    {"title": "Birdman", "year": 2014},
    {"title": "12 Years a Slave", "year": 2013}
]

movies.sort(key=lambda movie: movie["year"])

for movie in movies:
    print("{title} was released in {year}".format(**movie))
