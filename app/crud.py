from models.ability import Ability
from models.subskill import Subskill
from db import SessionLocal

def create_ability(name, description):
    db = SessionLocal()
    ability = Ability(name=name, description=description)
    db.add(ability)
    db.commit()
    db.refresh(ability)
    db.close()
    return ability

def create_subskill(ability_id, name, description):
    db = SessionLocal()
    subskill = Subskill(ability_id=ability_id, name=name, description=description)
    db.add(subskill)
    db.commit()
    db.refresh(subskill)
    db.close()
    return subskill