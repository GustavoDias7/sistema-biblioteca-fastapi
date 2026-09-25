from sqlalchemy import create_engine
from configs import DATABASE_URL

engine = create_engine(DATABASE_URL)