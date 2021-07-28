from selenium import webdriver
from bs4 import BeautifulSoup
import lxml


city = [
	'Череповец',
	'Ярославль',
	'Москва',
	'Белгород',
	'Воронеж',
	'Орел',
	'Воркута',
	'Колпино',
	'Оленегорск',
	'Санкт-Петербург',
	'Новосибирск'
	'Казань',
]


def get_young_professional_vacations():
	driver = webdriver.Chrome()
	driver.get('https://career.severstal.com/vacancies/?direction=%D0%BC%D0%BE%D0%BB%D0%BE%D0%B4%D0%BE%D0%B9+%D1%81%D0%BF%D0%B5%D1%86%D0%B8%D0%B0%D0%BB%D0%B8%D1%81%D1%82')
	soup = BeautifulSoup(driver.page_source, 'lxml')
	vacations = soup.find_all('a', class_='all-vacancies__table-tr')
	vacancies = []
	for vacation in vacations:
		while True:
			information_about_vacancy = vacation.find_all('div', class_='all-vacancies__table-td-content col-xs-12 col-sm-24')
			if vacation.find('div', class_='all-vacancies__table-main-sub-title').get_text(strip=True) not in city:
				break
			else:
				town = vacation.find('div', class_='all-vacancies__table-main-sub-title').get_text(strip=True)
			if information_about_vacancy[4].get_text(strip=True) == '':
				salary = 'Не указано'
			else:
				salary = information_about_vacancy[4].get_text(strip=True)
			vacancies.append({'description' : vacation.find('div', class_='all-vacancies__table-main-title').get_text(strip=True),
							  'city' : town,
							  'date_of_publication' : information_about_vacancy[0].get_text(strip=True),
							  'work_experience' : information_about_vacancy[1].get_text(strip=True),
							  'employment' : information_about_vacancy[2].get_text(strip=True),
							  'schedule' : information_about_vacancy[3].get_text(strip=True),
							  'salary' : salary,
			})
			break
	return vacancies