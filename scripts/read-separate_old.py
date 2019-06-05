# Hussein
# Separate in two files the LPMS-B sensors output
# Bogazici University April 2015
# Updated for 2 sensors, January 2017
# Updated name of files for "dog" and "person", data from Create-net internship

FOLDER="separated"

def read():
    import os
    from os import listdir    
    numFiles=len(listdir("."))
    #print "Files in directory: ", numFiles
    if not os.path.isdir(str(FOLDER)):
        os.mkdir(str(FOLDER))    
    
    for f in listdir("."):
        w_ext=f.split(".")
        if len(w_ext)>1 and w_ext[1]!="DS_Store" and w_ext[1]!="py":
            #Open & creation of files                
            #print "Processing ", f
            file=open(f,'r')
            file1=open(str(FOLDER)+"/"+str(w_ext[0])+" - 1.csv",'w')
            file2=open(str(FOLDER)+"/"+str(w_ext[0])+" - 2.csv",'w')
            file3=open(str(FOLDER)+"/"+str(w_ext[0])+" - 3.csv",'w')
            file4=open(str(FOLDER)+"/"+str(w_ext[0])+" - 4.csv",'w')
            file5=open(str(FOLDER)+"/"+str(w_ext[0])+" - 5.csv",'w')
            
            #Heading
            line=file.readline()
            words=line.split(",")
            #print "Heading:"
            file1.write(line)
            file2.write(line)
            file3.write(line)
            file4.write(line)
            file5.write(line)
            
            #Search SensorId column
            for i in range(len(words)):
                    #print words[i]
                if words[i]=="SensorId":
                    #print "SensorId encontrado: ", i
                    located = i
            
            #Separate into two files
            line=file.readline()    
            while line!="":
                words=line.split(",")
                if words[located]=="1":
                    file1.write(line)
                elif words[located]=="2":
                    file2.write(line)
                elif words[located]=="3":
                    file3.write(line)
                elif words[located]=="4":
                    file4.write(line)
                elif words[located]=="5":
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
