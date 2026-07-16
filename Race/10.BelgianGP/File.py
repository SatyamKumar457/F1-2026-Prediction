from pathlib import Path

File_Path = "Race/10.BelgianGP/"

dirs = [
    f"{File_Path}Data",
    f"{File_Path}Plots",
    f"{File_Path}Model",
]

files = [
    f"{File_Path}EDA.py",
    f"{File_Path}EDAforBelgianGP.py",
    f"{File_Path}ETL.py",
    f"{File_Path}ETLforBelgianGP.py",
    f"{File_Path}Evaluation.py",
    f"{File_Path}ModelTraining.py",
    f"{File_Path}Prediction.py",
    f"{File_Path}Result.py"
]


for dir in dirs:
    Path(dir).mkdir(parents=True, exist_ok=True)


for file in files:
    Path(file).touch(exist_ok=True)