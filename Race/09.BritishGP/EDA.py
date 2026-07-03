import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


AUS = pd.read_csv('Race/09.BritishGP/Data/AustraliaGP.csv')
CHI = pd.read_csv('Race/09.BritishGP/Data/ChinaGP.csv')
JAP = pd.read_csv('Race/09.BritishGP/Data/JapanGP.csv')
MIA  = pd.read_csv('Race/09.BritishGP/Data/MiamiGP.csv')
CAN = pd.read_csv('Race/09.BritishGP/Data/CanadaGP.csv')
MON = pd.read_csv('Race/09.BritishGP/Data/MonacoGP.csv')
BAR = pd.read_csv('Race/09.BritishGP/Data/BarcelonaGP.csv')
AUA = pd.read_csv('Race/09.BritishGP/Data/AustriaGP.csv')

TRA = pd.concat([AUS,CHI,JAP,MIA,CAN,MON,BAR,AUA],axis=0)

TRA.dropna(subset=['Qualifying_Time(s)','Race_Result'],inplace=True)
TRA['FP1_BestTime(s)'].fillna(TRA['FP1_BestTime(s)'].median(),inplace=True)
TRA['FP2_BestTime(s)'].fillna(TRA['FP2_BestTime(s)'].median(),inplace=True)
TRA['FP3_BestTime(s)'].fillna(TRA['FP3_BestTime(s)'].median(),inplace=True)
TRA['Sector1Time(s)'].fillna(TRA['Sector1Time(s)'].median(),inplace=True)
TRA['Sector2Time(s)'].fillna(TRA['Sector2Time(s)'].median(),inplace=True)
TRA['Sector3Time(s)'].fillna(TRA['Sector3Time(s)'].median(),inplace=True)
TRA['Average_Laptime(s)'].fillna(TRA['Average_Laptime(s)'].mean(),inplace=True)
TRA['AveragePointsFromLast3Races'].fillna(0,inplace=True)


plt.figure(figsize=(10,8))
sns.heatmap(TRA.iloc[:,2:].corr(method='spearman'), cmap='turbo')

plt.title('Correlation Between Features (Spearman)', fontsize=22, fontweight='bold',pad=20)
plt.savefig('Race/09.BritishGP/Plots/Correlation_Heatmap.png', dpi=300, bbox_inches='tight')


corr = TRA.iloc[:,2:].corr(method='spearman')[['Race_Result']]
plt.figure(figsize=(10,8))
plt.title('Correlation of Features with Race Result (Spearman)', fontsize=22, fontweight='bold',pad=20)
sns.heatmap(corr, annot=True, cmap='turbo')
plt.savefig('Race/09.BritishGP/Plots/Feature_RaceResult_Correlation.png', dpi=300, bbox_inches='tight')




AUS.dropna(subset=['Qualifying_Time(s)','Race_Result'],inplace=True)
AUS['FP1_BestTime(s)'].fillna(AUS['FP1_BestTime(s)'].median(),inplace=True)
AUS['FP2_BestTime(s)'].fillna(AUS['FP2_BestTime(s)'].median(),inplace=True)
AUS['FP3_BestTime(s)'].fillna(AUS['FP3_BestTime(s)'].median(),inplace=True)
AUS['Sector1Time(s)'].fillna(AUS['Sector1Time(s)'].median(),inplace=True)
AUS['Sector2Time(s)'].fillna(AUS['Sector2Time(s)'].median(),inplace=True)
AUS['Sector3Time(s)'].fillna(AUS['Sector3Time(s)'].median(),inplace=True)
AUS['Average_Laptime(s)'].fillna(AUS['Average_Laptime(s)'].mean(),inplace=True)
AUS['AveragePointsFromLast3Races'].fillna(0,inplace=True)

print("Data Cleaning Done")

AUS=AUS.sort_values('FP1_BestTime(s)', ascending=True).reset_index(drop=True)
AUS['FP1_Rank'] = AUS.index+1
AUS=AUS.sort_values('FP2_BestTime(s)', ascending=True).reset_index(drop=True)
AUS['FP2_Rank'] = AUS.index+1
AUS=AUS.sort_values('FP3_BestTime(s)', ascending=True).reset_index(drop=True)
AUS['FP3_Rank'] = AUS.index+1

