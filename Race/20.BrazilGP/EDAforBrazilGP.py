import pandas as pd

File_Path = "Race/20.BrazilGP/"

BRA = pd.read_csv(f"{File_Path}Data/BrazilGP.csv")



BRA.dropna(subset=['Qualifying_Time(s)'],inplace=True)
BRA['FP1_BestTime(s)'].fillna(BRA['FP1_BestTime(s)'].median(),inplace=True)
BRA['FP2_BestTime(s)'].fillna(BRA['FP2_BestTime(s)'].median(),inplace=True)
BRA['FP3_BestTime(s)'].fillna(BRA['FP3_BestTime(s)'].median(),inplace=True)
BRA['Sector1Time(s)'].fillna(BRA['Sector1Time(s)'].median(),inplace=True)
BRA['Sector2Time(s)'].fillna(BRA['Sector2Time(s)'].median(),inplace=True)
BRA['Sector3Time(s)'].fillna(BRA['Sector3Time(s)'].median(),inplace=True)
BRA['Average_Laptime(s)'].fillna(BRA['Average_Laptime(s)'].mean(),inplace=True)
BRA['AveragePointsFromLast3Races'].fillna(0,inplace=True)

print("Data Cleaning Done")

BRA=BRA.sort_values('FP1_BestTime(s)', ascending=True).reset_index(drop=True)
BRA['FP1_Rank'] = BRA.index+1
BRA=BRA.sort_values('FP2_BestTime(s)', ascending=True).reset_index(drop=True)
BRA['FP2_Rank'] = BRA.index+1
BRA=BRA.sort_values('FP3_BestTime(s)', ascending=True).reset_index(drop=True)
BRA['FP3_Rank'] = BRA.index+1

BRA['FP1_DeltaToFastest'] = BRA['FP1_BestTime(s)'] - BRA['FP1_BestTime(s)'].min()
BRA['FP2_DeltaToFastest'] = BRA['FP2_BestTime(s)'] - BRA['FP2_BestTime(s)'].min()
BRA['FP3_DeltaToFastest'] = BRA['FP3_BestTime(s)'] - BRA['FP3_BestTime(s)'].min()

BRA=BRA.sort_values('Sector1Time(s)', ascending=True).reset_index(drop=True)
BRA['Sector1_Rank'] = BRA.index+1
BRA=BRA.sort_values('Sector2Time(s)', ascending=True).reset_index(drop=True)
BRA['Sector2_Rank'] = BRA.index+1
BRA=BRA.sort_values('Sector3Time(s)', ascending=True).reset_index(drop=True)
BRA['Sector3_Rank'] = BRA.index+1

BRA['CombinedSectorTime'] = BRA['Sector1Time(s)']+BRA['Sector2Time(s)']+BRA['Sector3Time(s)']
BRA['CombinedSectorDelta'] = BRA['CombinedSectorTime']-BRA['CombinedSectorTime'].min()

BRA=BRA.sort_values('Average_Laptime(s)', ascending=True).reset_index(drop=True)
BRA['LapTime_Rank'] = BRA.index+1

BRA['DeltaToFastestLap'] = BRA['Average_Laptime(s)'] - BRA['Average_Laptime(s)'].min()

BRA['StartXConst'] = BRA['Starting_Pos']*BRA['ConstructorPoints']
BRA['DriXConst'] = BRA['DriverPoints']*BRA['ConstructorPoints']
BRA['FP3XStart'] = BRA['FP3_Rank']*BRA['Starting_Pos']


BRA = BRA.sort_values('Driver', ascending=True).reset_index(drop=True)

BRA.to_csv(f"{File_Path}Data/PredictionData.csv", index=False)
print("Data Loaded.")