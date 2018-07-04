import csv
import numpy as np
from sklearn.metrics import accuracy_score

def pakaiStemming():
    with open("dataKelas.csv",'r')as trueLbl, open("5000withStemmingk3.csv",'r')as stem3, open("5000withStemmingk5.csv",'r')as stem5, \
            open("5000withStemmingk7.csv",'r')as stem7, open("5000withStemmingk9.csv",'r')as stem9:
        trueLabel = csv.reader(trueLbl, delimiter=',')
        labelStem3 = csv.reader(stem3, delimiter=',')
        labelStem5 = csv.reader(stem5, delimiter=',')
        labelStem7 = csv.reader(stem7, delimiter=',')
        labelStem9 = csv.reader(stem9, delimiter=',')

        trueLabelFasilitas = []
        trueLabelLayanan = []
        for row in trueLabel:
            trueLabelFasilitas.append(int(row[1]))
            trueLabelLayanan.append(int(row[2]))

        stemm3Fasilitas = []
        stemm3Layanan = []
        for row in labelStem3:
            stemm3Fasilitas.append(int(row[1]))
            stemm3Layanan.append(int(row[2]))

        stemm5Fasilitas = []
        stemm5Layanan = []
        for row in labelStem5:
            stemm5Fasilitas.append(int(row[1]))
            stemm5Layanan.append(int(row[2]))

        stemm7Fasilitas = []
        stemm7Layanan = []
        for row in labelStem7:
            stemm7Fasilitas.append(int(row[1]))
            stemm7Layanan.append(int(row[2]))

        stemm9Fasilitas = []
        stemm9Layanan = []
        for row in labelStem9:
            stemm9Fasilitas.append(int(row[1]))
            stemm9Layanan.append(int(row[2]))

        akurasiStem3F = accuracy_score(trueLabelFasilitas,stemm3Fasilitas)
        akurasiStem3L = accuracy_score(trueLabelLayanan, stemm3Layanan)
        TotalStem3 = ((akurasiStem3F+akurasiStem3L)/2)*100
        print("============== Stemming ==============")
        print("Hasil Akurasi k=3 (Stemming)")
        print("Kategori Fasilitas :",akurasiStem3F)
        print("Kategori Layanan :", akurasiStem3L)
        print("Rata-rata :", TotalStem3,"\n")

        akurasiStem5F = accuracy_score(trueLabelFasilitas, stemm5Fasilitas)
        akurasiStem5L = accuracy_score(trueLabelLayanan, stemm5Layanan)
        TotalStem5 = ((akurasiStem5F + akurasiStem5L) / 2)*100
        print("Hasil Akurasi k=5 (Stemming)")
        print("Kategori Fasilitas :", akurasiStem5F)
        print("Kategori Layanan :", akurasiStem5L)
        print("Rata-rata :", TotalStem5, "\n")

        akurasiStem7F = accuracy_score(trueLabelFasilitas, stemm7Fasilitas)
        akurasiStem7L = accuracy_score(trueLabelLayanan, stemm7Layanan)
        TotalStem7 = ((akurasiStem7F + akurasiStem7L) / 2) * 100
        print("============== Stemming ==============")
        print("Hasil Akurasi k=3 (Stemming)")
        print("Kategori Fasilitas :", akurasiStem7F)
        print("Kategori Layanan :", akurasiStem7L)
        print("Rata-rata :", TotalStem7, "\n")

        akurasiStem9F = accuracy_score(trueLabelFasilitas, stemm9Fasilitas)
        akurasiStem9L = accuracy_score(trueLabelLayanan, stemm9Layanan)
        TotalStem9  = ((akurasiStem9F + akurasiStem9F) / 2) * 100
        print("============== Stemming ==============")
        print("Hasil Akurasi k=9 (Stemming)")
        print("Kategori Fasilitas :", akurasiStem9F)
        print("Kategori Layanan :", akurasiStem9L)
        print("Rata-rata :", TotalStem9, "\n")