AUS['FP1_DeltaToFastest'] = AUS['FP1_BestTime(s)'] - AUS['FP1_BestTime(s)'].min()
AUS['FP2_DeltaToFastest'] = AUS['FP2_BestTime(s)'] - AUS['FP2_BestTime(s)'].min()
AUS['FP3_DeltaToFastest'] = AUS['FP3_BestTime(s)'] - AUS['FP3_BestTime(s)'].min()

AUS=AUS.sort_values('Sector1Time(s)', ascending=True).reset_index(drop=True)
AUS['Sector1_Rank'] = AUS.index+1
AUS=AUS.sort_values('Sector2Time(s)', ascending=True).reset_index(drop=True)
AUS['Sector2_Rank'] = AUS.index+1
AUS=AUS.sort_values('Sector3Time(s)', ascending=True).reset_index(drop=True)
AUS['Sector3_Rank'] = AUS.index+1

AUS['CombinedSectorTime'] = AUS['Sector1Time(s)']+AUS['Sector2Time(s)']+AUS['Sector3Time(s)']
AUS['CombinedSectorDelta'] = AUS['CombinedSectorTime']-AUS['CombinedSectorTime'].min()

AUS=AUS.sort_values('Average_Laptime(s)', ascending=True).reset_index(drop=True)
AUS['LapTime_Rank'] = AUS.index+1

AUS['DeltaToFastestLap'] = AUS['Average_Laptime(s)'] - AUS['Average_Laptime(s)'].min()

AUS['StartXConst'] = AUS['Starting_Pos']*AUS['ConstructorPoints']
AUS['DriXConst'] = AUS['DriverPoints']*AUS['ConstructorPoints']
AUS['FP3XStart'] = AUS['FP3_Rank']*AUS['Starting_Pos']


AUS = AUS.sort_values('Driver', ascending=True).reset_index(drop=True)


CHI.dropna(subset=['Qualifying_Time(s)','Race_Result'],inplace=True)
CHI['FP1_BestTime(s)'].fillna(CHI['FP1_BestTime(s)'].median(),inplace=True)
CHI['FP2_BestTime(s)'].fillna(CHI['FP2_BestTime(s)'].median(),inplace=True)
CHI['FP3_BestTime(s)'].fillna(CHI['FP3_BestTime(s)'].median(),inplace=True)
CHI['Sector1Time(s)'].fillna(CHI['Sector1Time(s)'].median(),inplace=True)
CHI['Sector2Time(s)'].fillna(CHI['Sector2Time(s)'].median(),inplace=True)
CHI['Sector3Time(s)'].fillna(CHI['Sector3Time(s)'].median(),inplace=True)
CHI['Average_Laptime(s)'].fillna(CHI['Average_Laptime(s)'].mean(),inplace=True)
CHI['AveragePointsFromLast3Races'].fillna(0,inplace=True)

print("Data Cleaning Done")

CHI=CHI.sort_values('FP1_BestTime(s)', ascending=True).reset_index(drop=True)
CHI['FP1_Rank'] = CHI.index+1
CHI=CHI.sort_values('FP2_BestTime(s)', ascending=True).reset_index(drop=True)
CHI['FP2_Rank'] = CHI.index+1
CHI=CHI.sort_values('FP3_BestTime(s)', ascending=True).reset_index(drop=True)
CHI['FP3_Rank'] = CHI.index+1

CHI['FP1_DeltaToFastest'] = CHI['FP1_BestTime(s)'] - CHI['FP1_BestTime(s)'].min()
CHI['FP2_DeltaToFastest'] = CHI['FP2_BestTime(s)'] - CHI['FP2_BestTime(s)'].min()
CHI['FP3_DeltaToFastest'] = CHI['FP3_BestTime(s)'] - CHI['FP3_BestTime(s)'].min()

CHI=CHI.sort_values('Sector1Time(s)', ascending=True).reset_index(drop=True)
CHI['Sector1_Rank'] = CHI.index+1
CHI=CHI.sort_values('Sector2Time(s)', ascending=True).reset_index(drop=True)
CHI['Sector2_Rank'] = CHI.index+1
CHI=CHI.sort_values('Sector3Time(s)', ascending=True).reset_index(drop=True)
CHI['Sector3_Rank'] = CHI.index+1

