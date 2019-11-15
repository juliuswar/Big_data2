import pandas as pd
import numpy as np
import csv
import re



doc1 = pd.read_csv("pilpres2.csv",sep=';',error_bad_lines=False) #read csv DOC 1
doc2 = pd.read_csv("pilpres2.csv",sep=';',error_bad_lines=False) #read csv DOC 2
# df3 = doc1['text'] #print column text

df_doc1 = pd.DataFrame(data=doc1) #create data frame, doc1 is data csv 
df_doc2 = pd.DataFrame(data=doc2) #create data frame, doc1 is data csv 

split_doc1 = df_doc1.text.str.split(expand=True).stack() #split sentences and expand out into separate column
split_doc2 = df_doc2.text.str.split(expand=True).stack() #split sentences and expand out into separate column

#When using expand=True, the split elements will expand out into separate columns. 
#And If NaN is present, it is propagated throughout the columns during the split.

# hasil_split = pd.DataFrame({
#     'text': split.values
# # })  

# DOC 1
wordcount={}
for text in split_doc1: #text in split(read above)
    if re.search(r'(^#)', text)  : #if there is the word '#' in text(split)  
                              #then print word(text). and if none word '#' then nothing action
        
        op = re.compile(r'.+?(?=.ttp.*)',re.S) #...(http ...) memisahkan kata http dan word yang mengikuti setelah nya
        hasil1 = op.sub('',text) #kata yang dicari diganti '',dan kata itu pindah bawah sebelum kata tersebut
        hapus1 = re.compile(r'h.*',re.S) #compile kata 
        hapus_fin = hapus1.sub("",hasil1) #hapus kata semua kata dimulai .t
        
        op2 = re.compile(r'.+?(?=.tw)',re.S) # ...(compile kata sebelum kata .tw) memisahkan
        hasil2 = op2.sub('',hapus_fin) #kata yang dicari diganti '',dan kata itu pindah bawah sebelum kata tersebut
        hapus2 = re.compile(r'\.t.*',re.S) #compile kata yang dicari
        hapus_fin2 = hapus2.sub("",hasil2)#hapus kata semua kata dimulai .t
        
        if hapus_fin2.startswith('#'): 
            cari_titik = re.compile(r'\.',re.S)
            hapus_titik = cari_titik.sub('',hasil2)
            cari_koma = re.compile(r'\,',re.S)
            hapus_koma = cari_koma.sub("",hapus_titik)
            hasil_benar2_akhir = hapus_koma
       
            if hasil_benar2_akhir in wordcount :
                wordcount[hasil_benar2_akhir] = wordcount[hasil_benar2_akhir] + 1
                  
            else: 
                wordcount[hasil_benar2_akhir] = 1
        
        else:
            pass
        

# DOC 2
wordcount2={}
for text2 in split_doc2: #text in split(read above)
    if re.search(r'(^#)', text2)  : #if there is the word '#' in text(split)  
                              #then print word(text). and if none word '#' then nothing action
        
        op = re.compile(r'.+?(?=.ttp.*)',re.S) #...(http ...) memisahkan kata http dan word yang mengikuti setelah nya
        hasil1 = op.sub('',text2) #kata yang dicari diganti '',dan kata itu pindah bawah sebelum kata tersebut
        hapus1 = re.compile(r'h.*',re.S) #compile kata 
        hapus_fin = hapus1.sub("",hasil1) 
        
        op2 = re.compile(r'.+?(?=.tw)',re.S) # ...(compile kata sebelum kata .tw) memisahkan
        hasil2 = op2.sub('',hapus_fin) #kata yang dicari diganti '',dan kata itu pindah bawah sebelum kata tersebut
        hapus2 = re.compile(r'\.t.*',re.S) #compile kata yang dicari
        hapus_fin2 = hapus2.sub("",hasil2)#hapus kata semua kata dimulai .t
        
        if hapus_fin2.startswith('#'): 
            cari_titik = re.compile(r'\.',re.S)
            hapus_titik = cari_titik.sub('',hasil2)
            cari_koma = re.compile(r'\,',re.S)
            hapus_koma = cari_koma.sub("",hapus_titik)
            hasil_benar2_akhir_2 = hapus_koma
            

            if hasil_benar2_akhir_2 in wordcount2 :
                wordcount2[hasil_benar2_akhir_2] = wordcount2[hasil_benar2_akhir_2] + 1
                  
            else: 
                wordcount2[hasil_benar2_akhir_2] = 1
        
        else:
            pass
                       
# # Jumlah Data
# print(wordcount[hasil_benar2_akhir]) #hasil counts
# print(wordcount2[hasil_benar2_akhir_2]) #hasil counts

# Membuat list dan count
# for key,count in list(wordcount.items()): 
#      print('WORD 1')
#      print(key,':',count)

# Membuat list dan count
# for key,count in list(wordcount2.items()): 
#      print('WORD 2')
#      print(key,':',count)

# CODE WITH ALGORITMA JACCARD DISTANCE
def get_jaccard_sim(list1, list2): 
    doc1 = set(list1)
    doc2 = set(list2)
    c = doc1.intersection(doc2)

    hasil = float(len(c)) / (len(doc1) + len(doc2) - len(c))
    # print(hasil)
    return hasil
    
# print(5*'=','#Doc 1 = Doc 2 ')  
# #DOC 1 = Doc 2
# a = get_jaccard_sim(wordcount.keys(),wordcount2.keys())

#Tabel
def TabelJaccard(vardoc,vardoc2):
    lenList = len(set(vardoc)) #panjang list pada doc tersebut
    lenList2 = len(set(vardoc2)) #panjang list pada doc tersebut
    jarr = np.empty([lenList,lenList2]) #Return a new array of given shape and type, without initializing entries
    for i in range(lenList): # var i masuk jangkauan var Lenglist 
        for j in range(lenList2): #var i masuk jangkauan var Lenglist 
            if(i>j):
                jc = get_jaccard_sim(vardoc[i],vardoc2[j]) #var jc = manggil function jaccard (doc1[x],doc1[y])
                jarr[i][j] = jc #doc1[1][0]
                jarr[j][i] = jc #doc1[0][1]
       
            if lenList  == lenList2:   
                jc = get_jaccard_sim(vardoc[i],vardoc2[j]) #var jc = manggil function jaccard (doc1[x],doc1[y])
                jarr[i][j] = jc #doc1[1][0]
                jarr[j][i] = jc #doc1[0][1]
       
    
    return jarr

Doc1=wordcount.keys()
Doc2=wordcount2.keys()    
df_tabel = pd.DataFrame(data=TabelJaccard(Doc1,Doc2),index=Doc2,columns=Doc1)

# index=Doc[:1215] itu batas data sampai 1215. karna Doc 1 nya hanya 1215
print(df_tabel)


