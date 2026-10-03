import pandas as pd

File_Path = "Race/16.BahrainGP/"

BAH = pd.read_csv(f"{File_Path}Data/BahrainGP.csv")



BAH.dropna(subset=['Qualifying_Time(s)'],inplace=True)
BAH['FP1_BestTime(s)'].fillna(BAH['FP1_BestTime(s)'].median(),inplace=True)
BAH['FP2_BestTime(s)'].fillna(BAH['FP2_BestTime(s)'].median(),inplace=True)
BAH['FP3_BestTime(s)'].fillna(BAH['FP3_BestTime(s)'].median(),inplace=True)
BAH['Sector1Time(s)'].fillna(BAH['Sector1Time(s)'].median(),inplace=True)
BAH['Sector2Time(s)'].fillna(BAH['Sector2Time(s)'].median(),inplace=True)
BAH['Sector3Time(s)'].fillna(BAH['Sector3Time(s)'].median(),inplace=True)
BAH['Average_Laptime(s)'].fillna(BAH['Average_Laptime(s)'].mean(),inplace=True)
BAH['AveragePointsFromLast3Races'].fillna(0,inplace=True)

print("Data Cleaning Done")

BAH=BAH.sort_values('FP1_BestTime(s)', ascending=True).reset_index(drop=True)
BAH['FP1_Rank'] = BAH.index+1
BAH=BAH.sort_values('FP2_BestTime(s)', ascending=True).reset_index(drop=True)
BAH['FP2_Rank'] = BAH.index+1
BAH=BAH.sort_values('FP3_BestTime(s)', ascending=True).reset_index(drop=True)
BAH['FP3_Rank'] = BAH.index+1

BAH['FP1_DeltaToFastest'] = BAH['FP1_BestTime(s)'] - BAH['FP1_BestTime(s)'].min()
BAH['FP2_DeltaToFastest'] = BAH['FP2_BestTime(s)'] - BAH['FP2_BestTime(s)'].min()
BAH['FP3_DeltaToFastest'] = BAH['FP3_BestTime(s)'] - BAH['FP3_BestTime(s)'].min()

BAH=BAH.sort_values('Sector1Time(s)', ascending=True).reset_index(drop=True)
BAH['Sector1_Rank'] = BAH.index+1
BAH=BAH.sort_values('Sector2Time(s)', ascending=True).reset_index(drop=True)
BAH['Sector2_Rank'] = BAH.index+1
BAH=BAH.sort_values('Sector3Time(s)', ascending=True).reset_index(drop=True)
BAH['Sector3_Rank'] = BAH.index+1

BAH['CombinedSectorTime'] = BAH['Sector1Time(s)']+BAH['Sector2Time(s)']+BAH['Sector3Time(s)']
BAH['CombinedSectorDelta'] = BAH['CombinedSectorTime']-BAH['CombinedSectorTime'].min()

BAH=BAH.sort_values('Average_Laptime(s)', ascending=True).reset_index(drop=True)
BAH['LapTime_Rank'] = BAH.index+1

BAH['DeltaToFastestLap'] = BAH['Average_Laptime(s)'] - BAH['Average_Laptime(s)'].min()

BAH['StartXConst'] = BAH['Starting_Pos']*BAH['ConstructorPoints']
BAH['DriXConst'] = BAH['DriverPoints']*BAH['ConstructorPoints']
BAH['FP3XStart'] = BAH['FP3_Rank']*BAH['Starting_Pos']


BAH = BAH.sort_values('Driver', ascending=True).reset_index(drop=True)

BAH.to_csv(f"{File_Path}Data/PredictionData.csv", index=False)
print("Data Loaded.")