CHI['CombinedSectorTime'] = CHI['Sector1Time(s)']+CHI['Sector2Time(s)']+CHI['Sector3Time(s)']
CHI['CombinedSectorDelta'] = CHI['CombinedSectorTime']-CHI['CombinedSectorTime'].min()

CHI=CHI.sort_values('Average_Laptime(s)', ascending=True).reset_index(drop=True)
CHI['LapTime_Rank'] = CHI.index+1

CHI['DeltaToFastestLap'] = CHI['Average_Laptime(s)'] - CHI['Average_Laptime(s)'].min()

CHI['StartXConst'] = CHI['Starting_Pos']*CHI['ConstructorPoints']
CHI['DriXConst'] = CHI['DriverPoints']*CHI['ConstructorPoints']
CHI['FP3XStart'] = CHI['FP3_Rank']*CHI['Starting_Pos']


CHI = CHI.sort_values('Driver', ascending=True).reset_index(drop=True)


JAP.dropna(subset=['Qualifying_Time(s)','Race_Result'],inplace=True)
JAP['FP1_BestTime(s)'].fillna(JAP['FP1_BestTime(s)'].median(),inplace=True)
JAP['FP2_BestTime(s)'].fillna(JAP['FP2_BestTime(s)'].median(),inplace=True)
JAP['FP3_BestTime(s)'].fillna(JAP['FP3_BestTime(s)'].median(),inplace=True)
JAP['Sector1Time(s)'].fillna(JAP['Sector1Time(s)'].median(),inplace=True)
JAP['Sector2Time(s)'].fillna(JAP['Sector2Time(s)'].median(),inplace=True)
JAP['Sector3Time(s)'].fillna(JAP['Sector3Time(s)'].median(),inplace=True)
JAP['Average_Laptime(s)'].fillna(JAP['Average_Laptime(s)'].mean(),inplace=True)
JAP['AveragePointsFromLast3Races'].fillna(0,inplace=True)

print("Data Cleaning Done")

JAP=JAP.sort_values('FP1_BestTime(s)', ascending=True).reset_index(drop=True)
JAP['FP1_Rank'] = JAP.index+1
JAP=JAP.sort_values('FP2_BestTime(s)', ascending=True).reset_index(drop=True)
JAP['FP2_Rank'] = JAP.index+1
JAP=JAP.sort_values('FP3_BestTime(s)', ascending=True).reset_index(drop=True)
JAP['FP3_Rank'] = JAP.index+1

JAP['FP1_DeltaToFastest'] = JAP['FP1_BestTime(s)'] - JAP['FP1_BestTime(s)'].min()
JAP['FP2_DeltaToFastest'] = JAP['FP2_BestTime(s)'] - JAP['FP2_BestTime(s)'].min()
JAP['FP3_DeltaToFastest'] = JAP['FP3_BestTime(s)'] - JAP['FP3_BestTime(s)'].min()

JAP=JAP.sort_values('Sector1Time(s)', ascending=True).reset_index(drop=True)
JAP['Sector1_Rank'] = JAP.index+1
JAP=JAP.sort_values('Sector2Time(s)', ascending=True).reset_index(drop=True)
JAP['Sector2_Rank'] = JAP.index+1
JAP=JAP.sort_values('Sector3Time(s)', ascending=True).reset_index(drop=True)
JAP['Sector3_Rank'] = JAP.index+1

JAP['CombinedSectorTime'] = JAP['Sector1Time(s)']+JAP['Sector2Time(s)']+JAP['Sector3Time(s)']
JAP['CombinedSectorDelta'] = JAP['CombinedSectorTime']-JAP['CombinedSectorTime'].min()

JAP=JAP.sort_values('Average_Laptime(s)', ascending=True).reset_index(drop=True)
JAP['LapTime_Rank'] = JAP.index+1

JAP['DeltaToFastestLap'] = JAP['Average_Laptime(s)'] - JAP['Average_Laptime(s)'].min()

JAP['StartXConst'] = JAP['Starting_Pos']*JAP['ConstructorPoints']
JAP['DriXConst'] = JAP['DriverPoints']*JAP['ConstructorPoints']
JAP['FP3XStart'] = JAP['FP3_Rank']*JAP['Starting_Pos']


