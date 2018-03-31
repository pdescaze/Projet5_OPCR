#!/usr/bin/python3
# -*- coding: Utf-8 -*


class Recovery():

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


    def show_products(self, conn, categorie_id, limit, offset):

        products = conn.query("""
            SELECT * FROM products
            WHERE categorie_id = {0}
            LIMIT {1} OFFSET {2}
            """.format(categorie_id, limit, offset)
            )

        return products


    def show_product_from_categorie(self, conn, categorie_id, product_id):

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


    def substitutes_of_products(self, conn, product_id, categorie_id, nutrition_rate, limit, offset):

        substitutes = conn.query("""
            SELECT * FROM products
            WHERE product_id != {0}
            AND categorie_id = {1}
            AND nutrition_rate < '{2}'
            LIMIT {3} OFFSET {4}
            """.format(product_id, categorie_id, nutrition_rate, limit, offset)
            )

        return substitutes