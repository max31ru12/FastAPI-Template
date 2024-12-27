from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

from app.config import CONVENTION


class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=CONVENTION)
