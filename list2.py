my_bucket_list = [
    "Walk to Santiago from home",
    "Visit New York",
    "Visit Washington DC",
    "Visit Gettysburg"
]

my_bucket_list_2 = [
    "Visit Brasil",
    "Visit Uruguay",
    "Visit Auschwitz"
]

my_bucket_list.extend(my_bucket_list_2)

print(my_bucket_list)
print(my_bucket_list_2)

answer = my_bucket_list.index("Visit Uruguay")
print(answer)

number_list = [2,19,7,37,17,5]

answer2 = sorted(number_list)
print(answer2)

answer3 = answer2.reverse()
print(answer3)