import pandas as pd
import csv
import re

df2 = pd.read_csv("pilpres.csv",sep=';',error_bad_lines=False) #read csv
df3 = df2['text'] #print column text

# with open('pilpres.csv') as csv_file:
#1
# for row in df3:
        # for cell in row:
        #     # cell = re.sub(r'[^\w=]', '',cell)
        #     print cell
 
#2       
# for row in df3:
# s=pd.Series(df3)
# s.str.split(pat = "/")
# print(s)

#3
# length = len(string)
# for index in range(length):
#     if string[index] == " ":
#         print(" ")
#     else:
#         print(string[index])

#4
# listSplitted = [x for x in csv_file.replace(' ', ',')]
# for x in listSplitted:
#     print(x)

#5

df = pd.DataFrame(data=df2) #create data frame, df2 is data csv 
# print(df)
split = df.text.str.split(expand=True).stack() #split sentences and expand out into separate column

#When using expand=True, the split elements will expand out into separate columns. 
#And If NaN is present, it is propagated throughout the columns during the split.

# hasil_split = pd.DataFrame({
#     'text': split.values
# })  
wordcount={}
for text in split: #text in split(read above)
    if re.search(r'^#', text) is not None: #if there is the word '#' in text(split)  
        print(text)  #then print word(text). and if none word '#' then nothing action
        # if my_word == text:
        #     wordcount[my_word] = 1
        # else:
        #     wordcount[my_word] += 1