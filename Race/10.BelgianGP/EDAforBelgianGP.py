import pandas as pd

File_Path = "Race/10.BelgianGP/"

BEL = pd.read_csv(f"{File_Path}Data/BelgianGP.csv")



BEL.dropna(subset=['Qualifying_Time(s)'],inplace=True)
BEL['FP1_BestTime(s)'].fillna(BEL['FP1_BestTime(s)'].median(),inplace=True)
BEL['FP2_BestTime(s)'].fillna(BEL['FP2_BestTime(s)'].median(),inplace=True)
BEL['FP3_BestTime(s)'].fillna(BEL['FP3_BestTime(s)'].median(),inplace=True)
BEL['Sector1Time(s)'].fillna(BEL['Sector1Time(s)'].median(),inplace=True)
BEL['Sector2Time(s)'].fillna(BEL['Sector2Time(s)'].median(),inplace=True)
BEL['Sector3Time(s)'].fillna(BEL['Sector3Time(s)'].median(),inplace=True)
BEL['Average_Laptime(s)'].fillna(BEL['Average_Laptime(s)'].mean(),inplace=True)
BEL['AveragePointsFromLast3Races'].fillna(0,inplace=True)

print("Data Cleaning Done")

BEL=BEL.sort_values('FP1_BestTime(s)', ascending=True).reset_index(drop=True)
BEL['FP1_Rank'] = BEL.index+1
BEL=BEL.sort_values('FP2_BestTime(s)', ascending=True).reset_index(drop=True)
BEL['FP2_Rank'] = BEL.index+1
BEL=BEL.sort_values('FP3_BestTime(s)', ascending=True).reset_index(drop=True)
BEL['FP3_Rank'] = BEL.index+1

BEL['FP1_DeltaToFastest'] = BEL['FP1_BestTime(s)'] - BEL['FP1_BestTime(s)'].min()
BEL['FP2_DeltaToFastest'] = BEL['FP2_BestTime(s)'] - BEL['FP2_BestTime(s)'].min()
BEL['FP3_DeltaToFastest'] = BEL['FP3_BestTime(s)'] - BEL['FP3_BestTime(s)'].min()

BEL=BEL.sort_values('Sector1Time(s)', ascending=True).reset_index(drop=True)
BEL['Sector1_Rank'] = BEL.index+1
BEL=BEL.sort_values('Sector2Time(s)', ascending=True).reset_index(drop=True)
BEL['Sector2_Rank'] = BEL.index+1
BEL=BEL.sort_values('Sector3Time(s)', ascending=True).reset_index(drop=True)
BEL['Sector3_Rank'] = BEL.index+1

BEL['CombinedSectorTime'] = BEL['Sector1Time(s)']+BEL['Sector2Time(s)']+BEL['Sector3Time(s)']
BEL['CombinedSectorDelta'] = BEL['CombinedSectorTime']-BEL['CombinedSectorTime'].min()

BEL=BEL.sort_values('Average_Laptime(s)', ascending=True).reset_index(drop=True)
BEL['LapTime_Rank'] = BEL.index+1

BEL['DeltaToFastestLap'] = BEL['Average_Laptime(s)'] - BEL['Average_Laptime(s)'].min()

BEL['StartXConst'] = BEL['Starting_Pos']*BEL['ConstructorPoints']
BEL['DriXConst'] = BEL['DriverPoints']*BEL['ConstructorPoints']
BEL['FP3XStart'] = BEL['FP3_Rank']*BEL['Starting_Pos']


BEL = BEL.sort_values('Driver', ascending=True).reset_index(drop=True)

BEL.to_csv(f"{File_Path}Data/PredictionData.csv", index=False)
print("Data Loaded.")