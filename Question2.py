import csv

def getTopFivePerYear():
	with open('2014-2018.csv', encoding="utf8") as csvfile:
		extractedObj = []
		next(csvfile)
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			artistSong=(row[3]).split(' - ')
			extractedObj.append({
				'year': row[0],
				'artist':artistSong[0],
				'song':artistSong[1],
				'points':int(row[6])
			})

		top_per_year = sorted(extractedObj, key = lambda i: (i['points']), reverse=True)	
		# print(top_per_year)
		
		item = 0
		item1 = 0
		item2 = 0
		item3 = 0
		item4 = 0
		finalList = []
		for row in top_per_year:
			if(row['year'] == '2014' and item != 5):
				finalList.append(row)
				item += 1
			if(row['year'] == '2015' and item1 != 5):
				finalList.append(row)
				item1 += 1
			if(row['year'] == '2016' and item2 != 5):
				finalList.append(row)
				item2 += 1
			if(row['year'] == '2017' and item3 != 5):
				finalList.append(row)
				item3 += 1
			if(row['year'] == '2018' and item4 != 5):
				finalList.append(row)
				item4 += 1

		for element in finalList:
			print("'{}': Points: {}, name: {} - {}".format(element['year'], element['points'], element['artist'], element['song']))

		return finalList

# getTopFivePerYear()