JAP = JAP.sort_values('Driver', ascending=True).reset_index(drop=True)



MIA.dropna(subset=['Qualifying_Time(s)','Race_Result'],inplace=True)
MIA['FP1_BestTime(s)'].fillna(MIA['FP1_BestTime(s)'].median(),inplace=True)
MIA['FP2_BestTime(s)'].fillna(MIA['FP2_BestTime(s)'].median(),inplace=True)
MIA['FP3_BestTime(s)'].fillna(MIA['FP3_BestTime(s)'].median(),inplace=True)
MIA['Sector1Time(s)'].fillna(MIA['Sector1Time(s)'].median(),inplace=True)
MIA['Sector2Time(s)'].fillna(MIA['Sector2Time(s)'].median(),inplace=True)
MIA['Sector3Time(s)'].fillna(MIA['Sector3Time(s)'].median(),inplace=True)
MIA['Average_Laptime(s)'].fillna(MIA['Average_Laptime(s)'].mean(),inplace=True)
MIA['AveragePointsFromLast3Races'].fillna(0,inplace=True)

print("Data Cleaning Done")

MIA=MIA.sort_values('FP1_BestTime(s)', ascending=True).reset_index(drop=True)
MIA['FP1_Rank'] = MIA.index+1
MIA=MIA.sort_values('FP2_BestTime(s)', ascending=True).reset_index(drop=True)
MIA['FP2_Rank'] = MIA.index+1
MIA=MIA.sort_values('FP3_BestTime(s)', ascending=True).reset_index(drop=True)
MIA['FP3_Rank'] = MIA.index+1

MIA['FP1_DeltaToFastest'] = MIA['FP1_BestTime(s)'] - MIA['FP1_BestTime(s)'].min()
MIA['FP2_DeltaToFastest'] = MIA['FP2_BestTime(s)'] - MIA['FP2_BestTime(s)'].min()
MIA['FP3_DeltaToFastest'] = MIA['FP3_BestTime(s)'] - MIA['FP3_BestTime(s)'].min()

MIA=MIA.sort_values('Sector1Time(s)', ascending=True).reset_index(drop=True)
MIA['Sector1_Rank'] = MIA.index+1
MIA=MIA.sort_values('Sector2Time(s)', ascending=True).reset_index(drop=True)
MIA['Sector2_Rank'] = MIA.index+1
MIA=MIA.sort_values('Sector3Time(s)', ascending=True).reset_index(drop=True)
MIA['Sector3_Rank'] = MIA.index+1

MIA['CombinedSectorTime'] = MIA['Sector1Time(s)']+MIA['Sector2Time(s)']+MIA['Sector3Time(s)']
MIA['CombinedSectorDelta'] = MIA['CombinedSectorTime']-MIA['CombinedSectorTime'].min()

MIA=MIA.sort_values('Average_Laptime(s)', ascending=True).reset_index(drop=True)
MIA['LapTime_Rank'] = MIA.index+1

MIA['DeltaToFastestLap'] = MIA['Average_Laptime(s)'] - MIA['Average_Laptime(s)'].min()

MIA['StartXConst'] = MIA['Starting_Pos']*MIA['ConstructorPoints']
MIA['DriXConst'] = MIA['DriverPoints']*MIA['ConstructorPoints']
MIA['FP3XStart'] = MIA['FP3_Rank']*MIA['Starting_Pos']


MIA = MIA.sort_values('Driver', ascending=True).reset_index(drop=True)



MIA.dropna(subset=['Qualifying_Time(s)','Race_Result'],inplace=True)
MIA['FP1_BestTime(s)'].fillna(MIA['FP1_BestTime(s)'].median(),inplace=True)
MIA['FP2_BestTime(s)'].fillna(MIA['FP2_BestTime(s)'].median(),inplace=True)
MIA['FP3_BestTime(s)'].fillna(MIA['FP3_BestTime(s)'].median(),inplace=True)
MIA['Sector1Time(s)'].fillna(MIA['Sector1Time(s)'].median(),inplace=True)
MIA['Sector2Time(s)'].fillna(MIA['Sector2Time(s)'].median(),inplace=True)
MIA['Sector3Time(s)'].fillna(MIA['Sector3Time(s)'].median(),inplace=True)
MIA['Average_Laptime(s)'].fillna(MIA['Average_Laptime(s)'].mean(),inplace=True)
MIA['AveragePointsFromLast3Races'].fillna(0,inplace=True)

