from pandas import *
import dr_dbconnection

if __name__ == "__main__":

    server = "localhost"
    db = "IPGeolocation"
    user = "ipgeolocation_usr"
    password = "ipgeolocation"

    conn = dr_dbconnection.dr_establishConn(server, db, user, password)

    if conn is None:
        print "Error connecting to DB"
        exit(1)
    
    # This code uses the IP2LOCATION-LITE-DB11 from IP2LOCATION.
    df = read_csv('./IP2LOCATION-LITE-DB11/IP2LOCATION-LITE-DB11.CSV')

    counter = 1
    for row in df.iterrows():
        values = row[1]
        ipnumberlow = values['IPNumberLow']
        ipnumberhigh = values['IPNumberHigh']
        countrycode = values['CountryCode']
        countryname = values['CountryName']
        region = values['Region']
        city = values['City']
        latitude = values['Latitude']
        longitude = values['Longitude']
        zipcode = values['ZipCode']
        timezone = values['TimeZone']

        dr_dbconnection.dr_insertDataWireless(conn, ipnumberlow, ipnumberhigh,
                                              countrycode, countryname, region,
                                              city, latitude, longitude, zipcode, timezone)

    conn.close()
