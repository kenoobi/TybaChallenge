__Author__ = 'Santiago Benitez'

import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import random

# Estructure
class Tyba(unittest.TestCase):

	# Variables like Page Object Model
	ingresos = 'ingresosMensuales'
	plazo = "//*/select[@ng-model='termInYears']"
	opciones = "label"
	buttonCalcular = "//*/button[@ng-click='calculateByMonthlyIncome()']"
	tramitar = "lqn-bar-btn-container"

	def setUp(self):
		self.driver =  webdriver.Firefox(executable_path=r'geckodriver.exe')

	# Test Name
	def test_tramitarCredito(self):
		driver = self.driver
		driver.maximize_window()
		driver.get('https://www.metrocuadrado.com/calculadora-credito-hipotecario-vivienda/')

		driver.execute_script("window.scrollTo(0, 120)")

		# select a salary beetwen the minimun range and 4 mdc
		driver.find_element_by_id(self.ingresos).send_keys(random.randint(738000, 4000000))

		driver.find_element_by_xpath(self.plazo).click()

		# Select dropbox random
		select = Select(driver.find_element_by_xpath(self.plazo))
		select.select_by_index(random.randint(0,3))

		driver.find_element_by_xpath(self.buttonCalcular).click()

		# Assert to verify the text in the button
		element = driver.find_element_by_class_name(self.tramitar).text
		assert element == '¡TRAMITAR CRÉDITO!'

	def tearDown(self):
		self.driver.quit()
 
if __name__ == '__main__':
    unittest.main()