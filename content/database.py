""" Class Database : permits to generate the database throught methods
executed following user's input. Also permits to generate a database if 
executed directly with defaults parameters that users can change in this file"""

import re
import json
from math import ceil
import requests
import records
import sqlalchemy





class Database():
    """ Class that permits to connect to mysql and create database, tables related to 
    Pure Beurre's Application. Permits aswell to requests data from OpenFoodFacts' API
    and import them into tables"""

    def __init__(self, username, password, host):
        self.username = username
        self.password = password
        self.host = host
        self.mysql = "mysql"
        self.pymysql = "pymysql"
        self.conn_answer = str()
        self.conn = ""

        self.categories_json = str()
        self.categories_total = str()
        self.names = list()
        self.names_sorted = list()
        self.names_list = list()
        self.urls_list = list()
        self.urls = list()
        self.urls_sorted = list()
        self.url_categorie = str()
        self.categorie_json_single = str()
        self.categories_dict = dict()
        self.categories_dict_sql = dict()

        self.products_total = str()
        self.products_per_page = str()
        self.pages_total = str()

        self.url_product = str()
        self.product_json = str()
        self.products_nutrition_score_list = str()
        self.products_shops_list = str()
        self.products_names_list = str()
        self.products_urls_list = str()

        self.names_list_total = list()
        self.shops_list_total = list()
        self.nutrition_score_list_total = list()
        self.urls_list_total = list()
        self.categorie_id_list_total = list()

        self.names_list_stored = list()
        self.shops_list_stored = list()
        self.urls_list_stored = list()
        self.nutrition_score_list_stored = list()
        self.categorie_id_list_stored = list()

        self.categorie_id_init = 1
        self.product_id_init = 1
        self.previous_product = str()

        self.shops_list_indiv = str()
        self.names_list_indiv = str()
        self.nutrition_score_list_indiv = str()

        self.cat_id = 1
        self.categorie_product_id_list_final = list()
        self.product_id_list_final = list()
        self.principal_id_list = list()

        self.show_databases_list = list()
        self.categorie_count = 0
        self.product_count = 0
        self.substitute_count = 0
        self.registered_product_count = 0

        self.number_page_categorie = 0
        self.number_page_product = 0
        self.number_page_substitute = 0
        self.number_page_registered_product = 0


    def connect_to_mysql(self):
        """ Connection to mysql with informations inputed"""
        try:
            self.conn = records.Database('{mysql}+{pymysql}://{username}:{password}@{host}'.format(mysql=self.mysql, 
                                                                                                   pymysql=self.pymysql,
                                                                                                   username=self.username,
                                                                                                   password=self.password,
                                                                                                   host=self.host))
            self.conn_answer = ""
        except sqlalchemy.exc.OperationalError:
            self.conn_answer = "Informations indicated wrong. Cannot connect to mysql"

        return self.conn_answer


    def connect_to_database(self, database):
        """ Creation of offdb databse if not exists and Connection """
        try:
            self.conn.query(""" USE {0}""".format(database))

        except sqlalchemy.exc.InternalError:
            self.conn.query("""CREATE DATABASE {0} CHARACTER SET 'utf8' """.format(database))
            self.conn.query(""" USE {0}""".format(database))


    def tables_creation(self):
        """ Permits to create all tables in offdb database (products, categories,
        registered_products) """
        try:
            self.conn.query("""
                CREATE TABLE products(
                id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY ,
                name VARCHAR(400) NOT NULL,
                nutrition_rate CHAR (10) DEFAULT NULL,
                http_link VARCHAR(500) DEFAULT NULL,
                shop VARCHAR(300) DEFAULT NULL,
                categorie_id SMALLINT UNSIGNED NOT NULL,
                product_id SMALLINT UNSIGNED DEFAULT NULL)
                ENGINE = InnoDB
                """)
        except sqlalchemy.exc.InternalError:
            print("The table products has already been created")


        try:
            self.conn.query("""
                CREATE TABLE categories(
                id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY ,
                name VARCHAR(400) DEFAULT NULL,
                http_link VARCHAR (300) DEFAULT NULL)
                ENGINE = InnoDB
                """)
        except sqlalchemy.exc.InternalError:
            print("The table categories has already beed created")


        try:
            self.conn.query("""
                CREATE TABLE registered_products(
                id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(400) NOT NULL,
                nutrition_rate CHAR (10) DEFAULT NULL,
                http_link VARCHAR(500) DEFAULT NULL,
                shop VARCHAR(300) DEFAULT NULL,
                categorie_id SMALLINT UNSIGNED NOT NULL,
                product_id SMALLINT UNSIGNED DEFAULT NULL)
                ENGINE = InnoDB
                """)
        except sqlalchemy.exc.InternalError:
            print("The table registered_products has already been created")


    def get_categories_name_url(self):
        """Selection and isolation of categories' names and urls from OpenFoodFacts API"""
        self.categories_json = requests.get('https://fr.openfoodfacts.org/categories.json').json()
        self.categories_total = self.categories_json["count"]

        for categorie in range(0, self.categories_total, 100):
            self.names_list = self.categories_json["tags"][categorie]["name"]
            self.names.append(self.names_list)
            self.urls_list = self.categories_json["tags"][categorie]["url"]
            self.urls.append(self.urls_list)

        for i in range(0, len(self.urls)):
            if not re.search(r"(ru:|de:|es:|en:|vi:|%D)", self.urls[i]):
                self.names_sorted.append(self.names[i])
                self.urls_sorted.append(self.urls[i])

        for i in range(0, len(self.urls_sorted)):
            try:
                self.url_categorie = self.urls_sorted[i] + '.json'
                self.categorie_json_single = requests.get(self.url_categorie).json()
                self.categories_dict[self.names_sorted[i]] = self.urls_sorted[i]
            except json.decoder.JSONDecodeError:
                pass

        return self.categories_dict


    def insert_categories(self):
        """ Insertion of categories's names and url from OpenFoodFacts API into the database database"""
        for key, value in self.categories_dict.items():
            key = str(key)
            value = str(value)
            key = key.replace("'", " ")
            key = key.replace('"', " ")
            value = value.replace("'", " ")
            value = value.replace('"', " ")
            try:
                self.conn.query("""
                    INSERT INTO categories (name, http_link) 
                    VALUES('{0}', '{1}')
                    """.format(key, value))
            except UnicodeEncodeError:
                pass


    def get_products(self):
        """ Selection and isolation of products' names, nutrition_rate, url and shop (if available) 
        from Openfoodfacts API and Insertion into offdb database"""
        categories_request = self.conn.query("""
            SELECT * from categories
            """)

        for cat in categories_request:
            self.categories_dict_sql[cat.name] = cat.http_link

        for value in self.categories_dict_sql.values():            
            self.url_categorie = value + '.json'
            self.categorie_json_single = requests.get(self.url_categorie).json()
            self.products_total = self.categorie_json_single["count"]
            self.products_per_page = self.categorie_json_single["page_size"]
            self.pages_total = ceil(self.products_total / self.products_per_page)
            if self.pages_total == 1:                
                self.url_product = value + "/" + "1.json"
                self.product_json = requests.get(self.url_product).json()
                for product in range(0, self.products_per_page):
                    try:
                        self.products_nutrition_score_list = self.product_json["products"][product]["nutrition_grades"]
                        self.products_shops_list = self.product_json["products"][product]["stores_tags"]
                        self.products_names_list = self.product_json["products"][product]["product_name"]
                        self.products_urls_list = self.product_json["products"][product]["url"]
                        self.names_list_total.append(self.products_names_list)
                        self.shops_list_total.append(self.products_shops_list)
                        self.urls_list_total.append(self.products_urls_list)
                        self.nutrition_score_list_total.append(self.products_nutrition_score_list)
                        self.categorie_id_list_total.append(self.categorie_id_init)

                    except (KeyError, IndexError, json.decoder.JSONDecodeError):
                        pass

            else:
                for page in range(1, 2):
                    try:                  
                        self.url_product = value + "/" + str(page) + ".json"
                        self.product_json = requests.get(self.url_product).json()
                       
                        for product in range(0, self.products_per_page):
                            try:
                                self.products_nutrition_score_list = self.product_json["products"][product]["nutrition_grades"]
                                self.products_shops_list = self.product_json["products"][product]["stores_tags"]
                                self.products_names_list = self.product_json["products"][product]["product_name"]
                                self.products_urls_list = self.product_json["products"][product]["url"]
                                self.names_list_total.append(self.products_names_list)
                                self.shops_list_total.append(self.products_shops_list)
                                self.urls_list_total.append(self.products_urls_list)
                                self.nutrition_score_list_total.append(self.products_nutrition_score_list)
                                self.categorie_id_list_total.append(self.categorie_id_init)

                            except (KeyError, IndexError, json.decoder.JSONDecodeError):
                                pass

                    except json.decoder.JSONDecodeError:
                        pass

            self.categorie_id_init += 1
                  

        for i in range(0, len(self.names_list_total)):
            if self.previous_product != self.names_list_total[i]:
                self.names_list_stored.append(self.names_list_total[i])
                self.shops_list_stored.append(self.shops_list_total[i])
                self.urls_list_stored.append(self.urls_list_total[i])
                self.nutrition_score_list_stored.append(self.nutrition_score_list_total[i])
                self.categorie_id_list_stored.append(self.categorie_id_list_total[i])
                self.previous_product = self.names_list_total[i]

           
           
        for i in range(0, len(self.names_list_stored)):
            self.shops_list_indiv = str(self.shops_list_stored[i])
            self.shops_list_indiv = self.shops_list_indiv.replace("'", " ")
            self.shops_list_indiv = self.shops_list_indiv.replace('"', " ")
            self.names_list_indiv = self.names_list_stored[i].replace("'", " ")
            self.names_list_indiv = self.names_list_indiv.replace('"', " ")
            self.names_list_indiv = self.names_list_indiv.replace(":", " ")
            self.nutrition_score_list_indiv = self.nutrition_score_list_stored[i].replace("'", " ")
            self.nutrition_score_list_indiv = self.nutrition_score_list_indiv.replace('"', " ")
            try:
                self.conn.query("""
                    INSERT INTO products(name, nutrition_rate, http_link, shop, categorie_id)
                    VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')
                    """.format(self.names_list_indiv,
                               self.nutrition_score_list_indiv,
                               self.urls_list_stored[i],
                               self.shops_list_indiv,
                               self.categorie_id_list_stored[i]))
            except UnicodeEncodeError:
                pass



    def insert_product_cat_id(self):
        """ Recover of products and creation of product_id : id of product into its categorie"""
        rows = self.conn.query("""
            SELECT * FROM products
            """)

        for row in rows:
            if self.cat_id == row.categorie_id:
                self.product_id_list_final.append(self.product_id_init)
                self.categorie_product_id_list_final.append(row.categorie_id)
                self.principal_id_list.append(row.id)
                self.product_id_init += 1
            else:
                self.product_id_init = 1
                self.product_id_list_final.append(self.product_id_init)
                self.principal_id_list.append(row.id)
                self.cat_id += 1
                self.categorie_product_id_list_final.append(row.categorie_id)
                self.product_id_init += 1

        for i in range(0, len(self.product_id_list_final)):
            self.conn.query("""
                UPDATE products 
                SET product_id = '{0}'
                WHERE categorie_id = '{1}'
                AND id = '{2}'
                """.format(self.product_id_list_final[i],
                           self.categorie_product_id_list_final[i],
                           self.principal_id_list[i]))



def main(username, password, host, database_name):
    print("Database construction with direct lauch started\nWait it can take some time")
    base = Database(username, password, host)
    base.connect_to_mysql()
    base.connect_to_database(database_name)
    base.tables_creation()
    base.get_categories_name_url()
    base.insert_categories()
    base.get_products()
    base.insert_product_cat_id()
    print("Database finished")


if __name__ == "__main__":
    username = input("Write your mysql username : ")
    password = input("Write your mysql password : ")
    host = input("Write your mysql hor : ")
    database_name = input("Write a name for your database : ")
    main(username, password, host, database_name)
