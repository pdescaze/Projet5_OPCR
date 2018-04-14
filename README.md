# PUR BEURRE APPLICATION

# Resume
  
This software permits the user to search products and substitutes (products from the same categorie but with a lower nutrition rate) from various aliments' categories. All products and categories are based on OpenFoodFacts's API database.


# Description

As soon as the user execute the application, he has to input informations to connect himself to his own mysql server.
Then, the user has 3 choices :
  - He can create a database with categories and products based on OpenFoodFacts' API
  - He can delete databases from his mysql server
  - He can select a database to run the Application with.
  
Once the database is selected, the user will have 2 choices:
  - Search a product/substitutes from a categorie
  - Look into his registered products
  

For any choice and for any step, the user will have to inform an input. All commands that are available are displayed and will permits the user to use the Application correctly. The user can go forward in his research but he can also go backward throught specials' commands that are displayed.

If he choose to search for products and substitutes. A List of categories will be displayed and following the input (the id of the categorie), products of the categorie selected will be printed (10 per 10) through one or more pages if there is more than 10 products in the selected categorie.
Same conditions are applied for substitutes.

If he choose to look into his registered products, the user will be able to see details about the product/substitute he saved and to manage his registered products (delete one product, delete all).


# Requirements

  - Python 3.6
  - MySQL
  - packages informed in requirements.txt
  
 



