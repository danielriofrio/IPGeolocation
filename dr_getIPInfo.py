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

    IPs = ['116.31.116.26', '121.18.238.32', '209.92.176.15', '181.39.126.182', '116.31.116.27',
           '121.18.238.19', '221.194.44.194', '198.12.64.50', '218.64.253.179', '221.194.44.227']

    for ip in IPs:
        array = ip.split('.')
        w = int(array[0])
        x = int(array[1])
        y = int(array[2])
        z = int(array[3])
        ipnumber = 16777216 * w + 65536 * x + 256 * y + z

        value = dr_dbconnection.dr_getIPInfo(conn, ipnumber)

        print ip + ":" + str(ipnumber) + " - " + str(value)

    conn.close()
