import pandas as pd
import joblib

PRE = pd.read_csv("Race/09.BritishGP/Data/PredictionData.csv")

model = joblib.load("Race/09.BritishGP/Model/Rodge0.63.pkl")

columns = [
       'AveragePointsFromLast3Races', 'ConstructorAveragePointFromLast3Races',
       'FP1_BestTime(s)', 'FP2_BestTime(s)', 'FP3_BestTime(s)','Qualifying_Time(s)', 
       'Starting_Pos', 'DriverPoints', 'ConstructorPoints', 'FP1_Rank',
       'FP2_Rank', 'FP3_Rank', 'FP1_DeltaToFastest', 'FP2_DeltaToFastest',
       'FP3_DeltaToFastest','StartXConst', 'DriXConst', 'FP3XStart'
       ]


corr = 0.63

X= PRE[columns]
y_pred = model.predict(X)

PRE["Predicted_Result"] = y_pred

PRE = PRE.sort_values(by="Predicted_Result", ascending=True)
PRE = PRE.reset_index(drop=True)
PRE["Predicted_Pos"] = PRE.index + 1

podium = PRE.loc[:,["Driver"]]
print("\n Predicted Standing")
print(f"🥇P1: {podium.iloc[0]['Driver']}")
print(f"🥈P2: {podium.iloc[1]['Driver']}")
print(f"🥉P3: {podium.iloc[2]['Driver']}")
print(f"P4: {podium.iloc[3]['Driver']}")
print(f"P5: {podium.iloc[4]['Driver']}")
print(f"P6: {podium.iloc[5]['Driver']}")
print(f"P7: {podium.iloc[6]['Driver']}")
print(f"P8: {podium.iloc[7]['Driver']}")
print(f"P9: {podium.iloc[8]['Driver']}")
print(f"P10: {podium.iloc[9]['Driver']}")
print(f"P11: {podium.iloc[10]['Driver']}")
print(f"P12: {podium.iloc[11]['Driver']}")
print(f"P13: {podium.iloc[12]['Driver']}")
print(f"P14: {podium.iloc[13]['Driver']}")
print(f"P15: {podium.iloc[14]['Driver']}")
print(f"P16: {podium.iloc[15]['Driver']}")
print(f"P17: {podium.iloc[16]['Driver']}")
print(f"P18: {podium.iloc[17]['Driver']}")
print(f"P19: {podium.iloc[18]['Driver']}")
print(f"P20: {podium.iloc[19]['Driver']}")
print(f"P21: {podium.iloc[20]['Driver']}")

print(f"Spearman Rank (Predicted): {corr:.2f}")


PRE.to_csv("Race/09.BritishGP/Data/PredictedData.csv",index=False)