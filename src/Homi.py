# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:11:46 2016

@author: strider
"""

file_path = '../data/Crimes_-_2001_to_present.csv'

     #60645; 60076; 60202
def main():
    fin = open(file_path, 'r')
    fout = open('Homicide.csv','w')
    writer = csv.writer(fout, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for row in csv.reader(fin, delimiter=',') :
        if row[5] == 'HOMICIDE':
            #print(row[5], row[19],row[20])
            if filterLocation(row):
                writer.writerow(row)
    fout.close()
    fin.close()

def filterLocation(row):
    locations = [
        ((41.783841, -87.614370), (41.776787, -87.609319)),
        ((41.779991, -87.618097), (41.774582, -87.614932)),
        ((41.783483, -87.640084), (41.776193, -87.634035))
    ]
    flag = False
    try:
        lat = float(row[19])
        lon = float(row[20])# 
        #print(lat)
        #print(lon)           
    except (ValueError):
        lat = 0.0
        lon = 0.0
    for location in locations:
        if location[1][0] < lat < location[0][0] and location[0][1] < lon < location[1][1]:
            flag = True
            break;
    return flag
    
    
if __name__ == "__main__":
    main()
