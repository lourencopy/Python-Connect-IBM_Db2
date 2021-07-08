import ibm_db
#import ibm_db_sa

print("Primeiro teste de sincronização com GitHub")

dsn = "DATABASE=BLUDB;HOSTNAME=dashdb-txn-sbox-yp-dal09-14.services.dal.bluemix.net;PORT=50000;PROTOCOL=TCPIP;UID=cbp19550;PWD=vznz2f@5k44c0rq8;"
dsn_database = "BLUDB"
dsn_drive = "{IBM DB2 ODBC DRIVE}"
dsn_hostname = "dashdb-txn-sbox-yp-dal09-14.services.dal.bluemix.net"
dsn_port = "50000"
dsn_protocol = "TCPIP"
dsn_uid = "cbp19550"
dsn_pwd = "vznz2f@5k44c0rq8"

'''
#Create database connection string
dsn = (
    "DATABASE={0};"
    "HOSTNAME={1};"
    "PORT={2};"
    "PROTOCOL={3};"
    "UID={4};"
    "PWD={5};").format(dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)
'''

#print(dsn)
try:
    #conn = ibm_db.connect(dsn, "cbp19550", "vznz2f@5k44c0rq8")
    conn = ibm_db.connect(dsn, "", "")
    print("Connected!", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

    server = ibm_db.server_info(conn)

    print ("DBMS_NAME: ", server.DBMS_NAME)
    print ("DBMS_VER:  ", server.DBMS_VER)
    print ("DB_NAME:   ", server.DB_NAME)

    
    #stmt1 = ibm_db.exec_immediate(conn,"CREATE TABLE trucks(serial_no varchar(20) PRIMARY KEY NOT NULL, manufacturer varchar(20) NOT NULL, model varchar(20) NOT NULL, engine_size varchar(20) NOT NULL, truck_class varchar(20) NOT NULL)")
    #stmt2 = ibm_db.exec_immediate(conn,"INSERT INTO trucks(seri_no, model, manufacturer, engine_size, truck_class) VALUES('A1234', 'Lonestar', 'International Trucks', 'Cummins ISX15', 'Class 8');")
    #stmt3 = ibm_db.exec_immediate(conn, "INSERT INTO trucks(seri_no, model, manufacturer, engine_size, truck_class) VALUES('B5432', 'Volvo VN', 'Volvo Trucks', 'Volvo D11', 'Heavy Duty Class 8');")
    #stmt4 = ibm_db.exec_immediate(conn, "INSERT INTO trucks(seri_no, model, manufacturer, engine_size, truck_class) VALUES('C5674', 'Kenworth W900', 'Kenworth Truck Co', 'Caterpillar C9', 'Class 8');")

except:
    print("Unable to connect to database", ibm_db.conn_errormsg())
    #print(ibm_db.conn_error)
    #print(ibm_db.conn_errormsg)


# ibm_db.exec_immediate(Connect, "Statement", Options);
# Sintaxe para criar tabela no Db2 via Python;


#Finalizar conexão
ibm_db.close(conn)
