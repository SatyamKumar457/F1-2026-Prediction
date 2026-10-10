import pandas as pd

File_Path = "Race/17.SingaporeGP/"

SIN = pd.read_csv(f"{File_Path}Data/SingaporeGP.csv")



SIN.dropna(subset=['Qualifying_Time(s)'],inplace=True)
SIN['FP1_BestTime(s)'].fillna(SIN['FP1_BestTime(s)'].median(),inplace=True)
SIN['FP2_BestTime(s)'].fillna(SIN['FP2_BestTime(s)'].median(),inplace=True)
SIN['FP3_BestTime(s)'].fillna(SIN['FP3_BestTime(s)'].median(),inplace=True)
SIN['Sector1Time(s)'].fillna(SIN['Sector1Time(s)'].median(),inplace=True)
SIN['Sector2Time(s)'].fillna(SIN['Sector2Time(s)'].median(),inplace=True)
SIN['Sector3Time(s)'].fillna(SIN['Sector3Time(s)'].median(),inplace=True)
SIN['Average_Laptime(s)'].fillna(SIN['Average_Laptime(s)'].mean(),inplace=True)
SIN['AveragePointsFromLast3Races'].fillna(0,inplace=True)

print("Data Cleaning Done")

SIN=SIN.sort_values('FP1_BestTime(s)', ascending=True).reset_index(drop=True)
SIN['FP1_Rank'] = SIN.index+1
SIN=SIN.sort_values('FP2_BestTime(s)', ascending=True).reset_index(drop=True)
SIN['FP2_Rank'] = SIN.index+1
SIN=SIN.sort_values('FP3_BestTime(s)', ascending=True).reset_index(drop=True)
SIN['FP3_Rank'] = SIN.index+1

SIN['FP1_DeltaToFastest'] = SIN['FP1_BestTime(s)'] - SIN['FP1_BestTime(s)'].min()
SIN['FP2_DeltaToFastest'] = SIN['FP2_BestTime(s)'] - SIN['FP2_BestTime(s)'].min()
SIN['FP3_DeltaToFastest'] = SIN['FP3_BestTime(s)'] - SIN['FP3_BestTime(s)'].min()

SIN=SIN.sort_values('Sector1Time(s)', ascending=True).reset_index(drop=True)
SIN['Sector1_Rank'] = SIN.index+1
SIN=SIN.sort_values('Sector2Time(s)', ascending=True).reset_index(drop=True)
SIN['Sector2_Rank'] = SIN.index+1
SIN=SIN.sort_values('Sector3Time(s)', ascending=True).reset_index(drop=True)
SIN['Sector3_Rank'] = SIN.index+1

SIN['CombinedSectorTime'] = SIN['Sector1Time(s)']+SIN['Sector2Time(s)']+SIN['Sector3Time(s)']
SIN['CombinedSectorDelta'] = SIN['CombinedSectorTime']-SIN['CombinedSectorTime'].min()

SIN=SIN.sort_values('Average_Laptime(s)', ascending=True).reset_index(drop=True)
SIN['LapTime_Rank'] = SIN.index+1

SIN['DeltaToFastestLap'] = SIN['Average_Laptime(s)'] - SIN['Average_Laptime(s)'].min()

SIN['StartXConst'] = SIN['Starting_Pos']*SIN['ConstructorPoints']
SIN['DriXConst'] = SIN['DriverPoints']*SIN['ConstructorPoints']
SIN['FP3XStart'] = SIN['FP3_Rank']*SIN['Starting_Pos']


SIN = SIN.sort_values('Driver', ascending=True).reset_index(drop=True)

SIN.to_csv(f"{File_Path}Data/PredictionData.csv", index=False)
print("Data Loaded.")