import sys
from app import create_app
from app.extensions import db
from app.models import *

app = create_app()

# Check if "debug" or "init_db" is passed as a command-line argument
debug_mode = "debug" in sys.argv
init_db = "init_db" in sys.argv

if init_db:
    with app.app_context():
        db.create_all()

# Run the app with debug mode only if "debug" is in command-line arguments
app.run(debug=debug_mode, host="0.0.0.0", port=app.config.get("PORT"))
