import math
import numpy as np
import csv

num_folds = 10
jumlahK = 3
dominan = 3


def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)

def BubbleSort(val):
    for passnum in range(len(val) - 1, 0, -1):
        for i in range(passnum):
            if val[i] > val[i + 1]:
                temp = val[i]
                val[i] = val[i + 1]
                val[i + 1] = temp

def main2():
    with open('TFxIDF_5000.csv', 'r') as tfidf, open('dataKelas.csv') as bukacsv, open('hasilsistem.csv', 'w',
                                                                                     newline='')as nulishasil:
        DataTFIDF = csv.reader(tfidf, delimiter=',')
        DataLabel = csv.reader(bukacsv, delimiter=',')
        DataSistem = csv.writer(nulishasil, delimiter=',', quotechar='|')
        tempTFIDF = []
        idDataTFIDF = []
        for row in DataTFIDF:
            if row[0] == ' ':
                continue
            else:
                tempTFIDF.append(row[1:])
                idDataTFIDF.append(row[0])
        # data berisi label
        simpanLabel = []
        for row in DataLabel:
            simpanLabel.append(row)

        # k fold
        HasilAkhir = []

        subset_size = int(len(tempTFIDF) / num_folds)
        for i in range(num_folds):
            testing_this_round = idDataTFIDF[i * subset_size:][:subset_size]
            training_this_round = idDataTFIDF[:i * subset_size] + idDataTFIDF[(i + 1) * subset_size:]

            #ubah jadi integer
            testing_this_round = [int(x) for x in testing_this_round]
            training_this_round = [int(x) for x in training_this_round]
            # print('\n')
            print('============== k', i + 1, ' ==============')
            print('training : ', training_this_round)
            print("p training : ", len(training_this_round))
            print('testing : ', testing_this_round)
            print('p testing :', len(testing_this_round))

            # IDtesting = []
            # for j in [j for j, x in enumerate(tempTFIDF) if x in testing_this_round]:
            #     if len(IDtesting) == len(testing_this_round):
            #         break
            #     else:
            #         IDtesting.append(j)
            # print("ID testing : ", IDtesting)
            # print("pjg id testing : ", len(IDtesting))
            #
            # trainingID = []
            # for j in [j for j,x in enumerate(tempTFIDF) if x in training_this_round]:
            #     if len(trainingID) == len(training_this_round):
            #         break
            #     else:
            #         trainingID.append(j)
            # print("ID training : ", trainingID)
            # print("pjg id training : ", len(trainingID))
            # ---------------------------------------------------#
            finalData = []
            for cluster in range(len(testing_this_round)):
                nilaiEuclid = []
                id =  testing_this_round[cluster] #ambil id dalam data testing
                dataTesting = tempTFIDF[id]
                dataTesting = [float(x) for x in dataTesting]
                nilaiEuclid.append(testing_this_round[cluster])
                for k in range(len(training_this_round)):
                    idTraining = training_this_round[k]
                    dataTraining = [float(y) for y in tempTFIDF[idTraining]]
                    distance = euclideanDistance(dataTesting, dataTraining, 1546)  # menghitung euclidean
                    # print("distance ", distance)
                    idDanDistance = [] #menyimpan id training dan nilai euclid
                    idDanDistance.append(idTraining)
                    idDanDistance.append(distance)
                    nilaiEuclid.append(idDanDistance)
                finalData.append(nilaiEuclid)
                print("euclidean :",nilaiEuclid)

                # ------------------ KNN K -------------------#
                idDanEculid = nilaiEuclid[1:]
                euclidTerurut = []
                for k in range(len(idDanEculid)):
                    euclidTerurut.append(idDanEculid[k][1])

                BubbleSort(euclidTerurut)
                euclidTerurut = euclidTerurut[:jumlahK]
                print("euclid terurut :", euclidTerurut)

                idEuclidTerurut = [] #mengambil id dari id TFIDF berdasarkan nilai euclidean terkecil
                for k in range(len(euclidTerurut)):
                    for l in range(len(nilaiEuclid[1:])):
                        if nilaiEuclid[1:][l][0] in idEuclidTerurut:
                            continue
                        elif euclidTerurut[k] == nilaiEuclid[1:][l][1]:
                            # print(nilaiEuclid[1:][l])
                            idEuclidTerurut.append(nilaiEuclid[1:][l][0])
                            break
                print("id euclidean terurut :", idEuclidTerurut)

                # mencari label untuk data testing
                totalBiner = []
                for o in range(len(idEuclidTerurut)):
                    biner = simpanLabel[idEuclidTerurut[o]][1:]
                    biner = [int(x) for x in biner]
                    totalBiner.append(biner)
                print("total biner :", totalBiner)

                labelHasil = []
                # print("label hasil :",labelHasil)#PENTING
                # print("cluster ",cluster)#PENTING
                for k in range(len(totalBiner[0])):
                    # print("k ",k)
                    count1 = 0
                    count0 = 0
                    for o in range(len(totalBiner)):
                        # print(totalBiner[o][k])
                        if totalBiner[o][k] == 1:
                            count1 += 1
                        elif totalBiner[o][k] == 0:
                            count0 += 1
                    if count1 > count0:
                        labelHasil.append(1)
                    elif count0 > count1:
                        labelHasil.append(0)
                print("label hasil :",labelHasil)

                hasilSementara = []  # menyimpan label dan nomor kalimat
                hasilSementara.append(nilaiEuclid[0])
                hasilSementara.append(labelHasil)
                DataSistem.writerow(hasilSementara)
                HasilAkhir.append(hasilSementara)
                print('==============================================================')
        # mendapatkan ID untuk data testing
        # print("ID testing :", IDtesting) #PENTING

    print("Hasil akhir :", HasilAkhir) #
    print("\n")
    # print("panjang hasil akhir :", len(HasilAkhir))


main2()
