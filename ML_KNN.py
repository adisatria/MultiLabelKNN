import math
import numpy as np
import csv

def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

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

def main2():
	with open('TFxIDF2.csv') as tfidf, open('kelas.csv') as bukacsv:
		dataCSV = csv.reader(tfidf, delimiter=',')
		DataLabel = csv.reader(bukacsv, delimiter=',')
		tampung = []
		for row in dataCSV:
			if row[0] == ' ':
				continue
			else:
				tampung.append(row[1:])

		#data berisi label
		simpanLabel = []
		for row in DataLabel:
			simpanLabel.append(row)

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

				noUrut = []
				for j in [j for j, x in enumerate(tampung) if x in tempUrutan]:
					# noUrut.insert(0,j)
					noUrut.append(j)
				print("no urut ",noUrut)

				#mencari label untuk data testing
				totalBiner = []
				for o in range(len(noUrut)):
					print(noUrut[o])
					# print(simpanLabel[noUrut[o]])
					label = []
					kelas = []
					for m in range(len(simpanLabel[noUrut[o]])):
						# print(simpanLabel[noUrut[o]][m])
						noLabel, noKelas = simpanLabel[noUrut[o]][m].split(" ")
						label.append(noLabel)
						kelas.append(noKelas)
					print("label :", label)
					print("kelas :", kelas)

					label2 = [int(x) for x in label]
					biner = []
					indexKelas = 0
					for p in range(7):
						if p == 0:
							continue
						elif p in label2:
							biner.append(int(kelas[indexKelas]))
							indexKelas += 1
						else:
							biner.append(0)
					# print(biner)
					totalBiner.append(biner)
				print(totalBiner)

				labelClass = [1, 2, 4]
				for k in range(len(labelClass)):
					for o in range(len(totalBiner[0])):
						tambah = 0
						for p in range(len(totalBiner)):
							# print(data[j][i])
							if totalBiner[p][o] == labelClass[k]:
								tambah += 1
						if tambah >= 3:
							print(o, "yuhu")


main2()
