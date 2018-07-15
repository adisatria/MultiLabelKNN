import re, glob, nltk, string, csv, math
import numpy as np
from collections import Counter
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from scipy.spatial import distance
from sklearn.metrics import accuracy_score

num_folds = 10
jumlahK = 3
dominan = 3
dataset = 'PusatBahasaP5000.csv'

factory1 = StopWordRemoverFactory()
stopword = factory1.create_stop_word_remover()

factory2 = StemmerFactory()
stemmer = factory2.create_stemmer()

with open('kamus/katadasar.txt', 'r') as filekatadasar,open('kamus/dict_vocab.txt', 'r') as filevocab, \
        open('kamus/alfabet.txt', 'r') as filealfabet, open('kamus/english.txt','r') as fileenglish:
    katadasar = filekatadasar.read().replace('\n', ',')
    vocab = filevocab.read().replace('\n', ',')
    alfabet = filealfabet.read().replace('\n', ',')
    english = fileenglish.read().replace('\n', ',')

def preprocessing(dataset):
    tokenizing = dataset.split(' ')
    hasilprepro = []
    for i in range(len(tokenizing)):
        teks = re.sub('(\d)+(\.)*(\d)*', '', tokenizing[i])  # hapus digit
        teks = re.sub('[/+@.,%-%^*"!#-$-\']', '', teks)  # hapus simbol
        teks = teks.lower()

        #stopword removal
        prestopword = stopword.remove(teks)

        if prestopword not in alfabet:
            if prestopword not in english:
                if len(prestopword)>3:
                    if prestopword in vocab and prestopword != '':
                        hasilstem = stemmer.stem(prestopword)
                        if hasilstem in katadasar and hasilstem != '':
                            hasilprepro.append(hasilstem)
    return hasilprepro

def preprocessingTanpaStemm(dataset):
    tokenizing = dataset.split(' ')
    hasilprepro = []
    for i in range(len(tokenizing)):
        teks = re.sub('(\d)+(\.)*(\d)*', '', tokenizing[i])  # hapus digit
        teks = re.sub('[/+@.,%-%^*"!#-$-\']', '', teks)  # hapus simbol
        teks = teks.lower()

        #stopword removal
        prestopword = stopword.remove(teks)

        if prestopword not in alfabet:
            if prestopword not in english:
                if len(prestopword)>3:
                    if prestopword in vocab and prestopword != '':
                        hasilprepro.append(prestopword)
    return hasilprepro

def bacafile(filename):
    semua = []
    simpanLabel = []
    trueLabelFasilitas = []
    trueLabelLayanan = []
    idDataTFIDF = []
    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            print("Data ke-", row[0])
            if row:
                HasilPrepro = preprocessingTanpaStemm(row[1])
                dataLabel = row[2:5]
                dataLabel = [int(j) for j in dataLabel]
                simpanLabel.append(dataLabel)
                trueLabelFasilitas.append(dataLabel[0])
                trueLabelLayanan.append(dataLabel[1])
                semua.append(HasilPrepro)
                idDataTFIDF.append(int(row[0]))
            else:
                continue
            #print(HasilPrepro)
    return semua, simpanLabel, idDataTFIDF, trueLabelFasilitas, trueLabelLayanan

