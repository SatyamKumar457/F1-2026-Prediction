import pandas as pd
import numpy as np
import fastf1
import requests

def get_fp1_best(FP1):

    laps = FP1.laps.pick_quicklaps()

    best = laps.groupby("Driver")["LapTime"].min().dt.total_seconds().reset_index()

    return best

def get_fp2_best(FP2):

    laps = FP2.laps.pick_quicklaps()

    best = laps.groupby("Driver")["LapTime"].min().dt.total_seconds().reset_index()

    return best

def get_fp3_best(FP3):

    laps = FP3.laps.pick_quicklaps()

    best = laps.groupby("Driver")["LapTime"].min().dt.total_seconds().reset_index()

    return best

def get_sector_times (FP2):

    laps = FP2.laps

    sector_times = laps.groupby("Driver")[[
    "Sector1Time",
    "Sector2Time",
    "Sector3Time"
    ]].mean().apply(lambda x: x.dt.total_seconds()).reset_index()

    return sector_times

def get_average_laptime (FP2):

    laps = FP2.laps

    avg_lap = laps.groupby("Driver")["LapTime"].mean().dt.total_seconds().reset_index()

    return avg_lap

def get_qualifying_data(Qualify):

    results = Qualify.results.copy()

    qual_time = results[["Q3", "Q2", "Q1"]].bfill(axis=1).iloc[:, 0]

    qual = results[["Abbreviation"]].copy()
    qual["Qualifying_Time(s)"] = qual_time.dt.total_seconds()

    qual.rename(columns={"Abbreviation": "Driver"}, inplace=True)

    return qual

def get_starting_position(Qualify):

    quali_results = Qualify.results[['Abbreviation', 'Position']]
    quali_results.rename(columns={"Abbreviation":"Driver"},inplace=True)

    return quali_results

def get_race_results(Result):

    race = Result.results[["Abbreviation","Position"]]
    race.rename(columns={"Abbreviation":"Driver"},inplace=True)

    return race

# For Normal Races

races = ["Australia", "Japan"]
season = 2026

for race in races:
    FP1 = fastf1.get_session(season, race, 'FP1')
    FP1.load()
    FP2 = fastf1.get_session(season, race, 'FP2')
    FP2.load()
    FP3 = fastf1.get_session(season, race, 'FP3')
    FP3.load()

    Qualify = fastf1.get_session(season, race, 'Q')
    Qualify.load()

    Result = fastf1.get_session(season, race, 'R')
    Result.load()

    print(f"Done Loading Season {season} & Race {race}")

    fp1_best = get_fp1_best(FP1)
    fp2_best = get_fp2_best(FP2)
    fp3_best = get_fp3_best(FP3)
    sector_time_best = get_sector_times(FP2)
    average_laptime = get_average_laptime(FP2)
    stint = get_stint(FP2)
    tyre = get_tyre_compound(FP2)
    qualifying_time = get_qualifying_data(Qualify)
    starting_position = get_starting_position(Qualify)
    result = get_race_results(Result)

    print("Data Extraction Done.")

    fp1_best.set_index("Driver",inplace=True)
    fp2_best.set_index("Driver",inplace=True)
    fp3_best.set_index("Driver",inplace=True)
    sector_time_best.set_index("Driver",inplace=True)
    average_laptime.set_index("Driver",inplace=True)
    stint.set_index("Driver",inplace=True)
    tyre.set_index("Driver",inplace=True)
    qualifying_time.set_index("Driver",inplace=True)
    starting_position.set_index("Driver",inplace=True)
    result.set_index("Driver",inplace=True)

    print("Setting Index Done.")

    df = fp1_best.copy()
    df.rename(columns={"LapTime":"FP1_BestTime(s)"},inplace=True)
    df[["FP2_BestTime(s)"]] = fp2_best[["LapTime"]]
    df[["FP3_BestTime(s)"]] = fp3_best[["LapTime"]]
    df[["Sector1Time(s)","Sector2Time(s)","Sector3Time(s)"]] = sector_time_best[["Sector1Time","Sector2Time","Sector3Time"]]
    df[["Average_Laptime(s)"]] = average_laptime[["LapTime"]]
    df[["Longest_Stint"]] = stint[["LongestStint"]]
    df[["Tyre_Compound"]] = tyre[["Compound"]]
    df[["Qualifying_Time(s)"]] = qualifying_time[["Qualifying_Time(s)"]]
    df[["Starting_Pos"]] = starting_position[["Position"]]
    df[["Race_Result"]] = result[["Position"]]

    print("Data Transformation.")

    fp1_best.reset_index(inplace=True)
    fp2_best.reset_index(inplace=True)
    fp3_best.reset_index(inplace=True)
    sector_time_best.reset_index(inplace=True)
    average_laptime.reset_index(inplace=True)
    stint.reset_index(inplace=True)
    tyre.reset_index(inplace=True)
    qualifying_time.reset_index(inplace=True)
    starting_position.reset_index(inplace=True)
    result.reset_index(inplace=True)
    df.reset_index(inplace=True)

    print("Resetting Index Done.")


    df.to_csv(f"Race/05.CanadaGP/Data/{race}GP.csv",index=False)


