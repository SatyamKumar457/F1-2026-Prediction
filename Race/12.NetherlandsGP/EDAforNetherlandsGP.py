import pandas as pd

File_Path = "Race/12.NetherlandsGP/"

NET = pd.read_csv(f"{File_Path}Data/NetherlandsGP.csv")



NET.dropna(subset=['Qualifying_Time(s)'],inplace=True)
NET['FP1_BestTime(s)'].fillna(NET['FP1_BestTime(s)'].median(),inplace=True)
NET['FP2_BestTime(s)'].fillna(NET['FP2_BestTime(s)'].median(),inplace=True)
NET['FP3_BestTime(s)'].fillna(NET['FP3_BestTime(s)'].median(),inplace=True)
NET['Sector1Time(s)'].fillna(NET['Sector1Time(s)'].median(),inplace=True)
NET['Sector2Time(s)'].fillna(NET['Sector2Time(s)'].median(),inplace=True)
NET['Sector3Time(s)'].fillna(NET['Sector3Time(s)'].median(),inplace=True)
NET['Average_Laptime(s)'].fillna(NET['Average_Laptime(s)'].mean(),inplace=True)
NET['AveragePointsFromLast3Races'].fillna(0,inplace=True)

print("Data Cleaning Done")

NET=NET.sort_values('FP1_BestTime(s)', ascending=True).reset_index(drop=True)
NET['FP1_Rank'] = NET.index+1
NET=NET.sort_values('FP2_BestTime(s)', ascending=True).reset_index(drop=True)
NET['FP2_Rank'] = NET.index+1
NET=NET.sort_values('FP3_BestTime(s)', ascending=True).reset_index(drop=True)
NET['FP3_Rank'] = NET.index+1

NET['FP1_DeltaToFastest'] = NET['FP1_BestTime(s)'] - NET['FP1_BestTime(s)'].min()
NET['FP2_DeltaToFastest'] = NET['FP2_BestTime(s)'] - NET['FP2_BestTime(s)'].min()
NET['FP3_DeltaToFastest'] = NET['FP3_BestTime(s)'] - NET['FP3_BestTime(s)'].min()

NET=NET.sort_values('Sector1Time(s)', ascending=True).reset_index(drop=True)
NET['Sector1_Rank'] = NET.index+1
NET=NET.sort_values('Sector2Time(s)', ascending=True).reset_index(drop=True)
NET['Sector2_Rank'] = NET.index+1
NET=NET.sort_values('Sector3Time(s)', ascending=True).reset_index(drop=True)
NET['Sector3_Rank'] = NET.index+1

NET['CombinedSectorTime'] = NET['Sector1Time(s)']+NET['Sector2Time(s)']+NET['Sector3Time(s)']
NET['CombinedSectorDelta'] = NET['CombinedSectorTime']-NET['CombinedSectorTime'].min()

NET=NET.sort_values('Average_Laptime(s)', ascending=True).reset_index(drop=True)
NET['LapTime_Rank'] = NET.index+1

NET['DeltaToFastestLap'] = NET['Average_Laptime(s)'] - NET['Average_Laptime(s)'].min()

NET['StartXConst'] = NET['Starting_Pos']*NET['ConstructorPoints']
NET['DriXConst'] = NET['DriverPoints']*NET['ConstructorPoints']
NET['FP3XStart'] = NET['FP3_Rank']*NET['Starting_Pos']


NET = NET.sort_values('Driver', ascending=True).reset_index(drop=True)

NET.to_csv(f"{File_Path}Data/PredictionData.csv", index=False)
print("Data Loaded.")