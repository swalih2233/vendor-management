# vendor-management

## Installation

1. **First clone the repository in your system.**

   `https://github.com/swalih2233/vendor-management.git`

2. **Then start Virtual Environment within current Directory.**

   `python -m venv venv`

   `venv\Scripts\activate`

3. **Then install the dependencies from requirements.txt.**

   `pip install -r requirements.txt`


4. **Then change the PostgreSQL DB Details in settings.py**
   **If your dont have postgres you can use Sqlite3**


   **For sqlite3 Update DB Details in settings.py**

   DATABASES = { \
      'default': { \
         'ENGINE': 'django.db.backends.sqlite3', \
         'NAME': BASE_DIR / 'db.sqlite3', \
      } \
   } \

   **For PostgreSQL Update DB Details in settings.py**

   DATABASES = { \
      'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2', \
         'NAME': 'DB_NAME', \
         'USER':'DB_USER', \
         'PASSWORD':'DB_USER_PASSWORD', \
         'HOST':'localhost', \
         'PORT':'5432' \
      } \
   } \
   
5. **Then Apply Migrations.**

   `python manage.py makemigrations`

   `python manage.py migrate`

6. **Execute the manage.py file to runserver.**

   `python manage.py runserver`

7. **Use Postman to check api endpoints**

   `BASE_URL = http://127.0.0.1:8000/api/`

   `1. POST BASE_URL + vendors/`

      `SEND DATA = "name", "contact_details", "address"`

      `SAMPLE RESPONSE`

      { \
         "status_code": 6000, \
         "message" : "Vendor Created successfully" \
      } \

   `2. GET BASE_URL + vendors/`

      `SAMPLE RESPONSE`

      { \
         "status_code": 6000, \
         "data" : [vendors details] \
      } \


   `3. GET BASE_URL + vendors/id/`

      `SAMPLE RESPONSE`

      { \
         "status_code": 6000, \
         "data" : [vendor details] \
      } \
      
   
   `4. PUT BASE_URL + vendors/id/`

      `SAMPLE RESPONSE`

      { \
         "status_code": 6000, \
         "message" : "vender updated successfully" \
      } \

   `5. DELETE BASE_URL + vendors/id/`

      `SAMPLE RESPONSE`

      { \
         "status_code": 6000, \
         "message" : "vender deleted successfully" \
      } \

   `6. GET BASE_URL + vendors/id/perfomance/`

      `SAMPLE RESPONSE`

      { \
         "status_code": 6000, \
         "data" : [vendor perfomance details] \
      } \


   `7. POST BASE_URL + purchase_orders/`

      `SEND DATA = "vendor", "items", "quantity"`

      `send vendor id items list as a json`

      `SAMPLE RESPONSE`

      { \
         "status_code": 6000, \
         "message" : "Purchased successfully" \
      } \

   `8. GET BASE_URL + purchase_orders/`

      `SAMPLE RESPONSE`

      { \
         "status_code": 6000, \
         "data" : [orders details] \
      } \


   `9. GET BASE_URL + purchase_orders/id/`

      `SAMPLE RESPONSE`

      { \
         "status_code": 6000, \
         "data" : [order details] \
      } \

   `10. DELETE BASE_URL + purchase_orders/id/`

      `SAMPLE RESPONSE`

      { \
         "status_code": 6000, \
         "message" : "Deleted successfully" \
      } \

   `10. PUT BASE_URL + purchase_orders/id/issue_date/`

      `SAMPLE RESPONSE`

      { \
         "status_code": 6000, \
         "message" : "Updated successfully" \
      } \

   `11. PUT BASE_URL + purchase_orders/id/acknowledgment_date/`

      `SEND DATA = "date"`

      `send expected delivery date`

      `SAMPLE RESPONSE`

      { \
         "status_code": 6000, \
         "message" : "Updated successfully" \
      } \

   `12. PUT BASE_URL + purchase_orders/id/delivery_date/`

      `SAMPLE RESPONSE`

      { \
         "status_code": 6000, \
         "message" : "Updated successfully" \
      } \


   `13. PUT BASE_URL + purchase_orders/id/quality_rating/`

      `SEND DATA = "rate"`

      `send quality rating from 0 to 5. if give more that 5 it take as 5`

      `SAMPLE RESPONSE`

      { \
         "status_code": 6000, \
         "message" : "Updated successfully" \
      } \