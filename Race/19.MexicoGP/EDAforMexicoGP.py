import pandas as pd

File_Path = "Race/19.MexicoGP/"

MEX = pd.read_csv(f"{File_Path}Data/MexicoGP.csv")



MEX.dropna(subset=['Qualifying_Time(s)'],inplace=True)
MEX['FP1_BestTime(s)'].fillna(MEX['FP1_BestTime(s)'].median(),inplace=True)
MEX['FP2_BestTime(s)'].fillna(MEX['FP2_BestTime(s)'].median(),inplace=True)
MEX['FP3_BestTime(s)'].fillna(MEX['FP3_BestTime(s)'].median(),inplace=True)
MEX['Sector1Time(s)'].fillna(MEX['Sector1Time(s)'].median(),inplace=True)
MEX['Sector2Time(s)'].fillna(MEX['Sector2Time(s)'].median(),inplace=True)
MEX['Sector3Time(s)'].fillna(MEX['Sector3Time(s)'].median(),inplace=True)
MEX['Average_Laptime(s)'].fillna(MEX['Average_Laptime(s)'].mean(),inplace=True)
MEX['AveragePointsFromLast3Races'].fillna(0,inplace=True)

print("Data Cleaning Done")

MEX=MEX.sort_values('FP1_BestTime(s)', ascending=True).reset_index(drop=True)
MEX['FP1_Rank'] = MEX.index+1
MEX=MEX.sort_values('FP2_BestTime(s)', ascending=True).reset_index(drop=True)
MEX['FP2_Rank'] = MEX.index+1
MEX=MEX.sort_values('FP3_BestTime(s)', ascending=True).reset_index(drop=True)
MEX['FP3_Rank'] = MEX.index+1

MEX['FP1_DeltaToFastest'] = MEX['FP1_BestTime(s)'] - MEX['FP1_BestTime(s)'].min()
MEX['FP2_DeltaToFastest'] = MEX['FP2_BestTime(s)'] - MEX['FP2_BestTime(s)'].min()
MEX['FP3_DeltaToFastest'] = MEX['FP3_BestTime(s)'] - MEX['FP3_BestTime(s)'].min()

MEX=MEX.sort_values('Sector1Time(s)', ascending=True).reset_index(drop=True)
MEX['Sector1_Rank'] = MEX.index+1
MEX=MEX.sort_values('Sector2Time(s)', ascending=True).reset_index(drop=True)
MEX['Sector2_Rank'] = MEX.index+1
MEX=MEX.sort_values('Sector3Time(s)', ascending=True).reset_index(drop=True)
MEX['Sector3_Rank'] = MEX.index+1

MEX['CombinedSectorTime'] = MEX['Sector1Time(s)']+MEX['Sector2Time(s)']+MEX['Sector3Time(s)']
MEX['CombinedSectorDelta'] = MEX['CombinedSectorTime']-MEX['CombinedSectorTime'].min()

MEX=MEX.sort_values('Average_Laptime(s)', ascending=True).reset_index(drop=True)
MEX['LapTime_Rank'] = MEX.index+1

MEX['DeltaToFastestLap'] = MEX['Average_Laptime(s)'] - MEX['Average_Laptime(s)'].min()

MEX['StartXConst'] = MEX['Starting_Pos']*MEX['ConstructorPoints']
MEX['DriXConst'] = MEX['DriverPoints']*MEX['ConstructorPoints']
MEX['FP3XStart'] = MEX['FP3_Rank']*MEX['Starting_Pos']


MEX = MEX.sort_values('Driver', ascending=True).reset_index(drop=True)

MEX.to_csv(f"{File_Path}Data/PredictionData.csv", index=False)
print("Data Loaded.")