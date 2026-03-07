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

Formula 1 race outcomes depend on multiple factors such as:

- Qualifying performance
- Driver Historical result
- Race pace
- Team performance
- Clean air performance

This project builds a machine learning model that learns relationships between these factors and **predicts the race result or race time for each driver**.

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
├── AustraliaGP.ipynb
│
├── Prototype.ipynb
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

## 🧠 Features Used

Key features used in the model include:

- `QualifyingTime`
- `CleanAirRacePace`
- `TeamPerformance`
- `Result of 2023,2024,2025`

Additional engineered features may include:

- Track performance indicators
- Historical pace trends
- Team performance index

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

Example comparison:

Australia Grand Prix 2026 🇦🇺

| Driver | Predicted Position | Actual Position |
|------|------|------|
| RUS | 1 | TBD |
| PIA | 2 | TBD |
| NOR | 3 | TBD |

- **MAE (Based on 2025) :- 8.51(s)**
- **MAE (Based on 2026) :- TBD(s)**

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