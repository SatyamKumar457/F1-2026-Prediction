import pandas as pd

File_Path = "Race/18.UnitedStatesGP/"

USA = pd.read_csv(f"{File_Path}Data/UnitedStatesGP.csv")



USA.dropna(subset=['Qualifying_Time(s)'],inplace=True)
USA['FP1_BestTime(s)'].fillna(USA['FP1_BestTime(s)'].median(),inplace=True)
USA['FP2_BestTime(s)'].fillna(USA['FP2_BestTime(s)'].median(),inplace=True)
USA['FP3_BestTime(s)'].fillna(USA['FP3_BestTime(s)'].median(),inplace=True)
USA['Sector1Time(s)'].fillna(USA['Sector1Time(s)'].median(),inplace=True)
USA['Sector2Time(s)'].fillna(USA['Sector2Time(s)'].median(),inplace=True)
USA['Sector3Time(s)'].fillna(USA['Sector3Time(s)'].median(),inplace=True)
USA['Average_Laptime(s)'].fillna(USA['Average_Laptime(s)'].mean(),inplace=True)
USA['AveragePointsFromLast3Races'].fillna(0,inplace=True)

print("Data Cleaning Done")

USA=USA.sort_values('FP1_BestTime(s)', ascending=True).reset_index(drop=True)
USA['FP1_Rank'] = USA.index+1
USA=USA.sort_values('FP2_BestTime(s)', ascending=True).reset_index(drop=True)
USA['FP2_Rank'] = USA.index+1
USA=USA.sort_values('FP3_BestTime(s)', ascending=True).reset_index(drop=True)
USA['FP3_Rank'] = USA.index+1

USA['FP1_DeltaToFastest'] = USA['FP1_BestTime(s)'] - USA['FP1_BestTime(s)'].min()
USA['FP2_DeltaToFastest'] = USA['FP2_BestTime(s)'] - USA['FP2_BestTime(s)'].min()
USA['FP3_DeltaToFastest'] = USA['FP3_BestTime(s)'] - USA['FP3_BestTime(s)'].min()

USA=USA.sort_values('Sector1Time(s)', ascending=True).reset_index(drop=True)
USA['Sector1_Rank'] = USA.index+1
USA=USA.sort_values('Sector2Time(s)', ascending=True).reset_index(drop=True)
USA['Sector2_Rank'] = USA.index+1
USA=USA.sort_values('Sector3Time(s)', ascending=True).reset_index(drop=True)
USA['Sector3_Rank'] = USA.index+1

USA['CombinedSectorTime'] = USA['Sector1Time(s)']+USA['Sector2Time(s)']+USA['Sector3Time(s)']
USA['CombinedSectorDelta'] = USA['CombinedSectorTime']-USA['CombinedSectorTime'].min()

USA=USA.sort_values('Average_Laptime(s)', ascending=True).reset_index(drop=True)
USA['LapTime_Rank'] = USA.index+1

USA['DeltaToFastestLap'] = USA['Average_Laptime(s)'] - USA['Average_Laptime(s)'].min()

USA['StartXConst'] = USA['Starting_Pos']*USA['ConstructorPoints']
USA['DriXConst'] = USA['DriverPoints']*USA['ConstructorPoints']
USA['FP3XStart'] = USA['FP3_Rank']*USA['Starting_Pos']


USA = USA.sort_values('Driver', ascending=True).reset_index(drop=True)

USA.to_csv(f"{File_Path}Data/PredictionData.csv", index=False)
print("Data Loaded.")