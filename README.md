catatan pekerjaan

- orm model belum disetting untuk relasi
- database migration masih manual alias tidak dilanjutkan

- apa istilahnya untuk di dart yg memasukan suatu type ke T di <T>

# semaphore-api

# SSH

```sh
ssh -i "C:\Users\isnandar\Downloads\isnandar-keypair.pem" ubuntu@54.169.244.120

```

## Tested in

- Python 3.10.11

## Clone the project

```
git clone https://github.com/isnandar1471/semaphore-api.git
```

## Install dependensi

```
pip install -r requirements.txt
```

# Password Hashing

> Menggunakan BCrypt

# Token

> Menggunakan JWT

## How to migrate database?

(MANUAL)

alembic revision -m <filename...>
(kayaknya harus pakai str id, buka filename)

alembic upgrade <filename...>

alembic downgrade <-1>

## Run app

```
uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
```

```
python main.py
```

https://www.tensorflow.org/install/pip

## Auto install all package from requirements.txt

[reference](https://stackoverflow.com/questions/35802939/install-only-available-packages-using-conda-install-yes-file-requirements-t)

```
FOR /F "delims=~" %f in (requirements.txt) DO conda install --yes "%f"
```

```
FOR /F "delims=~" %f in (requirements.txt) DO pip install "%f"
```

no conda
pip

- opencv-python
- pm3
- python_dotenv

## How to use AutoFlake for remove unused import

```sh
autoflake --in-place --remove-all-unused-imports <filepath>
```

## Hot to use isort for sorting import statements

```sh
isort <filepath>
```

# Linter menggunakan pylint
