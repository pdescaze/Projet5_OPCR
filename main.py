""" main.py is the main file of Pure Beurre's Application
It permits to execute the Application. This is where all functions 
and methos are executed resulting in pages displaying"""

import os
import sys
import re
import sqlalchemy
import content.recovery as recovery
from content.ui import Ui
from content.database import Database



PROCEED_MENU = True
PAGE_COUNT_CATEGORIES = 0
PAGE_COUNT_PRODUCTS = 0
PAGE_COUNT_SUBSTITUTES = 0
PAGE_COUNT_REGISTERED = 0
CATEGORIES_NUMBER = 0
PRODUCTS_NUMBER = 0
SUBSTITUTES_NUMBER = 0
REGISTERED_NUMBER = 0

#Initialisation of ui's object
ui = Ui()



while PROCEED_MENU is True:

    os.system("cls")
    ui.main_page_database_display()

    if ui.choice_database == "1":
        os.system("cls")
        PROCEED_MENU = False
        PROCEED_USERNAME = True

        while PROCEED_USERNAME is True:
            os.system("cls")
            ui.username_display()

            if ui.choice_username == "#quit":
                sys.exit(recovery.closing_application())
            else:
                PROCEED_USERNAME = False
                PROCEED_PASSWORD = True

                while PROCEED_PASSWORD is True:
                    os.system("cls")
                    ui.password_display()

                    if ui.choice_password == "#quit":
                        sys.exit("Closing the Application")
                    elif ui.choice_password == "#un":
                        PROCEED_PASSWORD = False
                        PROCEED_USERNAME = True
                    else:
                        PROCEED_PASSWORD = False
                        PROCEED_HOST = True

                        while PROCEED_HOST is True:
                            os.system("cls")
                            ui.host_display()

                            if ui.choice_host == "#quit":
                                sys.exit("Closing the Application")

                            elif ui.choice_host == "#pm":
                                PROCEED_HOST = False
                                PROCEED_PASSWORD = True

                            elif ui.choice_host == "#un":
                                PROCEED_HOST = False
                                PROCEED_USERNAME = True

                            else:
                                base = Database(ui.choice_username, ui.choice_password, ui.choice_host)
                                base.connect_to_mysql()
                                if base.conn_answer != "":
                                    os.system("cls")
                                    ui.connect_database_fail()
                                    if ui.choice_connect_database_fail == "#quit":
                                        sys.exit("Closing the Application")
                                    else:
                                        PROCEED_HOST = False
                                        PROCEED_MENU = True
                                else:
                                    PROCEED_HOST = False
                                    PROCEED_DATABASE_MENU = True

                                    while PROCEED_DATABASE_MENU:
                                        os.system("cls")
                                        ui.database_menu()

                                        if ui.choice_database_menu == "#hm":
                                            PROCEED_DATABASE_MENU = False
                                            PROCEED_HOST = True

                                        elif ui.choice_database_menu == "#pm":
                                            PROCEED_DATABASE_MENU = False
                                            PROCEED_PASSWORD = True

                                        elif ui.choice_database_menu == "#un":
                                            PROCEED_DATABASE_MENU = False
                                            PROCEED_USERNAME = True

                                        elif ui.choice_database_menu == "1":
                                            PROCEED_DATABASE_MENU = False
                                            PROCEED_DATABASE_CREATION = True

                                            while PROCEED_DATABASE_CREATION:
                                                os.system("cls")
                                                ui.creation_database()

                                                if ui.choice_creation_database == "#quit":
                                                    sys.exit("Closing the Application")

                                                elif ui.choice_creation_database == "#dm":
                                                    PROCEED_DATABASE_CREATION = False
                                                    PROCEED_DATABASE_MENU = True

                                                else:
                                                    PROCEED_DATABASE_CREATION = False
                                                    PROCEED_DATABASE_CREATION_1 = True

                                                    while PROCEED_DATABASE_CREATION_1:
                                                        os.system("cls")
                                                        ui.creation_database_loading_page_start()

                                                        if ui.choice_creation_database in recovery.show_databases_check_list(base.conn):
                                                            PROCEED_DATABASE_CREATION_1 = False
                                                            PROCEED_DATABASE_CREATION_FAIL = True

                                                            while PROCEED_DATABASE_CREATION_FAIL:
                                                                os.system("cls")
                                                                ui.creation_database_loading_fail()

                                                                if ui.choice_creation_database_loading_fail == "#quit":
                                                                    sys.exit("Closing the Application")

                                                                elif ui.choice_creation_database_loading_fail == "#dm":
                                                                    PROCEED_DATABASE_CREATION_FAIL = False
                                                                    PROCEED_DATABASE_MENU = True

                                                                else:
                                                                    PROCEED_DATABASE_CREATION_FAIL = False
                                                                    PROCEED_DATABASE_CREATION = True

                                                        elif ui.choice_creation_database == "#quit":
                                                            sys.exit("Closing the Application")

                                                        else:
                                                            os.system("cls")
                                                            ui.creation_database_loading_started()
                                                            base.connect_to_database(ui.choice_creation_database)
                                                            base.tables_creation()
                                                            os.system("cls")
                                                            ui.creation_database_loading_in_progress("T", "F", "F")
                                                            base.get_categories_name_url()
                                                            base.insert_categories()
                                                            os.system("cls")
                                                            ui.creation_database_loading_in_progress("T", "C", "F")
                                                            base.get_products()
                                                            os.system("cls")
                                                            ui.creation_database_loading_in_progress("T", "C", "P")
                                                            base.insert_product_cat_id()
                                                            os.system("cls")
                                                            ui.creation_database_loading_page_end()

                                                            if ui.creation_database == "#dm":
                                                                PROCEED_DATABASE_CREATION = False
                                                                PROCEED_DATABASE_MENU = True

                                                            elif ui.creation_database == "#quit":
                                                                sys.exit("Closing the Application")

                                                            else:
                                                                PROCEED_DATABASE_CREATION_1 = False
                                                                PROCEED_DATABASE_MENU = True

                                        elif ui.choice_database_menu == "2":
                                            os.system("cls")
                                            PROCEED_DATABASE_MENU = False
                                            PROCEED_DATABASE_TO_DELETE = True

                                            while PROCEED_DATABASE_TO_DELETE:
                                                os.system("cls")
                                                ui.delete_database_start(base.conn)

                                                if ui.choice_delete_database_start == "#quit":
                                                    sys.exit("Closing the Application")

                                                elif ui.choice_delete_database_start == "#dm":
                                                    PROCEED_DATABASE_TO_DELETE = False
                                                    PROCEED_DATABASE_MENU = True

                                                elif ui.choice_delete_database_start in recovery.show_databases_check_list(base.conn):
                                                    recovery.delete_database(base.conn, ui.choice_delete_database_start)
                                                    PROCEED_DATABASE_TO_DELETE = False
                                                    PROCEED_DATABASE_DELETED = True

                                                    while PROCEED_DATABASE_DELETED is True:
                                                        os.system("cls")
                                                        ui.delete_database_end(ui.choice_delete_database_start)

                                                        if ui.choice_delete_database_end == "#dm":
                                                            PROCEED_DATABASE_DELETED = False
                                                            PROCEED_DATABASE_MENU = True

                                                        elif ui.choice_delete_database_end == "#quit":
                                                            sys.exit("Closing the Application")


                                        elif ui.choice_database_menu == "3":
                                            os.system("cls")
                                            PROCEED_DATABASE_MENU = False
                                            PROCEED_SELECT_DATABASE = True

                                            while PROCEED_SELECT_DATABASE is True:
                                                os.system("cls")
                                                ui.select_database(base.conn)                                           

                                                if ui.choice_select_database == "#quit":
                                                    sys.exit("Closing the Application")

                                                elif ui.choice_select_database == "#dm":
                                                    PROCEED_SELECT_DATABASE = False
                                                    PROCEED_DATABASE_MENU = True

                                                elif ui.choice_select_database in recovery.show_databases_check_list(base.conn):
                                                    base.connect_to_database(ui.choice_select_database)
                                                    PROCEED_SELECT_DATABASE = False
                                                    PROCEED_APP = True

                                                    while PROCEED_APP is True:                              
                                                        os.system("cls")
                                                        try:
                                                            ui.main_page_display()

                                                            if ui.choice_proceed_categories == "1":
                                                                PROCEED_APP = False
                                                                PROCEED_CATEGORIES = True

                                                                while PROCEED_CATEGORIES is True:
                                                                    os.system("cls")                                                                
                                                                    ui.categories_display(base.conn, PAGE_COUNT_CATEGORIES)
                                                                    ui.categories_id_check_list(base.conn, PAGE_COUNT_CATEGORIES)                                                                                                       

                                                                    if ui.choice_categorie == "#mm":
                                                                        PAGE_COUNT_CATEGORIES = 0
                                                                        PAGE_COUNT_PRODUCTS = 0
                                                                        PAGE_COUNT_SUBSTITUTES = 0
                                                                        PROCEED_CATEGORIES = False
                                                                        PROCEED_APP = True

                                                                    elif ui.choice_categorie == ">":
                                                                        if PAGE_COUNT_CATEGORIES < recovery.get_number_page_categories(base.conn, CATEGORIES_NUMBER):
                                                                            PAGE_COUNT_CATEGORIES += 1

                                                                    elif ui.choice_categorie == "<":
                                                                        if PAGE_COUNT_CATEGORIES > 0:
                                                                            PAGE_COUNT_CATEGORIES -= 1

                                                                    elif ui.choice_categorie == "#quit":
                                                                        sys.exit("Closing the Application")

                                                                    elif re.search("([0-9]{1,})", ui.choice_categorie):
                                                                        ui.choice_categorie = int(ui.choice_categorie)
                                                                        if ui.choice_categorie in ui.categories_id_list:
                                                                            PROCEED_CATEGORIES = False
                                                                            PROCEED_PRODUCTS = True

                                                                            while PROCEED_PRODUCTS is True:
                                                                                os.system("cls")
                                                                                ui.products_display(base.conn, ui.choice_categorie, PAGE_COUNT_PRODUCTS)
                                                                                ui.products_id_check_list(base.conn, ui.choice_categorie, PAGE_COUNT_PRODUCTS)                                                              

                                                                                if ui.choice_product == "#mm":
                                                                                    PAGE_COUNT_CATEGORIES = 0
                                                                                    PAGE_COUNT_PRODUCTS = 0
                                                                                    PAGE_COUNT_SUBSTITUTES = 0
                                                                                    PROCEED_PRODUCTS = False
                                                                                    PROCEED_APP = True

                                                                                elif ui.choice_product == ">":
                                                                                    if PAGE_COUNT_PRODUCTS < recovery.get_number_page_products(base.conn, ui.choice_categorie, PRODUCTS_NUMBER):
                                                                                        PAGE_COUNT_PRODUCTS += 1

                                                                                elif ui.choice_product == "<":
                                                                                    if PAGE_COUNT_PRODUCTS > 0:
                                                                                        PAGE_COUNT_PRODUCTS -= 1

                                                                                elif ui.choice_product == "#quit":
                                                                                    sys.exit("Closing the Application")

                                                                                elif ui.choice_product == "#cm":
                                                                                    PAGE_COUNT_CATEGORIES = 0
                                                                                    PAGE_COUNT_PRODUCTS = 0
                                                                                    PAGE_COUNT_SUBSTITUTES = 0
                                                                                    PROCEED_PRODUCTS = False
                                                                                    PROCEED_CATEGORIES = True

                                                                                elif re.search("([0-9]{1,})", ui.choice_product):
                                                                                    ui.choice_product = int(ui.choice_product)
                                                                                    if ui.choice_product in ui.products_id_list:
                                                                                        PROCEED_PRODUCTS = False
                                                                                        PROCEED_PRODUCTS_DETAILS = True

                                                                                        while PROCEED_PRODUCTS_DETAILS is True:
                                                                                            os.system("cls")
                                                                                            ui.products_details_display(base.conn, ui.choice_categorie, ui.choice_product)

                                                                                            if ui.choice_product_details == "#mm":
                                                                                                PAGE_COUNT_CATEGORIES = 0
                                                                                                PAGE_COUNT_PRODUCTS = 0
                                                                                                PAGE_COUNT_SUBSTITUTES = 0
                                                                                                PROCEED_PRODUCTS_DETAILS = False
                                                                                                PROCEED_APP = True

                                                                                            elif ui.choice_product_details == "#quit":
                                                                                                sys.exit("Closing the Application")

                                                                                            elif ui.choice_product_details == "#cm":
                                                                                                PAGE_COUNT_CATEGORIES = 0
                                                                                                PAGE_COUNT_PRODUCTS = 0
                                                                                                PAGE_COUNT_SUBSTITUTES = 0
                                                                                                PROCEED_PRODUCTS_DETAILS = False
                                                                                                PROCEED_CATEGORIES = True

                                                                                            elif ui.choice_product_details == "#pm":
                                                                                                PAGE_COUNT_PRODUCTS = 0
                                                                                                PAGE_COUNT_SUBSTITUTES = 0
                                                                                                PROCEED_PRODUCTS_DETAILS = False
                                                                                                PROCEED_PRODUCTS = True

                                                                                            elif ui.choice_product_details == "#substitute":
                                                                                                PROCEED_PRODUCTS_DETAILS = False
                                                                                                PROCEED_SUBSTITUTES = True

                                                                                                while PROCEED_SUBSTITUTES:
                                                                                                    os.system("cls")
                                                                                                    ui.substitutes_display(base.conn, ui.choice_categorie, ui.choice_product, PAGE_COUNT_SUBSTITUTES)
                                                                                                    ui.substitutes_id_check_list(base.conn, ui.choice_categorie, ui.choice_product, PAGE_COUNT_SUBSTITUTES)                                                                     

                                                                                                    if ui.choice_substitutes == "#quit":
                                                                                                        sys.exit("Closing the Application")

                                                                                                    elif ui.choice_substitutes == ">":
                                                                                                        if PAGE_COUNT_SUBSTITUTES < recovery.get_number_page_substitutes(base.conn, ui.choice_categorie, ui.choice_product, SUBSTITUTES_NUMBER):
                                                                                                            PAGE_COUNT_SUBSTITUTES += 1

                                                                                                    elif ui.choice_substitutes == "<":
                                                                                                        if PAGE_COUNT_SUBSTITUTES > 0:
                                                                                                            PAGE_COUNT_SUBSTITUTES -= 1

                                                                                                    elif ui.choice_substitutes == "#pd":
                                                                                                        PAGE_COUNT_SUBSTITUTES = 0
                                                                                                        PROCEED_SUBSTITUTES = False
                                                                                                        PROCEED_PRODUCTS_DETAILS = True

                                                                                                    elif ui.choice_substitutes == "#pm":
                                                                                                        PAGE_COUNT_PRODUCTS = 0
                                                                                                        PAGE_COUNT_SUBSTITUTES = 0
                                                                                                        PROCEED_SUBSTITUTES = False
                                                                                                        PROCEED_PRODUCTS = True

                                                                                                    elif ui.choice_substitutes == "#cm":
                                                                                                        PAGE_COUNT_CATEGORIES = 0
                                                                                                        PAGE_COUNT_PRODUCTS = 0
                                                                                                        PAGE_COUNT_SUBSTITUTES = 0
                                                                                                        PROCEED_SUBSTITUTES = False
                                                                                                        PROCEED_CATEGORIES = True

                                                                                                    elif ui.choice_substitutes == "#mm":
                                                                                                        PAGE_COUNT_CATEGORIES = 0
                                                                                                        PAGE_COUNT_PRODUCTS = 0
                                                                                                        PAGE_COUNT_SUBSTITUTES = 0
                                                                                                        PROCEED_SUBSTITUTES = False
                                                                                                        PROCEED_APP = True

                                                                                                    elif re.search("([0-9]{1,})", ui.choice_substitutes):
                                                                                                        ui.choice_substitutes = int(ui.choice_substitutes)
                                                                                                        if ui.choice_substitutes in ui.substitutes_id_list:
                                                                                                            PROCEED_SUBSTITUTES = False
                                                                                                            PROCEED_SUBSTITUTES_DETAILS = True

                                                                                                            while PROCEED_SUBSTITUTES_DETAILS:
                                                                                                                os.system("cls")
                                                                                                                ui.substitutes_details(base.conn, ui.choice_categorie, ui.choice_substitutes)

                                                                                                                if ui.choice_substitutes_details == "#quit":
                                                                                                                    sys.exit("Closing the Application")

                                                                                                                elif ui.choice_substitutes_details == "#save":
                                                                                                                    PROCEED_SUBSTITUTES_DETAILS = False
                                                                                                                    PROCEED_SUBSTITUTES_SAVED = True

                                                                                                                    while PROCEED_SUBSTITUTES_SAVED:
                                                                                                                        os.system("cls")
                                                                                                                        ui.save_substitute(base.conn, ui.choice_categorie, ui.choice_substitutes)

                                                                                                                        if ui.choice_substitute_saved == "#quit":
                                                                                                                            sys.exit("Closing the Application")
                                                                                                                        
                                                                                                                        elif ui.choice_substitute_saved == "#sd":
                                                                                                                            PROCEED_SUBSTITUTES_SAVED = False
                                                                                                                            PROCEED_SUBSTITUTES_DETAILS = True

                                                                                                                        elif ui.choice_substitute_saved == "#sm":
                                                                                                                            PAGE_COUNT_SUBSTITUTES = 0
                                                                                                                            PROCEED_SUBSTITUTES_SAVED = False
                                                                                                                            PROCEED_SUBSTITUTES = True

                                                                                                                        elif ui.choice_substitute_saved == "#pd":
                                                                                                                            PAGE_COUNT_SUBSTITUTES = 0
                                                                                                                            PROCEED_SUBSTITUTES_SAVED = False
                                                                                                                            PROCEED_PRODUCTS_DETAILS = True

                                                                                                                        elif ui.choice_substitute_saved == "#pm":
                                                                                                                            PAGE_COUNT_PRODUCTS = 0
                                                                                                                            PAGE_COUNT_SUBSTITUTES = 0
                                                                                                                            PROCEED_SUBSTITUTES_SAVED = False
                                                                                                                            PROCEED_PRODUCTS = True

                                                                                                                        elif ui.choice_substitute_saved == "#cm":
                                                                                                                            PAGE_COUNT_CATEGORIES = 0
                                                                                                                            PAGE_COUNT_PRODUCTS = 0
                                                                                                                            PAGE_COUNT_SUBSTITUTES = 0
                                                                                                                            PROCEED_SUBSTITUTES_SAVED = False
                                                                                                                            PROCEED_CATEGORIES = True

                                                                                                                        elif ui.choice_substitute_saved == "#mm":
                                                                                                                            PAGE_COUNT_CATEGORIES = 0
                                                                                                                            PAGE_COUNT_PRODUCTS = 0
                                                                                                                            PAGE_COUNT_SUBSTITUTES = 0
                                                                                                                            PROCEED_SUBSTITUTES_SAVED = False
                                                                                                                            PROCEED_APP = True                                                                                                          

                                                                                                                elif ui.choice_substitutes_details == "#sm":
                                                                                                                    PAGE_COUNT_SUBSTITUTES = 0
                                                                                                                    PROCEED_SUBSTITUTES_DETAILS = False
                                                                                                                    PROCEED_SUBSTITUTES = True

                                                                                                                elif ui.choice_substitutes_details == "#pd":
                                                                                                                    PAGE_COUNT_SUBSTITUTES = 0
                                                                                                                    PROCEED_SUBSTITUTES_DETAILS = False
                                                                                                                    PROCEED_PRODUCTS_DETAILS = True

                                                                                                                elif ui.choice_substitutes_details == "#pm":
                                                                                                                    PAGE_COUNT_PRODUCTS = 0
                                                                                                                    PAGE_COUNT_SUBSTITUTES = 0
                                                                                                                    PROCEED_SUBSTITUTES_DETAILS = False
                                                                                                                    PROCEED_PRODUCTS = True

                                                                                                                elif ui.choice_substitutes_details == "#cm":
                                                                                                                    PAGE_COUNT_CATEGORIES = 0
                                                                                                                    PAGE_COUNT_PRODUCTS = 0
                                                                                                                    PAGE_COUNT_SUBSTITUTES = 0
                                                                                                                    PROCEED_SUBSTITUTES_DETAILS = False
                                                                                                                    PROCEED_CATEGORIES = True

                                                                                                                elif ui.choice_substitutes_details == "#mm":
                                                                                                                    PAGE_COUNT_CATEGORIES = 0
                                                                                                                    PAGE_COUNT_PRODUCTS = 0
                                                                                                                    PAGE_COUNT_SUBSTITUTES = 0
                                                                                                                    PROCEED_SUBSTITUTES_DETAILS = False
                                                                                                                    PROCEED_APP = True

                                                                                            elif ui.choice_product_details == "#save":
                                                                                                PROCEED_PRODUCTS_DETAILS = False
                                                                                                PROCEED_PRODUCT_SAVED = True

                                                                                                while PROCEED_PRODUCT_SAVED:                                                                                    
                                                                                                    os.system("cls")
                                                                                                    ui.save_product(base.conn, ui.choice_categorie, ui.choice_product)

                                                                                                    if ui.choice_product_saved == "#quit":
                                                                                                        sys.exit("Closing the Application")

                                                                                                    elif ui.choice_product_saved == "#pd":
                                                                                                        PAGE_COUNT_SUBSTITUTES = 0
                                                                                                        PROCEED_PRODUCT_SAVED = False
                                                                                                        PROCEED_PRODUCTS_DETAILS = True

                                                                                                    elif ui.choice_product_saved == "#pm":
                                                                                                        PAGE_COUNT_PRODUCTS = 0
                                                                                                        PAGE_COUNT_SUBSTITUTES = 0
                                                                                                        PROCEED_PRODUCT_SAVED = False
                                                                                                        PROCEED_PRODUCTS = True

                                                                                                    elif ui.choice_product_saved == "#cm":
                                                                                                        PAGE_COUNT_CATEGORIES = 0
                                                                                                        PAGE_COUNT_PRODUCTS = 0
                                                                                                        PAGE_COUNT_SUBSTITUTES = 0
                                                                                                        PROCEED_PRODUCT_SAVED = False
                                                                                                        PROCEED_CATEGORIES = True

                                                                                                    elif ui.choice_product_saved == "#mm":
                                                                                                        PAGE_COUNT_CATEGORIES = 0
                                                                                                        PAGE_COUNT_PRODUCTS = 0
                                                                                                        PAGE_COUNT_SUBSTITUTES = 0
                                                                                                        PROCEED_PRODUCT_SAVED = False
                                                                                                        PROCEED_APP = True

                                                            elif ui.choice_proceed_categories == "2":
                                                                PROCEED_REGISTERED_PRODUCTS = True

                                                                while PROCEED_REGISTERED_PRODUCTS:
                                                                    os.system("cls")
                                                                    ui.show_registered_products(base.conn, PAGE_COUNT_REGISTERED)
                                                                    ui.registered_product_id_check_list(base.conn, PAGE_COUNT_REGISTERED)                                                                           

                                                                    if ui.choice_registered_products == "#mm":
                                                                        PAGE_COUNT_REGISTERED = 0
                                                                        PROCEED_REGISTERED_PRODUCTS = False
                                                                        PROCEED_CATEGORIES = True

                                                                    elif ui.choice_registered_products == "#quit":
                                                                        sys.exit("Closing the Application")

                                                                    elif ui.choice_registered_products == "#all":
                                                                        PAGE_COUNT_REGISTERED = 0
                                                                        PROCEED_REGISTERED_PRODUCTS = False
                                                                        PROCEED_REGISTERED_PRODUCTS_ALL_DELETED = True

                                                                        while PROCEED_REGISTERED_PRODUCTS_ALL_DELETED:
                                                                            os.system("cls")
                                                                            ui.registered_products_all_deleted(base.conn)

                                                                            if ui.choice_registered_products_all_deleted == "#quit":
                                                                                sys.exit("Closing the Application")

                                                                            elif ui.choice_registered_products_all_deleted == "#mm":
                                                                                PAGE_COUNT_REGISTERED = 0
                                                                                PROCEED_REGISTERED_PRODUCTS_ALL_DELETED = False
                                                                                PROCEED_APP = True

                                                                    elif ui.choice_registered_products == ">":
                                                                        if PAGE_COUNT_REGISTERED < recovery.get_number_page_registered_products(base.conn, REGISTERED_NUMBER):
                                                                            PAGE_COUNT_REGISTERED += 1

                                                                    elif ui.choice_registered_products == "<":
                                                                        if PAGE_COUNT_REGISTERED > 0:
                                                                            PAGE_COUNT_REGISTERED -= 1

                                                                    elif re.search("([0-9]{1,})", ui.choice_registered_products):
                                                                        ui.choice_registered_products = int(ui.choice_registered_products)
                                                                        if ui.choice_registered_products in ui.registered_products_id:
                                                                            PROCEED_REGISTERED_PRODUCTS = False
                                                                            PROCEED_REGISTERED_PRODUCTS_DETAILS = True

                                                                            while PROCEED_REGISTERED_PRODUCTS_DETAILS:
                                                                                os.system("cls")
                                                                                ui.registered_products_details_display(base.conn, ui.choice_registered_products)

                                                                                if ui.choice_registered_products_details_display == "#quit":
                                                                                    sys.exit("Closing the Application")

                                                                                elif ui.choice_registered_products_details_display == "#mm":
                                                                                    PAGE_COUNT_REGISTERED = 0
                                                                                    PROCEED_REGISTERED_PRODUCTS_DETAILS = False
                                                                                    PROCEED_CATEGORIES = True

                                                                                elif ui.choice_registered_products_details_display == "#rp":
                                                                                    PAGE_COUNT_REGISTERED = 0
                                                                                    PROCEED_REGISTERED_PRODUCTS_DETAILS = False
                                                                                    PROCEED_REGISTERED_PRODUCTS = True
                                                                        
                                                                    elif ui.choice_registered_products == "#del":
                                                                        PAGE_COUNT_REGISTERED = 0
                                                                        PROCEED_REGISTERED_PRODUCTS = False
                                                                        PROCEED_REGISTERED_PRODUCTS_TO_DEL = True

                                                                        while PROCEED_REGISTERED_PRODUCTS_TO_DEL:
                                                                            os.system("cls")
                                                                            ui.show_registered_products_to_del(base.conn, PAGE_COUNT_REGISTERED)
                                                                            ui.registered_product_id_check_list(base.conn, PAGE_COUNT_REGISTERED)                                                                  
                                                                            
                                                                            if ui.choice_registered_products_to_del == "#mm":
                                                                                PAGE_COUNT_REGISTERED = 0
                                                                                PROCEED_REGISTERED_PRODUCTS_TO_DEL = False
                                                                                PROCEED_CATEGORIES = True

                                                                            elif ui.choice_registered_products_to_del == "#quit":
                                                                                sys.exit("Closing the Application")

                                                                            elif ui.choice_registered_products_to_del == "#rp":
                                                                                PAGE_COUNT_REGISTERED = 0
                                                                                PROCEED_REGISTERED_PRODUCTS_TO_DEL = False
                                                                                PROCEED_REGISTERED_PRODUCTS = True

                                                                            elif ui.choice_registered_products_to_del == ">":
                                                                                if PAGE_COUNT_REGISTERED < recovery.get_number_page_registered_products(base.conn, REGISTERED_NUMBER):
                                                                                    PAGE_COUNT_REGISTERED += 1

                                                                            elif ui.choice_registered_products_to_del == "<":
                                                                                if PAGE_COUNT_REGISTERED > 0:
                                                                                    PAGE_COUNT_REGISTERED -= 1

                                                                            elif re.search("([0-9]{1,})", ui.choice_registered_products_to_del):
                                                                                ui.choice_registered_products_to_del = int(ui.choice_registered_products_to_del)
                                                                                
                                                                                if ui.choice_registered_products_to_del in ui.registered_products_id:
                                                                                    PROCEED_REGISTERED_PRODUCTS_TO_DEL = False
                                                                                    PROCEED_REGISTERED_PRODUCTS_DELETED = True

                                                                                    while PROCEED_REGISTERED_PRODUCTS_DELETED:
                                                                                        os.system("cls")
                                                                                        ui.delete_registered_product(base.conn, ui.choice_registered_products_to_del)

                                                                                        if ui.choice_delete_registered_product == "#mm":
                                                                                            PAGE_COUNT_REGISTERED = 0
                                                                                            PROCEED_REGISTERED_PRODUCTS_DELETED = False
                                                                                            PROCEED_APP = True

                                                                                        elif ui.choice_delete_registered_product == "#rp":
                                                                                            PAGE_COUNT_REGISTERED = 0
                                                                                            PROCEED_REGISTERED_PRODUCTS_DELETED = False
                                                                                            PROCEED_REGISTERED_PRODUCTS = True

                                                                                        elif ui.choice_delete_registered_product == "#quit":
                                                                                            sys.exit("Closing the Application")

                                                            elif ui.choice_proceed_categories == "#quit":
                                                                sys.exit("Closing the Application")

                                                            elif ui.choice_proceed_categories == "#dm":
                                                                PROCEED_APP = False
                                                                PROCEED_DATABASE_MENU = True

                                                        except sqlalchemy.exc.ProgrammingError:
                                                            ui.error_message_tables_check()
                                                            PROCEED_APP = False
                                                            PROCEED_DATABASE_MENU = True

                                        elif ui.choice_database_menu == "#quit":
                                            sys.exit("Closing the Application")

                                        elif ui.choice_database_menu == "#un":
                                            PROCEED_DATABASE_MENU = False
                                            PROCEED_USERNAME = True

                                        elif ui.choice_database_menu == "#pw":
                                            PROCEED_DATABASE_MENU = False
                                            PROCEED_PASSWORD = True

                                        elif ui.choice_database_menu == "#hm":
                                            PROCEED_DATABASE_MENU = False
                                            PROCEED_HOST = True

    elif ui.choice_database == "#quit":
        sys.exit("Closing the Application")


os.system("pause")
