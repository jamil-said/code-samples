#!/usr/bin/env python3

# Copyright (C) 2018 Jamil Said Jr

""" Script(s) Goal
This script will extract, check, fix (when possible), transform and load 
data from a txt file of domestic US flights into a PostgreSQL database. 
This script will save a log with missing entries on missing_data.tx, and 
a log with obviously erroneous entries (not fixed by the script) on 
bad_data.txt, both logs created on the same directory where the script is 
run from. The logs can be used later to refine this script.
"""

import flights_db
import time
import re

def processFile(f):
    startTime = time.time()
    tmp, badData, missData, countLns = [], {}, {}, 0
    setFal = {'F', 'f', 'false', 'False', 'FALSE', '0'}
    setTru = {'T', 't', 'true', 'True', 'TRUE', '1'}
    badDataSet, missDataSet = set(), set()
    
    # reading the document and splitting the fields based on lines
    with open(f) as fObj:
        lineLst = fObj.read().splitlines()
    countLns = len(lineLst)
    
    # split fields based on pipe character and save in new list
    for l in lineLst:
        tmp.append(l.split('|'))

    # Status update function
    def statUp(uMsg):
        print(uMsg, 'Time:', time.time()-startTime)
    
    # PostgreSQL prevailing convention for identifiers is lower case, thus 
    # transform existing colunm names into lowercase. Also record cols # and 
    # create new list for clean data. Check for column name collision and 
    # exit if collision found
    nCols = len(tmp[0])
    colLst = tmp.pop(0)
    colLst = [i.lower() for i in colLst]
    fliLst = [[] for i in range(len(tmp))]
    if len(colLst) != len(set(colLst)): 
        print('Error: duplicate column name. Aborted.')
        return

    # Two functions which add bad & missing remaining results (after etl runs)
    # to dictionary logs, and also add a "filler" to data array in place of 
    # erroneous entries. Note that "j" is added by 2 to match processed file 
    # line number (compensates 0 index start and lack of 'column names' row). 
    # Error parameter should start with column name and then have either a 
    # space before the next word or nothing after column name.
    def addBadData(j, err, filler):
        fliLst[j].append(filler)
        badDataSet.add(err[0].split()[0])
        if j+2 not in badData: badData[j+2] = err
        else: badData[j+2].extend(err)

    def addMissData(j, err, filler):
        fliLst[j].append(filler)
        missDataSet.add(err[0].split()[0])
        if j+2 not in missData: missData[j+2] = err
        else: missData[j+2].extend(err)

    # Data check: check data for problems & transform/save data in new list.
    # Assumptions were made about data types (ex: transaction ID is numeric)
    # Error/missing logs will be created later and can be used to refine 
    # this script
    for i, row in enumerate(tmp):
        col = 0
        
        # Column number check - if a row is not matching the cols # then abort
        if len(row) != nCols: return [i, ' Missing columns error']
        
        # TRANSACTIONID check (only numbers)  
        if row[col] != '':
            try: fliLst[i].append(int(row[col]))
            except Exception as e: 
                addBadData(i, ['TRANSACTIONID Error', row[col], str(e)], None)
        else: addMissData(i, ['TRANSACTIONID Missing'], None)
        col += 1
        
        # FLIGHTDATE check (8 numbers) 
        if row[col] != '':
            if len(row[col]) == 8 and row[col].isdigit(): 
                fliLst[i].append(row[col])
            else: addBadData(i, ['FLIGHTDATE Error', row[col]], None)
        else: addMissData(i, ['FLIGHTDATE Missing'], None)
        col += 1
        
        # AIRLINECODE check (capital english letters or numbers)
        if row[col] != '':
            if re.match("^[A-Za-z0-9]*$", row[col]): 
                fliLst[i].append(row[col].upper())
            else: addBadData(i, ['AIRLINECODE Error', row[col]], None)
        else: addMissData(i, ['AIRLINECODE Missing'], None)
        col += 1
        
        # AIRLINENAME check (string, title letters) extract string before 
        # last colon occurence, remove leading and trailing whitespaces
        if row[col] != '':
            try: fliLst[i].append(row[col].rsplit(':', 1)[0].strip().title())
            except Exception as e: 
                addBadData(i, ['AIRLINENAME error', row[col], str(e)], None)
        else: addMissData(i, ['AIRLINENAME Missing'], None)
        col += 1
        
        # TAILNUM check (capital alphanumeric plus dash '-', remove any 
        # "@", "'", "`"  character)
        if row[col] != '':
            if re.match("^[A-Za-z0-9-@`']*$", row[col]): 
                fliLst[i].append(re.sub("[@]|`|'", "", row[col]).upper())
            else: addBadData(i, ['TAILNUM error', row[col]], None)
        else: addMissData(i, ['TAILNUM Missing'], None)
        col += 1
        
        # FLIGHTNUM check (only numbers)
        if row[col] != '':
            try: fliLst[i].append(int(row[col]))
            except Exception as e: 
                addBadData(i, ['FLIGHTNUM error', row[col], str(e)], None)
        else: addMissData(i, ['FLIGHTNUM Missing'], None)
        col += 1
        
        # ORIGINAIRPORTCODE check (3 or 4 Capital English letters)
        if row[col] != '':
            if 3 <= len(row[col]) <= 4 and re.match("^[A-Za-z]*$", row[col]): 
                fliLst[i].append(row[col].upper())
            else: addBadData(i, ['ORIGINAIRPORTCODE error', row[col]], None)
        else: addMissData(i, ['ORIGINAIRPORTCODE Missing'], None)
        col += 1
        
        # ORIGAIRPORTNAME check (string, title letters) extract string after
        # first colon occurence, remove leading and trailing whitespaces
        if row[col] != '':
            try: fliLst[i].append(row[col].split(':', 1)[1].strip().title())
            except Exception as e: 
                addBadData(i, ['ORIGAIRPORTNAME error', row[col], str(e)], None)
        else: addMissData(i, ['ORIGAIRPORTNAME Missing'], None)
        col += 1
        
        # ORIGINCITYNAME check (string, title letters) remove leading and 
        # trailing whitespaces
        if row[col] != '':
            try: fliLst[i].append(row[col].strip().title())
            except Exception as e: 
                addBadData(i, ['ORIGINCITYNAME error', row[col], str(e)], None)
        else: addMissData(i, ['ORIGINCITYNAME Missing'], None)
        col += 1
        
        # ORIGINSTATE check (2 Capital English letters)
        if row[col] != '':
            if len(row[col]) == 2 and re.match("^[A-Za-z]*$", row[col]): 
                fliLst[i].append(row[col].upper())
            else: addBadData(i, ['ORIGINSTATE error', row[col]], None)
        else: addMissData(i, ['ORIGINSTATE Missing'], None)
        col += 1
        
        # ORIGINSTATENAME check (string, title letters) remove leading and 
        # trailing whitespaces
        if row[col] != '':
            try: fliLst[i].append(row[col].strip().title())
            except Exception as e: 
                addBadData(i, ['ORIGINSTATENAME error', row[col], str(e)], None)
        else: addMissData(i, ['ORIGINSTATENAME Missing'], None)
        col += 1
        
        # DESTAIRPORTCODE check (3 or 4 capital English letters)
        if row[col] != '':
            if 3 <= len(row[col]) <= 4 and re.match("^[A-Za-z]*$", row[col]): 
                fliLst[i].append(row[col].upper())
            else: addBadData(i, ['DESTAIRPORTCODE error', row[col]], None)
        else: addMissData(i, ['DESTAIRPORTCODE Missing'], None)
        col += 1
        
        # DESTAIRPORTNAME check (string, title letters) extract string 
        # after first colon occurence, remove leading and trailing whitespaces
        if row[col] != '':
            try: fliLst[i].append(row[col].split(':', 1)[1].strip().title())
            except Exception as e: 
                addBadData(i, ['DESTAIRPORTNAME error', row[col], str(e)], None)
        else: addMissData(i, ['DESTAIRPORTNAME Missing'], None)
        col += 1
        
        # DESTCITYNAME check (string, title letters), remove leading and 
        # trailing whitespaces
        if row[col] != '':
            try: fliLst[i].append(row[col].strip().title())
            except Exception as e: 
                addBadData(i, ['DESTCITYNAME error', row[col], str(e)], None)
        else: addMissData(i, ['DESTCITYNAME Missing'], None)
        col += 1
        
        # DESTSTATE check (2 capital English letters)
        if row[col] != '':
            if len(row[col]) == 2 and re.match("^[A-Za-z]*$", row[col]): 
                fliLst[i].append(row[col].upper())
            else: addBadData(i, ['DESTSTATE error', row[col]], None)
        else: addMissData(i, ['DESTSTATE Missing'], None)
        col += 1
        
        # DESTSTATENAME check (string, title letters) remove leading and 
        # trailing whitespaces
        if row[col] != '':
            try: fliLst[i].append(row[col].strip().title())
            except Exception as e: 
                addBadData(i, ['DESTSTATENAME error', row[col], str(e)], None)
        else: addMissData(i, ['DESTSTATENAME Missing'], None)
        col += 1
        
        # CRSDEPTIME check (1 to 4 numbers) transform value into 4 digits 
        # if needed by adding "0"s at the front to normalize time
        if row[col] != '':
            if 1 <= len(row[col]) <= 4 and row[col].isdigit(): 
                difDig = 4 - len(row[col])
                fliLst[i].append(difDig*'0'+row[col])
            else: addBadData(i, ['CRSDEPTIME error', row[col]], None)
        else: addMissData(i, ['CRSDEPTIME Missing'], None)
        col += 1
        
        # DEPTIME check (1 to 4 numbers) transform value into 4 digits 
        # if needed by adding "0"s at the front to normalize time
        if row[col] != '':
            if 1 <= len(row[col]) <= 4 and row[col].isdigit(): 
                difDig = 4 - len(row[col])
                fliLst[i].append(difDig*'0'+row[col])
            else: addBadData(i, ['DEPTIME error', row[col]], None)
        else: addMissData(i, ['DEPTIME Missing'], None)
        col += 1
        
        # DEPDELAY check (only numbers, may be signed)
        if row[col] != '':
            try: fliLst[i].append(int(row[col]))
            except Exception as e: 
                addBadData(i, ['DEPDELAY error', row[col], str(e)], None)
        else: addMissData(i, ['DEPDELAY Missing'], None)
        col += 1
        
        # TAXIOUT check (only numbers)
        if row[col] != '':
            try: fliLst[i].append(int(row[col]))
            except Exception as e: 
                addBadData(i, ['TAXIOUT error', row[col], str(e)], None)
        else: addMissData(i, ['TAXIOUT Missing'], None)
        col += 1
        
        # WHEELSOFF check (1 to 4 numbers) transform value into 4 digits 
        # if needed by adding "0"s at the front to normalize time
        if row[col] != '':
            if 1 <= len(row[col]) <= 4 and row[col].isdigit(): 
                difDig = 4 - len(row[col])
                fliLst[i].append(difDig*'0'+row[col])
            else: addBadData(i, ['WHEELSOFF error', row[col]], None)
        else: addMissData(i, ['WHEELSOFF Missing'], None)
        col += 1
        
        # WHEELSON check (1 to 4 numbers) transform value into 4 digits 
        # if needed by adding "0"s at the front to normalize time
        if row[col] != '':
            if 1 <= len(row[col]) <= 4 and row[col].isdigit(): 
                difDig = 4 - len(row[col])
                fliLst[i].append(difDig*'0'+row[col])
            else: addBadData(i, ['WHEELSON error', row[col]], None)
        else: addMissData(i, ['WHEELSON Missing'], None)
        col += 1
        
        # TAXIIN check (only numbers)
        if row[col] != '':
            try: fliLst[i].append(int(row[col]))
            except Exception as e: 
                addBadData(i, ['TAXIIN error', row[col], str(e)], None)
        else: addMissData(i, ['TAXIIN Missing'], None)
        col += 1
        
        # CRSARRTIME check (1 to 4 numbers) transform value into 4 digits 
        # if needed by adding "0"s at the front to normalize time
        if row[col] != '':
            if 1 <= len(row[col]) <= 4 and row[col].isdigit(): 
                difDig = 4 - len(row[col])
                fliLst[i].append(difDig*'0'+row[col])
            else: addBadData(i, ['CRSARRTIME error', row[col]], None)
        else: addMissData(i, ['CRSARRTIME Missing'], None)
        col += 1
        
        # ARRTIME check (1 to 4 numbers) transform value into 4 digits 
        # if needed by adding "0"s at the front to normalize time
        if row[col] != '':
            if 1 <= len(row[col]) <= 4 and row[col].isdigit(): 
                difDig = 4 - len(row[col])
                fliLst[i].append(difDig*'0'+row[col])
            else: addBadData(i, ['ARRTIME error', row[col]], None)
        else: addMissData(i, ['ARRTIME Missing'], None)
        col += 1
        
        # ARRDELAY check (only numbers, may be signed)
        if row[col] != '':
            try: fliLst[i].append(int(row[col]))
            except Exception as e: 
                addBadData(i, ['ARRDELAY error', row[col], str(e)], None)
        else: addMissData(i, ['ARRDELAY Missing'], None)
        col += 1
        
        # CRSELAPSEDTIME check (only numbers)
        if row[col] != '':
            try: fliLst[i].append(int(row[col]))
            except Exception as e: 
                addBadData(i, ['CRSELAPSEDTIME error', row[col], str(e)], None)
        else: addMissData(i, ['CRSELAPSEDTIME Missing'], None)
        col += 1
        
        # ACTUALELAPSEDTIME check (only numbers)
        if row[col] != '':
            try: fliLst[i].append(int(row[col]))
            except Exception as e: 
                addBadData(i, ['ACTUALELAPSEDTIME error', row[col], str(e)], None)
        else: addMissData(i, ['ACTUALELAPSEDTIME Missing'], None)
        col += 1
        
        # CANCELLED check boolean -- transform 0, F and False, etc into boolean
        if row[col] != '':
            if row[col] in setFal: fliLst[i].append(False)
            elif row[col] in setTru: fliLst[i].append(True)
            else: addBadData(i, ['CANCELLED error', row[col]], None)
        else: addMissData(i, ['CANCELLED Missing'], None)
        col += 1
        
        # DIVERTED check boolean -- transform 0, F and False, etc into boolean
        if row[col] != '':
            if row[col] in setFal: fliLst[i].append(False)
            elif row[col] in setTru: fliLst[i].append(True)
            else: addBadData(i, ['DIVERTED error', row[col]], None)
        else: addMissData(i, ['DIVERTED Missing'], None)
        col += 1
        
        # DISTANCE check (numbers only) extract string before first space 
        # to eliminate 'miles'
        if row[col] != '':
            try: fliLst[i].append(int(row[col].split(' ', 1)[0]))
            except Exception as e: 
                addBadData(i, ['DISTANCE error', row[col], str(e)], None)
        else: addMissData(i, ['DISTANCE Missing'], None)
        col += 1

    # integrity check, check # of columns and rows, abort if error
    # note: countLns is subtracted by one to account for extracted row of 
    # column names
    for i in range(len(fliLst)):
        if nCols != len(fliLst[i]): 
            return ['Error nCols ', nCols, 'lenfliLst', len(fliLst[i]), 'i', i]
    if countLns-1 != len(fliLst):
        return ['Error countLns ', countLns, 'len(fliLst)', len(fliLst)]

    # Status update
    statUp('Data cleaning succeeded.')

    # Function to print remaining data errors/omissions to log (reviewed 
    # manually later and used to refine this script). If no errors/omissions 
    # are remaining, note that on the log. 
    def printLogs(logFile, dicLog, setLog, messErr, messOk):
        if dicLog:
            with open(logFile, 'w') as f:
                for key, value in sorted(dicLog.items()):
                    f.write('Line %s:%s\n' % (key, value))        
            with open(logFile, 'r+') as f: 
                s = f.read()
                f.seek(0)
                f.write(messErr+str(sorted(setLog))+'\n'+s)
        else: 
            with open(logFile, 'w') as f: 
                f.write(messOk)
    
    # Function call to print bad/missing logs. 
    # Argument list: (logFile, dicLog, setLog, messErr, messOk)
    printLogs('bad_data.txt', badData, badDataSet, 'Columns presenting'
    +' errors (alphabetical order): ', 'No clearly erroneous data found '
    +'(after ETL script run)\n')
    printLogs('missing_data.txt', missData, missDataSet, 'Columns with '
    +'missing entries (alphabetical order): ', 'No missing entries found \n')
    
    # Status update
    statUp('Log printing succeeded.')
    
    # Connect and upload all data to PostgreSQL database (handled by module 
    # flights_db)
    flights_db.uploadDB(fliLst, colLst, startTime)

    # Status update
    statUp('ETL succeeded.')

    return

# Start the script with the file to be processed (flights.txt), which should
# be put on same directory as this script
if __name__ == '__main__': processFile('flights.txt')
