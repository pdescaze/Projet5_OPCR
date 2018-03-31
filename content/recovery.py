#!/usr/bin/python3
# -*- coding: Utf-8 -*

from math import *



class Recovery():

    def __init__(self):

        self.databases_list = list()
        self.categories_count = 0
        self.products_count = 0
        self.substitutes_count = 0
        self.registered_products_count = 0

        self.number_page_categories = 0
        self.number_page_products = 0
        self.number_page_substitutes = 0
        self.number_page_registered_products = 0


    def show_databases(self, conn):

        databases = conn.query("""
            SHOW DATABASES
            """)

        return databases


    def show_categories(self, conn, limit, offset):

        categories = conn.query("""
            SELECT * FROM categories
            LIMIT {0} OFFSET {1}
            """.format(limit, offset)
            )

        return categories


    def show_products_from_spec_categorie(self, conn, categorie_id, limit, offset):

        products = conn.query("""
            SELECT * FROM products
            WHERE categorie_id = {0}
            LIMIT {1} OFFSET {2}
            """.format(categorie_id, limit, offset)
            )

        return products


    def show_spec_product_from_spec_categorie(self, conn, categorie_id, product_id):

        products = conn.query("""
            SELECT * FROM products
            WHERE categorie_id = {0}
            AND product_id = {1}
            """.format(categorie_id, product_id)
            )

        return products


    def save_into_registered_products(self,conn, name, nutrition_rate, url, shop, categorie_id, product_id):

        saving = conn.query("""
            INSERT INTO registered_products (name, nutrition_rate, url, shop, categorie_id, product_cat_id)
            VALUES ('{0}', '{1}', '{2}', '{3}', {4}, {5})
            """.format(name, nutrition_rate, url, shop, categorie_id, product_id)
            )

        return saving


    def show_registered_products(self,conn, limit, offset):

        registered_products = conn.query("""
            SELECT * FROM registered_products
            LIMIT {0} OFFSET {1}
            """.format(limit, offset)
            )

        return registered_products


    def show_registered_product_with_id(self,conn, id_reg):

        registered_product = conn.query("""
            SELECT * FROM registered_products
            WHERE id = {0}
            """.format(id_reg)
            )

        return registered_product


    def drop_table_registered_products(self,conn):

        table = conn.query("""
            DROP TABLE registered_products
            """)

        return table


    def create_table_registered_products(self,conn):

        table = conn.query("""
            CREATE TABLE registered_products(
            id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR (400) NOT NULL,
            nutrition_rate CHAR(10) NOT NULL,
            http_link VARCHAR(500) NOT NULL,
            shop VARCHAR(300) DEFAULT NULL,
            categorie_id SMALLINT UNSIGNED NOT NULL,
            product_id SMALLINT UNSIGNED NOT NULL)
            ENGINE = InnoDB
            """)

        return table


    def show_substitutes_of_products(self, conn, product_id, categorie_id, nutrition_rate, limit, offset):

        substitutes = conn.query("""
            SELECT * FROM products
            WHERE product_id != {0}
            AND categorie_id = {1}
            AND nutrition_rate < '{2}'
            LIMIT {3} OFFSET {4}
            """.format(product_id, categorie_id, nutrition_rate, limit, offset)
            )

        return substitutes


    def delete_database(self, conn, database):

        database = conn.query("""
            DROP DATABASE {0}
            """.format(database)
            )

        return database


    def show_databases_check_list(self,conn):

        databases = conn.query("""
            SHOW DATABASES
            """)

        for database in databases:
            self.databases_list.append(database.Database)

        return self.databases_list


    def get_categories_count(self, conn):

        categories = conn.query("""
            SELECT name FROM categories
            """)

        for categorie in categories:
            self.categories_count += 1

        return self.categories_count


    def get_products_count_from_spec_categorie(self, conn, categorie_id):

        products = conn.query("""
            SELECT name FROM products
            WHERE categorie_id = {0}
            """.format(categorie_id)
            )

        for product in products:
            self.products_count +=1

        return self.products_count


    def get_substitutes_count(self, conn, categorie_id, product_id):

        product_selected = conn.query("""
            SELECT * FROM products
            WHERE categorie_id = {0}
            AND product_id = {1}
            """.format(categorie_id, product_id)
            )

        for product in product_selected:
            product_nutrition_rate = product.nutrition_rate


        substitutes = conn.query("""
            SELECT name FROM products
            WHERE categorie_id = {0}
            AND product_id != {1}
            AND nutrition_rate < '{2}'
            """.format(categorie_id, product_id, product_nutrition_rate)
            )

        for substitute in substitutes:
            self.substitutes_count += 1

        return self.substitutes_count


    def get_registered_products_count(self, conn):

        registered_products = conn.query("""
            SELECT name FROM registered_products
            """)

        for registered_product in registered_products:
            self.registered_products_count += 1

        return self.registered_products_count


    def get_number_page_categories(self,conn, categories_number):

        categories = conn.query("""
            SELECT name FROM categories
            """)

        for categorie in categories:
            categories_number += 1

        self.number_page_categories = floor(categories_number / 10)

        return self.number_page_categories


    def get_number_page_products(self, conn, categorie_id, products_number):

        products = conn.query("""
            SELECT name FROM products
            WHERE categorie_id = {0}
            """.format(categorie_id)
            )

        for product in products:
            products_number += 1

        self.number_page_products = floor(products_number / 10)

        return self.number_page_products


    def get_number_page_substitutes(self, conn, categorie_id, product_id, substitutes_number):

        product_selected = conn.query("""
            SELECT name FROM products
            WHERE categorie_id = {0}
            AND product_id = {1}
            """.format(categorie_id, product_id)
            )

        for product in product_selected:
            product_nutrition_rate = product.nutrition_rate

        substitutes = conn.query("""
            SELECT name FROM products
            WHERE categorie_id = {0}
            AND product_id != {1}
            AND nutrition_rate < {2}
            """.format(categorie_id, product_id, product_nutrition_rate)
            )

        for substitute in substitutes:
                substitutes_number += 1

        self.number_page_substitutes = floor(substitutes_number / 10)

        return self.number_page_substitutes


    def get_number_page_registered_products(self, conn, registered_products_number):

        registered_products = conn.query("""
            SELECT name FROM registered_products
            """)

        for registered_product in registered_products:
            registered_products_number += 1

        self.number_page_registered_products = floor(registered_products_number / 10)

        return self.number_page_registered_products