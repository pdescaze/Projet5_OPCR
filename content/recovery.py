""" File recovery.py : contains all requests functions
the Application does with mysql """

from math import floor


def show_databases(conn):
    """ Function that permits to recover databases from mysql"""
    databases = conn.query("""
        SHOW DATABASES
        """)

    return databases


def show_categories(conn, limit, offset):
    """ Recover categories from table categories and return them"""
    categories = conn.query("""
        SELECT * FROM categories
        LIMIT {0} OFFSET {1}
        """.format(limit, offset))

    return categories


def show_products_from_spec_categorie(conn, categorie_id, limit, offset):
    """ Recover products from a specific categorie and return them"""
    products = conn.query("""
        SELECT * FROM products
        WHERE categorie_id = {0}
        LIMIT {1} OFFSET {2}
        """.format(categorie_id, limit, offset))

    return products


def show_spec_product_from_spec_categorie(conn, categorie_id, product_id):
    """ Recover a specific product from a specific categorie and return it"""
    products = conn.query("""
        SELECT * FROM products
        WHERE categorie_id = {0}
        AND product_id = {1}
        """.format(categorie_id, product_id))

    return products


def save_into_registered_products(conn, name, nutrition_rate, url,
                                  shop, categorie_id, product_id):
    """ Save product informations into registered_products table """
    saving = conn.query("""
        INSERT INTO registered_products (name, nutrition_rate, http_link,
        shop, categorie_id, product_id)
        VALUES ('{0}', '{1}', '{2}', '{3}', {4}, {5})
        """.format(name, nutrition_rate, url, shop, categorie_id, product_id))

    return saving


def show_registered_products(conn, limit, offset):
    """ Recover product(s) from registered_products table and return it/them"""
    registered_products = conn.query("""
        SELECT * FROM registered_products
        LIMIT {0} OFFSET {1}
        """.format(limit, offset))

    return registered_products


def show_registered_product_with_id(conn, id_reg):
    """ Recover specific product from registered_products table based on id inputed"""
    registered_product = conn.query("""
        SELECT * FROM registered_products
        WHERE id = {0}
        """.format(id_reg))

    return registered_product


def drop_table_registered_products(conn):
    """ Delete registered_products table"""
    table = conn.query("""
        DROP TABLE registered_products
        """)

    return table


def create_table_registered_products(conn):
    """ Create registered products table """
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


def show_substitutes_of_products(conn, product_id, categorie_id, nutrition_rate, limit, offset):
    """ Recover product's substitutes and return them : substitutes are products
    from the same categorie with a lower nutrition rate"""
    substitutes = conn.query("""
        SELECT * FROM products
        WHERE product_id != {0}
        AND categorie_id = {1}
        AND nutrition_rate < '{2}'
        LIMIT {3} OFFSET {4}
        """.format(product_id, categorie_id, nutrition_rate, limit, offset))

    return substitutes


def delete_database(conn, database):
    """ Delete database inputed """
    database = conn.query("""
        DROP DATABASE {0}
        """.format(database))

    return database


def delete_registered_product(conn, registered_product_id):
    """ Delete a specific product from registered_products table based on his id"""
    registered_product_del = conn.query("""
        DELETE FROM registered_products
        WHERE id = {0}
        """.format(registered_product_id))

    return registered_product_del


def show_databases_check_list(conn):
    """ Recover all databases from mysql and return them throught a list
    that will be tested (presence or not of database inputed into that list)"""
    databases_list = list()
    databases = conn.query("""
        SHOW DATABASES
        """)

    for database in databases:
        databases_list.append(database.Database)

    return databases_list


def show_tables_list(conn):
    """ Recover all tables from mysql and return them throught a list
    that will be tested (presence or not of tables categories, products
    and registered_products to validate or not the use of the database selected)"""
    tables_list = list()
    tables = conn.query("""
        SHOW TABLES
        """)

    for table in tables:
        tables_list.append(table.Table)

    return tables_list


def get_categories_count(conn):
    """ Recover categories' count and return it """
    categories_count = 0
    categories = conn.query("""
        SELECT name FROM categories
        """)

    for categorie in categories:
        categories_count += 1

    return categories_count


def get_products_count_from_spec_categorie(conn, categorie_id):
    """Recover products' count from a specific categorie and return it """
    products_count = 0
    products = conn.query("""
        SELECT name FROM products
        WHERE categorie_id = {0}
        """.format(categorie_id))

    for product in products:
        products_count += 1

    return products_count


def get_substitutes_count(conn, categorie_id, product_id):
    """ Recover substitutes' count and return it """
    substitutes_count = 0
    product_selected = conn.query("""
        SELECT * FROM products
        WHERE categorie_id = {0}
        AND product_id = {1}
        """.format(categorie_id, product_id))

    for product in product_selected:
        product_nutrition_rate = product.nutrition_rate

    substitutes = conn.query("""
        SELECT name FROM products
        WHERE categorie_id = {0}
        AND product_id != {1}
        AND nutrition_rate < '{2}'
        """.format(categorie_id, product_id, product_nutrition_rate))

    for substitute in substitutes:
        substitutes_count += 1

    return substitutes_count


def get_registered_products_count(conn):
    """ Recover registered products' count and return it """
    registered_products_count = 0
    registered_products = conn.query("""
        SELECT name FROM registered_products
        """)

    for registered_product in registered_products:
        registered_products_count += 1

    return registered_products_count


def get_number_page_categories(conn, categories_number):
    """ Recover number of categories' page according to the number of categories"""
    number_page_categories = 0
    categories = conn.query("""
        SELECT name FROM categories
        """)

    for categorie in categories:
        categories_number += 1

    number_page_categories = floor(categories_number / 10)

    return number_page_categories


def get_number_page_products(conn, categorie_id, products_number):
    """ Recovert number of products' page according to the number of products
    for a specific categorie """
    number_page_products = 0
    products = conn.query("""
        SELECT name FROM products
        WHERE categorie_id = {0}
        """.format(categorie_id))

    for product in products:
        products_number += 1

    number_page_products = floor(products_number / 10)

    return number_page_products


def get_number_page_substitutes(conn, categorie_id, product_id, substitutes_number):
    """ Recover substitutes' page number according to the number of substitutes and return it """
    number_page_substitutes = 0
    product_selected = conn.query("""
        SELECT * FROM products
        WHERE categorie_id = {0}
        AND product_id = {1}
        """.format(categorie_id, product_id))

    for product in product_selected:
        product_nutrition_rate = product.nutrition_rate

    substitutes = conn.query("""
        SELECT name FROM products
        WHERE categorie_id = {0}
        AND product_id != {1}
        AND nutrition_rate < '{2}'
        """.format(categorie_id, product_id, product_nutrition_rate))

    for substitute in substitutes:
        substitutes_number += 1

    number_page_substitutes = floor(substitutes_number / 10)

    return number_page_substitutes


def get_number_page_registered_products(conn, registered_products_number):
    """ Recover registered products' pages number according to the number of 
    registered products present, and return it """
    registered_products = conn.query("""
        SELECT name FROM registered_products
        """)

    for registered_product in registered_products:
        registered_products_number += 1

    number_page_registered_products = floor(registered_products_number / 10)

    return number_page_registered_products
