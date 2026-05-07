# 🏎️ F1 2026 Race Prediction

Machine Learning project that predicts Formula 1 race outcomes using historical race data, telemetry metrics, and team performance indicators.

This project uses data from previous seasons (primarily 2024–2025) to train a model that predicts race performance for the **2026 Formula 1 season**.

The goal is to explore how data science and machine learning can be applied to motorsport analytics.

---
## 📢 Race Predictions Updates

I will be posting the **predictions for every Formula 1 Grand Prix of the 2026 season on LinkedIn**.

Each post will include:
- 🏎️ Predicted race results
- 📊 Model predictions vs actual race results
- 📈 Accuracy analysis
- 🔧 Improvements made to the model during the season

Follow the updates here:

🔗 LinkedIn: https://www.linkedin.com/in/satyam-kumar-a01959326/

This project will evolve throughout the season as the model improves with more race data.

---

## 📊 Project Overview

The objective of this project is to explore:

- Whether **machine learning can predict Formula 1 race outcomes**
- How **driver pace, team performance, and qualifying results** influence race performance
- How **model performance changes when regulations or competitive order shift**

The project predicts race times for each driver, which are then used to determine the predicted race order and podium.

---

## ⚙️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- FastF1
- Matplotlib / Seaborn

---

## 📂 Project Structure
```
F1-2026-Prediction
|
├── Experiments
│ ├── DataExtraction.ipynb
| ├── DataExtractionV2.ipynb
│ ├── Prototype.ipynb
│
├── Race
│ ├── 01.AustraliaGP
|   ├── Data
│     ├── f1_dataset_progress_2019.csv
│     ├── f1_dataset_progress_2024.csv
│     ├── f1_dataset_progress_2025.csv
│     ├── f1_dataset_progress_2026copy.csv
|     ├── f1_dataset_progress_2026.csv 
│   ├──AustraliaGP.ipynb
│   
│ ├── 02.ChinaGP
│   ├── Data
│     ├── f1_dataset_progress_2019.csv
│     ├── f1_dataset_progress_2024.csv
│     ├── f1_dataset_progress_2025.csv
│     ├── f1_dataset_progress_2026.csv
│     ├── f1_dataset_progress_2026(2).csv
│   ├──ChinaGP.ipynb
|
│ ├── 03.JapanGP
│   ├──Data
│     ├──AustraliaGP.csv
│     ├──AustraliaGPModified.csv
│     ├──Japan_result.csv
│     ├──JapanGP.csv
│     ├──JapanGPModified.csv
│   ├──EDA&Feature.ipynb
│   ├──ETL.ipynb
│   ├──ModelTraining.ipynb
│
├── .gitignore
│ ├── # FastF1 cache
│     ├──f1_cache/
│     ├──*.sqlite
│     ├──*.pkl
│ ├── # Python
│     ├──__pycache__/
│     ├──*.pyc
│     ├──.venv/
│ ├── # OS
│     ├──.DS_Store
│
├── README.md
│
└── requirements.txt

```
---

## 📥 Data Sources

The project uses:

- **FastF1 API** for telemetry and session data
- Historical race results
- Lap time data
- Qualifying session data
- Driver and constructor information

---

