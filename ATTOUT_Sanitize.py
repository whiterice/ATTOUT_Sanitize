import sys
import os
import argparse
import csv
import xlwt
import datetime as DT
from xlrd import open_workbook
from string import whitespace
import re


File_List=[]
Heading=[]
Body=[]
BodyOut=[]

def sanitize(list1, list2):
        i=0
	for SubList in list1:
                list2.append([])
		for each in SubList:
			#each = each.replace(' ', '')
                        list2[i].append(each.split())
		i=i+1

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

def save_csv(myfile, List1, List2):
    
    with open(myfile, 'wb') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(List2)
        a.writerows(List1)    


def main():

    parser = argparse.ArgumentParser(description='Sanitize ATTOUT Files')
    parser.add_argument('DWG_File', help='Text File Name or "All" to process directory')
    args = parser.parse_args()

    if (args.DWG_File == "All") or (args.DWG_File == "all"):
        for each in os.listdir(os.getcwd()):
            if each.endswith(".txt"):
                    File_List.append(each)
            Type = "All"
    else:
        File_List.append(args.DWG_File)
        (Type, ext) = str(args.DWG_File).split('.')


    print File_List


    for each in File_List:
        get_csv(each)

	sanitize(Body, BodyOut)

    Workbook_FileName = '{!s}[{:%Y-%m-%d_%H%M%S}].csv'.format(Type, DT.datetime.now())

    
    save_csv(Workbook_FileName, BodyOut, Heading)

    print "\n...Complete \n\n{!s} Generated".format(Workbook_FileName)
 

if __name__ == '__main__':
    main()
    sys.exit()
