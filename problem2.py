import matplotlib.pyplot as plt
import csv

"""Plot a stacked bar chart of matches won of all teams over all the years of IPL.

"""

rows = []
matches_dataset = 'matches.csv'

"""open csv file and read it"""
with open(matches_dataset, 'r') as matches_csvfile:
    reader = csv.reader(matches_csvfile, delimiter=',')

    """next() reads one row and moves pointer to next row. fields stores headers"""
    fields = next(reader)

    """store all rows except header row into list rows"""
    for row in reader:
        rows.append(row)

count = 0
season = 0
"""seasonDict contains season-wise total match data"""
seasonDict = dict()

"""loop to populate seasonDict"""
for row in rows:
    if int(row[1]) != season:
        if season != 0:
            # plt.bar(season, count)
            seasonDict[season] = count
        season = int(row[1])
        count = 0
    count += 1
# plt.bar(season, count)
seasonDict[season] = count

teamList = []
"""loop to populate teamList"""
for row in rows:
    if row[10] not in teamList:
        teamList.append(row[10])

"""remove empty string from list"""
teamList.remove("")

print(teamList)
print(len(teamList))

"""storing team names as a list of dictionaries"""
teams = []
for team in teamList:
    teamDict = dict(name=team)
    teams.append(teamDict)

"""loop to populate each team dictionary in teams list"""
for team in teams:
    for year in seasonDict:
        count = 0
        for row in rows:
            if row[10] == team["name"] and int(row[1]) == year:
                count += 1
        team[year] = count


for year in seasonDict:
    previousYear = 0
    for team in teams:
        for item in team:
            if item == year:
                plt.bar(x=year, height=int(team[item]), bottom=int(previousYear))
                previousYear = int(team[item])

plt.show()
