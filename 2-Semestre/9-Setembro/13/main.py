from database import SessionLocal
from models import User

db = SessionLocal()
users = db.query(User)

for USER in users:
  print(f'id: {USER.CD_USER}')
  print(f'id: {USER.NM_USER}')