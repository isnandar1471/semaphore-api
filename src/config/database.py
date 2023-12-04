import sqlalchemy
import sqlalchemy.orm
import src.config.environment


URL_ENGINE = f"mysql+pymysql://{src.config.environment.APP_DATABASE_USERNAME}:{src.config.environment.APP_DATABASE_PASSWORD}@{src.config.environment.APP_DATABASE_HOST}:{src.config.environment.APP_DATABASE_PORT}/{src.config.environment.APP_DATABASE_NAME}"
print(f"DATABASE_URL_ENGINE {type(URL_ENGINE)} {URL_ENGINE}")

ENGINE = sqlalchemy.create_engine(url=URL_ENGINE, echo=src.config.environment.APP_DATABASE_LOG_QUERY_IN_TERMINAL)
print(f"DATABASE_ENGINE {type(ENGINE)} {ENGINE}")

SESSION_MAKER = sqlalchemy.orm.sessionmaker(bind=ENGINE, expire_on_commit=False)
print(f"DATABASE_SESSION {type(SESSION_MAKER)} {SESSION_MAKER}")
