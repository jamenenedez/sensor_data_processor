# Jose Menendez
# Separate in 5 files the LPMS-B sensors output


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def split_by_sensors():
    import os
    from os import listdir
    numFiles = len(listdir("."))

    for f in listdir("."):
        w_ext = f.split(".")
        if len(w_ext) > 1 and w_ext[1] in ['txt', 'csv']:
            # Open & creation of files
            file = open(f, 'r')
            file1 = open(str(w_ext[0])+" - 1.csv", 'w')
            file2 = open(str(w_ext[0])+" - 2.csv", 'w')
            file3 = open(str(w_ext[0])+" - 3.csv", 'w')
            file4 = open(str(w_ext[0])+" - 4.csv", 'w')
            file5 = open(str(w_ext[0])+" - 5.csv", 'w')

            # Heading
            line = file.readline()
            words = line.split(",")
            file1.write(line)
            file2.write(line)
            file3.write(line)
            file4.write(line)
            file5.write(line)

            # Search SensorId column
            for i in range(len(words)):
                if words[i] == "SensorId":
                    located = i

            # Separate into two files
            line = file.readline()
            while line != "":
                words = line.split(",")
                if words[located] == "1":
                    file1.write(line)
                elif words[located] == "2":
                    file2.write(line)
                elif words[located] == "3":
                    file3.write(line)
                elif words[located] == "4":
                    file4.write(line)
                elif words[located] == "5":
                    file5.write(line)
                line = file.readline()

            # Close files
            file.close()
            file1.close()
            file2.close()
            file3.close()
            file4.close()
            file5.close()


def split_by_timestamp():
    import re
    import os
    from os import listdir
    numFiles = len(listdir("."))
    folder_name = ''
    base_files = []
    non_base_files = []

    for f in listdir("."):
        if re.search('[0-9]+', f) == None:
            base_files.append(f)
        else:
            non_base_files.append(f)
        w_ext = f.split(".")
        if len(w_ext) > 1 and w_ext[1] in ['txt', 'csv'] and f not in base_files:
            # Open & creation of files
            tokens = w_ext[0].split("_")
            tokens.remove(tokens[0]);
            folder_name = ' '.join(tokens)[0].upper() + ' '.join(tokens)[1:]
            folder_name = re.sub(r'\s\-\s[0-9]*', '', folder_name)

            if not os.path.isdir(str(folder_name)):
                os.mkdir(str(folder_name))
            if not os.path.isdir(str(folder_name)+"/Sesion 1"):
                os.mkdir(str(folder_name)+"/Sesion 1")
            if not os.path.isdir(str(folder_name)+"/Sesion 2"):
                os.mkdir(str(folder_name)+"/Sesion 2")
            if not os.path.isdir(str(folder_name)+"/Sesion 3"):
                os.mkdir(str(folder_name)+"/Sesion 3")
            if not os.path.isdir(str(folder_name)+"/Sesion 4"):
                os.mkdir(str(folder_name)+"/Sesion 4")
            if not os.path.isdir(str(folder_name)+"/Sesion 5"):
                os.mkdir(str(folder_name)+"/Sesion 5")

    for f in non_base_files:
        w_ext = f.split(".")
        if len(w_ext) > 1 and w_ext[1] in ['txt', 'csv']:
            fileHandle = open(f, "r")
            lineList = fileHandle.readlines()
            fileHandle.close()
            data = lineList[-1]
            max_number = ""
            if(is_number(data.split(",")[1])):
                max_number = float(data.split(",")[1])
            season = 1
            files = []
            segment1 = max_number/5
            segment2 = segment1 * 2
            segment3 = segment1 * 3
            segment4 = segment1 * 4
            segment5 = segment1 * 5

            for n in range(1, 6):
                files.append(open(str(folder_name)+"/"+str("Sesion ")+str(n)+"/" +
                             str(w_ext[0].replace(" - ", " - "+str(season)+" - "))+".csv", 'w'))
                season += 1

            located = ""
            non_base_file = open(f, 'r')
            line = non_base_file.readline()
            words = line.split(",")

            for ff in files:
                # Heading
                ff.write(line)

            # Search TimeStamp column
            for i in range(len(words)):
                if re.sub('[\s+]', '', words[i]) == "TimeStamp(s)":
                    located = i

            # Separate into five files
            inner_line = non_base_file.readline()
            while inner_line != '' and max_number != '':
                words = inner_line.split(",")
                if (float(words[located]) <= (segment1)):
                    files[0].write(inner_line)
                elif (float(words[located]) > (segment1)) & (float(words[located]) <= (segment2)):
                    files[1].write(inner_line)
                elif (float(words[located]) > (segment2)) & (float(words[located]) <= (segment3)):
                    files[2].write(inner_line)
                elif (float(words[located])>(segment3)) & (float(words[located])<=(segment4)):
                    files[3].write(inner_line)
                elif (float(words[located])>(segment4)) & (float(words[located])<=(segment5)):
                    files[4].write(inner_line)                
                inner_line=non_base_file.readline()

            for ff in files:
                ff.close()
            non_base_file.close()

    for nbf in non_base_files:
        os.remove(nbf)

split_by_sensors()
split_by_timestamp()    
