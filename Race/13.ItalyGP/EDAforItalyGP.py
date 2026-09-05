import pandas as pd

File_Path = "Race/13.ItalyGP/"

ITA = pd.read_csv(f"{File_Path}Data/ItalyGP.csv")



ITA.dropna(subset=['Qualifying_Time(s)'],inplace=True)
ITA['FP1_BestTime(s)'].fillna(ITA['FP1_BestTime(s)'].median(),inplace=True)
ITA['FP2_BestTime(s)'].fillna(ITA['FP2_BestTime(s)'].median(),inplace=True)
ITA['FP3_BestTime(s)'].fillna(ITA['FP3_BestTime(s)'].median(),inplace=True)
ITA['Sector1Time(s)'].fillna(ITA['Sector1Time(s)'].median(),inplace=True)
ITA['Sector2Time(s)'].fillna(ITA['Sector2Time(s)'].median(),inplace=True)
ITA['Sector3Time(s)'].fillna(ITA['Sector3Time(s)'].median(),inplace=True)
ITA['Average_Laptime(s)'].fillna(ITA['Average_Laptime(s)'].mean(),inplace=True)
ITA['AveragePointsFromLast3Races'].fillna(0,inplace=True)

print("Data Cleaning Done")

ITA=ITA.sort_values('FP1_BestTime(s)', ascending=True).reset_index(drop=True)
ITA['FP1_Rank'] = ITA.index+1
ITA=ITA.sort_values('FP2_BestTime(s)', ascending=True).reset_index(drop=True)
ITA['FP2_Rank'] = ITA.index+1
ITA=ITA.sort_values('FP3_BestTime(s)', ascending=True).reset_index(drop=True)
ITA['FP3_Rank'] = ITA.index+1

ITA['FP1_DeltaToFastest'] = ITA['FP1_BestTime(s)'] - ITA['FP1_BestTime(s)'].min()
ITA['FP2_DeltaToFastest'] = ITA['FP2_BestTime(s)'] - ITA['FP2_BestTime(s)'].min()
ITA['FP3_DeltaToFastest'] = ITA['FP3_BestTime(s)'] - ITA['FP3_BestTime(s)'].min()

ITA=ITA.sort_values('Sector1Time(s)', ascending=True).reset_index(drop=True)
ITA['Sector1_Rank'] = ITA.index+1
ITA=ITA.sort_values('Sector2Time(s)', ascending=True).reset_index(drop=True)
ITA['Sector2_Rank'] = ITA.index+1
ITA=ITA.sort_values('Sector3Time(s)', ascending=True).reset_index(drop=True)
ITA['Sector3_Rank'] = ITA.index+1

ITA['CombinedSectorTime'] = ITA['Sector1Time(s)']+ITA['Sector2Time(s)']+ITA['Sector3Time(s)']
ITA['CombinedSectorDelta'] = ITA['CombinedSectorTime']-ITA['CombinedSectorTime'].min()

ITA=ITA.sort_values('Average_Laptime(s)', ascending=True).reset_index(drop=True)
ITA['LapTime_Rank'] = ITA.index+1

ITA['DeltaToFastestLap'] = ITA['Average_Laptime(s)'] - ITA['Average_Laptime(s)'].min()

ITA['StartXConst'] = ITA['Starting_Pos']*ITA['ConstructorPoints']
ITA['DriXConst'] = ITA['DriverPoints']*ITA['ConstructorPoints']
ITA['FP3XStart'] = ITA['FP3_Rank']*ITA['Starting_Pos']


ITA = ITA.sort_values('Driver', ascending=True).reset_index(drop=True)

ITA.to_csv(f"{File_Path}Data/PredictionData.csv", index=False)
print("Data Loaded.")