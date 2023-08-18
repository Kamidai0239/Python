text=input('何を記載しますか？>>')
file=open('diary.txt','a')
file=write(text+'\n')
file.close()