print("Data Cleaning Done")

MIA=MIA.sort_values('FP1_BestTime(s)', ascending=True).reset_index(drop=True)
MIA['FP1_Rank'] = MIA.index+1
MIA=MIA.sort_values('FP2_BestTime(s)', ascending=True).reset_index(drop=True)
MIA['FP2_Rank'] = MIA.index+1
MIA=MIA.sort_values('FP3_BestTime(s)', ascending=True).reset_index(drop=True)
MIA['FP3_Rank'] = MIA.index+1

MIA['FP1_DeltaToFastest'] = MIA['FP1_BestTime(s)'] - MIA['FP1_BestTime(s)'].min()
MIA['FP2_DeltaToFastest'] = MIA['FP2_BestTime(s)'] - MIA['FP2_BestTime(s)'].min()
MIA['FP3_DeltaToFastest'] = MIA['FP3_BestTime(s)'] - MIA['FP3_BestTime(s)'].min()

MIA=MIA.sort_values('Sector1Time(s)', ascending=True).reset_index(drop=True)
MIA['Sector1_Rank'] = MIA.index+1
MIA=MIA.sort_values('Sector2Time(s)', ascending=True).reset_index(drop=True)
MIA['Sector2_Rank'] = MIA.index+1
MIA=MIA.sort_values('Sector3Time(s)', ascending=True).reset_index(drop=True)
MIA['Sector3_Rank'] = MIA.index+1

MIA['CombinedSectorTime'] = MIA['Sector1Time(s)']+MIA['Sector2Time(s)']+MIA['Sector3Time(s)']
MIA['CombinedSectorDelta'] = MIA['CombinedSectorTime']-MIA['CombinedSectorTime'].min()

MIA=MIA.sort_values('Average_Laptime(s)', ascending=True).reset_index(drop=True)
MIA['LapTime_Rank'] = MIA.index+1

MIA['DeltaToFastestLap'] = MIA['Average_Laptime(s)'] - MIA['Average_Laptime(s)'].min()

MIA['StartXConst'] = MIA['Starting_Pos']*MIA['ConstructorPoints']
MIA['DriXConst'] = MIA['DriverPoints']*MIA['ConstructorPoints']
MIA['FP3XStart'] = MIA['FP3_Rank']*MIA['Starting_Pos']


MIA = MIA.sort_values('Driver', ascending=True).reset_index(drop=True)



CAN.dropna(subset=['Qualifying_Time(s)','Race_Result'],inplace=True)
CAN['FP1_BestTime(s)'].fillna(CAN['FP1_BestTime(s)'].median(),inplace=True)
CAN['FP2_BestTime(s)'].fillna(CAN['FP2_BestTime(s)'].median(),inplace=True)
CAN['FP3_BestTime(s)'].fillna(CAN['FP3_BestTime(s)'].median(),inplace=True)
CAN['Sector1Time(s)'].fillna(CAN['Sector1Time(s)'].median(),inplace=True)
CAN['Sector2Time(s)'].fillna(CAN['Sector2Time(s)'].median(),inplace=True)
CAN['Sector3Time(s)'].fillna(CAN['Sector3Time(s)'].median(),inplace=True)
CAN['Average_Laptime(s)'].fillna(CAN['Average_Laptime(s)'].mean(),inplace=True)
CAN['AveragePointsFromLast3Races'].fillna(0,inplace=True)

print("Data Cleaning Done")

CAN=CAN.sort_values('FP1_BestTime(s)', ascending=True).reset_index(drop=True)
CAN['FP1_Rank'] = CAN.index+1
CAN=CAN.sort_values('FP2_BestTime(s)', ascending=True).reset_index(drop=True)
CAN['FP2_Rank'] = CAN.index+1
CAN=CAN.sort_values('FP3_BestTime(s)', ascending=True).reset_index(drop=True)
CAN['FP3_Rank'] = CAN.index+1

