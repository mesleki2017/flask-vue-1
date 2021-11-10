import sqlite3 as sql

tablo_kolon1=[["title","TEXT"],
            ["done","INT"],
            ]


def sql_kolon_txt(tablo_kolon):
    ff="(id INTEGER PRIMARY KEY AUTOINCREMENT,"
    for aa in tablo_kolon:
        ff=ff+aa[0]+"  "+aa[1]+"  NOT NULL,"
    ff=ff[:-1]
    ff=ff+");"
    return ff
    
def ekle_txt(tablo_kolon):
    ff="  ("
    for aa in tablo_kolon:
        ff=ff+aa[0]+","
    ff=ff[:-1]
    ff=ff+") VALUES ("
    for aa in tablo_kolon:
        ff=ff+"?,"
    ff=ff[:-1]
    ff=ff+")"
    return ff


tablo_kolon=sql_kolon_txt(tablo_kolon1)
tablo_ekle_txt=ekle_txt(tablo_kolon1)


def sql_tablo_olustur(tabloisim):
    try:
        conn = sql.connect('liste1.db')
        print ("Opened database successfully")
        komut="CREATE TABLE "
        tablo_ismi=tabloisim+" "
        tablo_ici=tablo_kolon
        komut_son=komut+tablo_ismi+tablo_ici
        conn.execute(komut_son)
        print ("Table created successfully")
    except:
        conn.close()

def addToSqlTable(tabloismi,*args):
    with sql.connect("liste1.db") as con:
        cur = con.cursor()
        komut="INSERT INTO "+ tabloismi+ tablo_ekle_txt
        cur.execute(komut,(args) )  
        con.commit()
        msg = "Record successfully added"
        print(msg)
    con.close()


def tablodan_sil(tabloisim,silenecek_satirlar_listesi):
    komut = "delete from "+ tabloisim +" where id in (%s)" % ','.join(['?'] * len(silenecek_satirlar_listesi))
    con = sql.connect("liste1.db")
    cur = con.cursor()
    cur.execute(komut,silenecek_satirlar_listesi)
    con.commit()
    print("deleted")


def tabloda_duzenle(tabloisim ,duzenlenecek_satir ,duzenlenecek_etiket ,yenideger ):
    komut = "UPDATE " + tabloisim +" SET " + duzenlenecek_etiket + " = " +'"'+ str(yenideger)+'"' + " WHERE ID = " + duzenlenecek_satir
    print ( komut)
    con = sql.connect("liste1.db")
    cur = con.cursor()
    cur.execute(komut)
    con.commit()

def sql_to_list(tabloismi):
    records=sqltabloyu_objeye_aktar(tabloismi)
    liste=objeyi_listeye_aktar(records)
    return liste

#sql databasedeki belirlene tabloyu objeye aktar
def sqltabloyu_objeye_aktar(tabloismi):  
    con = sql.connect("liste1.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from "+ tabloismi )
    records = cur.fetchall()
    cur.close()
    return records

def objeyi_listeye_aktar(obje1):
    liste1=[]
    for xxx in obje1:
        liste1.append(dict(xxx))
    return liste1

