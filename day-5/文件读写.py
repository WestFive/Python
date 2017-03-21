fw = open('sample.txt','w')
fw.write('write somethin to txt\n')
fw.write('only joks\n')
fw.close()

fr = open('sample.txt','r')
print(fr.read())
text = fr.read()
print(text)