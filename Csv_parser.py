#!/usr/bin/python3.6.1
#
#   Program Name: Csv_parser
#
#   Author: Temisan Aghoghovbia
#
#   Requirements: Python 3.6.1
#
#   Description:  This will parse a csv
#
#   Date (MM.DD.YYYY): 06.12.17
#
#   Input(s): Filename
#
#
#   Output(s):
#               Returns requested information about csv file,
#               new csv; name based on inputted csv name with date and time
#
#   Copyright Hewlett Packard Enterprise 2017
#
#   Revision History:
#
# ****************************************************************

import csv
import re
from datetime import datetime
import datetime
import os
from  os import path
import sys
import time




#Does file exist
def existence():
    path_loc = path.exists(sys.argv[1])
    if path_loc == True:
        pass
    else:
        print ("{} does not exist".format(sys.argv[1]))
    return path_loc

#countdown for file completion [Changes for python 2]
def countdown(t):
    for i in range(t,0,-1):
        print('.', end='', flush=True)
        time.sleep(1)

#writes new csv
def Csv_parser():

    if len(sys.argv) == 2 and existence() == True:
        output_csv = str(datetime.datetime.now().strftime("hsswe-%Y%m%d_%H_%M_%p")) + '.csv' #name of new file
    else:
        sys.exit(0)
    output_fields = ['Timestamp', "Count", 'C00', 'C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'E40', 'E41', 'E42',
                     'E43', 'E44','E45', 'E46', 'E47']


    with open(output_csv, "w",newline='') as outfile:

        writer = csv.writer(outfile)

        Data = zip(ts(),count(),c00(),c01(),c02(),c03(),c04(),c05(),c06(),c07(),e40(),e41(),e42(),e43(),e44(),e45(),e46(),e47())  # this is Gold

        countdown(11)
        writer.writerow(output_fields)
        writer.writerows(Data)

    print ('End of program')


# *** EACH FUNCTION RETURN AN ARRAY ON 18 ELEMENTS ???/ ***

def ts():
    ts_array = []
    for line in open(sys.argv[1]or input_csv):
        line = line.strip()
        Timestamp = re.search(r'^\d+:\d{2}:\d{2}.\d{2}', line)
        if Timestamp:
            T= 'T'
            found = Timestamp.group(0)
            ts_array.append(found + ' ' +T)
    return ts_array

def count():
    count_array = []
    for line in open(sys.argv[1]or input_csv):
        line = line.strip()
        Count = re.search(r'Count:\s[0-9]+', line ,re.I)
        if Count:
            found = Count.group(0)
            count_array.append(found)
    return count_array

def c00():
    c00_array = []
    for line in open(sys.argv[1]or input_csv):
        line = line.strip()
        C00 = re.search(r'^00\s+(\d?x\d{8})\s{8}', line,re.M)
        if C00:
            found = C00.group(1)
            c00_array.append(found)
    return c00_array

def c01():
    C01_array = []
    for line in open(sys.argv[1]or input_csv):
        line = line.strip()
        C01 = re.search(r'^01\s+(\d?x\d{8})\s{8}', line ,re.M)
        if C01:
            found = C01.group(1)
            C01_array.append(found)
    return C01_array

def c02():
    C02_array = []
    for line in open(sys.argv[1]or input_csv):
        line = line.strip()
        C02 = re.search(r'^02\s+(\d?x\d{8})\s{8}', line ,re.M)
        if C02:
            found = C02.group(1)
            C02_array.append(found)
    return C02_array

def c03():
    C03_array = []
    for line in open(sys.argv[1]or input_csv):
        line = line.strip()
        C03 = re.search(r'^03\s+(\d?x\d{8})\s{8}', line ,re.M)
        if C03:
            found = C03.group(1)
            C03_array.append(found)
    return C03_array

