import mysql.connector

def main():
    exit=1;
    print ("\n>>>>>>>>>>>>> WELCOME TO CHITRAKALA SYSTEM <<<<<<<<<<<<<<")
    while (exit!=0):
        print ("\n\n\t\t\tYou are now in MAIN MENU\n\n")
        print("\t1. Arts Information \n \t2. Customers Information \n \t3. Search \n\t4. Show tables")
        option=int(input("\n\nEnter your value of choice: "));
        if (option == 1):
            art_zone()
        elif (option==2):
            customer_zone()
        elif (option==3):
            search_zone()
        elif (option==4):
            show_tables()
        else:
            print ("\nInvalid input!!");
            continue;

        exit=int(input("\n\nPress 0 to exit or 1 to go back to Main Menu: "));
    print("\n\n***************Thank you for using CHITRAKALA SYSTEM!***************");

def art_zone():
    print("\n\n \t\t\tYou are now in ARTS INFORMATION ZONE\n\n")
    print("\t1. Add a new art \n \t2. Update existing art information")
    choice=int((input( "\nWhat do u want to do? ")))
    if (choice==1):
        add_art()
    elif (choice==2):
        update_art()
    else:
        print("\n\tInvalid input")
        art_zone()

def customer_zone():
    print("\n\n \t\t\tYou are now in CUSTOMERS INFORMATION ZONE \n\n")
    print("\t1. Add a new customer \n \t2. Remove a customer \n \t3. Update existing customer information")
    choice=int((input( "\nWhat do u want to do? ")))
    if (choice==1):
        add_customer()
    elif (choice==2):
        remove_customer()
    elif (choice==3):
        update_customer()
    else:
        print("\n\tInvalid input")
        customer_zone()

def search_zone():
    print("\n\n \t\t\tYou are now in SEARCH ZONE \n\n")
    print("\t1. Search for a customer \n \t2. Search for an art")
    choice=int((input( "\nWhat do u want to search: ")))
    if choice==1:
        customer=input("\nEnter the name of customer: ")
        sql6="select* from tbl_customers where Customer_name like'%"+customer+"%';"
    if choice==2:
        art=input("Enter the name of art or artist: ")
        sql6="select * from tbl_art where Art_name like '%"+art+"%'or Artist_name like'%"+art+"%';"
    db_connection1(sql6)
    option=int(input("\n\t1. Go back to SEARCH ZONE \n\t2. Exit SEARCH ZONE\n\nEnter you choice: "))
    if (option==1):
        search_zone()
    elif(option==2):
        return 0;
    else:
        print("\n\tInvalid input!")

def show_tables():
    print("\n--You are now in VIEW ZONE--")
    choice=int(input("\n\t1. Art table \n\t2. Customer table\n\n Enter you choice: "))
    if(choice==1):
        query7="Select * from tbl_art;"
    elif (choice==2):
        query7="Select * from tbl_customers;"
    else:
        print("\n\t Invalid input!")
        show_tables()
    db_connection1(query7)

def add_art():
    print("\n--You chose to add art!--")
    Art_code=input("\nEnter Art code: ");
    Art_name=input("Enter Art title: ");
    Artist_name=input("Enter Artist name: ");
    Art_style=input("Enter Art style: ");
    Art_datemade=input("Enter the Date made(yyyy-mm-dd): ");
    Art_status=input("Enter art status(Available/Sold): ");
    Art_buy_price=input("Enter buying price of art: ");
    sql1="insert into tbl_art values ("+Art_code+",'"+Art_name+"','"+Artist_name+"', '"+Art_style+"', '"+Art_datemade+"','"+Art_status+"',"+Art_buy_price+");"
    db_connection(sql1)
    print("\n\t**Value added!**")
    option=int(input("\n\t1. Enter again \n\t2. Go back to ART ZONE \n\t3. Exit ART ZONE\n\nEnter you choice: "))
    if (option==1):
        add_art()
    elif(option==2):
        art_zone()
    elif(option==3):
        return 0;
    else:
        print("\n\tInvalid input!")

def update_art():
    print("\n--You chose to update art!--")
    choice=int(input("\nOptions:\n \t1. Art Name \n\t2. Artist Name \n\t3. Art style \n\t4. Art Datemade \n\t5. Art Status \n\t6. Art Buy price\n\nEnter what to update:"))
    if(choice>6):
        print("\n\nInvalid input choice!!")
        update_art()
    Update_old=input("Enter Art code to be updated: ")
    Updated_value=input("\nEnter new value: ")
    if (choice==1):
        sql4="update tbl_art set Art_name='"+Updated_value+"' where Art_code="+Update_old+";"
    elif (choice==2):
        sql4="update tbl_art set Artist_name='"+Updated_value+"' where Art_code="+Update_old+";"
    elif (choice==3):
        sql4="update tbl_art set Art_style='"+Updated_value+"' where Art_code="+Update_old+";"
    elif (choice==4):
        sql4="update tbl_art set Art_datemade='"+Updated_value+"' where Art_code="+Update_old+";"
    elif (choice==5):
        sql4="update tbl_art set Art_status='"+Updated_value+"'where Art_code="+Update_old+";"
    elif (choice==6):
        sql4="update tbl_art set Art_buyprice="+Updated_value+" where Art_code="+Update_old+";"
    db_connection(sql4)
    print("\n\t**Value updated!**")
    option=int(input("\n\t1. Enter again \n\t2. Go back to ART ZONE \n\t3. Exit ART ZONE\n\nEnter you choice: "))
    if (option==1):
        update_art()
    elif(option==2):
        art_zone()
    elif(option==3):
        return 0;
    else:
        print("\n\tInvalid input!")

