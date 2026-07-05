import pandas as pd



BRI = pd.read_csv("Race/09.BritishGP/Data/BritishGP.csv")



BRI.dropna(subset=['Qualifying_Time(s)'],inplace=True)
BRI['FP1_BestTime(s)'].fillna(BRI['FP1_BestTime(s)'].median(),inplace=True)
BRI['FP2_BestTime(s)'].fillna(BRI['FP2_BestTime(s)'].median(),inplace=True)
BRI['FP3_BestTime(s)'].fillna(BRI['FP3_BestTime(s)'].median(),inplace=True)
BRI['Sector1Time(s)'].fillna(BRI['Sector1Time(s)'].median(),inplace=True)
BRI['Sector2Time(s)'].fillna(BRI['Sector2Time(s)'].median(),inplace=True)
BRI['Sector3Time(s)'].fillna(BRI['Sector3Time(s)'].median(),inplace=True)
BRI['Average_Laptime(s)'].fillna(BRI['Average_Laptime(s)'].mean(),inplace=True)
BRI['AveragePointsFromLast3Races'].fillna(0,inplace=True)

print("Data Cleaning Done")

BRI=BRI.sort_values('FP1_BestTime(s)', ascending=True).reset_index(drop=True)
BRI['FP1_Rank'] = BRI.index+1
BRI=BRI.sort_values('FP2_BestTime(s)', ascending=True).reset_index(drop=True)
BRI['FP2_Rank'] = BRI.index+1
BRI=BRI.sort_values('FP3_BestTime(s)', ascending=True).reset_index(drop=True)
BRI['FP3_Rank'] = BRI.index+1

BRI['FP1_DeltaToFastest'] = BRI['FP1_BestTime(s)'] - BRI['FP1_BestTime(s)'].min()
BRI['FP2_DeltaToFastest'] = BRI['FP2_BestTime(s)'] - BRI['FP2_BestTime(s)'].min()
BRI['FP3_DeltaToFastest'] = BRI['FP3_BestTime(s)'] - BRI['FP3_BestTime(s)'].min()

BRI=BRI.sort_values('Sector1Time(s)', ascending=True).reset_index(drop=True)
BRI['Sector1_Rank'] = BRI.index+1
BRI=BRI.sort_values('Sector2Time(s)', ascending=True).reset_index(drop=True)
BRI['Sector2_Rank'] = BRI.index+1
BRI=BRI.sort_values('Sector3Time(s)', ascending=True).reset_index(drop=True)
BRI['Sector3_Rank'] = BRI.index+1

BRI['CombinedSectorTime'] = BRI['Sector1Time(s)']+BRI['Sector2Time(s)']+BRI['Sector3Time(s)']
BRI['CombinedSectorDelta'] = BRI['CombinedSectorTime']-BRI['CombinedSectorTime'].min()

BRI=BRI.sort_values('Average_Laptime(s)', ascending=True).reset_index(drop=True)
BRI['LapTime_Rank'] = BRI.index+1

BRI['DeltaToFastestLap'] = BRI['Average_Laptime(s)'] - BRI['Average_Laptime(s)'].min()

BRI['StartXConst'] = BRI['Starting_Pos']*BRI['ConstructorPoints']
BRI['DriXConst'] = BRI['DriverPoints']*BRI['ConstructorPoints']
BRI['FP3XStart'] = BRI['FP3_Rank']*BRI['Starting_Pos']


BRI = BRI.sort_values('Driver', ascending=True).reset_index(drop=True)

BRI.to_csv("Race/09.BritishGP/Data/PredictionData.csv", index=False)
print("Data Loaded.")