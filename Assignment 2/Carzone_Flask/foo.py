def db_add_one(item, db):
    try:
        db.session.add(item)
        db.session.commit()
        return None
    except:
        return 'There was an issue adding your car'