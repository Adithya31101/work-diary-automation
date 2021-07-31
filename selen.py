import os
import json

def init_config():
	print("Configuration file initialization for the program...")
	print("Writing to `config.json` file...")
	name = input("Enter name: ")
	regno = input("Enter register number: ")
	email = input("Enter email: ")
	chromedriver = input("Enter file location of chrome driver: ")
	config = { 'name': name, 'regno': regno, 'email': email, 'chromedriver': chromedriver }
	config_fp = open('config.json', 'w')
	json.dump(config, config_fp)
	config_fp.close()
	return config

def load():
	try:
		conf_fp = open('config.json')
		config = json.load(conf_fp)
		conf_fp.close()
		return config
	except: 
		print("Error in JSON encoding in config file")
		exit(1)

def start(config):
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.common.action_chains import ActionChains
	import datetime
	import time
	print("Opening browser window with the form, please wait...")
	date = datetime.datetime.now()
	date_input = date.strftime('%d%m%Y')
	time_input = None
	if(date.isoweekday() == 6):
		time_input = "9:00 AM - 11:00 AM"
	if(date.isoweekday() == 4):
		time_input = "2:00 PM - 4:00 PM"
	
	browser = webdriver.Chrome(config['chromedriver'])
	browser.get("https://docs.google.com/forms/d/1XkiTZhJ4Av1-Zv678B3ossjtEfvN7vhEBCll86vLrLU/viewform?edit_requested=true")
	time.sleep(2)
	actions = ActionChains(browser)
	email = browser.find_element_by_css_selector('input[type=email]')
	email.send_keys(config['email'])
	email.send_keys(Keys.TAB)
	key_txt = "{}\t{}\t{}\t{}"
	actions.send_keys(key_txt.format(config['name'], config['regno'], date_input, time_input ))
	actions.perform()
	end = None
	while not end == "end":
		end = input()
	
if os.path.isfile('config.json'):
	config = load()
else: 
	config = init_config()
start(config)


