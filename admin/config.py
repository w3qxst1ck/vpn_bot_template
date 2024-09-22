import os
import dotenv

dotenv.load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN_ADMIN")
ADMINS = [str(user_id) for user_id in os.getenv("ADMINS").split(",")]