CAN['FP1_DeltaToFastest'] = CAN['FP1_BestTime(s)'] - CAN['FP1_BestTime(s)'].min()
CAN['FP2_DeltaToFastest'] = CAN['FP2_BestTime(s)'] - CAN['FP2_BestTime(s)'].min()
CAN['FP3_DeltaToFastest'] = CAN['FP3_BestTime(s)'] - CAN['FP3_BestTime(s)'].min()

CAN=CAN.sort_values('Sector1Time(s)', ascending=True).reset_index(drop=True)
CAN['Sector1_Rank'] = CAN.index+1
CAN=CAN.sort_values('Sector2Time(s)', ascending=True).reset_index(drop=True)
CAN['Sector2_Rank'] = CAN.index+1
CAN=CAN.sort_values('Sector3Time(s)', ascending=True).reset_index(drop=True)
CAN['Sector3_Rank'] = CAN.index+1

CAN['CombinedSectorTime'] = CAN['Sector1Time(s)']+CAN['Sector2Time(s)']+CAN['Sector3Time(s)']
CAN['CombinedSectorDelta'] = CAN['CombinedSectorTime']-CAN['CombinedSectorTime'].min()

CAN=CAN.sort_values('Average_Laptime(s)', ascending=True).reset_index(drop=True)
CAN['LapTime_Rank'] = CAN.index+1

CAN['DeltaToFastestLap'] = CAN['Average_Laptime(s)'] - CAN['Average_Laptime(s)'].min()

CAN['StartXConst'] = CAN['Starting_Pos']*CAN['ConstructorPoints']
CAN['DriXConst'] = CAN['DriverPoints']*CAN['ConstructorPoints']
CAN['FP3XStart'] = CAN['FP3_Rank']*CAN['Starting_Pos']


CAN = CAN.sort_values('Driver', ascending=True).reset_index(drop=True)



MON.dropna(subset=['Qualifying_Time(s)','Race_Result'],inplace=True)
MON['FP1_BestTime(s)'].fillna(MON['FP1_BestTime(s)'].median(),inplace=True)
MON['FP2_BestTime(s)'].fillna(MON['FP2_BestTime(s)'].median(),inplace=True)
MON['FP3_BestTime(s)'].fillna(MON['FP3_BestTime(s)'].median(),inplace=True)
MON['Sector1Time(s)'].fillna(MON['Sector1Time(s)'].median(),inplace=True)
MON['Sector2Time(s)'].fillna(MON['Sector2Time(s)'].median(),inplace=True)
MON['Sector3Time(s)'].fillna(MON['Sector3Time(s)'].median(),inplace=True)
MON['Average_Laptime(s)'].fillna(MON['Average_Laptime(s)'].mean(),inplace=True)
MON['AveragePointsFromLast3Races'].fillna(0,inplace=True)

print("Data Cleaning Done")

MON=MON.sort_values('FP1_BestTime(s)', ascending=True).reset_index(drop=True)
MON['FP1_Rank'] = MON.index+1
MON=MON.sort_values('FP2_BestTime(s)', ascending=True).reset_index(drop=True)
MON['FP2_Rank'] = MON.index+1
MON=MON.sort_values('FP3_BestTime(s)', ascending=True).reset_index(drop=True)
MON['FP3_Rank'] = MON.index+1

MON['FP1_DeltaToFastest'] = MON['FP1_BestTime(s)'] - MON['FP1_BestTime(s)'].min()
MON['FP2_DeltaToFastest'] = MON['FP2_BestTime(s)'] - MON['FP2_BestTime(s)'].min()
MON['FP3_DeltaToFastest'] = MON['FP3_BestTime(s)'] - MON['FP3_BestTime(s)'].min()

MON=MON.sort_values('Sector1Time(s)', ascending=True).reset_index(drop=True)
MON['Sector1_Rank'] = MON.index+1
MON=MON.sort_values('Sector2Time(s)', ascending=True).reset_index(drop=True)
MON['Sector2_Rank'] = MON.index+1
MON=MON.sort_values('Sector3Time(s)', ascending=True).reset_index(drop=True)
MON['Sector3_Rank'] = MON.index+1

MON['CombinedSectorTime'] = MON['Sector1Time(s)']+MON['Sector2Time(s)']+MON['Sector3Time(s)']
MON['CombinedSectorDelta'] = MON['CombinedSectorTime']-MON['CombinedSectorTime'].min()

