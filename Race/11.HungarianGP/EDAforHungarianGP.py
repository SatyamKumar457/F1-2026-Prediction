import pandas as pd

File_Path = "Race/11.HungarianGP/"

HUN = pd.read_csv(f"{File_Path}Data/HungarianGP.csv")



HUN.dropna(subset=['Qualifying_Time(s)'],inplace=True)
HUN['FP1_BestTime(s)'].fillna(HUN['FP1_BestTime(s)'].median(),inplace=True)
HUN['FP2_BestTime(s)'].fillna(HUN['FP2_BestTime(s)'].median(),inplace=True)
HUN['FP3_BestTime(s)'].fillna(HUN['FP3_BestTime(s)'].median(),inplace=True)
HUN['Sector1Time(s)'].fillna(HUN['Sector1Time(s)'].median(),inplace=True)
HUN['Sector2Time(s)'].fillna(HUN['Sector2Time(s)'].median(),inplace=True)
HUN['Sector3Time(s)'].fillna(HUN['Sector3Time(s)'].median(),inplace=True)
HUN['Average_Laptime(s)'].fillna(HUN['Average_Laptime(s)'].mean(),inplace=True)
HUN['AveragePointsFromLast3Races'].fillna(0,inplace=True)

print("Data Cleaning Done")

HUN=HUN.sort_values('FP1_BestTime(s)', ascending=True).reset_index(drop=True)
HUN['FP1_Rank'] = HUN.index+1
HUN=HUN.sort_values('FP2_BestTime(s)', ascending=True).reset_index(drop=True)
HUN['FP2_Rank'] = HUN.index+1
HUN=HUN.sort_values('FP3_BestTime(s)', ascending=True).reset_index(drop=True)
HUN['FP3_Rank'] = HUN.index+1

HUN['FP1_DeltaToFastest'] = HUN['FP1_BestTime(s)'] - HUN['FP1_BestTime(s)'].min()
HUN['FP2_DeltaToFastest'] = HUN['FP2_BestTime(s)'] - HUN['FP2_BestTime(s)'].min()
HUN['FP3_DeltaToFastest'] = HUN['FP3_BestTime(s)'] - HUN['FP3_BestTime(s)'].min()

HUN=HUN.sort_values('Sector1Time(s)', ascending=True).reset_index(drop=True)
HUN['Sector1_Rank'] = HUN.index+1
HUN=HUN.sort_values('Sector2Time(s)', ascending=True).reset_index(drop=True)
HUN['Sector2_Rank'] = HUN.index+1
HUN=HUN.sort_values('Sector3Time(s)', ascending=True).reset_index(drop=True)
HUN['Sector3_Rank'] = HUN.index+1

HUN['CombinedSectorTime'] = HUN['Sector1Time(s)']+HUN['Sector2Time(s)']+HUN['Sector3Time(s)']
HUN['CombinedSectorDelta'] = HUN['CombinedSectorTime']-HUN['CombinedSectorTime'].min()

HUN=HUN.sort_values('Average_Laptime(s)', ascending=True).reset_index(drop=True)
HUN['LapTime_Rank'] = HUN.index+1

HUN['DeltaToFastestLap'] = HUN['Average_Laptime(s)'] - HUN['Average_Laptime(s)'].min()

HUN['StartXConst'] = HUN['Starting_Pos']*HUN['ConstructorPoints']
HUN['DriXConst'] = HUN['DriverPoints']*HUN['ConstructorPoints']
HUN['FP3XStart'] = HUN['FP3_Rank']*HUN['Starting_Pos']


HUN = HUN.sort_values('Driver', ascending=True).reset_index(drop=True)

HUN.to_csv(f"{File_Path}Data/PredictionData.csv", index=False)
print("Data Loaded.")