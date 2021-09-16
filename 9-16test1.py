def find_times(filename,char):
    count = 0
    with open (filename,'r',encoding='utf-8') as file:
        txt = file.read()
        txt = txt.lower()
        for k in txt:
            if char == k:
                count+=1
    return count
print(find_times('text2.txt','e'))
