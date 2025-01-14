import mysql.connector,tabulate

mydb = mysql.connector.connect(host="localhost", user="root", passwd="root")
mycursor = mydb.cursor()
mycursor.execute("USE GMS")

def checktableexists(tablename):
    mycursor.execute("SHOW TABLES LIKE %s", (tablename,))
    rec1 = mycursor.fetchone()
    return rec1

def game():
    if checktableexists("game"):
        pass
    else:
        mycursor.execute("CREATE TABLE game(Game_Number INT, Game_Name VARCHAR(20), Game_Details VARCHAR(20), Application VARCHAR(20));")

def subscriber():
    if checktableexists("subscriber"):
        pass
    else:
        mycursor.execute("CREATE TABLE subscriber(Subscriber_Number INT, Subscriber_Name VARCHAR(20), Subscriber_Email VARCHAR(20), Subscriber_Status VARCHAR(20), Newsletter_Status VARCHAR(10));")

def addgame():
    n = int(input("No. Records to be Added:"))
    for i in range(n):
        print("\nRecord:" + str(i + 1))
        gano = int(input("Enter Game Number:"))
        gana = input("Enter Game Name:")
        gade = input("Enter Game Details:")
        app = input("Enter Application:")
        mycursor.execute("INSERT INTO game VALUES(%s, %s, %s, %s)", (gano, gana, gade, app))
        mydb.commit()

def addsubscriber():
    n = int(input("No. Records to be Added:"))
    for i in range(n):
        print("\nRecord:" + str(i + 1))
        suno = int(input("Enter Subscriber Number:"))
        suna = input("Enter Subscriber Name:")
        suid = input("Enter Subscriber EmailID :")
        while True:
            sust = input("Enter Subscriber Status(Active/Closed):")
            if sust in ["Active", "Closed"]:
                break
            else:
                print("Not a valid Option:")
        while True:
            nes = input("Enter Newsletter Status(Sent/Returned):")
            if nes in ["Sent", "Returned"]:
                break
            else:
                print("Not a valid Option:")
        mycursor.execute("INSERT INTO subscriber VALUES(%s, %s, %s, %s, %s)", (suno, suna, suid, sust, nes))
        mydb.commit()

def modify(tablename):
    tarfie = input("Enter Field to be modified:")
    if tablename == "game":
        if tarfie in ["Game_Number", "Game_Name", "Game_Details", "Application"]:
            tarval = int(input("Enter Game_Number:"))
            chanval = eval(input("Enter new value:"))
            mycursor.execute("UPDATE %s SET %s=%s WHERE %s=%s" % (tablename, tarfie, chanval, "Game_Number", tarval))
            mydb.commit()
        else:
            print("Field Does not Exist")
    else:
        if tarfie in ["Subscriber_Number", "Subscriber_Name", "Subscriber_Email", "Subscriber_Status", "Newsletter_Status"]:
            tarval = int(input("Enter Subscriber_Number:"))
            chanval = eval(input("Enter new value:"))
            mycursor.execute("UPDATE %s SET %s=%s WHERE %s=%s" % (tablename, tarfie, chanval, "Subscriber_Number", tarval))
            mydb.commit()
        else:
            print("Field Does not Exist")

def delete(tablename):
    if tablename == "game":
        gano = int(input("Enter Game Number:"))
        mycursor.execute("DELETE FROM %s WHERE Game_Number=%s" % (tablename, gano))
        mydb.commit()
    else:
        suno = int(input("Enter Subscriber Number:"))
        mycursor.execute("DELETE FROM %s WHERE Subscriber_Number=%s" % (tablename, suno))
        mydb.commit()

def search(tablename):
    if tablename == "game":
        ch = int(input("Search Using\n1.Game Number\n2.Game Name\nOption:"))
        if ch == 1:
            gano = int(input("Enter Game Number:"))
            mycursor.execute("SELECT * FROM game WHERE Game_Number=%s", (gano,))
        elif ch == 2:
            gana = input("Enter Game Name:")
            mycursor.execute("SELECT * FROM game WHERE Game_Name=%s", (gana,))
        header = ["Game Number", "Game Name", "Game Details", "Application"]
    else:
        ch = int(input("Search Using\n1.Subscriber Number\n2.Subscriber Name\nOption:"))
        if ch == 1:
            suno = int(input("Enter Subscriber Number:"))
            mycursor.execute("SELECT * FROM subscriber WHERE Subscriber_Number=%s", (suno,))
        elif ch == 2:
            suna = input("Enter Subscriber Name:")
            mycursor.execute("SELECT * FROM subscriber WHERE Subscriber_Name=%s", (suna,))
        header = ["Subscriber Number", "Subscriber Name", "Subscriber Email", "Subscriber Status", "Newsletter Status"]
    rec = mycursor.fetchall()
    print(tabulate.tabulate(rec, header, tablefmt="grid"))

def ger():
    ch = int(input("Generate Report\n1.Active Subscriber\n2.Closed Subscriber\n3.Newsletter Sent\n4.Newsletter Returned\nOption:"))
    if ch == 1:
        mycursor.execute("SELECT * FROM subscriber WHERE Subscriber_Status='Active'")
        rec = mycursor.fetchall()
        header = ["Subscriber Number", "Subscriber Name", "Subscriber Email", "Subscriber Status", "Newsletter Status"]
        print(tabulate.tabulate(rec, header, tablefmt="grid"))
    elif ch == 2:
        mycursor.execute("SELECT * FROM subscriber WHERE Subscriber_Status='Closed'")
        rec = mycursor.fetchall()
        header = ["Subscriber Number", "Subscriber Name", "Subscriber Email", "Subscriber Status", "Newsletter Status"]
        print(tabulate.tabulate(rec, header, tablefmt="grid"))
    elif ch == 3:
        mycursor.execute("SELECT * FROM subscriber WHERE Newsletter_Status='Sent'")
        rec = mycursor.fetchall()
        header = ["Subscriber Number", "Subscriber Name", "Subscriber Email", "Subscriber Status", "Newsletter Status"]
        print(tabulate.tabulate(rec, header, tablefmt="grid"))
    else:
        mycursor.execute("SELECT * FROM subscriber WHERE Newsletter_Status='Returned'")
        rec = mycursor.fetchall()
        header = ["Subscriber Number", "Subscriber Name", "Subscriber Email", "Subscriber Status", "Newsletter Status"]
        print(tabulate.tabulate(rec, header, tablefmt="grid"))

def admin():
    while True:
        ch = int(input("--------" * 7 + "Gaming Management System" + "--------" * 7 + "\n\nWelcome To Gaming Management System\nAdmin Menu\n\t1.Game\n\t2.Subscriber\n\t3.Generate Report\n\t4.Exit\nOption:"))
        if ch == 1:
            game()
            opt = int(input("\nGame Menu\n\t1.Add\n\t2.Modify\n\t3.Delete\n\t4.Search\nOption:"))
            if opt == 1:
                addgame()
            elif opt == 2:
                modify("game")
            elif opt == 3:
                delete("game")
            elif opt == 4:
                search("game")
            else:
                print("Option does not exist")
        elif ch == 2:
            subscriber()
            opt = int(input("\nSubscriber Menu\n\t1.Add\n\t2.Modify\n\t3.Delete\n\t4.Search\nOption:"))
            if opt == 1:
                addsubscriber()
            elif opt == 2:
                modify("subscriber")
            elif opt == 3:
                delete("subscriber")
            elif opt == 4:
                search("subscriber")
            else:
                print("Option does not exist")
        elif ch == 3:
            ger()
        elif ch == 4:
            break
        else:
            print("Option does not exist")

admin()
        