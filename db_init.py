from app import create_app, db

app = create_app()

with app.app_context():
    try:
        db.create_all()
        print("Database tables created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the tables: {e}")
