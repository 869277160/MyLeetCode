with open("file.txt") as f:
    for line in f :
        #print (line)
        #line=f.readline()
        if  line[0].isdigit() and line[1].isdigit() and line[2].isdigit() and line[3]=='-' and  line[4].isdigit() and line[5].isdigit() and line[6].isdigit() and line[7]=='-' and  line[8].isdigit() and line[9].isdigit() and line[10].isdigit() and line[11].isdigit():
            print(line)
        if  line[0]=='(' and line[1].isdigit() and line[2].isdigit() and line[3].isdigit()  and  line[4]==')' and line[5]==' ' and line[6].isdigit() and line[7].isdigit() and line[8].isdigit() and line[9]=='-' and line[10].isdigit() and line[11].isdigit() and line[12].isdigit() and line[13].isdigit():
            print(line)


#grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt