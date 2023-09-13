from sqlalchemy import create_engine
from sqlalchemy.orm import declaraive_base, sessionmaker

# Isso aqui é a estruturada
# db_url = "driver://user:password@server/database"
engine = create_engine(db_url)

SessionLocal = sessionmaker(
  bind=engine,
  autoflush=False,
  autocommit=False
)