def add_customer():
    print("\n--You chose to add customer!--")
    Customer_id=input("\nEnter Customer's id: ");
    Customer_name=input("Enter Customer's name: ");
    Customer_phone=input("Enter Customer's phone number: ");
    Customer_address=input("Enter Customer's address: ");
    Art_code=input("Enter the Art code: ");
    Art_sell_price=input("Enter the selling price: ")
    sql5="update tbl_art set Art_status='Sold'where Art_code='"+Art_code+"';"
    db_connection(sql5)
    sql2="insert into tbl_customers value("+Customer_id+",'"+Customer_name+"',"+Customer_phone+", '"+Customer_address+"', "+Art_code+","+Art_sell_price+");"
    db_connection(sql2)
    print("\n\t**Value added!**")
    option=int(input("\n\t1. Enter again \n\t2. Go back to CUSTOMER ZONE \n\t3. Exit CUSTOMER ZONE\n\nEnter you choice: "))
    if (option==1):
        add_customer()
    elif(option==2):
        customer_zone()
    elif(option==3):
        return 0;
    else:
        print("\n\tInvalid input!")

def remove_customer():
    print("\n--You chose to remove customer!--")
    Delete_id=input("\nEnter the Customer id to be deleted: ");
    sql3="delete from tbl_customers where Customer_id="+Delete_id+";"
    db_connection(sql3);
    print("\n\t**Value removed!**")
    option=int(input("\n\t1. Enter again \n\t2. Go back to CUSTOMER ZONE \n\t3. Exit CUSTOMER ZONE\n\nEnter you choice: "))
    if (option==1):
        remove_customer()
    elif(option==2):
        customer_zone()
    elif(option==3):
        return 0;
    else:
        print("\n\tInvalid input!")

def update_customer():
    print("/n--You chose to update customer!--")
    choice=int(input("\nOptions:\n \t1. Customer Name \n\t2. Customer phone number\n\t3. Customer Address\n\nEnter what to update:"))
    if(choice>3):
        print("\n\nInvalid input choice!!")
        update_customer()
    Update_old=input("Enter Customer code to be updated: ")
    Updated_value=input("\nEnter new value: ")
    if (choice==1):
        sql5="update tbl_customers set Customer_name='"+Updated_value+"' where Customer_id="+Update_old+";"
    elif (choice==2):
        sql5="update tbl_customers set Customer_phone="+Updated_value+" where Customer_id="+Update_old+";"
    elif (choice==3):
        sql5="update tbl_customers set Customer_address='"+Updated_value+"' where Customer_id="+Update_old+";"
    db_connection(sql5)
    print("\n\t**Value updated!**")
    option=int(input("\n\t1. Enter again \n\t2. Go back to CUSTOMER ZONE \n\t3. Exit CUSTOMER ZONE\n\nEnter you choice: "))
    if (option==1):
        update_customer()
    elif(option==2):
        customer_zone()
    elif(option==3):
        return 0;
    else:
        print("\n\tInvalid input!")

def db_connection(sql_query):
    try:
        cnx=mysql.connector.connect(user="root", password='root', host='127.0.0.1', database='Chitrakala')
        cur=cnx.cursor()
        cur.execute(sql_query)
        cnx.commit()
        cnx.close()
    except mysql.connector.DataError as e:
        print("DataError")
        print(e)

    except mysql.connector.InternalError as e:
        print("InternalError")
        print(e)

    except mysql.connector.IntegrityError as e:
        print("IntegrityError")
        print(e)

    except mysql.connector.OperationalError as e:
        print("OperationalError")
        print(e)

    except mysql.connector.NotSupportedError as e:
        print("NotSupportedError")
        print(e)

    except mysql.connector.ProgrammingError as e:
        print("ProgrammingError")
        print(e)

    except :
        print("Unknown error occurred")

def db_connection1(sql_query):
    cnx=mysql.connector.connect(user="root", password='root', host='127.0.0.1', database='Chitrakala')
    cur=cnx.cursor()
    cur.execute(sql_query)
    for row in cur.fetchall():
        print(row)
    cnx.close()

main()
