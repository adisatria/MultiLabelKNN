import math
import ast
import numpy as np
import sys, argparse, csv

#
# def column(matrix, i):
#     return [row[i] for row in matrix]

def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)
#
# data1 = ['0','1']
# data2 = ['2','3']
# distance = euclideanDistance(data1, data2, 2)
# print ('Distance: ' + repr(distance))
def k_fold_validation():
	training = [[2.11, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [9, 3, 6, 2], [3, 6, 3, 8], [3, 8, 8, 9],
				[12, 24, 6, 12], [22, 25, 63, 11]]
	num_folds = 3
	subset_size = int(len(training) / num_folds)
	print(training[1][:2])
	for i in range(num_folds):
		testing_this_round = training[i * subset_size:][:subset_size]
		training_this_round = training[:i * subset_size] + training[(i + 1) * subset_size:]
		print('\n')
		print('============== k', i + 1, ' ==============')
		print('training : ', training_this_round)
		print('testing : ', testing_this_round)

def main():
	with open('TFxIDF2.csv') as tfidf:
		data= csv.reader(tfidf, delimiter=',')

		tampung = []
		for row in data:
			tampung.append(row)
		# print(tampung[11])
		# data=[1,2,3,4]
		print(tampung[1])
		blok1 = tampung[1:5]
		tampung2=[]
		for i in range(len(blok1)):
			results = blok1[i][1:]
			results = [float(j) for j in results]
			Datatest = [float(k) for k in tampung[11][1:]]
			distance = euclideanDistance(results, Datatest, 1963)

			tampung2.append(distance)

		tampung2.insert(0, tampung[11][0])
		print(tampung2)
		print(tampung[11][0])

def main2():
	with open('TFxIDF2.csv') as tfidf:
		dataCSV = csv.reader(tfidf, delimiter=',')
		tampung = []
		for row in dataCSV:
			if row[0] == ' ':
				continue
			else:
				tampung.append(row[1:])

		#k fold
		num_folds = 6
		subset_size = int(len(tampung) / num_folds)
		for i in range(num_folds):
			testing_this_round = tampung[i * subset_size:][:subset_size]
			training_this_round = tampung[:i * subset_size] + tampung[(i + 1) * subset_size:]
			print('\n')
			print('============== k', i + 1, ' ==============')
			print('training : ', training_this_round)
			print("p training : ", len(training_this_round))
			print('testing : ', testing_this_round)
			print('p testing :', len(testing_this_round))

			#####################################################
			finalData = []
			for j in range(len(testing_this_round)):
				dataTesting = testing_this_round[j]
				dataTesting = [float(x) for x in dataTesting]
				nilaiEuclid = []
				for k in range(len(training_this_round)):
					dataTraining = [float(y) for y in training_this_round[k]]
					distance = euclideanDistance(dataTraining, dataTesting, 1963) #menghitung euclidean
					nilaiEuclid.append(distance)
				finalData.append(nilaiEuclid)
			# tampung2.insert(0, tampung[10][0])
				print("____________________________________________________________")
				print("nilai euclidean :", nilaiEuclid)
				print('panjang tampung2 :', len(nilaiEuclid))
				# ------------------ KNN K -------------------#
				finalDataNP = np.array(nilaiEuclid) #memasukkan list ke dalama array numpy
				k = 5
				idx = np.argpartition(finalDataNP, k) #mengurutkan dari yg terkecil sejumlah k
				hasil = finalDataNP[idx[:k]] #mengurutkan dari yg terkecil sejumlah k
				print("hasil k :", hasil)
				# print('\n')

				tempUrutan = []
				for j in [j for j, x in enumerate(nilaiEuclid) if x in hasil]:
					print(j," :",training_this_round[j])
					tempUrutan.append(training_this_round[j])

				for j in [j for j, x in enumerate(tampung) if x in tempUrutan]:
					print(j)
		# for i in range(len(finalData)):
			# 	print("____________________________________________________________")
			# 	print("nilai euclidean ",i,":",finalData[i])
			# 	print('panjang tampung2 :', len(finalData[i]))
			# 	#------------------ KNN K -------------------#
			# 	finalDataNP = np.array(finalData[i])
			# 	k = 3
			# 	idx = np.argpartition(finalDataNP, k)
			# 	hasil = finalDataNP[idx[:k]]
			# 	print("hasil k :",hasil)
			# 	# print('\n')
            #
			# 	for j in [j for j, x in enumerate(finalData[i]) if x in hasil]:
			# 		print(j)
			# # print(tampung[10][0])


main2()
