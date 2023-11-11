from MindReaderAI import MindReader

import os
from dotenv import load_dotenv

load_dotenv()

db_path = os.environ["DB_PATH"]
email = os.environ["YAY_ACCOUNT_EMAIL"]
password = os.environ["YAY_ACCOUNT_PASSWORD"]
root_post_id = os.environ["ROOT_POST_ID"]

# Start MindReader AI
bot = MindReader(db_path, email, password)
bot.run(root_post_id)
