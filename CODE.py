# 1/9
import csv
file = open('full_data.csv', 'r')
posts_with_header = list(csv.reader(file))
data = posts_with_header [1:]
print('1:', data[0:4])
# 2/9
headers = posts_with_header [0]
print('2:', headers)
# 3/9
year = set(row[1] for row in data)
print('3:', year)
year_counts = {}
for row in data:
    if row[1] in year_counts:
        year_counts[row[1]] += 1
    else:
        year_counts[row[1]] = 1
print('3:', year_counts)
# 4/9
import datetime
dates = []
for row in data:
    year = int(row[1])
    month = int(row[2])
    date = datetime.datetime(year=year, month=month, day = 1)
    dates.append(date)
# dates = [datetime.datetime(year=int(row[1]), month=int(row[2]), day=1) for row in data]
print('4:', dates[0:4])
date_count = {}
for date in dates:
    if date in date_count:
        date_count[date] += 1
    else:
        date_count[date] = 1
print('4:', date_count)
# 5/9
sex_counts = {}
race_counts = {}
for row in data:
    if row[5] not in sex_counts:
        sex_counts[row[5]] = 0
    sex_counts[row[5]] += 1
    if row[7] not in race_counts:
        race_counts[row[7]] = 0
    race_counts[row[7]] += 1
print('5:', sex_counts, race_counts)
# 6/9
file_census = open('census.csv', 'r')
census = list(csv.reader(file_census))
print('6:', census)
# 7/9
mapping = {
    'Asian/Pacific Islander': int(census[1][14]) + int(census[1][15]),
    'Black': int(census[1][12]),
    'Native American/Native Alaskan': int(census[1][13]),
    'Hispanic': int(census[1][11]),
    'White': int(census[1][10])
}
print('7 - census:', mapping)
race_per_hundredk = {}
for key, value in race_counts.items():
    race_per_hundredk[key] = (value / mapping[key]) * 100000
print('7:', race_per_hundredk)
# 8/9
type_of_intents = set(row[3] for row in data)
type_of_races = set(row[7] for row in data)
print('8.1:', type_of_intents, type_of_races)
intents = [row[3] for row in data]
races = [row[7] for row in data]
homicide_race_counts = {}
for i, race in enumerate(races):
   if race not in homicide_race_counts:
       homicide_race_counts[race] = 0
   if intents[i] == 'Homicide':
       homicide_race_counts[race] += 1
print('8.3:', homicide_race_counts)
race_per_hundredk_1 = {}
for key, value in homicide_race_counts.items():
    race_per_hundredk_1[key] = (value / mapping[key]) *100000
print('8.4:', race_per_hundredk_1)