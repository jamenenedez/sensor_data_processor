# Jose Menendez
# Separate in 5 files the LPMS-B sensors output
# CICESE May 2019
def read():
    import re    
    import os
    from os import listdir
    numFiles=len(listdir("."))
    print ("Files in directory: ", numFiles)

    for f in listdir("."):
        w_ext=f.split(".")
        if len(w_ext)>1 and w_ext[1] in ['txt', 'csv']:
            #Open & creation of files                
            print ("Processing ", f)
            tokens = w_ext[0].split("_")
            tokens.remove(tokens[0]);                        
            folderName = ' '.join(tokens)[0].upper() + ' '.join(tokens)[1:]

            if not os.path.isdir(str(folderName)):
                os.mkdir(str(folderName))

            if not os.path.isdir(str(folderName)+"/Sesion I"):
                os.mkdir(str(folderName)+"/Sesion I")
            if not os.path.isdir(str(folderName)+"Sesion II"):
                os.mkdir(str(folderName)+"/Sesion II")
            if not os.path.isdir(str(folderName)+"Sesion III"):
                os.mkdir(str(folderName)+"/Sesion III")
            if not os.path.isdir(str(folderName)+"Sesion IV"):
                os.mkdir(str(folderName)+"/Sesion IV")
            if not os.path.isdir(str(folderName)+"Sesion V"):
                os.mkdir(str(folderName)+"/Sesion V")

            fileHandle = open ( f,"r" )
            lineList = fileHandle.readlines()
            fileHandle.close()
            data = lineList[-1]
            max_number = float(data.split(",")[1])
            print (max_number)
            
            segment1 = max_number/5
            segment2 = segment1 * 2
            segment3 = segment1 * 3
            segment4 = segment1 * 4
            segment5 = segment1 * 5

            file=open(f,'r')
            file1=open(str(folderName)+"/"+str("Sesion I")+"/"+str(w_ext[0])+" - 1.csv",'w')
            file2=open(str(folderName)+"/"+str("Sesion II")+"/"+str(w_ext[0])+" - 2.csv",'w')
            file3=open(str(folderName)+"/"+str("Sesion III")+"/"+str(w_ext[0])+" - 3.csv",'w')
            file4=open(str(folderName)+"/"+str("Sesion IV")+"/"+str(w_ext[0])+" - 4.csv",'w')
            file5=open(str(folderName)+"/"+str("Sesion V")+"/"+str(w_ext[0])+" - 5.csv",'w')

            #Heading
            line=file.readline()
            words=line.split(",")
            print("Heading:")
            file1.write(line)
            file2.write(line)
            file3.write(line)
            file4.write(line)
            file5.write(line)
            
            #Search SensorId column
            for i in range(len(words)):
                #print (words[i])
                if re.sub('[\s+]', '', words[i]) == "TimeStamp(s)":
                    located = i

            #Separate into two files
            line=file.readline()  
            while line!="":
                words=line.split(",")   
                if (float(words[located])<=(segment1)):
                    file1.write(line)
                elif (float(words[located])>(segment1)) & (float(words[located])<=(segment2)):
                    file2.write(line)
                elif (float(words[located])>(segment2)) & (float(words[located])<=(segment3)):
                    file3.write(line)
                elif (float(words[located])>(segment3)) & (float(words[located])<=(segment4)):
                    file4.write(line)
                elif (float(words[located])>(segment4)) & (float(words[located])<=(segment5)):
                    file5.write(line)
                line=file.readline()

            #Close files
            file.close()
            file1.close()
            file2.close()
            file3.close()
            file4.close()
            file5.close()
read()