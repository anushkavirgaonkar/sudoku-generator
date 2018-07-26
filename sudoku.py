import random

row1,row2,row3,row4,row5,row6,row7,row8,row9=[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]
numbers = [1,2,3,4,5,6,7,8,9]

for i in range(0,9) :
	row1[i] = random.choice(numbers)
	numbers.remove(row1[i])

numbers = [1,2,3,4,5,6,7,8,9]
a = {row1[0] , row1[1] , row1[2] }
b = {row1[3] , row1[4] , row1[5] }
c = {row1[6] , row1[7] , row1[8] }

while(0 in row2) :
	numbers = [3,4,5,6,7,8]
	for number in a :
		i = random.choice(numbers)	
		if(row2[i] ==0) :
			row2[i] = number
			numbers.remove(i)
		else : 
			i = random.choice(numbers)
			row2[i] = number
			numbers.remove(i)
	
	numbers = [0,1,2,6,7,8]
	for number in b:
		i = random.choice(numbers)	
		if(row2[i] ==0) :
			row2[i] = number
			numbers.remove(i)
		else : 
			i = random.choice(numbers)
			row2[i] = number
			numbers.remove(i)
			
	numbers = [0,1,2,3,4,5]
	for number in c:
		i = random.choice(numbers)	
		if(row2[i] ==0) :
			row2[i] = number
			numbers.remove(i)
		else : 
			i = random.choice(numbers)
			row2[i] = number
			numbers.remove(i)
			
	if(0 in row2) : row2 = [0,0,0,0,0,0,0,0,0]

def thirdrow() : 
	for j in [0,3,6] :
		numbers = [1,2,3,4,5,6,7,8,9]
		numbers.remove(row1[j])
		numbers.remove(row1[j+1])
		numbers.remove(row1[j+2])
		numbers.remove(row2[j])
		numbers.remove(row2[j+1])
		numbers.remove(row2[j+2])
		place = [j,j+1,j+2]
		for number in numbers :
			i = random.choice(place)
			if(row3[i] ==0) :
				row3[i] = number
				place.remove(i)
			else : 
				i = random.choice(place)
				row3[i] = number
				place.remove(i)
	return row3

row3 = thirdrow()

def rows_4789(rowno , row) :
	while(0 in row):
		for i in range(0,9) :
			numbers = [1,2,3,4,5,6,7,8,9]
			numbers.remove(row1[i])
			numbers.remove(row2[i])
			numbers.remove(row3[i])
			if(rowno>4) :
				numbers.remove(row4[i])
				numbers.remove(row5[i])
				numbers.remove(row6[i])
				if(rowno>7) :
					numbers.remove(row7[i])
				if(rowno==9) :
					numbers.remove(row8[i])
			j=i
			while(j>0) :
				j=j-1
				if(row[j] in numbers) : numbers.remove(row[j])
			if(len(numbers) != 0) : row[i] = random.choice(numbers)
		if(0 in row) : row = [0,0,0,0,0,0,0,0,0]
	return row

row4 = rows_4789(4,row4)

def fifthrow(row5) :
	while(0 in row5) :
		for i in range(0,9) :
			numbers = [1,2,3,4,5,6,7,8,9]
			numbers.remove(row1[i])
			numbers.remove(row2[i])
			numbers.remove(row3[i])
			if(i<=2) : 
				for k in range(0,3) :
					if(row4[k] in numbers) : numbers.remove(row4[k])
			if(i<=5 and i>2) : 
				for k in range(3,6) :
					if(row4[k] in numbers) : numbers.remove(row4[k])
			if(i>5) : 
				for k in range(6,9) :
					if(row4[k] in numbers) : numbers.remove(row4[k])
			k=0
			while(k<=i) :
				if(row5[k] in numbers) : numbers.remove(row5[k])
				k=k+1
			if(len(numbers)!=0) : row5[i] = random.choice(numbers)
			else :
				row5 = [0,0,0,0,0,0,0,0,0]
				break
	return row5

row5 = fifthrow(row5)
	
