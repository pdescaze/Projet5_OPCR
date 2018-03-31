#!/usr/bin/python3
# -*- coding: Utf-8 -*

import os
import sys
import records
import re

from content.ui import Ui
from content.recovery import Recovery
from content.database import Database



proceed_menu = True
page_count_categories = 0
page_count_products = 0
page_count_substitutes = 0
page_count_registered = 0
categories_number = 0
products_number = 0
substitutes_number = 0
registered_number = 0

#Initialisation of objects
ui = Ui()
sql_main = Recovery()


while proceed_menu is True:

	os.system("cls")
	ui.main_page_database_display()

	if ui.choice_database == "1":
		os.system("cls")
		proceed_menu = False
		proceed_username = True

		while proceed_username is True:
			os.system("cls")
			ui.username_display()

			if ui.choice_username == "#quit":
				sys.exit("Closing the application")
			else:
				proceed_username = False
				proceed_password = True

				while proceed_password is True:
					os.system("cls")
					ui.password_display()

					if ui.choice_password == "#quit":
						sys.exit("Closing the Application")
					elif ui.choice_password == "#un":
						proceed_password = False
						proceed_username = True
					else:
						proceed_password = False
						proceed_host = True

						while proceed_host is True:
							os.system("cls")
							ui.host_display()

							if ui.choice_host == "#quit":
								sys.exit("Closing the Application")

							elif ui.choice_host == "#pm":
								proceed_host = False
								proceed_password = True

							elif ui.choice_host == "#un":
								proceed_host = False
								proceed_username = True

							else:
								base = Database(ui.choice_username, ui.choice_password, ui.choice_host)
								base.connect_to_mysql()
								if base.conn_answer != "":
									os.system("cls")
									ui.connect_database_fail()
									if ui.choice_connect_database_fail == "#quit":
										sys.exit("Closing the Application")
									else:
										proceed_host = False
										proceed_menu = True
								else:
									proceed_host = False
									proceed_database_menu = True

									while proceed_database_menu is True:
										os.system("cls")
										ui.database_menu()

										if ui.choice_database_menu == "#hm":
											proceed_database_menu = False
											proceed_host = True

										elif ui.choice_database_menu == "#pm":
											proceed_database_menu = False
											proceed_password = True

										elif ui.choice_database_menu =="#un":
											proceed_database_menu = False
											proceed_username = True

										elif ui.choice_database_menu == "1":
											proceed_database_menu = False
											proceed_database_creation = True

											while proceed_database_creation:
												os.system("cls")
												ui.creation_database()
												os.system("cls")
												ui.creation_database_loading_page_start()
												base.connect_to_database(ui.choice_creation_database)
												base.tables_creation()
												base.get_categories_name_url()
												base.insert_categories()
												base.get_products()
												base.insert_product_cat_id()
												ui.creation_database_loading_page_end()

												if ui.creation_databse == "#dm":
													proceed_database_creation = False
													proceed_database_menu = True

												elif ui.creation_databse == "#quit":
													sys.exit("Closing the Application")

												else:
													proceed_database_creation = False
													proceed_database_menu = True

										elif ui.choice_database_menu == "2":
											os.system("cls")
											ui.delete_database_start(base.conn)

											if ui.choice_delete_database_start == "#quit":
												sys.exit("Closing the Application")

											elif ui.choice_delete_database_start == "#dm":
												proceed_database_menu = True

											else:
												base.delete_database(ui.choice_delete_database_start)
												ui.delete_database_end(ui.choice_delete_database_start)

												if ui.choice_delete_database_end == "#dm":
													proceed_database_menu = True

												elif ui.choice_delete_database_end == "#quit":
													sys.exit("Closing the Application")


										elif ui.choice_database_menu == "3":
											os.system("cls")
											proceed_select_database = True

											while proceed_select_database is True:
												os.system("cls")
												ui.select_database(base.conn)
												base.show_databases()												

												if ui.choice_select_database == "#quit":
													sys.exit("Closing the Application")

												elif ui.choice_select_database == "#dm":
													proceed_select_database = False
													proceed_database_menu = True

												elif ui.choice_select_database in base.show_databases_list:
													base.connect_to_database(ui.choice_select_database)
													proceed_select_database = False
													proceed_app = True

													while proceed_app is True:								
														os.system("cls")
														ui.main_page_display()

														if ui.choice_step_1 == "1":
															proceed_app = False
															step_1 = True

															while step_1 is True:
																os.system("cls")																
																ui.categories_display(base.conn, page_count_categories)
																base.number_page_categories(categories_number)														

																if ui.choice_categorie == "#mm":
																	page_count_categories = 0
																	page_count_products = 0
																	page_count_substitutes = 0
																	step_1 = False
																	proceed_app = True

																elif ui.choice_categorie == ">":
																	if page_count_categories < base.number_page_categorie:
																		page_count_categories += 1

																elif ui.choice_categorie == "<":
																	if page_count_categories > 0:
																		page_count_categories -= 1

																elif ui.choice_categorie =="#quit":
																	sys.exit("Closing the Application")

																elif re.search("([0-9]{1,})",ui.choice_categorie):
																	ui.choice_categorie = int(ui.choice_categorie)
																	base.categories_count()
																	if ui.choice_categorie >= 1 and ui.choice_categorie <= base.categorie_count:
																		print(ui.choice_categorie)
																		print(type(ui.choice_categorie))
																		step_1 = False
																		step_2 = True

																		while step_2 is True:
																			os.system("cls")
																			ui.products_display(base.conn, ui.choice_categorie, page_count_products)
																			base.number_page_products(ui.choice_categorie, products_number)

																			if ui.choice_product == "#mm":
																				page_count_categories = 0
																				page_count_products = 0
																				page_count_substitutes = 0
																				step_2 = False
																				proceed_app = True

																			elif ui.choice_product == ">":
																				if page_count_products < base.number_page_product:
																					page_count_products += 1

																			elif ui.choice_product == "<":
																				if page_count_products > 0:
																					page_count_products -= 1

																			elif ui.choice_product == "#quit":
																				sys.exit("Closing the Application")

																			elif ui.choice_product == "#cm":
																				page_count_categories = 0
																				page_count_products = 0
																				page_count_substitutes = 0
																				step_2 = False
																				step_1 = True

																			elif re.search("([0-9]{1,})",ui.choice_product):
																				ui.choice_product =int(ui.choice_product)
																				base.products_count(ui.choice_categorie)
																				if ui.choice_product >= 1 and ui.choice_product <= base.product_count:
																					step_2 = False
																					step_3 = True

																					while step_3 is True:
																						os.system("cls")
																						ui.products_details_display(base.conn, ui.choice_categorie, ui.choice_product)

																						if ui.choice_product_details == "#mm":
																							page_count_categories = 0
																							page_count_products = 0
																							page_count_substitutes = 0
																							step_3 = False
																							proceed_app = True

																						elif ui.choice_product_details == "#quit":
																							sys.exit("Closing the Application")

																						elif ui.choice_product_details == "#cm":
																							page_count_categories = 0
																							page_count_products = 0
																							page_count_substitutes = 0
																							step_3 = False
																							step_1 = True

																						elif ui.choice_product_details == "#pm":
																							page_count_products = 0
																							page_count_substitutes = 0
																							step_3 = False
																							step_2 = True

																						elif ui.choice_product_details == "#substitute":
																							step_3 = False
																							proceed_substitutes = True

																							while proceed_substitutes:
																								os.system("cls")
																								ui.substitutes_display(base.conn, ui.choice_categorie, ui.choice_product, page_count_substitutes)
																								base.number_page_substitutes(ui.choice_categorie, ui.choice_product, substitutes_number)

																								if ui.choice_substitutes == "#quit":
																									sys.exit("Closing the Application")

																								elif ui.choice_substitutes == ">":
																									if page_count_substitutes < base.number_page_substitute:
																										page_count_substitutes += 1

																								elif ui.choice_substitutes == "<":
																									if page_count_substitutes > 0:
																										page_count_substitutes -= 1

																								elif ui.choice_substitutes == "#pd":
																									page_count_substitutes = 0
																									proceed_substitutes = False
																									step_3 = True

																								elif ui.choice_substitutes == "#pm":
																									page_count_products = 0
																									page_count_substitutes = 0
																									proceed_substitutes = False
																									step_2 = True

																								elif ui.choice_substitutes == "#cm":
																									page_count_categories = 0
																									page_count_products = 0
																									page_count_substitutes = 0
																									proceed_substitutes = False
																									step_1 = True

																								elif ui.choice_substitutes == "#mm":
																									page_count_categories = 0
																									page_count_products = 0
																									page_count_substitutes = 0
																									proceed_substitutes = False
																									proceed_app = True

																								elif re.search("([0-9]{1,})",ui.choice_substitutes):
																									ui.choice_substitutes = int(ui.choice_substitutes)
																									base.substitutes_count(ui.choice_categorie, ui.choice_product)
																									if ui.choice_substitutes >= 1 and ui.choice_substitutes <= base.substitute_count:
																										proceed_substitutes = False
																										proceed_substitute_details = True

																										while proceed_substitute_details:
																											os.system("cls")
																											ui.substitutes_details(base.conn, ui.choice_categorie, ui.choice_substitutes)

																											if ui.choice_substitutes_details == "#quit":
																												sys.exit("Closing the Application")

																											elif ui.choice_substitutes_details == "#save":
																												proceed_substitute_details = False
																												proceed_substitute_saved = True

																												while proceed_substitute_saved:
																													os.system("cls")
																													ui.save_substitute(base.conn, ui.choice_categorie, ui.choice_substitutes)

																													if ui.choice_substitute_saved == "#quit":
																														sys.exit("Closing the Application")
																													
																													elif ui.choice_substitute_saved == "#sd":
																														proceed_substitute_saved = False
																														proceed_substitute_details = True

																													elif ui.choice_substitute_saved == "#sm":
																														page_count_substitutes = 0
																														proceed_substitute_saved = False
																														proceed_substitutes = True

																													elif ui.choice_substitute_saved == "#pd":
																														page_count_substitutes = 0
																														proceed_substitute_saved = False
																														step_3 = True

																													elif ui.choice_substitute_saved == "#pm":
																														page_count_products = 0
																														page_count_substitutes = 0
																														proceed_substitute_saved = False
																														step_2 = True

																													elif ui.choice_substitute_saved == "#cm":
																														page_count_categories = 0
																														page_count_products = 0
																														page_count_substitutes = 0
																														proceed_substitute_saved = False
																														step_1 = True

																													elif ui.choice_substitute_saved == "#mm":
																														page_count_categories = 0
																														page_count_products = 0
																														page_count_substitutes = 0
																														proceed_substitute_saved = False
																														proceed_app = True																											

																											elif ui.choice_substitutes_details == "#sm":
																												page_count_substitutes = 0
																												proceed_substitute_details = False
																												proceed_substitutes = True

																											elif ui.choice_substitutes_details == "#pd":
																												page_count_substitutes = 0
																												proceed_substitute_details = False
																												step_3 = True

																											elif ui.choice_substitutes_details == "#pm":
																												page_count_products = 0
																												page_count_substitutes = 0
																												proceed_substitute_details = False
																												step_2 = True

																											elif ui.choice_substitutes_details == "#cm":
																												page_count_categories = 0
																												page_count_products = 0
																												page_count_substitutes = 0
																												proceed_substitute_details = False
																												step_1 = True

																											elif ui.choice_substitutes_details == "#mm":
																												page_count_categories = 0
																												page_count_products = 0
																												page_count_substitutes = 0
																												proceed_substitute_details = False
																												proceed_app = True

																						elif ui.choice_product_details == "#save":
																							step_3 = False
																							proceed_product_saved = True

																							while proceed_product_saved:																					
																								os.system("cls")
																								ui.save_product(base.conn, ui.choice_categorie, ui.choice_product)

																								if ui.choice_product_saved == "#quit":
																									sys.exit("Closing the Application")

																								elif ui.choice_product_saved == "#pd":
																									page_count_substitutes = 0
																									proceed_product_saved = False
																									step_3 = True

																								elif ui.choice_product_saved == "#pm":
																									page_count_products = 0
																									page_count_substitutes = 0
																									proceed_product_saved = False
																									step_2 = True

																								elif ui.choice_product_saved == "#cm":
																									page_count_categories = 0
																									page_count_products = 0
																									page_count_substitutes = 0
																									proceed_product_saved = False
																									step_1 = True

																								elif ui.choice_product_saved == "#mm":
																									page_count_categories = 0
																									page_count_products = 0
																									page_count_substitutes = 0
																									proceed_product_saved = False
																									proceed_app = True

														elif ui.choice_step_1 == "2":
															proceed_registered_products = True

															while proceed_registered_products:
																os.system("cls")
																ui.show_registered_products(base.conn, page_count_registered)
																base.number_page_registered_products(registered_number)

																if ui.choice_registered_products == "#mm":
																	page_count_registered = 0
																	proceed_registered_products = False
																	step_1 = True

																elif ui.choice_registered_products == "#quit":
																	sys.exit("Closing the Application")

																elif ui.choice_registered_products == "#all":
																	page_count_registered = 0
																	proceed_registered_products = False
																	proceed_registered_products_all_deleted = True

																	while proceed_registered_products_all_deleted:
																		os.system("cls")
																		ui.registered_products_all_deleted(base.conn)

																		if ui.choice_registered_products_all_deleted == "#quit":
																			sys.exit("Closing the Application")

																		elif ui.choice_registered_products_all_deleted == "#mm":
																			page_count_registered = 0
																			proceed_registered_products_all_deleted = False
																			proceed_app = True

																elif ui.choice_registered_products == ">":
																	if page_count_registered < base.number_page_registered_product:
																		page_count_registered += 1

																elif ui.choice_registered_products == "<":
																	if page_count_registered > 0:
																		page_count_registered -= 1

																elif re.search("([0-9]{1,})",ui.choice_registered_products):
																	ui.choice_registered_products = int(ui.choice_registered_products)
																	base.registered_products_count()
																	if ui.choice_registered_products >= 1 and ui.choice_registered_products <= base.registered_product_count:
																		proceed_registered_products = False
																		proceed_registered_products_details = True

																		while proceed_registered_products_details:
																			os.system("cls")
																			ui.registered_products_details_display(base.conn, ui.choice_registered_products)

																			if ui.choice_registered_products_details_display == "#quit":
																				sys.exit("Closing the Application")

																			elif ui.choice_registered_products_details_display == "#mm":
																				page_count_registered = 0
																				proceed_registered_products_details = False
																				step_1 = True

																			elif ui.choice_registered_products_details_display == "#rp":
																				page_count_registered = 0
																				proceed_registered_products_details = False
																				proceed_registered_products = True
																	
																elif ui.choice_registered_products == "#del":
																	page_count_registered = 0
																	proceed_registered_products = False
																	proceed_registered_products_to_del = True

																	while proceed_registered_products_to_del:
																		os.system("cls")
																		ui.show_registered_products_to_del(base.conn, page_count_registered)
																		print("recoller tout ce qui est fait plus haut en changeant les nombres par delete au lieu de details")

														elif ui.choice_step_1 == "#quit":
															sys.exit("Closing the Application")

														elif ui.choice_step_1 == "#dm":
															proceed_app = False
															proceed_database_menu = True

										elif ui.choice_database_menu == "#quit":
											sys.exit("Closing the Application")

										elif ui.choice_database_menu == "#un":
											proceed_database_menu = False
											proceed_username = True

										elif ui.choice_database_menu == "#pw":
											proceed_database_menu = False
											proceed_password = True

										elif ui.choice_database_menu == "#hm":
											proceed_database_menu = False
											proceed_host = True

	elif ui.choice_database == "#quit":
		sys.exit("Closing the Application")


os.system("pause")