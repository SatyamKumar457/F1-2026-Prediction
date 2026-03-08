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

Example comparison:
---
## Australia Grand Prix 2026 🇦🇺

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

Because of this, **historical race data (2023–2025)** became much less reliable for predicting **2026 performance.**
---
## 🔧 Updated Approach

To adapt to the new regulations, the project will now focus more on **current-season performance indicators** rather than relying heavily on historical race data.

Future model improvements will include:

- Practice session pace
- Qualifying performance
- Current-season team strength
- Race weekend data

The goal is to make the model **adaptive to regulation changes and evolving team performance.**
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