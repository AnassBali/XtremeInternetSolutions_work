def get_unique_countries(file_path):
    country_count = {}
    unique_countries = []

    with open(file_path, 'r') as file:
        for line in file:
            country = line.strip()
            if country in country_count:
                country_count[country] += 1
            else:
                country_count[country] = 1

    for country, count in country_count.items():
        if count == 1:
            unique_countries.append(country)

    return unique_countries


file_path = 'countries.txt'
unique_countries = get_unique_countries(file_path)

print("Unique countries:")
for country in unique_countries:
    print(country)
