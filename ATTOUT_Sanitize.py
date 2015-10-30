import sys
import os
import argparse
import csv
import xlwt
import datetime as DT
from xlrd import open_workbook


File_List=[]
Heading=[]
Body=[]

def get_csv(myfile):
    i=0
    with open(myfile, 'rb') as csvfile:
        FileReader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        for row in FileReader:
            if i == 0:
                Heading.append(row)
                i=1
            else:
                if (len(row[0]) > 2):
                    Body.append(row)
                else:
                    pass

def txt_to_csv(myfile):

    Workbook_FileName = '{!s}[{:%Y-%m-%d_%H%M%S}].csv'.format(myfile, DT.datetime.now())

    i=0
    with open(myfile, 'rb') as csvfile:
        FileReader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        for row in FileReader:
            if i == 0:
                Heading.append(row)
                i=1
            else:
                if (len(row[0]) > 2):
                    Body.append(row)
                else:
                    pass
    
    writer = csv.writer(open("../", 'w'))
    for row in data:
        if counter[row[0]] >= 4:
            writer.writerow(row)

def main():

    parser = argparse.ArgumentParser(description='Sanitize ATTOUT Files')
    parser.add_argument('DWG_File', help='Text File Name or "All" to process directory')
    args = parser.parse_args()

    if (args.DWG_File == "All") or (args.DWG_File == "all"):
        for each in os.listdir(os.getcwd()):
            if each.endswith(".txt"):
                    File_List.append(each)
    else:
        File_List.append(args.DWG_File)

    print File_List
'''      
    get_csv(args.DWG_File)
    get_SHDWGNAM(DWG_List)
    push_csv(DWG_List)


    print "\n...Complete \n\n{!s} Generated".format(Workbook_FileName)
'''   

if __name__ == '__main__':
    main()
    sys.exit()