MON=MON.sort_values('Average_Laptime(s)', ascending=True).reset_index(drop=True)
MON['LapTime_Rank'] = MON.index+1

MON['DeltaToFastestLap'] = MON['Average_Laptime(s)'] - MON['Average_Laptime(s)'].min()

MON['StartXConst'] = MON['Starting_Pos']*MON['ConstructorPoints']
MON['DriXConst'] = MON['DriverPoints']*MON['ConstructorPoints']
MON['FP3XStart'] = MON['FP3_Rank']*MON['Starting_Pos']


MON = MON.sort_values('Driver', ascending=True).reset_index(drop=True)



BAR.dropna(subset=['Qualifying_Time(s)','Race_Result'],inplace=True)
BAR['FP1_BestTime(s)'].fillna(BAR['FP1_BestTime(s)'].median(),inplace=True)
BAR['FP2_BestTime(s)'].fillna(BAR['FP2_BestTime(s)'].median(),inplace=True)
BAR['FP3_BestTime(s)'].fillna(BAR['FP3_BestTime(s)'].median(),inplace=True)
BAR['Sector1Time(s)'].fillna(BAR['Sector1Time(s)'].median(),inplace=True)
BAR['Sector2Time(s)'].fillna(BAR['Sector2Time(s)'].median(),inplace=True)
BAR['Sector3Time(s)'].fillna(BAR['Sector3Time(s)'].median(),inplace=True)
BAR['Average_Laptime(s)'].fillna(BAR['Average_Laptime(s)'].mean(),inplace=True)
BAR['AveragePointsFromLast3Races'].fillna(0,inplace=True)

print("Data Cleaning Done")

BAR=BAR.sort_values('FP1_BestTime(s)', ascending=True).reset_index(drop=True)
BAR['FP1_Rank'] = BAR.index+1
BAR=BAR.sort_values('FP2_BestTime(s)', ascending=True).reset_index(drop=True)
BAR['FP2_Rank'] = BAR.index+1
BAR=BAR.sort_values('FP3_BestTime(s)', ascending=True).reset_index(drop=True)
BAR['FP3_Rank'] = BAR.index+1

BAR['FP1_DeltaToFastest'] = BAR['FP1_BestTime(s)'] - BAR['FP1_BestTime(s)'].min()
BAR['FP2_DeltaToFastest'] = BAR['FP2_BestTime(s)'] - BAR['FP2_BestTime(s)'].min()
BAR['FP3_DeltaToFastest'] = BAR['FP3_BestTime(s)'] - BAR['FP3_BestTime(s)'].min()

BAR=BAR.sort_values('Sector1Time(s)', ascending=True).reset_index(drop=True)
BAR['Sector1_Rank'] = BAR.index+1
BAR=BAR.sort_values('Sector2Time(s)', ascending=True).reset_index(drop=True)
BAR['Sector2_Rank'] = BAR.index+1
BAR=BAR.sort_values('Sector3Time(s)', ascending=True).reset_index(drop=True)
BAR['Sector3_Rank'] = BAR.index+1

BAR['CombinedSectorTime'] = BAR['Sector1Time(s)']+BAR['Sector2Time(s)']+BAR['Sector3Time(s)']
BAR['CombinedSectorDelta'] = BAR['CombinedSectorTime']-BAR['CombinedSectorTime'].min()

BAR=BAR.sort_values('Average_Laptime(s)', ascending=True).reset_index(drop=True)
BAR['LapTime_Rank'] = BAR.index+1

BAR['DeltaToFastestLap'] = BAR['Average_Laptime(s)'] - BAR['Average_Laptime(s)'].min()

BAR['StartXConst'] = BAR['Starting_Pos']*BAR['ConstructorPoints']
BAR['DriXConst'] = BAR['DriverPoints']*BAR['ConstructorPoints']
BAR['FP3XStart'] = BAR['FP3_Rank']*BAR['Starting_Pos']


BAR = BAR.sort_values('Driver', ascending=True).reset_index(drop=True)



