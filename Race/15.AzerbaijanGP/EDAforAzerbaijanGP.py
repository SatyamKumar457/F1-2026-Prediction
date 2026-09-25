import pandas as pd

File_Path = "Race/15.AzerbaijanGP/"

AZE = pd.read_csv(f"{File_Path}Data/AzerbaijanGP.csv")



AZE.dropna(subset=['Qualifying_Time(s)'],inplace=True)
AZE['FP1_BestTime(s)'].fillna(AZE['FP1_BestTime(s)'].median(),inplace=True)
AZE['FP2_BestTime(s)'].fillna(AZE['FP2_BestTime(s)'].median(),inplace=True)
AZE['FP3_BestTime(s)'].fillna(AZE['FP3_BestTime(s)'].median(),inplace=True)
AZE['Sector1Time(s)'].fillna(AZE['Sector1Time(s)'].median(),inplace=True)
AZE['Sector2Time(s)'].fillna(AZE['Sector2Time(s)'].median(),inplace=True)
AZE['Sector3Time(s)'].fillna(AZE['Sector3Time(s)'].median(),inplace=True)
AZE['Average_Laptime(s)'].fillna(AZE['Average_Laptime(s)'].mean(),inplace=True)
AZE['AveragePointsFromLast3Races'].fillna(0,inplace=True)

print("Data Cleaning Done")

AZE=AZE.sort_values('FP1_BestTime(s)', ascending=True).reset_index(drop=True)
AZE['FP1_Rank'] = AZE.index+1
AZE=AZE.sort_values('FP2_BestTime(s)', ascending=True).reset_index(drop=True)
AZE['FP2_Rank'] = AZE.index+1
AZE=AZE.sort_values('FP3_BestTime(s)', ascending=True).reset_index(drop=True)
AZE['FP3_Rank'] = AZE.index+1

AZE['FP1_DeltaToFastest'] = AZE['FP1_BestTime(s)'] - AZE['FP1_BestTime(s)'].min()
AZE['FP2_DeltaToFastest'] = AZE['FP2_BestTime(s)'] - AZE['FP2_BestTime(s)'].min()
AZE['FP3_DeltaToFastest'] = AZE['FP3_BestTime(s)'] - AZE['FP3_BestTime(s)'].min()

AZE=AZE.sort_values('Sector1Time(s)', ascending=True).reset_index(drop=True)
AZE['Sector1_Rank'] = AZE.index+1
AZE=AZE.sort_values('Sector2Time(s)', ascending=True).reset_index(drop=True)
AZE['Sector2_Rank'] = AZE.index+1
AZE=AZE.sort_values('Sector3Time(s)', ascending=True).reset_index(drop=True)
AZE['Sector3_Rank'] = AZE.index+1

AZE['CombinedSectorTime'] = AZE['Sector1Time(s)']+AZE['Sector2Time(s)']+AZE['Sector3Time(s)']
AZE['CombinedSectorDelta'] = AZE['CombinedSectorTime']-AZE['CombinedSectorTime'].min()

AZE=AZE.sort_values('Average_Laptime(s)', ascending=True).reset_index(drop=True)
AZE['LapTime_Rank'] = AZE.index+1

AZE['DeltaToFastestLap'] = AZE['Average_Laptime(s)'] - AZE['Average_Laptime(s)'].min()

AZE['StartXConst'] = AZE['Starting_Pos']*AZE['ConstructorPoints']
AZE['DriXConst'] = AZE['DriverPoints']*AZE['ConstructorPoints']
AZE['FP3XStart'] = AZE['FP3_Rank']*AZE['Starting_Pos']


AZE = AZE.sort_values('Driver', ascending=True).reset_index(drop=True)

AZE.to_csv(f"{File_Path}Data/PredictionData.csv", index=False)
print("Data Loaded.")