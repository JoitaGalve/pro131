import csv
import plotly.express as px

rows = []

with open("stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers = rows[0]
stars_data_rows = rows[1:]

print(headers)
print(stars_data_rows[0])

headers[0] = "row_num"
solar_system_stars_count = {}
for stars_data in stars_data_rows:
    if solar_system_stars_count.get(stars_data[2]):
        solar_system_stars_count[stars_data[2]] += 1

    else:
        solar_system_stars_count[stars_data[2]] = 1

max_solar_system = max(solar_system_stars_count, key = solar_system_stars_count.get)

print("Solar system {} has maximum stars {} out of the solar system we have discovered so far".format(max_solar_system, solar_system_stars_count[max_solar_system]))

sun_star = []

for stars_data in stars_data_rows:
    if max_solar_system == stars_data[2]:
        sun_star.append(stars_data)

#print(len(KOI_351_planet))
#print(KOI_351_planet)
sun_star_masses = []
sun_star_names = []

for planet_data in sun_star:
    sun_star_masses.append(stars_data[3])
    sun_star_names.append(stars_data[1])

sun_star_masses.append(1)
sun_star_names.append("Sun")

fig = px.bar(x = sun_star_names, y = sun_star_masses)
fig.show()

planetGravity = []
for index, name in enumerate(stars_names):
    gravity = (float(star_masses[index]) * 5.972e+24) / (float(star_radius[index]) * float(star_radius[index]) * 6371000 * 6371000) * 6.674e-11
    planetGravity.append(gravity)

fig = px.scatter(x = star_radius, y = star_masses, size = planetGravity, hover_data = [stars_data])
fig.show()