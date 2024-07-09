from sqlalchemy import Column, Integer, String, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class RamoAtividade(Base):
    __table_args__ = {"schema": "Crm"}
    __tablename__ = 'RamoAtividade'

    Id = Column(BigInteger, primary_key=True, autoincrement=True)
    Version = Column(Integer, nullable=False)
    Nome = Column(String(50), nullable=False)
    UltimaAlteracao = Column(DateTime, nullable=False)
    UltimoLogin = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<RamoAtividade(Id={self.Id}, Nome={self.Nome})>"