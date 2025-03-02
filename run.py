import os
from config import config_dict
from app import create_app
from dotenv import load_dotenv

print("Running the App...")
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, '.env'))

get_config_mode = os.getenv("CONFIG_MODE")
print(f"CONFIG_MODE: {get_config_mode}")
app_config = config_dict[get_config_mode]
app = create_app(app_config) 

# ----------------------------------------------- #

# Applications Routes
# from app.accounts import urls
# from .items import urls

# ----------------------------------------------- #

if __name__ == "__main__":
    # To Run the Server in Terminal => flask run -h localhost -p 5000
    # To Run the Server with Automatic Restart When Changes Occurred => FLASK_DEBUG=1 flask run -h localhost -p 5000
    
    app.run()