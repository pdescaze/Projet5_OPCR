""" File of Ui's Class. Generate pages that are displayed into the App
according to users' input"""

import content.heading as heading
import content.recovery as recovery

class Ui():
    """ Class which represents the User Interface """
    def __init__(self):
        self.categories_limit = 10
        self.categories_offset = 1
        self.products_limit = 10
        self.products_offset = 1
        self.substitutes_limit = 10
        self.substitutes_offset = 1
        self.registered_products_limit = 10
        self.registered_products_offset = 1

        self.product_id_details = str()
        self.substitute_id_details = str()
        self.registered_product_id_details = str()
        self.product_names = list()
        self.product_id = list()
        self.products_id_list = list()
        self.names_list = list()
        self.nutrition_rate_list = list()

        self.products_names_list = list()
        self.categorie_id_list = list()
        self.categorie_name_list = list()
        
        self.products_product_id_list = list()
        self.products_name_list = list()
        self.substitutes_product_id_list = list()
        self.substitutes_name_list = list()
        self.substitutes_id_list = list()
        self.registered_products_id_list = list()
        self.registered_products_name_list = list()
        self.registered_products_id = list()


    def main_page_database_display(self):
        """ Generate main_page display with 2 input options"""
        heading.main_page_loading()
        print('\t\t1 - Connection to mysql \n\n\n')
        self.choice_database = input('[Connection] : Type 1\n'
                                     '[Quit] : #quit\n\n\t=> ')

        return self.choice_database


    def username_display(self):
        """ Generate username input page display"""
        heading.main_page_loading()
        print('\t\t1 - Write your mysql username \n\n\n')
        self.choice_username = input('[Quit] : #quit\n\n\t=> ')

        return self.choice_username


    def password_display(self):
        """ Generate password input page display """
        heading.main_page_loading()
        print('\t\t1 - Write your mysql password \n\n\n')
        self.choice_password = input('[Username menu] : #un\n'
                                     '[Quit] : #quit\n\n\t=> ')

        return self.choice_password


    def host_display(self):
        """ Generate host input page display"""
        heading.main_page_loading()
        print('\t\t1 - Write your mysql host \n\n\n')
        self.choice_host = input('[Username menu] : #un\n'
                                 '[Password menu] : #pm\n'
                                 'Quit] : #quit\n\n\t=> ')

        return self.choice_host


    def database_menu(self):
        """ Generate database menu input page display"""
        heading.main_page_loading()
        print('\t\t1 - Do you want to create your database? \n\n'
              '\t\t2 - Delete a database \n\n'
              '\t\t3 - Select a database \n\n\n')
        self.choice_database_menu = input('[Create a database] : Type 1\n'
                                          '[Delete a database] : Type 2\n'
                                          '[Select a database] : Type 3\n'
                                          '[Username menu] : #un\n'
                                          '[Password menu] : #pm\n'
                                          '[Host menu] : #hm\n'
                                          '[Quit] : #quit\n\n\t=> ')

        return self.choice_database_menu


    def creation_database(self):
        """ Generate database creation page display"""
        heading.main_page_loading()
        print('\t\tPlease, write the name of the database\n')
        self.choice_creation_database = input('[Database Menu] : #dm\n'
                                              '[Quit] : #quit\n\n\t=> ')

        return self.choice_creation_database


    def creation_database_loading_page_start(self):
        """ Generate database creation start page display"""
        heading.main_page_loading()
        print('\t\tCreation of the Database ... 0%\n\n'
              '\t\tPlease wait... it can take some time\n\n')


    def creation_database_loading_started(self):
        """ Generate database creation started display"""
        heading.main_page_loading()
        print('\t\tCreation of the Database ... 0%\n\n'
              '\t\t- - - - - - - - - - - - - - - - - - - - -\n\n')



    def creation_database_loading_in_progress(self, tables, categories, products):
        """ Generate database creation progress display"""
        heading.main_page_loading()
        if tables == "T":
            print('\t\tCreation of the Database ... 0%\n\n'
                  '\t\t- - - - - - - - - - - - - - - - - - - - -\n\n'
                  '\t\tTables created \n\n')

        elif tables == "T" and categories == "C":
            print('\t\tCreation of the Database ... 0%\n\n'
                  '\t\t- - - - - - - - - - - - - - - - - - - - -\n\n'
                  '\t\tTables created \n\n'
                  '\t\t- - - - - - - - - - - - - - - - - - - - -\n\n'
                  '\t\tCategories imported\n\n')

        elif tables == "T" and categories == "C" and products == "P":
            print('\t\tCreation of the Database ... 0%\n\n'
                  '\t\t- - - - - - - - - - - - - - - - - - - - -\n\n'
                  '\t\tTables created \n\n'
                  '\t\t- - - - - - - - - - - - - - - - - - - - -\n\n'
                  '\t\tCategories imported\n\n'
                  '\t\t- - - - - - - - - - - - - - - - - - - - -\n\n'
                  '\t\tProducts imported\n\n')



    def creation_database_loading_page_end(self):
        """ Generate database creation end display"""
        heading.main_page_loading()
        print('\t\tCreation of the Database ... 0%\n\n'
              '\t\t- - - - - - - - - - - - - - - - - - - - -\n\n'
              '\t\tTables created \n\n'
              '\t\t- - - - - - - - - - - - - - - - - - - - -\n\n'
              '\t\tCreation of the Database ... 0%\n\n'
              '\t\t- - - - - - - - - - - - - - - - - - - - -\n\n'
              '\t\tTables created \n\n'
              '\t\t- - - - - - - - - - - - - - - - - - - - -\n\n'
              '\t\tCategories imported\n\n'
              '\t\t- - - - - - - - - - - - - - - - - - - - -\n\n'
              '\t\tProducts imported\n\n'
              '\t\t- - - - - - - - - - - - - - - - - - - - -\n\n'
              '\t\tDatabase created\n\n')

        self.choice_creation_database = input('[Database menu] : #dm\n'
                                              '[Quit] : #quit \n\n\t=>')

        return self.choice_creation_database


    def creation_database_loading_fail(self):
        """ Generate database creation error display"""
        heading.main_page_loading()
        print('\t\tThe database''s you wrote already exists\n\n'
              '\t\tType anything to come back to database writing name menu\n\n'
              '\t\tType #dm to come back to Database Menu or #quit to Quit\n\n')

        self.choice_creation_database_loading_fail = input('[Writing database''s name] : Type anything\n'
                                                           '[Database menu] : #dm\n'
                                                           '[Quit] : #quit \n\n\t=> ')

        return self.choice_creation_database_loading_fail


    def connect_database_fail(self):
        """ Generate database connection error display"""
        heading.main_page_loading()
        print('\t\tWrong Informations indicated.\n\n'
              '\t\tType anything to come back to mysql menu\n')
        self.choice_connect_database_fail = input('[Quit] : #quit\n\n\t=> ')

        return self.choice_connect_database_fail



    def delete_database_start(self, conn):
        """ Generate database deletion start display"""
        heading.main_page_loading()
        databases = recovery.show_databases(conn)
        print('\t\tDelete a database\n\n')
        for database in databases:
            print('\t\t', database.Database, '\n')
        self.choice_delete_database_start = input('[Delete] : Type the name of the database\n'
                                                  '[Database menu] : #dm\n'
                                                  '[Quit] : #quit \n\n\t=>')

        return self.choice_delete_database_start



    def delete_database_end(self, database):
        """ Generate database deletion end display"""
        heading.main_page_loading()
        print('\t\tDatabase : ', database, ' deleted\n\n')
        self.choice_delete_database_end = input('[Database menu] : #dm\n'
                                                '[Quit] : #quit \n\n\t=>')

        return self.choice_delete_database_end



    def select_database(self, conn):
        """ Generate database selection display"""
        heading.main_page_loading()
        databases = recovery.show_databases(conn)
        print('\t\tSelect a database\n\n')
        for database in databases:
            print('\t\t', database.Database, '\n')
        self.choice_select_database = input('[Select] : Type the name of the database\n'
                                            '[Database menu] : #dm\n'
                                            '[Quit] : #quit \n\n\t=>')

        return self.choice_select_database


    def main_page_display(self):
        """ Generate main page display"""
        heading.main_page_loading() 
        print('\t\t1 - What product do you want to replace ? \n\n'
              '\t\t2 - Find my substitutes products \n\n\n')
        self.choice_proceed_categories = input('[Products] : Type 1\n'
                                   '[Substitutes] : Type 2\n'
                                   '[Database Menu] : #dm\n'
                                   '[Quit] : #quit \n\n\t=> ')

        return self.choice_proceed_categories


    def categories_display(self, conn, page_count):
        """ Generate categories page display"""
        heading.categories_page_loading()
        self.categories_offset = page_count * 10
        categories = recovery.show_categories(conn, self.categories_limit, self.categories_offset)
        print('\n\t\t\t', 'Name', '\n\n\n')

        for categorie in categories:
            self.categorie_id_list.append(categorie.id)
            self.categorie_name_list.append(categorie.name)

        if self.categorie_name_list == []:
            print('\t No categories registered in this database\n')
        else:
            for i in range(0, len(self.categorie_name_list)):
                print('\t\t', self.categorie_id_list[i], '\t', self.categorie_name_list[i], '\n\n')

        self.choice_categorie = input('[Categorie Details] : write related number ; example : 1\n'
                                      '[Main Menu] : #mm\n[Previous Page] : <\n[Next Page] : >\n'
                                      '[Quit] : #quit\n\n\t=> ')

        self.categorie_id_list = list()
        self.categorie_name_list = list()

        return self.choice_categorie


    def products_display(self, conn, categorie_id, page_count):
        """ Generate products page display"""
        heading.products_page_loading()
        self.products_offset = page_count * 10
        products = recovery.show_products_from_spec_categorie(conn, categorie_id, self.products_limit, self.products_offset)
        print('\n\t\t\t', 'Name', '\n\n\n')
        for product in products:
            self.products_product_id_list.append(product.product_id)
            self.products_name_list.append(product.name)

        if self.products_name_list == []:
            print('\t No products registered for this categorie\n\n\n')
        else:
            for i in range(0, len(self.products_name_list)):
                print('\t\t', self.products_product_id_list[i], '\t', self.products_name_list[i], '\n\n')

        self.choice_product = input('[Product Details] : write related number ; example : 1\n'
                                    '[Main Menu] : #mm\n'
                                    '[Categories Menu] : #cm\n[Previous Page] : <\n[Next Page] : >\n'
                                    '[Quit] : #quit\n\n\t=> ')

        self.products_product_id_list = list()
        self.products_name_list = list()

        return self.choice_product



    def products_details_display(self, conn, categorie_id, product_id):
        """ Generate products details page display"""
        heading.products_details_page_loading()
        products = recovery.show_spec_product_from_spec_categorie(conn, categorie_id, product_id)
        for product in products:
            self.product_id_details = self.choice_product
            print('  ', self.product_id_details, '\t', product.name, '\n\n\n\t shop(s) : ', product.shop, '\n\n\t nutrition_rate : ', product.nutrition_rate,
                  '\n\n', product.http_link, '\n\n\n')

        self.choice_product_details = input('[Save Product] : #save\n'
                                            '[Show Substitutes]: #substitute\n'
                                            '[Main Menu] : #mm\n'
                                            '[Products Menu] : #pm\n'
                                            '[Categories Menu] : #cm\n[Quit] : #quit\n\n\t=> ')

        return self.choice_product_details



    def save_product(self, conn, categorie_id, product_id):
        """ Generate saving product page display"""
        product = recovery.show_spec_product_from_spec_categorie(conn, categorie_id, product_id)

        for pro in product:
            name = pro.name
            url = pro.http_link
            shop = pro.shop
            nutrition_rate = pro.nutrition_rate
            cat_id = pro.categorie_id
            pro_id = pro.product_id

        save = recovery.save_into_registered_products(conn, name, nutrition_rate, url, shop, cat_id, pro_id)

        heading.product_saved_loading()
        print('\t\tProduct correctly saved.\n\n')
        self.choice_product_saved = input('[Main Menu] : #mm\n'
                                          '[Categories Menu] : #cm\n'
                                          '[Products Menu] : #pm\n'
                                          '[Product Details] : #pd\n'
                                          '[Quit] : #quit\n\n\t=> ')

        return self.choice_product_saved



    def save_substitute(self, conn, categorie_id, product_id):
        """ Generate saving substitute page display"""
        product = recovery.show_spec_product_from_spec_categorie(conn, categorie_id, product_id)

        for pro in product:
            name = pro.name
            url = pro.http_link
            shop = pro.shop
            nutrition_rate = pro.nutrition_rate
            cat_id = pro.categorie_id
            pro_id = pro.product_id

        save = recovery.save_into_registered_products(conn, name, nutrition_rate, url, shop, cat_id, pro_id)

        heading.substitute_saved_loading()
        print('\t\tSubstitute correctly saved.\n\n')
        self.choice_substitute_saved = input('[Main Menu] : #mm\n'
                                             '[Categories Menu] : #cm\n'
                                             '[Products Menu] : #pm\n'
                                             '[Products Details] : #pd\n'
                                             '[Substitutes Menu] : #sm\n'
                                             '[Substitute Details] : #sd\n'
                                             '[Quit] : #quit\n\n\t=> ')

        return self.choice_substitute_saved



    def show_registered_products(self, conn, page_count):
        """ Generate registered products page display"""
        heading.registered_products_loading()
        self.registered_products_offset = page_count * 10
        reg_products = recovery.show_registered_products(conn, self.registered_products_limit,
                                                         self.registered_products_offset)

        print('\n\t\t\t', 'Name', '\n\n\n')
        for reg in reg_products:
            self.registered_products_id_list.append(reg.id)
            self.registered_products_name_list.append(reg.name)

        if self.registered_products_name_list == []:
            print('\t No products registered yet\n\n\n')
        else:
            for i in range(0, len(self.registered_products_name_list)):
                print('\t\t', self.registered_products_id_list[i], '\t',
                      self.registered_products_name_list[i], '\n \n')

        self.choice_registered_products = input('[Main menu] : #mm\n'
                                                '[Next page] : >\n'
                                                '[Previous page] : <\n'
                                                '[Registered product details] : Type id of product\n'
                                                '[Delete a product] : #del\n'
                                                '[Delete all] : #all\n'
                                                '[Quit] : #quit\n\n\t=> ')

        self.registered_products_id_list = list()
        self.registered_products_name_list = list()

        return self.choice_registered_products 



    def registered_products_details_display(self, conn, id_reg):
        """ Generate registered products details display"""
        heading.registered_products_loading()
        registered_product = recovery.show_registered_product_with_id(conn, id_reg)

        for reg in registered_product:
            self.registered_product_id_details = self.choice_registered_products
            print('  ', self.registered_product_id_details, '\t', reg.name, '\n\n\n\t shop(s) : ',
                  reg.shop, '\n\n\t nutrition_rate : ', reg.nutrition_rate,
                  '\n\n', reg.http_link, '\n\n\n')

        self.choice_registered_products_details_display = input('[Registered products] : #rp\n'
                                                                '[Main Menu] : #mm\n'
                                                                '[Quit] : #quit\n\n\t=> ')

        return self.choice_registered_products_details_display



    def registered_products_all_deleted(self, conn):
        """ Generate registered product total deletion display"""
        heading.registered_products_loading()

        try:
            recovery.drop_table_registered_products(conn)
        except TypeError:
            pass

        recovery.create_table_registered_products(conn)  
        print('\t\tAll products from registered_products\n'
              '\t\twere deleted\n')
        self.choice_registered_products_all_deleted = input('[Main Menu] : #mm\n'
                                                            '[Quit] : #quit\n\n\t=> ')

        return self.choice_registered_products_all_deleted



    def substitutes_display(self, conn, categorie_id, product_id, page_count):
        """ Generate substitutes page display"""
        heading.products_substitutes_loading()
        self.substitutes_offset = page_count * 10

        product_selected = recovery.show_spec_product_from_spec_categorie(conn, categorie_id, product_id)

        for product in product_selected:
            pro_nutrition_rate = product.nutrition_rate

        substitutes = recovery.show_substitutes_of_products(conn, product_id, categorie_id, pro_nutrition_rate, 
                                                            self.substitutes_limit, self.substitutes_offset) 
        print('\n\t\t\t', 'Name', '\n\n\n')
        for substitute in substitutes:
            self.substitutes_product_id_list.append(substitute.product_id)
            self.substitutes_name_list.append(substitute.name)

        
        if self.substitutes_product_id_list == []:
            print('\tNo substitutes registered for this product\n'
                  '\tSubstitutes mean products with a lower nutrition rate\n\n')
        else:
            for i in range(0, len(self.substitutes_product_id_list)):
                print('\t\t', self.substitutes_product_id_list[i], '\t',
                      self.substitutes_name_list[i], '\n\n')

        self.substitutes_product_id_list = list()
        self.substitutes_name_list = list()

        self.choice_substitutes = input('[Product Details] : #pd\n'
                                        '[Products Menu] : #pm\n'
                                        '[Categories Menu] : #cm\n'
                                        '[Main Menu] : #mm\n'
                                        '[Next Page] : >\n'
                                        '[Previous Page] : <\n'
                                        '[Quit] : #quit\n\n\t=> ')
        return self.choice_substitutes



    def substitutes_details(self, conn, categorie_id, product_id):
        """ Generate substitutes details page display"""
        heading.substitutes_details_loading()
        substitute = recovery.show_spec_product_from_spec_categorie(conn, categorie_id, product_id)

        for sub in substitute:
            self.substitute_id_details = self.choice_substitutes
            print('  ', self.substitute_id_details, '\t', sub.name, '\n\n\n\t shop(s) : ',
                  sub.shop, '\n\n\t nutrition_rate : ', sub.nutrition_rate,
                  '\n\n', sub.http_link, '\n\n\n')

        self.choice_substitutes_details = input('[Save Product] : #save\n'
                                                '[Substitutes Menu] : #sm\n'
                                                '[Product Details] : #pd\n'
                                                '[Products Menu] : #pm\n'
                                                '[Categories Menu] : #cm\n'
                                                '[Main Menu] : #mm\n'
                                                '[Quit] : #quit\n\n\t=> ')

        return self.choice_substitutes_details


    def substitutes_id_check_list(self, conn, categorie_id, product_id, page_count):
        """ Generate substitutes id_list for check"""
        self.substitutes_id_list = list()
        self.substitutes_offset = page_count * 10
        product_selected = recovery.show_spec_product_from_spec_categorie(conn, categorie_id, product_id)

        for product in product_selected:
            pro_nutrition_rate = product.nutrition_rate

        substitutes = recovery.show_substitutes_of_products(conn, product_id, categorie_id,
                                                            pro_nutrition_rate, self.substitutes_limit,
                                                            self.substitutes_offset)
        for substitute in substitutes:
            self.substitutes_id_list.append(substitute.product_id)

        return self.substitutes_id_list


    def categories_id_check_list(self, conn, page_count):
        """ Generate categories id_list for check"""
        self.categories_id_list = list()
        self.categories_offset = page_count * 10

        categories = recovery.show_categories(conn, self.categories_limit, self.categories_offset)

        for categorie in categories:
            self.categories_id_list.append(categorie.id)

        return self.categories_id_list


    def products_id_check_list(self, conn, categorie_id, page_count):
        """ Generate products id_list for check"""
        self.products_id_list = list()
        self.products_offset = page_count * 10

        products_selected = recovery.show_products_from_spec_categorie(conn, categorie_id,
                                                                       self.products_limit,
                                                                       self.products_offset)

        for product in products_selected:
            self.products_id_list.append(product.product_id)

        return self.products_id_list


    def registered_product_id_check_list(self, conn, page_count):
        """ Generate registered products id_list for check"""
        self.registered_products_id = list()
        self.registered_products_offset = page_count * 10

        registered_products = recovery.show_registered_products(conn, self.registered_products_limit,
                                                                self.registered_products_offset)

        for registered_product in registered_products:
            self.registered_products_id.append(registered_product.id)

        return self.registered_products_id


    def show_registered_products_to_del(self, conn, page_count):
        """ Generate registered product individual deletion display"""
        heading.registered_products_loading()
        self.registered_products_offset = page_count * 10
        reg_products = recovery.show_registered_products(conn, self.registered_products_limit,
                                                         self.registered_products_offset)

        print('\n\t\t\t', 'Name', '\n\n\n')
        for reg in reg_products:
            self.registered_products_id_list.append(reg.id)
            self.registered_products_name_list.append(reg.name)

        if self.registered_products_name_list == []:
            print('\t No products registered yet\n\n\n')
        else:
            for i in range(0, len(self.registered_products_name_list)):
                print('\t\t', self.registered_products_id_list[i], '\t',
                      self.registered_products_name_list[i], '\n \n')

        self.choice_registered_products_to_del = input('[Main menu] : #mm\n'
                                                       '[Registered products] : #rp\n'
                                                       '[Next page] : >\n'
                                                       '[Previous page] : <\n'
                                                       '[Delete a product] : Type the id of the product\n'
                                                       '[Quit] : #quit\n\n\t=> ')

        self.registered_products_id_list = list()
        self.registered_products_name_list = list()

        return self.choice_registered_products_to_del



    def delete_registered_product(self, conn, registered_product_id):
        """ Generate registered product individual deletion end display"""
        heading.registered_products_loading()
        reg_product_detail = recovery.show_registered_product_with_id(conn, registered_product_id)
        for reg in reg_product_detail:
            reg_name = reg.name
            reg_shop = reg.shop
            reg_url = reg.http_link
            reg_nutrition_rate = reg.nutrition_rate

        reg_product = recovery.delete_registered_product(conn, registered_product_id)

        print('  Registered product [', reg_name, '] has been deleted\n\n')

        self.choice_delete_registered_product = input('[Main menu] : #mm\n'
                                                      '[Registered products] : #rp\n'
                                                      '[Quit] : #quit\n\n\t=> ')

        return self.choice_delete_registered_product



    def error_message_tables_check(self):
        """ Generate error message if presence of tables is False"""
        print('\t\t The database you chose is not fitted to run the application\n'
              '\t\t It does not contain tables categories ; products and registered_products\n'
              '\t\t Come back to Database Menu and create a database\n')

        self.choice_error_message_tables_check = input('[Type anything to come back to Database menu] : \n\n\t=> ')

        return self.choice_error_message_tables_check
