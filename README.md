# Discount-Hub-
A django and Scrapy based common ground to find all discounts from various portals

Initially daraz.com.bd and pickaboo.com has been crawled by scrapy framework and a demo website represents the data along with a cool search functionality which has backend support of django framework. The scrapy project and django project were combined through django pipeline.

To use this project and to contribute to it:

create a virtual environment:
  virtualenv venv
activate the venv environment by:
  source venv/bin/activate
now inside the environment install all requirements:
  pip install -r requirements.txt
  
run the django project:
  python manage.py runserver

to access admin:
  admin: ph03
  password: ph03ph03

to crawl discount informations go to the project root and then:
  cd olx/olx/
  scrapy crawl daraz (to crawl daraz.com.bd)
  or
  scrapy crawl pickaboo (to crawl pickaboo.com)
  

  