def tanpaStemming():
    with open("dataKelas.csv",'r')as trueLbl, open("5000withoutStemmingk3.csv",'r')as stem3, open("5000withoutStemmingk5.csv",'r')as stem5\
            , open("5000withoutStemmingk7.csv",'r')as stem7, open("5000withoutStemmingk9.csv",'r')as stem9:
        trueLabel = csv.reader(trueLbl, delimiter=',')
        labelTStem3 = csv.reader(stem3, delimiter=',')
        labelTStem5 = csv.reader(stem5, delimiter=',')
        labelTStem7 = csv.reader(stem7, delimiter=',')
        labelTStem9 = csv.reader(stem9, delimiter=',')

        trueLabelFasilitas = []
        trueLabelLayanan = []
        for row in trueLabel:
            trueLabelFasilitas.append(int(row[1]))
            trueLabelLayanan.append(int(row[2]))

        Tstemm3Fasilitas = []
        Tstemm3Layanan = []
        for row in labelTStem3:
            Tstemm3Fasilitas.append(int(row[1]))
            Tstemm3Layanan.append(int(row[2]))

        Tstemm5Fasilitas = []
        Tstemm5Layanan = []
        for row in labelTStem5:
            Tstemm5Fasilitas.append(int(row[1]))
            Tstemm5Layanan.append(int(row[2]))

        Tstemm7Fasilitas = []
        Tstemm7Layanan = []
        for row in labelTStem7:
            Tstemm7Fasilitas.append(int(row[1]))
            Tstemm7Layanan.append(int(row[2]))

        Tstemm9Fasilitas = []
        Tstemm9Layanan = []
        for row in labelTStem9:
            Tstemm9Fasilitas.append(int(row[1]))
            Tstemm9Layanan.append(int(row[2]))

        akurasiTStem3F = accuracy_score(trueLabelFasilitas,Tstemm3Fasilitas)
        akurasiTStem3L = accuracy_score(trueLabelLayanan, Tstemm3Layanan)
        TotalTStem3 = ((akurasiTStem3F + akurasiTStem3L) / 2)*100
        print("============== Tanpa Stemming ==============")
        print("Hasil Akurasi k=3 (Tanpa Stemming)")
        print("Kategori Fasilitas :",akurasiTStem3F)
        print("Kategori Layanan :", akurasiTStem3L)
        print("Rata-rata : ",TotalTStem3,"\n")

        akurasiTStem5F = accuracy_score(trueLabelFasilitas, Tstemm5Fasilitas)
        akurasiTStem5L = accuracy_score(trueLabelLayanan, Tstemm5Layanan)
        TotalTStem5 = ((akurasiTStem5F + akurasiTStem5L) / 2)*100
        print("Hasil Akurasi k=5 (Tanpa Stemming)")
        print("Kategori Fasilitas :", akurasiTStem5F)
        print("Kategori Layanan :", akurasiTStem5L)
        print("Rata-rata : ", TotalTStem3,"\n")

        akurasiTStem7F = accuracy_score(trueLabelFasilitas, Tstemm7Fasilitas)
        akurasiTStem7L = accuracy_score(trueLabelLayanan, Tstemm7Layanan)
        TotalTStem7 = ((akurasiTStem7F + akurasiTStem7L) / 2) * 100
        print("Hasil Akurasi k=5 (Tanpa Stemming)")
        print("Kategori Fasilitas :", akurasiTStem7F)
        print("Kategori Layanan :", akurasiTStem7L)
        print("Rata-rata : ", TotalTStem7, "\n")

        akurasiTStem9F = accuracy_score(trueLabelFasilitas, Tstemm9Fasilitas)
        akurasiTStem9L = accuracy_score(trueLabelLayanan, Tstemm9Layanan)
        TotalTStem9 = ((akurasiTStem9F + akurasiTStem9L) / 2) * 100
        print("Hasil Akurasi k=5 (Tanpa Stemming)")
        print("Kategori Fasilitas :", akurasiTStem9F)
        print("Kategori Layanan :", akurasiTStem9L)
        print("Rata-rata : ", TotalTStem9, "\n")
pakaiStemming()
tanpaStemming()