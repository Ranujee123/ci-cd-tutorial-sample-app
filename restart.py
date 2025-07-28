from app import app, db

print("🚀 Starting Flask Application...")
try:
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
        print("✅ Database initialized")
    
    print("🌐 Starting server on http://127.0.0.1:5000")
    print("📍 Available endpoints: /, /menu, /dish")
    print("Press Ctrl+C to stop")
    
    # Run the application
    app.run(debug=True, host='127.0.0.1', port=5000)
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    input("Press Enter to exit...")
