import pandas as pd
import csv
import re
import nltk

doc1 = pd.read_csv("pilpres6.csv",sep=';',error_bad_lines=False) #read csv DOC 1
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
            hasil_benar2_akhir_2 = hapus_koma
            

            if hasil_benar2_akhir_2 in wordcount2 :
                wordcount2[hasil_benar2_akhir_2] = wordcount2[hasil_benar2_akhir_2] + 1
                  
            else: 
                wordcount2[hasil_benar2_akhir_2] = 1
        
        else:
            pass
                       
# print(wordcount[hasil_benar2_akhir]) #hasil counts

#Membuat list dan count
# for key,count in list(wordcount.items()): 
#      print('WORD 1')
#      print(key,':',count)

# #Membuat list dan count
# for key,count in list(wordcount2.items()): 
#      print('WORD 2')
#      print(key,':',count)


# CODE WITH ALGORITMA JACCARD DISTANCE 
def get_jaccard_sim(hasil_benar2_akhir, hasil_benar2_akhir_2): 
    doc1 = set(hasil_benar2_akhir)
    doc2 = set(hasil_benar2_akhir_2)
    c = doc1.intersection(doc2)
    
    # nltk.jaccard_distance(doc1, doc2)
    print (float(len(c)) / (len(doc1) + len(doc2) - len(c)), 'Jaccard Distance between doc1 and doc2')


get_jaccard_sim(hasil_benar2_akhir,hasil_benar2_akhir_2)    


