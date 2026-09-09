from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from modulos import Base
pass
engine = create_engine("sqlite:///jogos.db", echo=True)
Session = sessionmaker(bind = engine)

def criar_banco():
    Base.metadata.create_all(engine)