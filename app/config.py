from dotenv import load_dotenv

load_dotenv()

DB_HOST = "localhost"
DB_PORT = "5432"
DB_PASSWORD = "test"
DB_USER = "test"
DB_NAME = "test"

DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@postgres:{DB_PORT}/{DB_NAME}"
