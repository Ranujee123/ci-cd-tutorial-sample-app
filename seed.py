from app import app, db
from app.models import Menu

class Seeder(object):
    def populate_database(self):
        with app.app_context():
            record = Menu.query.first()
            if not record:
                items = [
                    Menu(name="Baked potatoes"),
                    Menu(name="Grilled chicken"),
                    Menu(name="Caesar salad"),
                    Menu(name="Chocolate cake"),
                    Menu(name="Fish and chips")
                ]
                for item in items:
                    db.session.add(item)
                db.session.commit()
                print(f"Added {len(items)} menu items")
            else:
                print("Database already has menu items")

if __name__ == '__main__':
    print("Seeding...")
    seeder = Seeder()
    seeder.populate_database()
    print("Seeding complete.")
