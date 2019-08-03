content = open('dupppp.txt','r').readlines()
content_set = set(content)
cleandata = open('clean.txt','w')
for line in content_set:
    cleandata.write(line)