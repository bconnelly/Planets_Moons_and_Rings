import math
import random
import matplotlib.pyplot as plot

def crateringSim():
	#make new list to store crater coordinates
	craters = []
	cratersOverTime = []
	densityRec = [(0,0)]

	#this loop should end when the density doesn't change more than
	#5% when the time doubles
	iterations = 0
	while(iterations == 0 or (densityRec[iterations][1] - densityRec[iterations/2][1])/densityRec[iterations][1] >.05):
		#generate random coordinates in 500x500 grid
		x = random.randint(0, 500)
		y = random.randint(0, 500)

		#check if it obliterates any existing craters
		for crater in craters:
			if(math.sqrt((crater[0] - x)**2 + (crater[1] - y)**2) <= 60):
				print('Removing crater at x: ' + str(crater[0]) + ' y: ' + str(crater[1]))
				craters.remove(crater)
		print('Adding crater at x: ' + str(x) + ' y: ' + str(y))
		craters.append((x, y))
		#update record of densities
		densityRec.append((iterations, float(len(craters))/float(500*500)))
		print('Density: ' + str(densityRec[iterations]) + '\n')
		#record number of craters over time
		cratersOverTime.append((iterations*10000, len(craters)))
		iterations += 1
	print("Final number of Craters: " + str(len(craters)))
	print("Final crater Density: " + str(densityRec[iterations][1]) + " per km^2")
	print("Years until peak density reached: " + str(iterations * 10000))

	#plot number of craters over time
	plot.plot(*zip(*cratersOverTime))
	plot.title('Number of craters over time')
	plot.xlabel('Time (Years)')
	plot.ylabel('Craters')
	plot.axis()
	plot.show()

	#plot the circles
	fig = plot.gcf()
	plot.axis([0, 500, 0, 500])
	for crater in craters:
		circle = plot.Circle((crater[0], crater[1]), 50, fill = False)
		fig.gca().add_artist(circle)
	fig.show()

	raw_input()
	
crateringSim()