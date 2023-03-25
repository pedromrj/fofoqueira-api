from src.database.mongo import db

class BazarService:
    def __init__(self) -> None:
        pass

    def getBazar(self):
        bazares = []
        for bazar in db.bazar.find():
            bazar['_id'] = str(bazar['_id'])
            bazares.append(bazar)
        
        return bazares
