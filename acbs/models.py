from acbs import Base
from sqlalchemy import Column, Integer, String


class Ocorrencia(Base):
    __tablename__ = "ocorrencias"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    month = Column(Integer)
    year = Column(Integer)
    qtd = Column(Integer)


class Produtividade(Base):
    __tablename__ = "produtividades"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    month = Column(Integer)
    year = Column(Integer)
    qtd = Column(Integer)
