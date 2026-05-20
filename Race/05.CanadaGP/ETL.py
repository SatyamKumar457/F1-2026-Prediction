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


def get_stint(FP2):

    laps = FP2.laps

    stints = (
        laps.groupby(["Driver","Stint"])
        .size()
        .reset_index(name="LapCount")
    )

    longest_stint = (
        stints.groupby("Driver")["LapCount"]
        .max()
        .reset_index(name="LongestStint")
    )

    return longest_stint

def get_tyre_compound (FP2):

    laps = FP2.laps

    tyres = laps.groupby("Driver")["Compound"].agg(lambda x: x.mode()[0]).reset_index()

    return tyres

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

