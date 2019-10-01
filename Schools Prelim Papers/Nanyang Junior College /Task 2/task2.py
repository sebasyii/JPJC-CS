# The question ask to paste it into my code but there's so many countries
# So i am just gonna read and make it into a list

infile = open("COUNTRIES.txt", "r")

countries = [line[:-1] for line in infile]


def insertion_sort(arr, n):
    if n <= 1:
        return arr

    insertion_sort(arr, n - 1)

    last = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > last:

        arr[j + 1] = arr[j]

        j = j - 1
    print(f"Element at position {n-1} is being inserted in position {j+1}")
    arr[j + 1] = last
    return arr


new_countries = insertion_sort(countries, len(countries))
for country in new_countries:
    print(country)
print(len(countries))
