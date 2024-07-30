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

dependensi yang penting:
- `tensorflow` untuk membaca model yang diimpor
- `bcrypt` untuk enkripsi password
- `sqlalchemy` untuk orm
- `sqlalchemy-seeder` untuk seeder
- `alembic` untuk database version control
- `fastapi` untuk rest api
- `startlette`
- `uvicorn`
- `python-dotenv` untuk membaca env file
- `pymysql`
- `pydantic`
- `pyjwt` untuk menggenerate jwt
- `pillow`
- `numpy` untuk mengonversi gambar

# Error yang perlu didokumentasikan

## `sqlalchemy` membutuhkan `pymysql`, tetapi tidak terinstall otomatis

## ???? membutuhkan `pillow`


# Token

> Menggunakan JWT

# Database

## Migration

### membuat migrasi 
alembic revision -m <filename...>
(kayaknya harus pakai str id, buka filename)

### menjalankan migrasi hingga migrasi tertentu
alembic upgrade <filename...>

### menjalankan migrasi hingga migrasi terakhir
alembic upgrade head

### menjalankan rollback hingga x migrasi ke belakang
alembic downgrade <-1>

## Seeding

```shell
python -m src.seeder.seeder
```

## Run app

```
python main.py
```

https://www.tensorflow.org/install/pip

## Auto install all package from requirements.txt

[reference](https://stackoverflow.com/questions/35802939/install-only-available-packages-using-conda-install-yes-file-requirements-t)

## How to use AutoFlake for remove unused import

```sh
autoflake --in-place --remove-all-unused-imports <filepath>
```

## Hot to use isort for sorting import statements

```sh
isort <filepath>
```

# Linter menggunakan pylint