def sixthrow(row6) :
	while(0 in row6[:3]) :
		for i in range(0,3) :
			numbers = [1,2,3,4,5,6,7,8,9]
			numbers.remove(row1[i])
			numbers.remove(row2[i])
			numbers.remove(row3[i])
			if(i<=2) : 
				for k in range(0,3) :
					if(row4[k] in numbers) : numbers.remove(row4[k])
					if(row5[k] in numbers) : numbers.remove(row5[k])
			k=0
			while(k<=i) :
				if(row6[k] in numbers) : numbers.remove(row6[k])
				k=k+1	
			if(len(numbers)!=0) : row6[i] = random.choice(numbers)
			else :
				row6 = [0,0,0,0,0,0,0,0,0]
				break
	while(0 in row6[3:6]) :		
		for i in range(3,6) :
			numbers = [1,2,3,4,5,6,7,8,9]
			numbers.remove(row1[i])
			numbers.remove(row2[i])
			numbers.remove(row3[i])
			if(i<=5 and i>2) : 
				for k in range(3,6) :
					if(row4[k] in numbers) : numbers.remove(row4[k])
					if(row5[k] in numbers) : numbers.remove(row5[k])
			k=0
			while(k<=i) :
				if(row6[k] in numbers) : numbers.remove(row6[k])
				k=k+1	
			if(len(numbers)!=0) : row6[i] = random.choice(numbers)
			else :
				row6[3] = 0
				row6[4] = 0
				row6[5] = 0
				row6[6] = 0
				row6[7] = 0
				row6[8] = 0
				break
	while(0 in row6[6:]) :
		for i in range(6,9) :
			numbers = [1,2,3,4,5,6,7,8,9]
			numbers.remove(row1[i])
			numbers.remove(row2[i])
			numbers.remove(row3[i])
			if(i>5) : 
				for k in range(6,9) :
					if(row4[k] in numbers) : numbers.remove(row4[k])
					if(row5[k] in numbers) : numbers.remove(row5[k])
			k=0
			while(k<=i) :
				if(row6[k] in numbers) : numbers.remove(row6[k])
				k=k+1
			if(len(numbers)!=0) : row6[i] = random.choice(numbers)
			else :
				row6[6]= 0
				row6[7] = 0
				row6[8] = 0
				break
	return row6

row6 = sixthrow(row6)
row7 = rows_4789(7,row7)
row8 = rows_4789(8,row8)
row9 = rows_4789(9,row9)
print('-------------------------------')	
print('| %d  %d  %d | %d  %d  %d | %d  %d  %d |' % (row1[0] , row1[1], row1[2] , row1[3] , row1[4] , row1[5] , row1[6] , row1[7] , row1[8]))
print('| %d  %d  %d | %d  %d  %d | %d  %d  %d |'% (row2[0] , row2[1], row2[2] , row2[3] , row2[4] , row2[5] , row2[6] , row2[7] , row2[8]))
print('| %d  %d  %d | %d  %d  %d | %d  %d  %d |'% (row3[0] , row3[1], row3[2] , row3[3] , row3[4] , row3[5] , row3[6] , row3[7] , row3[8]))
print('-------------------------------')
print('| %d  %d  %d | %d  %d  %d | %d  %d  %d |'% (row4[0] , row4[1], row4[2] , row4[3] , row4[4] , row4[5] , row4[6] , row4[7] , row4[8]))
print('| %d  %d  %d | %d  %d  %d | %d  %d  %d |'% (row5[0] , row5[1], row5[2] , row5[3] , row5[4] , row5[5] , row5[6] , row5[7] , row5[8]))
print('| %d  %d  %d | %d  %d  %d | %d  %d  %d |'% (row6[0] , row6[1], row6[2] , row6[3] , row6[4] , row6[5] , row6[6] , row6[7] , row6[8]))
print('-------------------------------')
print('| %d  %d  %d | %d  %d  %d | %d  %d  %d |'% (row7[0] , row7[1], row7[2] , row7[3] , row7[4] , row7[5] , row7[6] , row7[7] , row7[8]))	
print('| %d  %d  %d | %d  %d  %d | %d  %d  %d |'% (row8[0] , row8[1], row8[2] , row8[3] , row8[4] , row8[5] , row8[6] , row8[7] , row8[8]))	
print('| %d  %d  %d | %d  %d  %d | %d  %d  %d |'% (row9[0] , row9[1], row9[2] , row9[3] , row9[4] , row9[5] , row9[6] , row9[7] , row9[8]))	
print('-------------------------------')