## 1. Australia Grand Prix 2026 🇦🇺  
(https://github.com/SatyamKumar457/F1-2026-Prediction/tree/main/Race/01.AustraliaGP)
---

## 🧠 Features Used

The model currently uses the following features:

- Qualifying Time
- Clean Air Race Pace
- Team Performance Score
- Previous race performance indicators
- DNF / Non-participation indicators

These features aim to represent both driver pace and team competitiveness.

---

## 🤖 Model

The current model uses:

**XGBoost Regressor**

The model predicts:
PredictedRaceTime (seconds)


Drivers are then ranked based on predicted race time to estimate finishing order.

---

## 📈 Evaluation

Model performance is evaluated using:

- **MAE (Mean Absolute Error)**

Predictions are compared against real race results to measure accuracy.

---

| Driver | Predicted Position | Actual Position |
|------|------|------|
| RUS | 1 | 1 |
| PIA | 2 | DNF |
| NOR | 3 | 5 |

- **MAE (Based on 2025) :- 8.51(s)**
- **MAE (Based on 2026) :- 1047(s)**

This large error occurred because **Formula 1 introduced major regulation changes in 2026**, which drastically altered:

- Car design
- Team competitiveness
- Performance hierarchy

Because of this, historical race data (2023–2025) became much less reliable for predicting 2026 performance.
---
## 2. China Grand Prix 2026 🇨🇳  
(https://github.com/SatyamKumar457/F1-2026-Prediction/tree/main/Race/02.ChinaGP)
---

## 🧠 Features Used

The model currently uses the following features:

- FP 1/2/3 Best Time
- Sector 1/2/3 Time
- Average Lap Time
- Stint
- Tyre Data
- Qualifying Time

These features aim to represent both driver pace and team competitiveness.
---

## 🤖 Model

The current model uses:

**Random Forest Regressor**

The model predicts:
Final Standing


Drivers are then ranked based on Final Standing to estimate finishing order.

---

## 📈 Evaluation

Model performance is evaluated using:

- **Spearman Rank**

Predictions are compared against real race results to measure accuracy.

---

| Driver | Predicted Position | Actual Position |
|------|------|------|
| ANT | 1 | 1 |
| RUS | 2 | 2 |
| LEC | 3 | 4 |

- **Spearman Rank (Based on Australia 2026) :- 0.80**
- **MAE (Based on China 2026) :- 0.46**

---
## 🔧 Improvements

Future model improvements will include:

- Team Performance
- Weather Factor
- Current season team performance
- More ... 

The goal is simple: Imporve the Model after every race using new Data and Features.

---

## 3. Japanese Grand Prix 2026 🇯🇵  
(https://github.com/SatyamKumar457/F1-2026-Prediction/tree/main/Race/03.JapanGP)
---

## 🧠 Features Used

The model currently uses the following features:

- FP 1/2/3 Best Time
- Sector 1/2/3 Time
- Average Lap Time
- Stint
- Tyre Data
- Qualifying Time

These features aim to capture both driver pace and team performance under race conditions.
---

## 🤖 Model

The current model uses:

**Random Forest Regressor**

The model predicts:

➡️ Final Standing (continuous value)

Drivers are then ranked based on predicted values to estimate the final race order.

---

## 📈 Evaluation

Model performance is evaluated using:

- **Spearman Rank Correlation**

This measures how well the predicted order matches the actual finishing order.
---

| Driver | Predicted Position | Actual Position |
|------|------|------|
| ANT | 1 | 1 |
| HAM | 2 | 6 |
| NOR | 3 | 5 |

- **Spearman Rank (Japan GP 2026): 0.70**
- **Previous Race (China GP 2026): 0.461**

**📊 Improvement: ~51.8% increase in ranking correlation**

---
## 🔧 Improvements

Key improvements in this iteration:

- Better ETL (Extract, Transform, Load) pipeline
- Improved EDA (Exploratory Data Analysis)
- Cleaner and more consistent input features

These directly contributed to the performance jump.

---
## 🚀 Next Steps

Future model improvements will include:

- Team Performance Metrics
- Weather Factors
- Current Season Form
- More race-specific features

The goal is simple:
Improve the model after every race using new data and better features.
---
## 📊 Example Visualization

The project also includes visualizations comparing:

- Predicted vs Actual race results
- Feature importance
- Model performance

Example plots include:

- Feature importance graphs
- Predicted vs Actual finishing order
- Race pace distributions

---

---

## 4. Maimi Grand Prix 2026 🇯🇵  
(https://github.com/SatyamKumar457/F1-2026-Prediction/tree/main/Race/03.MiamiGP)
---

## 🧠 Features Used

The model currently uses the following features:

- FP 1/2/3 Best Time
- Average Lap Time
- Starting Position
- Qualifying Time

These features aim to capture both driver pace and team performance under race conditions.
---

## 🤖 Model

The current model uses:

**Rigde Regressor**

The model predicts:

➡️ Final Standing (continuous value)

Drivers are then ranked based on predicted values to estimate the final race order.

---

## 📈 Evaluation

Model performance is evaluated using:

- **Spearman Rank Correlation**

This measures how well the predicted order matches the actual finishing order.
---

| Driver | Predicted Position | Actual Position |
|------|------|------|
| ANT | 1 | 1 |
| VER | 2 | 5 |
| NOR | 3 | 2 |
| LEC | 4 | 8 |
| HAM | 5 | 6 |
| PIA | 6 | 3 |
| RUS | 7 | 4 |
| LAW | 8 | 20 |
| HAD | 9 | 22 |
| SAI | 10 | 9 |
| HUL | 11 | 19 |
| BEA | 12 | 11 |
| GAS | 13 | 21 |
| COL | 14 | 7 |
| OCO | 15 | 13 |
| ALB | 16 | 15|
| LIN | 17 | 14 |
| PER | 18 | 16 |
| STR | 19 | 17 |
| ALO | 20 | 15 |
| BOT | 21 | 18 |
| BOR | 22 | 12 |

- **Spearman Rank (Miami GP 2026): 0.60**
- **Previous Race (Japan GP 2026): 0.70**

**📊 Improvement: ~51.8% increase in ranking correlation**

---
## 🔧 Improvements

Key improvements in this iteration:

- Better EDA (Explorary Data Analysis)
- Feature Correlations
- Changed the Model

These directly contributed to the performance jump.

---
## 🚀 Next Steps

Future model improvements will include:

- More Features
- More Data
- More Hypertuning

The goal is simple:
Improve the model after every race using new data and better features.
---
## 📊 Example Visualization

The project also includes visualizations comparing:

- Predicted vs Actual race results
- Feature importance
- Model performance
- Correlations between Features
- Correlation between Race Results

Example plots include:

- Feature importance graphs
- Predicted vs Actual finishing order
- Correlation Heatmap
- Result Correlation Heatmap
- Result Features

---

## 🚀 How to Run

Clone the repository:

```bash
git clone https://github.com/SatyamKumar457/F1-2026-Prediction.git
cd F1-2026-Prediction 
```

Install dependencies:
```bash

pip install -r requirements.txt

```

## 📌 Future Improvements

Planned improvements:

- Add tyre strategy features
- Include weather conditions
- Improve feature engineering
- Add more seasons for training data
- Build a dashboard for race predictions

## 📜 License

This project is open source and available under the MIT License.

## 🙌 Contributions

Suggestions and improvements are welcome.
If you have ideas to improve the prediction model, feel free to open an issue or submit a pull request.