import pandas as pd
import csv
import re

df2 = pd.read_csv("pilpres.csv",sep=';',error_bad_lines=False) #read csv
df3 = df2['text'] #print column text

df = pd.DataFrame(data=df2) #create data frame, df2 is data csv 

split = df.text.str.split(expand=True).stack() #split sentences and expand out into separate column

#When using expand=True, the split elements will expand out into separate columns. 
#And If NaN is present, it is propagated throughout the columns during the split.

# hasil_split = pd.DataFrame({
#     'text': split.values
# })  
wordcount={}
for text in split: #text in split(read above)
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
            print(hasil_benar2_akhir) #print word 

            if hasil_benar2_akhir in wordcount :
                wordcount[hasil_benar2_akhir] = wordcount[hasil_benar2_akhir] + 1
                  
            else: 
                wordcount[hasil_benar2_akhir] = 1
        
        else:
            pass
            
# print(wordcount[hasil_benar2_akhir]) #hasil counts

#Membuat list dan count
# for key,count in list(wordcount.items()): 
#      print(key,':',count)
   