import pandas as pd

File_Path = "Race/14.SpainGP/"

SPA = pd.read_csv(f"{File_Path}Data/SpainGP.csv")



SPA.dropna(subset=['Qualifying_Time(s)'],inplace=True)
SPA['FP1_BestTime(s)'].fillna(SPA['FP1_BestTime(s)'].median(),inplace=True)
SPA['FP2_BestTime(s)'].fillna(SPA['FP2_BestTime(s)'].median(),inplace=True)
SPA['FP3_BestTime(s)'].fillna(SPA['FP3_BestTime(s)'].median(),inplace=True)
SPA['Sector1Time(s)'].fillna(SPA['Sector1Time(s)'].median(),inplace=True)
SPA['Sector2Time(s)'].fillna(SPA['Sector2Time(s)'].median(),inplace=True)
SPA['Sector3Time(s)'].fillna(SPA['Sector3Time(s)'].median(),inplace=True)
SPA['Average_Laptime(s)'].fillna(SPA['Average_Laptime(s)'].mean(),inplace=True)
SPA['AveragePointsFromLast3Races'].fillna(0,inplace=True)

print("Data Cleaning Done")

SPA=SPA.sort_values('FP1_BestTime(s)', ascending=True).reset_index(drop=True)
SPA['FP1_Rank'] = SPA.index+1
SPA=SPA.sort_values('FP2_BestTime(s)', ascending=True).reset_index(drop=True)
SPA['FP2_Rank'] = SPA.index+1
SPA=SPA.sort_values('FP3_BestTime(s)', ascending=True).reset_index(drop=True)
SPA['FP3_Rank'] = SPA.index+1

SPA['FP1_DeltaToFastest'] = SPA['FP1_BestTime(s)'] - SPA['FP1_BestTime(s)'].min()
SPA['FP2_DeltaToFastest'] = SPA['FP2_BestTime(s)'] - SPA['FP2_BestTime(s)'].min()
SPA['FP3_DeltaToFastest'] = SPA['FP3_BestTime(s)'] - SPA['FP3_BestTime(s)'].min()

SPA=SPA.sort_values('Sector1Time(s)', ascending=True).reset_index(drop=True)
SPA['Sector1_Rank'] = SPA.index+1
SPA=SPA.sort_values('Sector2Time(s)', ascending=True).reset_index(drop=True)
SPA['Sector2_Rank'] = SPA.index+1
SPA=SPA.sort_values('Sector3Time(s)', ascending=True).reset_index(drop=True)
SPA['Sector3_Rank'] = SPA.index+1

SPA['CombinedSectorTime'] = SPA['Sector1Time(s)']+SPA['Sector2Time(s)']+SPA['Sector3Time(s)']
SPA['CombinedSectorDelta'] = SPA['CombinedSectorTime']-SPA['CombinedSectorTime'].min()

SPA=SPA.sort_values('Average_Laptime(s)', ascending=True).reset_index(drop=True)
SPA['LapTime_Rank'] = SPA.index+1

SPA['DeltaToFastestLap'] = SPA['Average_Laptime(s)'] - SPA['Average_Laptime(s)'].min()

SPA['StartXConst'] = SPA['Starting_Pos']*SPA['ConstructorPoints']
SPA['DriXConst'] = SPA['DriverPoints']*SPA['ConstructorPoints']
SPA['FP3XStart'] = SPA['FP3_Rank']*SPA['Starting_Pos']


SPA = SPA.sort_values('Driver', ascending=True).reset_index(drop=True)

SPA.to_csv(f"{File_Path}Data/PredictionData.csv", index=False)
print("Data Loaded.")