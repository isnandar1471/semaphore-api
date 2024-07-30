from sqlalchemyseeder import ResolvingSeeder
from src.config.database import SESSION_MAKER
# src.config.database import (SESSION_MAKER)
from .data import data

session = SESSION_MAKER()
seeder = ResolvingSeeder(session)

new_entities = seeder.load_entities_from_data_dict(data)

session.commit()
