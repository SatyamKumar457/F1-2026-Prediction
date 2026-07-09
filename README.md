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
- Pickle

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
│   ├── AustraliaGP.ipynb
│   ├── Evaluation.ipynb
│   
│ ├── 02.ChinaGP
│   ├── Data
│     ├── f1_dataset_progress_2019.csv
│     ├── f1_dataset_progress_2024.csv
│     ├── f1_dataset_progress_2025.csv
│     ├── f1_dataset_progress_2026.csv
│     ├── f1_dataset_progress_2026(2).csv
│   ├── ChinaGP.ipynb
|
│ ├── 03.JapanGP
│   ├── Data
│     ├── AustraliaGP.csv
│     ├── AustraliaGPModified.csv
│     ├── Japan_result.csv
│     ├── JapanGP.csv
│     ├── JapanGPModified.csv
│   ├── EDA&Feature.ipynb
│   ├── ETL.ipynb
│   ├── ModelTraining.ipynb
|
│ ├── 04.MiamiGP
│   ├── Data
│     ├── AustraliaGP.csv
│     ├── ChinaGP.csv
│     ├── JapanGP.csv
│     ├── MiamiGP.csv
│     ├── Predicted_Results.csv
│     ├── Prediction_Data.csv
│     ├── Training_Data.csv
|   ├── Model
|     ├── RandomForestModel1.pkl
|   ├── Plots
|     ├── Correlation_Heatmap.png
|     ├── Feature_importance.png
|     ├── Feature_RaceResult_Correlation.png
|     ├── Result_Correlation_Heatmap.png
|     ├── Result_Feature_RaceResult_Correlation.png
│   ├── EDA.ipynb
│   ├── ETL.ipynb
|   ├── Evaluation.ipynb
│   ├── ModelTraining.ipynb
│
├── .gitignore
│ ├── # FastF1 cache
│     ├── f1_cache/
│     ├── *.sqlite
│     ├── *.pkl
│ ├── # Python
│     ├── __pycache__/
│     ├── *.pyc
│     ├── .venv/
│ ├── # OS
│     ├── .DS_Store
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

---

## 5. Canada Grand Prix 2026 🇨🇦  
(https://github.com/SatyamKumar457/F1-2026-Prediction/tree/main/Race/05.CanadaGP)
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

| Driver | Actual Position | Predicted Position |
|------|------|------|
| ANT | 1 | 2 |
| HAM | 2 | 5 |
| VER | 3 | 6 |
| LEC | 4 | 8 |
| HAD | 5 | 7 |
| COL | 6 | DNF |
| LAW | 7 | 10 |
| GAS | 8 | 12 |
| SAI | 9 | 14 |
| BEA | 10 | 15 |
| PIA | 11 | 4 |
| HUL | 12 | 13 |
| BOR | 13 | 11 |
| COL | 14 | 21 |
| STR | 15 | 18 |
| BOT | 16 | 20 |
| PER | 17 | 17 |
| NOR | 18 | 3 |
| RUS | 19 | 1 |
| ALO | 20 | 16 |
| ALB | 21 | 19 |
| LIN | 22 | 9 |

- **Spearman Rank (Canada GP 2026): 0.30**
- **Previous Race (Miami GP 2026): 0.60**

**📊 Improvement: ~ -50% increase in ranking correlation**

---
## 🔧 Improvements

Key improvements in this iteration:

- Built a better ETL pipeline.
- Feature Correlations.

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

See the Plots :- https://github.com/SatyamKumar457/F1-2026-Prediction/tree/main/Race/05.CanadaGP/Plots

---
---

## 4. Maimi Grand Prix 2026 🇯🇵  
(https://github.com/SatyamKumar457/F1-2026-Prediction/tree/main/Race/04.MiamiGP)
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

**📊 Improvement: ~-14.29% increase in ranking correlation**

---
## 🔧 Improvements

Key improvements in this iteration:

- Better EDA (Explorary Data Analysis)
- Feature Correlations

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

See the Plots :- https://github.com/SatyamKumar457/F1-2026-Prediction/tree/main/Race/04.MiamiGP/Plots

---
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
| PIA | 4 | 2 |
| RUS | 5 | 4 |
| LEC | 6 | 3 |
| COL | 7 | 16 |
| HAD | 8 | 12 |
| LAW | 9 | 9 |
| BOR | 10 | 13 |
| BEA | 11 | 22 |
| BOT | 12 | 19 |
| VER | 13 | 8 |
| GAS | 14 | 7 |
| SAI | 15 | 15 |
| OCO | 16 | 10 |
| HUL | 17 | 11 |
| STR | 18 | 21 |
| LIN | 19 | 14 |
| PER | 20 | 17 |
| ALB | 21 | 20 |

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
| GAS | 4 | 6 |
| HAD | 5 | 8 |
| COL | 6 | 10 |
| LAW | 7 | 7 |
| ALB | 8 | 22 |
| HAM | 9 | 3 |
| PIA | 10 | 19 |
| NOR | 11 | 20 |
| VER | 12 | 16 |
| HUL | 13 | 11 |
| OCO | 14 | 14 |
| LIN | 15 | 12 |
| BOR | 16 | 21 |
| ALO | 17 | 17 |
| BOT | 18 | 13 |
| STR | 19 | 18 |
| PER | 20 | 15 |
| BEA | 21 | 5 |
| SAI | 22 | 9 |

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
| ANT | 4 | 2 |
| HAD | 5 | DNF |
| LEC | 6 | 3 |
| HAM | 7 | 4 |
| VER | 8 | 6 |
| LIN | 9 | 13 |
| LAW | 10 | 9 |
| BOR | 11 | 12 |
| HUL | 12 | DNF |
| BEA | 13 | 10 |
| OCO | 14 | 8 |
| GAS | 15 | 11 |
| ALB | 16 | 7 |
| COL | 17 | 14 |
| ALO | 18 | DNF |
| PER | 19 | 16 |
| BOT | 20 | DNF |
| STR | 21 | 17 |
| SAI | 22 | 15 |

- **MAE (Based on 2025) :- 8.51(s)**
- **MAE (Based on 2026) :- 1047(s)**
- **Spearman Rank (Based on Australia 2026) :- 0.59**

This large error occurred because **Formula 1 introduced major regulation changes in 2026**, which drastically altered:

- Car design
- Team competitiveness
- Performance hierarchy

Because of this, historical race data (2023–2025) became much less reliable for predicting 2026 performance.
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