import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from scipy.stats import spearmanr
from sklearn.metrics import make_scorer
import random
import joblib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.pipeline import Pipeline

File_Path = "Race/10.BelgianGP/"

TRA = pd.read_csv(f"{File_Path}Data/TrainingData.csv")

columns = [
       'AveragePositionFromLast3Races',
       'AveragePointsFromLast3Races', 'ConstructorAveragePointFromLast3Races',
       'FP1_BestTime(s)', 'FP2_BestTime(s)', 'FP3_BestTime(s)',
       'Qualifying_Time(s)', 'Starting_Pos',
       'DriverPoints', 'ConstructorPoints', 'FP1_Rank',
       'FP2_Rank', 'FP3_Rank', 'FP1_DeltaToFastest', 'FP2_DeltaToFastest',
       'FP3_DeltaToFastest','StartXConst', 'DriXConst', 'FP3XStart'
       ]

X = TRA[columns]

y = TRA['Race_Result']

X_train, X_test, y_train, y_test = train_test_split(X , y, test_size = 0.30, random_state = 23)



model = Pipeline([
    ("scaler", StandardScaler()),
    ("ridge", Ridge())
])


param_grid = {
    "ridge__alpha": [0.01, 0.1, 1, 10, 25, 50, 100, 250, 500, 1000, 5000, 10000],
    "ridge__fit_intercept": [True, False],
    "ridge__solver": ["auto", "svd", "cholesky", "lsqr"],
    "ridge__max_iter": [100, 200, 500, 1000],
    "ridge__positive": [True, False],
    "ridge__random_state": [42]
}

def spearman_rank(y_true, y_pred):
    if len(np.unique(y_true)) < 2 or len(np.unique(y_pred)) < 2:
        return 0.0
    return spearmanr(y_true, y_pred).statistic

spearman_scorer = make_scorer(spearman_rank, greater_is_better=True)


regcv = GridSearchCV(
    model,
    param_grid,
    cv=5,
    scoring=spearman_scorer
)

regcv.fit(X_train, y_train)

y_pred = regcv.predict(X_test)

print(regcv.best_params_)

corr, _ = spearmanr(y_pred, y_test)
print("Spearman Rank:", corr)


joblib.dump(regcv, f"{File_Path}Model/Ridge{corr:.2f}.pkl")


best_model = regcv.best_estimator_.named_steps["ridge"]

feature_importance = pd.Series(
    best_model.coef_,
    index=X.columns
)

feature_importance.sort_values(key=abs, ascending=False)
features = X.columns

plt.figure(figsize=(10,6))
plt.barh(features, feature_importance, color='skyblue')
plt.xlabel("Importance")
plt.title("Feature Importance After Feature Selection", fontsize=16, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig(f"{File_Path}Plots/Feature_importance.png", dpi=300, bbox_inches='tight')
