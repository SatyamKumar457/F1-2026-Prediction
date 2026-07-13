from pathlib import Path

dirs = [
    "Experiments/Race/Data/2018",
    "Experiments/Race/Data/2019",
    "Experiments/Race/Data/2020",
    "Experiments/Race/Data/2021",
    "Experiments/Race/Data/2022",
    "Experiments/Race/Data/2023",
    "Experiments/Race/Data/2024",
    "Experiments/Race/Data/2025"
]

file = "Experiments/Race/ETL.py"


for dir in dirs:
    Path(dir).mkdir(parents=True, exist_ok=True)

Path(file).touch(exist_ok=True)