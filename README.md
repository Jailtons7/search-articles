# SEARCH ARTICLES

Scientific research is part of lives of reasearchers and academic specialists. 
This project aims to create a web platform that make life easier to researchers offering 
a quick and assertive search for scientific articles.

### 1. Running the api

> For the correct operation of the commands below it is advisable to have `python >= 3.8` and 
[create and activate a python virtual environment.](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)

#### 1.1. Install python dependencies:
```shell
pip install -r requirements.txt
```

#### 1.2. Setting environment variables:
Create a `.env` file and copy and past the content of `local.env` file to it.

You must provide a `DATABASE_URL`

#### 1.3. Run migrations:
```shell
python manage.py migrate
```

#### 1.4. Run the WEB API:
```shell
python manage.py runserver
```

### 2. Adding data
To populate database you must provide a json file per table inside `api/fixtures/` folder. The name
 of each file must be the name of the class that define the table. 

After that, use the `upload_data` custom command to upload. This command needs a `--model` option.
If model has f-keys use the option `--foreign-key` and if your json file has keys that is not in you
table structure use the `--not_use` option. 

Below there are some examples of use of this command.
```shell
./manage.py upload_data -m TblServidores -f CodCargo CodSiglaOrgaoIE -n NumSiape CodJornadaTrab CodOrgaoIEExerc DatIngressoOrgao AnoIngressoOrgao ValTempoServicoIE CodLattes FlagPesquisador
```

```shell
./manage.py upload_data -m TblArtigoPublicado -f CodSiglaAtuacaoProfissionalLattes CodIssn CodTitulosArtigos CodIdioma CodServidor -n CodLattes ID_ARTIGO CodDoi
```

```shell
./manage.py upload_data -m TblPalavraChaveArt
```

```shell

```

### 3. API calls

#### 3.1. Authentication

##### 3.1.1. Create User
```shell
POST /authentication/users/create/
{
    "first_name": "name",
    "last_name": "surname",
    "email": "name@example.com",
    "cpf": "12345678912",
    "phone": "+55 (82) 3333 3333",
    "password": "my-secret"
}
```
Response: the created user with status code 201.

##### 3.1.2. Obtain token
```shell
POST /authentication/token/obtain/
{
  "email": "name@example.com",
  "password": "my-secret"
}
```
Response: the access and refresh tokens with status code 200.

##### 3.1.3. Refresh token
```shell
POST /authentication/token/refresh/
{
  "refresh": refresh_token
}
```
Response: the access and refresh tokens with status code 200.

##### 3.1.4. Update User
```shell
POST /authentication/users/update/
# headers
{
  'Authorization': 'Bearer ' + access_token
}
# body
{
    "first_name": "name2",
    "last_name": "surname2",
    "email": "name2@example.com",
    "cpf": "12345678912",
    "phone": "+55 (82) 3333 3333",
    "password": "my-secret"
}
```
Response: the user with status code 200.

##### 3.1.5. Get User
```shell
POST /authentication/users/
# headers
{
  'Authorization': 'Bearer ' + access_token
}
```
Response: the user with status code 200.

##### 3.1.6. Delete User
```shell
DELETE /authentication/users/delete/
# headers
{
  'Authorization': 'Bearer ' + access_token
}
```
Response: no content with status code 204.

### 3.2. Articles

#### 3.2.1 Get Articles

```shell
GET /api/v1/articles/
# headers
{
  'Authorization': 'Bearer ' + access_token
}
```
Methods POST, PUT and DELETE are not allowed.
