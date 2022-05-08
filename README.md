# CodeMonk Backend Developer Assignment

In this assignment you will be writing a backend server for a CodeMonk application. 
User Can Upload Multiple Paragraphs of Text and Serach a 'Word' that will ouput the Paragraph's ID and the Paragraph containing the 'Word'.

## 1 Clone the Repository 
```bash
git clone https://github.com/shazam-baba/CodeMonk.git
```

## 2 Install the dependencies

```bash
cd CodeMonk
pip install -r requirements.txt
```

## 3 Run the migrations & Run the server

```bash
python manage.py mmakemigrations
python manage.py migrate
python manage.py runserver  
```

## 4.1 open the browser and navigate to http://localhost:8000/api/

Here you can find the API Urls and what they are doing. 

```python
{
    "Login": "/api/login-page/",
    "Logout": "/api/logout-page/",
    "Register": "/api/register-page/",
    "GET Get-Paras": "/api/text-list/",
    "POST Post-Paras": "/api/text-upload/",
    "POST Search-Word": "/api/word-search/"
}
```

## 4.2 If you are using Postman, naviagte to the following url: http://localhost:8000/api/
 1> You first have to "Login" or "Register" as a user. 
    Only Then you can upload paragraphs and search for a word. Else API won't work.
*   And Dont Forget to add X-CSRFToken to the header.  (X-CSRFToken is the token that is used to verify that the request is coming from the same origin.)

## 5.1 Login  (POST) /api/login-page/
    Inside Postman add the following <ins>form-data</ins> (in the body):
    ```
        KEY         VALUE
        email       your_email
        password    your_password
    ```
    And click on "Send" button. 

##  5.2 Logout (GET) /api/logout-page/
    Just visit the url and you will be logged out.

## 5.3 Register (POST) /api/register-page/
    As a new user, you can register by visiting the url.
    Inside Postman add the following <ins>form-data</ins> (in the body):   
    ``` 
        KEY         VALUE
        name        your_name
        email       your_email
        password    your_password
        password2   your_password_again
        dob         your_date_of_birth format(YYYY-MM-DD)  *
    ``` 
    And click on "Send" button.
    * If you dont want to add dob, just leave it empty.

## 5.4 Upload Paragraphs (POST) /api/text-upload/
    You can upload paragraphs by visiting the url.
    Inside Postman add the following <ins>form-data</ins> (in the body):
    ```
        KEY         VALUE
        text        your_paragraph      *
    ```
    And click on "Send" button.
    * Empty Text wont be accepted and will return an error.
    * Also you can't upload same text twice.

## 5.5 Search for a Word (POST) /api/word-search/
    You can search for a word by visiting the url.
    Inside Postman add the following <ins>form-data</ins> (in the body):
    ```
        KEY         VALUE   
        word        your_word    
    ```
    And click on "Send" button.

## 5.6 Qquery All Paragraphs (GET) /api/text-list/
    You can query all paragraphs by visiting the url.


# Thanks you for using CodeMonk Backend Developer Assignment.
## BY - [Siddharth](https://github.com/shazam-baba)