def c04():
    C04_array = []
    for line in open(sys.argv[1]or input_csv):
        line = line.strip()
        C04 = re.search(r'^04\s+(\d?x\d{8})\s{8}', line ,re.M)
        if C04:
            found = C04.group(1)
            C04_array.append(found)
    return C04_array

def c05():
    C05_array = []
    for line in open(sys.argv[1]or input_csv):
        line = line.strip()
        C05 = re.search(r'^05\s+(\d?x\d{8})\s{8}', line ,re.M)
        if C05:
            found = C05.group(1)
            C05_array.append(found)
    return C05_array

def c06():
    C06_array = []
    for line in open(sys.argv[1]or input_csv):
        line = line.strip()
        C06 = re.search(r'^06\s+(\d?x\d{8})\s{8}', line ,re.M)
        if C06:
            found = C06.group(1)
            C06_array.append(found)
    return C06_array

def c07():
    C07_array = []
    for line in open(sys.argv[1]or input_csv):
        line = line.strip()
        C07 = re.search(r'^07\s+(\d?x\d{8})\s{8}', line ,re.M)
        if C07:
            found = C07.group(1)
            C07_array.append(found)
    return C07_array

def e40():
    E40_array = []
    for line in open(sys.argv[1]or input_csv):
        line = line.strip()
        E40 = re.search(r'^40\s+(\d?x\d{8})\s{7}', line ,re.M)
        if E40:
            found = E40.group(1)
            E40_array.append(found)
    return E40_array

def e41():
    E41_array = []
    for line in open(sys.argv[1]or input_csv):
        line = line.strip()
        E41 = re.search(r'^41\s+(\d?x\d{8})\s{7}', line ,re.M)
        if E41:
            found = E41.group(1)
            E41_array.append(found)
    return E41_array

def e42():
    E42_array = []
    for line in open(sys.argv[1]or input_csv):
        line = line.strip()
        E42 = re.search(r'^42\s+(\d?x\d{8})\s{7}', line ,re.M)
        if E42:
            found = E42.group(1)
            E42_array.append(found)
    return E42_array

def e43():
    E43_array = []
    for line in open(sys.argv[1]or input_csv):
        line = line.strip()
        E43 = re.search(r'^43\s+(\d?x\d{8})\s{7}', line ,re.M)
        if E43:
            found = E43.group(1)
            E43_array.append(found)
    return E43_array

def e44():
    E44_array = []
    for line in open(sys.argv[1]or input_csv):
        line = line.strip()
        E44 = re.search(r'^44\s+(\d?x\d{8})\s{7}', line ,re.M)
        if E44:
            found = E44.group(1)
            E44_array.append(found)
    return E44_array

def e45():
    E45_array = []

    for line in open(sys.argv[1]or input_csv):
        line = line.strip()
        E45 = re.search(r'^45\s+(\d?x\d{8})\s{7}', line ,re.M)
        if E45:
            found = E45.group(1)
            E45_array.append(found)
    return E45_array

def e46():
    E46_array = []

    for line in open(sys.argv[1]or input_csv):
        line = line.strip()
        E46 = re.search(r'^46\s+(\d?x\d{8})\s{7}', line ,re.M)
        if E46:
            found = E46.group(1)
            E46_array.append(found)
    return E46_array

def e47():
    E47_array = []
    for line in open(sys.argv[1]or input_csv):
        line = line.strip()
        E47 = re.search(r'^47\s+(\d?x\d{8})\s{7}', line ,re.M)
        if E47:
            found = E47.group(1)
            E47_array.append(found)
    return E47_array


if __name__=="__main__":

    if len(sys.argv) >= 3:
        print("Out of range, enter one filename")
        input_csv = input('Enter Filename (ex: yourfile.csv)   ')
        os.system("python Csv_parser.py" + ' ' + input_csv)
    elif len(sys.argv) <= 1:
        input_csv = input('Enter Filename (ex: yourfile.csv)   ')
        os.system("python Csv_parser.py" + ' ' + input_csv)
    else:
        pass


    Csv_parser()