def tfidf():
    panjangTang, simpanLabel, idDataTFIDF, trueLabelFasilitas, trueLabelLayanan = bacafile(dataset)
    daftarDokumen = {}
    # tampung data dari direktori ke variable daftarDokumen
    for i in range(len(panjangTang)):
        daftarDokumen[i] = Counter(panjangTang[i])

    print(len(panjangTang))
    # print("handle data ", handledata)
    print("panjang tanggapan ", panjangTang)
    print("daftar dokumen ", daftarDokumen)

    # menampung daftar string
    daftarString = []
    for key, val in daftarDokumen.items():  # melompati(loop over) key di kamus
        for word, count_w in val.items():
            if word not in daftarString:
                daftarString.append(word)  # append untuk menambah objek word baru kedalam list

    print("daftar string : ", daftarString)
    # Membuat TF
    with open('hasil/TF.csv', 'w', newline='') as csvfile, open('hasil/IDF.csv', 'w', newline='') as csvfileIDF, open('hasil/TFxIDF5000.csv', 'w', newline='') as csvfileTFIDF:
        reswriterTFIDF = csv.writer(csvfileTFIDF, delimiter=',', quotechar='|')
        reswriterIDF = csv.writer(csvfileIDF, delimiter=',', quotechar='|')
        reswriter = csv.writer(csvfile, delimiter=',', quotechar='|')
        tempWord = [' ']
        tempWord.extend(daftarString)  # menambah string2 dari variable daftarString ke tempWord
        reswriter.writerow(tempWord)  # write 1 row
        reswriterIDF.writerow(tempWord)  # write 1 row
        reswriterTFIDF.writerow(tempWord)  # write 1 row
        secondDF = []
        TF = []
        ############### TF ###################
        for i in range(len(panjangTang)):
            rowjudul = str(i)
            # hitung pertanggapan
            words = panjangTang[i]
            x = []
            currentDF = []
            for j in range(len(daftarString)):
                temp = daftarString[j]
                count = 0
                for k in range(len(words)):
                    if (temp == words[k]):
                        count += 1
                # Frequency weighting
                if count > 0:
                    count = round(1 + np.log(count), 2)
                    currentDF.append(1)
                else:
                    currentDF.append(0)
                x.append(count)

            x.insert(0, rowjudul)
            TF.append(x)
            reswriter.writerow(x)
            secondDF.append(currentDF)
        ############### TF ###################

        ############### IDF ###################
        hasilDF = []
        for i in range(len(secondDF)):
            first = []
            second = []
            dalem = secondDF[i]
            if i == 0:
                for j in range(len(dalem)):
                    hasilDF.append(dalem[j])
            else:
                for j in range(len(dalem)):
                    first.append(hasilDF[j])
                    second.append(dalem[j])
                hasilDF = []
            for k in range(len(first)):
                hasilDF.append(first[k] + second[k])
        # print("ini baru DF :", hasilDF)

        IDF=[]
        for j in range(len(hasilDF)):
            if hasilDF[j]==0:
                IDF.append(0)
            else:
                nilaiutkIDF = len(panjangTang)/hasilDF[j]
                nilaiIDF = math.log(nilaiutkIDF,10)
                IDF.append(nilaiIDF)
        #print("Hasil IDFnya :", IDF)
        IDF.insert(0,"IDFnya")
        # reswriterIDF.writerow(IDF)
        ############### IDF ###################

        ############### TFxIDF ###################
        TFxIDF =[]
        for k in range(len(TF)):
            dalem = TF[k]
            sumTFIDF = []
            for i in range(len(dalem)):
                if i == 0:
                    continue
                else:
                    sumTFIDF.append(dalem[i]*IDF[i])
            # sumTFIDF.insert(0, rowjudul)
            # reswriterTFIDF.writerow(sumTFIDF)
            TFxIDF.append(sumTFIDF)
        ############### TFxIDF ###################
        return TFxIDF, simpanLabel, idDataTFIDF, trueLabelFasilitas, trueLabelLayanan

def sort_list(data):
    return sorted(data)

