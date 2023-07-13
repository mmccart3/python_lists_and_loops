def film_check(film):
    if film == "Ghostbusters":
        return "Yey its Ghostbusters"
    else:
        return "Boo we want ghostbusters"

number_list = [2,19,7,37,17,5]

# The magic of Python for loops!
for my_fav_numbers in number_list:
    print(my_fav_numbers)

#A more traditional approach for other programming languages    
for i in range(len(number_list)):
    print(number_list[i])

# The very old traditional method for for loops
for i in range(1,11):
    print(i)
    
#The 3 times table

for i in range(3,37,3):
    print(i)

fav_films = ["Casablanca","Crimson Tide", "The Longest Day", "The Shawshank Redemption", "Ghostbusters"]

for films in fav_films:
    print(films,"...", film_check(films))

for x in range(9,-1,-1):
    print(x)

