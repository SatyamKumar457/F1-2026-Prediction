import duckdb
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR/"data"/"f1_predictions.db"

def get_db_connection():
    try:
        conn = duckdb.connect(str(DB_PATH))
        return conn
    except Exception as e:
        print(f"Error connecting to DuckDB database at {DB_PATH}: {e}")
        raise e