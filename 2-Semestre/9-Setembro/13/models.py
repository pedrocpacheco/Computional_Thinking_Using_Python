from database import Base
class User:
  __table__ = "T_AISB_USUARIO"
  CD_USUARIO = Column(Integer)
  NM_USUARIO = Column(String)