AUA.dropna(subset=['Qualifying_Time(s)','Race_Result'],inplace=True)
AUA['FP1_BestTime(s)'].fillna(AUA['FP1_BestTime(s)'].median(),inplace=True)
AUA['FP2_BestTime(s)'].fillna(AUA['FP2_BestTime(s)'].median(),inplace=True)
AUA['FP3_BestTime(s)'].fillna(AUA['FP3_BestTime(s)'].median(),inplace=True)
AUA['Sector1Time(s)'].fillna(AUA['Sector1Time(s)'].median(),inplace=True)
AUA['Sector2Time(s)'].fillna(AUA['Sector2Time(s)'].median(),inplace=True)
AUA['Sector3Time(s)'].fillna(AUA['Sector3Time(s)'].median(),inplace=True)
AUA['Average_Laptime(s)'].fillna(AUA['Average_Laptime(s)'].mean(),inplace=True)
AUA['AveragePointsFromLast3Races'].fillna(0,inplace=True)

print("Data Cleaning Done")

AUA=AUA.sort_values('FP1_BestTime(s)', ascending=True).reset_index(drop=True)
AUA['FP1_Rank'] = AUA.index+1
AUA=AUA.sort_values('FP2_BestTime(s)', ascending=True).reset_index(drop=True)
AUA['FP2_Rank'] = AUA.index+1
AUA=AUA.sort_values('FP3_BestTime(s)', ascending=True).reset_index(drop=True)
AUA['FP3_Rank'] = AUA.index+1

AUA['FP1_DeltaToFastest'] = AUA['FP1_BestTime(s)'] - AUA['FP1_BestTime(s)'].min()
AUA['FP2_DeltaToFastest'] = AUA['FP2_BestTime(s)'] - AUA['FP2_BestTime(s)'].min()
AUA['FP3_DeltaToFastest'] = AUA['FP3_BestTime(s)'] - AUA['FP3_BestTime(s)'].min()

AUA=AUA.sort_values('Sector1Time(s)', ascending=True).reset_index(drop=True)
AUA['Sector1_Rank'] = AUA.index+1
AUA=AUA.sort_values('Sector2Time(s)', ascending=True).reset_index(drop=True)
AUA['Sector2_Rank'] = AUA.index+1
AUA=AUA.sort_values('Sector3Time(s)', ascending=True).reset_index(drop=True)
AUA['Sector3_Rank'] = AUA.index+1

AUA['CombinedSectorTime'] = AUA['Sector1Time(s)']+AUA['Sector2Time(s)']+AUA['Sector3Time(s)']
AUA['CombinedSectorDelta'] = AUA['CombinedSectorTime']-AUA['CombinedSectorTime'].min()

AUA=AUA.sort_values('Average_Laptime(s)', ascending=True).reset_index(drop=True)
AUA['LapTime_Rank'] = AUA.index+1

AUA['DeltaToFastestLap'] = AUA['Average_Laptime(s)'] - AUA['Average_Laptime(s)'].min()

AUA['StartXConst'] = AUA['Starting_Pos']*AUA['ConstructorPoints']
AUA['DriXConst'] = AUA['DriverPoints']*AUA['ConstructorPoints']
AUA['FP3XStart'] = AUA['FP3_Rank']*AUA['Starting_Pos']


AUA = AUA.sort_values('Driver', ascending=True).reset_index(drop=True)


TRA = pd.concat([AUS,CHI,JAP,MIA,CAN,MON,BAR,AUA],axis=0)


plt.figure(figsize=(10,8))
sns.heatmap(TRA.iloc[:,2:].corr(method='spearman'), cmap='turbo')

plt.title('Correlation Between Features After Feature Engineering (Spearman)', fontsize=22, fontweight='bold',pad=20)
plt.savefig('Race/09.BritishGP/Plots/Correlation_Heatmap_After_Feature_Engineering.png', dpi=300, bbox_inches='tight')

corr = TRA.iloc[:,2:].corr(method='spearman')[['Race_Result']]
plt.figure(figsize=(10,8))
plt.title('Correlation of Features with Race Result After Feature Engineering (Spearman)', fontsize=22, fontweight='bold',pad=20)
sns.heatmap(corr, annot=True, cmap='turbo')
plt.savefig('Race/09.BritishGP/Plots/Feature_RaceResult_Correlation_After_Feature_Engineering.png', dpi=300, bbox_inches='tight')


TRA.to_csv("Race/09.BritishGP/Data/TrainingData.csv",index=False)

