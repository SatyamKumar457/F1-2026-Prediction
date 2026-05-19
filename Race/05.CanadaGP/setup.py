import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Setting up for our specific GP context
gp_folder = "Race/05.CanadaGP"



list_of_files = [
    # Data Layer (DuckDB setup & ingestion)
    f"{gp_folder}/data/f1_predictions.db", 
    f"{gp_folder}/src/__init__.py",
    f"{gp_folder}/src/database/__init__.py",
    f"{gp_folder}/src/database/connection.py",
    f"{gp_folder}/src/database/ingest_history.py",
    
    # Feature Engineering Layer
    f"{gp_folder}/src/features/__init__.py",
    f"{gp_folder}/src/features/build_features.py",
    
    # ML Modeling Layer (Learning-to-Rank)
    f"{gp_folder}/src/models/__init__.py",
    f"{gp_folder}/src/models/train_ranker.py",
    f"{gp_folder}/src/models/predict_race.py",
    
    # Notebooks & Root Artifacts
    f"{gp_folder}/notebooks/exploratory_analysis.ipynb",
    f"{gp_folder}/requirements.txt",
    f"{gp_folder}/README.md"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directories if they don't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    # Create empty files if they don't exist or are empty (except for the .db binary file placeholders)
    if not os.path.exists(filepath) or (os.path.getsize(filepath) == 0):
        # We don't want to create an empty text file over our database binary format placeholder, 
        # DuckDB handles that itself, but creating the empty data folder structure is important.
        if filename.endswith(".db"):
            continue 
            
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")