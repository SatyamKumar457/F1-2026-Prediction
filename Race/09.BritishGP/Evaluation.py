import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from scipy.stats import spearmanr



result = pd.read_csv("Race/09.BritishGP/Data/Result.csv")
PRE = pd.read_csv("Race/09.BritishGP/Data/PredictedData.csv")


PRE.set_index("Driver", inplace=True)
result.set_index("Driver", inplace=True)

Final = result.copy()
Final["Predicted_Pos"] = PRE["Predicted_Pos"]

PRE.reset_index(inplace=True)
Final.reset_index(inplace=True)
result.reset_index(inplace=True)



rho, p_value = spearmanr(Final['Position'],Final['Predicted_Pos'])
print(f"{rho}, {p_value}\n")


podium = Final.loc[:,["Driver"]]
print("\n Final Standing")
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

print(f"Spearman Rank (Final): {rho:.2f}")




PRE.set_index("Driver", inplace=True)
result.set_index("Driver", inplace=True)

df = PRE.copy()
df["Actual_Pos"] = result["Position"]


PRE.reset_index(inplace=True)
Final.reset_index(inplace=True,drop=True)

df.reset_index("Driver", inplace=True)



plt.figure(figsize=(10,8))
sns.heatmap(df.drop(columns=["Driver","Constructor"]).corr(method='spearman'), cmap='turbo')

plt.title('Correlation Between Features of the Actual Race Results (Spearman)', fontsize=22, fontweight='bold',pad=20)
plt.savefig('Race/09.BritishGP/Plots/Result_Correlation_Heatmap.png', dpi=300, bbox_inches='tight')







corr = df.drop(columns=["Driver","Constructor"]).corr(method='spearman')[['Actual_Pos']].sort_values(by='Actual_Pos', ascending=False)
plt.figure(figsize=(10,8))
plt.title('Correlation of Features with Race Result (Spearman)', fontsize=22, fontweight='bold',pad=20)
sns.heatmap(corr, annot=True, cmap='turbo')
plt.savefig('Race/09.BritishGP/Plots/Result_Feature_RaceResult_Correlation.png', dpi=300, bbox_inches='tight')





Final["Position_Diff"] = Final["Predicted_Pos"] - Final["Position"]

Final_sorted = Final.sort_values("Position_Diff")
print(Final)

plt.figure(figsize=(8,10))

sns.barplot(
    data=Final_sorted,
    y="Driver",
    x="Position_Diff"
)

plt.axvline(0, linestyle="--" )
plt.title("Position Difference by Driver")

plt.tight_layout()
plt.savefig('Race/09.BritishGP/Plots/Position_Difference_by_Driver.png', dpi=300, bbox_inches='tight')