def KNN():
    with open('5000withStemmingK9.csv', 'w',newline='')as nulishasil:
        DataSistem = csv.writer(nulishasil, delimiter=',', quotechar='|')

        headerHasilSistem = ['ID', 'Sentimen Fasilitas', 'Sentimen Layanan']
        DataSistem.writerow(headerHasilSistem)
        tempTFIDF, simpanLabel, idDataTFIDF, trueLabelFasilitas, trueLabelLayanan = tfidf()
        print(simpanLabel)
        print("ten tfidf ",len(tempTFIDF))
        print("len id ",len(idDataTFIDF))
        # k fold
        HasilAkhir = []
        predicLabelFasilitas = []
        predicLabelLayanan = []
        subset_size = int(len(tempTFIDF) / num_folds)
        for i in range(num_folds):
            testing_this_round = idDataTFIDF[i * subset_size:][:subset_size]
            training_this_round = idDataTFIDF[:i * subset_size] + idDataTFIDF[(i + 1) * subset_size:]

            print('============== k', i + 1, ' ==============')
            print('testing : ', testing_this_round)
            print('length testing : ', len(testing_this_round))
            print('length training : ', len(training_this_round))
            # finalData = []
            for cluster in range(len(testing_this_round)):
                nilaiEuclid = []
                euclidBelumTerurut = []
                id = testing_this_round[cluster]  # ambil id dalam data testing
                dataTesting = tempTFIDF[id]
                nilaiEuclid.append(testing_this_round[cluster])
                for k in range(len(training_this_round)):
                    # k += 1
                    idTraining = training_this_round[k]
                    dataTraining = tempTFIDF[idTraining]
                    # print(dataTraining)
                    dst = distance.euclidean(dataTesting, dataTraining)  # menghitung euclidean
                    # print("distance ", distance)
                    idDanDistance = []  # menyimpan id training dan nilai euclid
                    idDanDistance.append(idTraining)
                    idDanDistance.append(dst)
                    nilaiEuclid.append(idDanDistance)
                    euclidBelumTerurut.append(dst)
                # finalData.append(nilaiEuclid)
                # print("euclidean :",nilaiEuclid)

                # ------------------ KNN K -------------------#
                euclidTerurut=sort_list(euclidBelumTerurut)
                euclidTerurut = euclidTerurut[:jumlahK]
                # print("euclid terurut :", euclidTerurut)

                idEuclidTerurut = []  # mengambil id dari id TFIDF berdasarkan nilai euclidean terkecil
                for k in range(len(euclidTerurut)):
                    for l in range(len(nilaiEuclid[1:])):
                        # print(nilaiEuclid[1:][l][0])
                        if nilaiEuclid[1:][l][0] in idEuclidTerurut:
                            continue
                        elif euclidTerurut[k] == nilaiEuclid[1:][l][1]:
                            # print(nilaiEuclid[1:][l])
                            idEuclidTerurut.append(nilaiEuclid[1:][l][0])
                            break
                # print("id euclidean terurut :", idEuclidTerurut)

                # mencari label untuk data testing
                totalBiner = []
                for o in range(len(idEuclidTerurut)):
                    biner = simpanLabel[idEuclidTerurut[o]][0:]
                    totalBiner.append(biner)
                # print("total biner :", totalBiner)

                labelHasil = []
                labelHasil.append(nilaiEuclid[0])
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
                print("label hasil prediksi", labelHasil[0], ":", labelHasil[1:])

                hasilSementara = []  # menyimpan label dan nomor kalimat
                DataSistem.writerow(labelHasil)
                HasilAkhir.append(labelHasil)
                predicLabelFasilitas.append(labelHasil[0])
                predicLabelLayanan.append(labelHasil[1])
        # mendapatkan ID untuk data testing
        # print("ID testing :", IDtesting) #PENTING
        print("p true F ", len(trueLabelFasilitas))
        print("p predic F ", len(predicLabelFasilitas))
        akurasiFasilitas = accuracy_score(trueLabelFasilitas, predicLabelFasilitas)
        akurasiLayanan = accuracy_score(trueLabelLayanan, predicLabelLayanan)
        TotalAkurasi = ((akurasiFasilitas + akurasiLayanan) / 2) * 100
        print("Akurasi Fasilitas : ", akurasiFasilitas)
        print("Akurasi Layanan : ", akurasiLayanan)
        print("Akurasi Total : ", TotalAkurasi)
    print("Hasil akhir :", HasilAkhir)  #
    print("\n")

KNN()