from sqlalchemy import Column, Integer, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Subskill(Base):
    __tablename__ = 'subskills'
    id = Column(Integer, primary_key=True)
    ability_id = Column(Integer, ForeignKey('abilities.id'), nullable=False)
    name = Column(Text, nullable=False)
    description = Column(Text)
    created_at = Column(TIMESTAMP, server_default='now()')

    ability = relationship("Ability", back_populates="subskills")