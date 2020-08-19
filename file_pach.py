import os.path
if os.path.isfile('n.txt'):
    print('存在')
    file=open('new.txt','a')
    file.write('檔案94存在')
    file.close()
else:
    print('不存在')
    file=open('n.txt','w')
    file.write('這是新的檔案')
    file.close()