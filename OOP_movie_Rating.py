class movie_rating :
    def __init__(self,data):
        self.data = data
    def calculate_average_rating(self):
        l = []
        for i in dataset:
            l.append(i['Rating'])
        # print(l)

        avg = sum(l) / len(l)
        return avg

    def highest_rated_movie(self):
        l= []
        movie =[]
        for i in dataset:
            l.append(i['Rating'])
            max_rating =max(l)
            for i in self.data:
                if i['Rating']==max_rating:
                    movie.append(i['Title'])
            return movie

    def number_of_movies_per_genere(self):
        m = []
        for i in dataset:
            m.append(i['Genre'])
            # print(m)
        d = {i: m.count(i) for i in m}
        # print(d)
        for i, j in d.items():
            print(i, j)



import json
data = open(r"E:\cybersucess\Project\json\movie_ratings.json", 'r')
dataset = json.loads(data.read())

movie = movie_rating(dataset)
print('Average Movie Rating Is: ',movie.calculate_average_rating())

print()
print()

print('Highest Rated Movies Are: ')
for i in movie.highest_rated_movie():
    print(i)

print()
print()
print('Number Of Movies Per Genre: ')
movie.number_of_movies_per_genere()
