#!/usr/bin/env python3

import MySQLdb
import base64
import time

def uploadDB(fliLst, colLst, startTime):
    conn, dicCol = None, {}
    
    # Function to get database credentials (stored in private folder with 
    # obfuscated pswd) and connect to database
    def connectDB():
        with open('private/cred_local.txt') as fObj:
            credL = fObj.read().splitlines()
        dbN, userN, hostN, portN = credL[0], credL[1], credL[3], int(credL[4])
        pswd = base64.b64decode(credL[2]).decode('utf-8')
        return MySQLdb.connect(db=dbN, user=userN, passwd=pswd, host=hostN, \
        port=portN)

    # Function to control exiting the script. It closes connection if open 
    # without commiting to any changes
    def exitScript(errMsg):
        try:
            if conn: conn.close()
            raise Exception
        except Exception: raise ValueError(str(errMsg))

    # Connect to database and create cursor
    try: conn = connectDB()
    except Exception as e: exitScript(['Problem connecting to DB.', str(e)])
    cur = conn.cursor()
    
    # Status update function
    def statUp(uMsg):
        print(uMsg, 'Time:', time.time()-startTime)
    
    # Status update
    statUp('Connecting to DB succeeded.')

    # Function to commit and update status
    def comUp(cMsg, k):
        conn.commit()
        print(cMsg, 'row', k, 'Time:', time.time()-startTime)

    
    # Save column names and indexes in a dictionary
    for idx, colName in enumerate(colLst):
        if colName in dicCol: 
            exitScript(['Error: column name duplicate.', colName])
        else: dicCol[colName] = idx
    
    # Create dimension tables. Exit program without commiting if any of the  
    # tables already exist (or otherwise fail to create) -- this also serves   
    # as a safeguard against running this script by accident 
    try:
        # Creating dim_time table
        cur.execute("""CREATE TABLE  dim_time (
            time_id INT AUTO_INCREMENT PRIMARY KEY,
            flightdate DATE NOT NULL,
            deptime TIME,
            arrtime TIME,
            depdelay INT,
            arrdelay INT,
            actualelapsedtime INT,
            crsdeptime TIME,
            crsarrtime TIME,
            crselapsedtime INT,
            taxiin INT,
            taxiout INT,
            wheelsoff TIME,
            wheelson TIME
        );""")
        
        # Creating dim_airline table
        cur.execute("""CREATE TABLE  dim_airline (
            airline_id INT AUTO_INCREMENT PRIMARY KEY,
            airlinecode VARCHAR(255) NOT NULL,
            airlinename VARCHAR(255) NOT NULL
        );""")
        
        # Creating dim_origin table
        cur.execute("""CREATE TABLE  dim_origin (
            origin_id INT AUTO_INCREMENT PRIMARY KEY,
            originairportcode VARCHAR(255) NOT NULL,
            origairportname VARCHAR(255),
            origincityname VARCHAR(255),
            originstate VARCHAR(255),
            originstatename VARCHAR(255)
        );""")
        
        # Creating dim_destination table
        cur.execute("""CREATE TABLE  dim_destination (
            dest_id INT AUTO_INCREMENT PRIMARY KEY,
            destairportcode VARCHAR(255) NOT NULL,
            destairportname VARCHAR(255),
            destcityname VARCHAR(255),
            deststate VARCHAR(255),
            deststatename VARCHAR(255)
        );""")        
    except Exception as e: exitScript(["Problem creating dim tables.", str(e)])

    # Status update
    statUp('Creating dim tables succeeded.')

    # Insert data from array to dim tables. Using parameterized queries 
    # for security. Note that %s (positional arguments) must always be 
    # passed as a sequence, thus put value in a list. If error on inserting 
    # happens, then exit script without commiting
    try:
        for i in range(len(fliLst)):
            # insert data on dim_time table
            cur.execute("""INSERT INTO dim_time (
                flightdate, deptime, arrtime, depdelay, arrdelay, 
                actualelapsedtime, crsdeptime, crsarrtime, crselapsedtime, 
                taxiin, taxiout, wheelsoff, wheelson) VALUES (%s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
                ([fliLst[i][dicCol['flightdate']], fliLst[i][dicCol['deptime']],
                fliLst[i][dicCol['arrtime']], fliLst[i][dicCol['depdelay']],
                fliLst[i][dicCol['arrdelay']], 
                fliLst[i][dicCol['actualelapsedtime']],
                fliLst[i][dicCol['crsdeptime']], fliLst[i][dicCol['crsarrtime']],
                fliLst[i][dicCol['crselapsedtime']], fliLst[i][dicCol['taxiin']],
                fliLst[i][dicCol['taxiout']], fliLst[i][dicCol['wheelsoff']],
                fliLst[i][dicCol['wheelson']]]))
  
            # insert data on dim_airline table
            cur.execute("""INSERT INTO dim_airline (
                airlinecode, airlinename) VALUES (%s, %s)""", 
                ([fliLst[i][dicCol['airlinecode']], 
                fliLst[i][dicCol['airlinename']]]))
            
            # insert data on dim_origin table
            cur.execute("""INSERT INTO dim_origin (
                originairportcode, origairportname, origincityname, 
                originstate, originstatename) VALUES (%s, %s, %s, %s, %s)""", 
                ([fliLst[i][dicCol['originairportcode']], 
                fliLst[i][dicCol['origairportname']],
                fliLst[i][dicCol['origincityname']],
                fliLst[i][dicCol['originstate']],
                fliLst[i][dicCol['originstatename']]]))

            # insert data on dim_destination table
            cur.execute("""INSERT INTO dim_destination (
                destairportcode, destairportname, destcityname, 
                deststate, deststatename) VALUES (%s, %s, %s, %s, %s)""", 
                ([fliLst[i][dicCol['destairportcode']], 
                fliLst[i][dicCol['destairportname']],
                fliLst[i][dicCol['destcityname']],
                fliLst[i][dicCol['deststate']],
                fliLst[i][dicCol['deststatename']]]))
            if i % 10000 == 0: comUp('inserting data on dim tables', i)
    except Exception as e: exitScript(["Problem inserting dim data.", str(e)])

    # Create the fact table. Exit program without commiting if any of the  
    # tables already exist (or otherwise fail to create) -- this also serves   
    # as a safeguard against running this script by accident 
    try:
        # Creating fact_flights table
        cur.execute("""CREATE TABLE fact_flights (
            flights_id INT AUTO_INCREMENT PRIMARY KEY,
            transactionid BIGINT NOT NULL,
            time_id INT REFERENCES dim_time (time_id),
            airline_id INT REFERENCES dim_airline (airline_id),
            origin_id INT REFERENCES dim_origin (origin_id),
            dest_id INT REFERENCES dim_destination (dest_id),
            flightnum INT,
            tailnum VARCHAR(255),
            cancelled BOOLEAN,
            diverted BOOLEAN,
            distance INT
        );""")
    except Exception as e: exitScript(["Problem creating fact table.", str(e)])

    # Status update
    statUp('Creating fact table OK.')

    # Insert data from array to the fact table. Using parameterized queries 
    # for security. Note that %s (positional arguments) must always be 
    # passed as a sequence, thus put value in a list. If error on inserting 
    # happens, then exit script without commiting
    try:
        for i in range(len(fliLst)):
            # Insert data on fact_flights table
            cur.execute("""INSERT INTO fact_flights (
                transactionid, time_id, airline_id, origin_id, dest_id, 
                flightnum, tailnum, cancelled, diverted, distance) VALUES (
                %s, (SELECT time_id FROM dim_time WHERE dim_time.time_id = %s),
                (SELECT airline_id FROM dim_airline WHERE dim_airline.airline_id 
                = %s), (SELECT origin_id FROM dim_origin WHERE 
                dim_origin.origin_id = %s), (SELECT dest_id FROM dim_destination 
                WHERE dim_destination.dest_id = %s), %s, %s, %s, %s, %s)""", 
                ([fliLst[i][dicCol['transactionid']], i+1, i+1, i+1, i+1, 
                fliLst[i][dicCol['flightnum']], fliLst[i][dicCol['tailnum']],
                fliLst[i][dicCol['cancelled']], fliLst[i][dicCol['diverted']],
                fliLst[i][dicCol['distance']]]))
            if i % 10000 == 0: comUp('inserting data on fact table', i)
    except Exception as e: exitScript(["Problem inserting fact data.", str(e)])
    
    # Adding new requested columns and views
    colLst.extend(['depdelayover15', 'distance_group'])
    colDep, colDis = colLst.index('depdelay'), colLst.index('distance')
    tmpLst = [[], []]
    for row in fliLst:
        # creating a new column "depdelayover15" that indicates if the 
        # departure delay in minutes (DEPDELAY) is greater than 15
        if row[colDep] == None: tmpLst[0].append(None)
        elif row[colDep] > 15: tmpLst[0].append(True)
        else: tmpLst[0].append(False)

        # adding column "distance_group". 
        fltDiv, flrDiv = row[colDis]/100, row[colDis]//100
        if flrDiv == 0: tmpLst[1].append('0-100')
        elif fltDiv > flrDiv: 
            tmpLst[1].append(str(flrDiv*100+1)+'-'+str((flrDiv*100)+100))
        else: 
            tmpLst[1].append(str((flrDiv*100+1)-100)+'-'+str(flrDiv*100))
		
	# Creating extra columns on the fact_flights table
    try:
        cur.execute("""ALTER TABLE fact_flights ADD COLUMN depdelayover15 
        BOOLEAN, ADD COLUMN distance_group VARCHAR(255);""")
    except Exception as e: 
        exitScript(["Problem creating cols in fact table.", str(e)])

    # Status update
    statUp('Creating columns fact table OK.')

    # Inserting data from array to the newly created columns
    try:
        for i in range(len(fliLst)):
            cur.execute("""UPDATE fact_flights SET depdelayover15 = (%s), 
            distance_group = (%s) WHERE flights_id = (%s)""", 
            ([tmpLst[0][i], tmpLst[1][i], i+1]))
            if i % 10000 == 0: comUp('inserting data on new columns', i)
        statUp('Inserting data in new cols fact table OK') # Status Update
    except Exception as e: 
        exitScript(["Problem inserting new cols fact table data", str(e)])

    #Create view
    try:
        cur.execute("""CREATE VIEW lax_cancelled
        AS SELECT dim_origin.originairportcode, fact_flights.cancelled, 
        fact_flights.transactionid
        FROM dim_origin, fact_flights
        WHERE dim_origin.origin_id=fact_flights.flights_id
        AND fact_flights.cancelled = True
        AND dim_origin.originairportcode = 'LAX'
        """)
    except Exception as e: exitScript(["Problem creating view.", str(e)])

    # Status update
    statUp('Creating view OK.')
    
    # Integrity test function (compares select array data to data in the db)
    def intTest():
        lenArr = len(fliLst)
        cur.execute("""SELECT distance FROM fact_flights WHERE flights_id 
        = (%s)""", ([lenArr]))
        dbv1, lv1 = cur.fetchone()[0], fliLst[lenArr-1][30]
        cur.execute("""SELECT deststatename FROM dim_destination WHERE dest_id 
        = (%s)""", ([lenArr]))
        dbv2, lv2 = cur.fetchone()[0], fliLst[lenArr-1][15]
        cur.execute("""SELECT distance FROM fact_flights WHERE flights_id 
        = (%s)""", ([lenArr//2]))
        dbv3, lv3 = cur.fetchone()[0], fliLst[(lenArr//2)-1][30]
        cur.execute("""SELECT deststatename FROM dim_destination WHERE dest_id 
        = (%s)""", ([lenArr//2]))
        dbv4, lv4 = cur.fetchone()[0], fliLst[(lenArr//2)-1][15]
        if dbv1 != lv1 or dbv2 != lv2 or dbv3 != lv3 or dbv4 != lv4: 
            print('some integrity tests did not match', dbv1, lv1, dbv2
            , lv2, dbv3, lv3, dbv4, lv4)
            exitScript(["Problem on db vs array integrity test"])
        else: statUp('Database integrity test OK.') # status update
    
    # Call data integrity test
    intTest()

    # Commit to the transaction and close connection
    conn.commit()
    conn.close()
