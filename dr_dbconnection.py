import psycopg2

def dr_establishConn(server, db, user, password):
    try:
        conn = psycopg2.connect("dbname='"+db+"' user='"+user+"' host='"+server+"' password='"+password+"'")
        return conn
    except psycopg2.Error as e:
        print "Unable to connect to the database"
        print str(e)
        return None

def dr_insertDataWireless(conn, ipnumberlow, ipnumberhigh,
                          countrycode, countryname, region,
                          city, latitude, longitude, zipcode, timezone):
    cur = conn.cursor()
    try:
        query = "INSERT INTO ipgeolocationinfo(" \
                "ipnumberlow, ipnumberhigh, countrycode, countryname, region," \
                "city, latitude, longitude, zipcode, timezone)"\
                "VALUES (%s, %s, %s, %s, %s, " \
                        "%s, %s, %s, %s, %s)"
        cur.execute(query, (ipnumberlow, ipnumberhigh, countrycode, countryname, region, city, latitude, longitude, zipcode, timezone))
        return_value = True
    except psycopg2.Error as e:
        print "Unable to insert data into ipgeolocationinfo: " + str(ipnumberlow) + " - " + str(ipnumberhigh)
        print str(e)
        conn.rollback()
        return_value = False
    else:
        conn.commit()

    return return_value

def dr_getIPInfo(conn, ipnumber):
    cur = conn.cursor()
    try:
        query = "SELECT ipnumberlow, ipnumberhigh, countrycode, countryname, " \
                "       region, city, latitude, longitude, zipcode, timezone " \
                "FROM   ipgeolocationinfo " \
                "WHERE  ipnumberlow <= %s AND ipnumberhigh >= %s"
        cur.execute(query, (ipnumber, ipnumber))
        value = cur.fetchone()
        return_value = value
    except psycopg2.Error as e:
        print "Unable to execute query"
        print str(e)
        conn.rollback()
        return_value = None
    else:
        conn.commit()
    cur.close()
    return return_value
