from pathlib import Path

Race = "Netherlands"

File_Path = f"Race/12.{Race}GP/"

dirs = [
    f"{File_Path}Data",
    f"{File_Path}Plots",
    f"{File_Path}Model",
]

files = [
    f"{File_Path}EDA.py",
    f"{File_Path}EDAfor{Race}GP.py",
    f"{File_Path}ETL.py",
    f"{File_Path}ETLfor{Race}GP.py",
    f"{File_Path}Evaluation.py",
    f"{File_Path}ModelTraining.py",
    f"{File_Path}Prediction.py",
    f"{File_Path}Result.py"
]


for dir in dirs:
    Path(dir).mkdir(parents=True, exist_ok=True)


for file in files:
    Path(file).touch(exist_ok=True)