# For Sprint Races

races = ["China", "Miami"]

for race in races:


    FP1 = fastf1.get_session(season, race, 'FP1')
    FP1.load()
    FP2 = fastf1.get_session(season, race, 'SQ')
    FP2.load()
    FP3 = fastf1.get_session(season, race, 'S')
    FP3.load()

    Qualify = fastf1.get_session(season, race, 'Q')
    Qualify.load()

    Result = fastf1.get_session(season, race, 'R')
    Result.load()

    print(f"Done Loading Season {season} & Race {race}")

    fp1_best = get_fp1_best(FP1)
    fp2_best = get_fp2_best(FP2)
    fp3_best = get_fp3_best(FP3)
    sector_time_best = get_sector_times(FP2)
    average_laptime = get_average_laptime(FP2)
    stint = get_stint(FP2)
    tyre = get_tyre_compound(FP2)
    qualifying_time = get_qualifying_data(Qualify)
    starting_position = get_starting_position(Qualify)
    result = get_race_results(Result)

    print("Data Extraction Done.")

    fp1_best.set_index("Driver",inplace=True)
    fp2_best.set_index("Driver",inplace=True)
    fp3_best.set_index("Driver",inplace=True)
    sector_time_best.set_index("Driver",inplace=True)
    average_laptime.set_index("Driver",inplace=True)
    stint.set_index("Driver",inplace=True)
    tyre.set_index("Driver",inplace=True)
    qualifying_time.set_index("Driver",inplace=True)
    starting_position.set_index("Driver",inplace=True)
    result.set_index("Driver",inplace=True)

    print("Setting Index Done.")

    df = fp1_best.copy()
    df.rename(columns={"LapTime":"FP1_BestTime(s)"},inplace=True)
    df[["FP2_BestTime(s)"]] = fp2_best[["LapTime"]]
    df[["FP3_BestTime(s)"]] = fp3_best[["LapTime"]]
    df[["Sector1Time(s)","Sector2Time(s)","Sector3Time(s)"]] = sector_time_best[["Sector1Time","Sector2Time","Sector3Time"]]
    df[["Average_Laptime(s)"]] = average_laptime[["LapTime"]]
    df[["Longest_Stint"]] = stint[["LongestStint"]]
    df[["Tyre_Compound"]] = tyre[["Compound"]]
    df[["Qualifying_Time(s)"]] = qualifying_time[["Qualifying_Time(s)"]]
    df[["Starting_Pos"]] = starting_position[["Position"]]
    df[["Race_Result"]] = result[["Position"]]

    print("Data Transformation.")

    fp1_best.reset_index(inplace=True)
    fp2_best.reset_index(inplace=True)
    fp3_best.reset_index(inplace=True)
    sector_time_best.reset_index(inplace=True)
    average_laptime.reset_index(inplace=True)
    stint.reset_index(inplace=True)
    tyre.reset_index(inplace=True)
    qualifying_time.reset_index(inplace=True)
    starting_position.reset_index(inplace=True)
    result.reset_index(inplace=True)
    df.reset_index(inplace=True)

    print("Resetting Index Done.")

    df.to_csv(f"Race/05.CanadaGP/Data/{race}GP.csv",index=False)


print("Done with ETL")