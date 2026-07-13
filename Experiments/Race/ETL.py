import pandas as pd
import numpy as np
import fastf1
from fastf1.ergast import Ergast
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

    Race = Result.results[["Abbreviation","Position"]]
    Race.rename(columns={"Abbreviation":"Driver"},inplace=True)

    return Race

def get_driver_performance_recent(sessions_list):
    
    if not sessions_list:
        return pd.DataFrame()
    all_race_data = []
    
    for session in sessions_list:
        event_name = session.event['EventName']
        results = session.results.copy()
        
        driver_data = results[["Abbreviation", "Position", "Points"]].copy()
        driver_data.rename(columns={"Abbreviation": "Driver"}, inplace=True)
        driver_data["Event"] = event_name
        
        all_race_data.append(driver_data)
        
    combined_df = pd.concat(all_race_data, ignore_index=True)
    
    performance_summary = combined_df.pivot(
        index="Driver", 
        columns="Event", 
        values=["Position", "Points"]
    )
    
    performance_summary.columns = [f"{col[0]}_{col[1]}" for col in performance_summary.columns]
    
    return performance_summary.reset_index()

def get_constructor_performance_recent(sessions_list):

    if not sessions_list:
        return pd.DataFrame()
        
    all_constructor_data = []
    
    for session in sessions_list:
        event_name = session.event['EventName']
        results = session.results.copy()
        
        team_points = results.groupby("TeamName")["Points"].sum().reset_index()
        team_points.rename(columns={"TeamName": "Constructor"}, inplace=True)
        team_points["Event"] = event_name
        
        all_constructor_data.append(team_points)
        
    combined_df = pd.concat(all_constructor_data, ignore_index=True)
    
    constructor_summary = combined_df.pivot(
        index="Constructor", 
        columns="Event", 
        values="Points"
    )
    
    if isinstance(constructor_summary.columns, pd.MultiIndex):
        constructor_summary.columns = [f"Points_{col[1]}" for col in constructor_summary.columns]
    else:
        constructor_summary.columns = [f"Points_{col}" for col in constructor_summary.columns]
    
    return constructor_summary.reset_index()

def get_driver_points_before_race(Season, race_name):
    event = fastf1.get_event(Season, race_name)
    current_round = event.RoundNumber
    
    ergast = Ergast()
    
    if current_round == 1:
        drivers = ergast.get_driver_info(season=Season, round=1)
        
        driver_points = drivers[["driverCode"]].copy()
        driver_points.rename(columns={"driverCode": "Driver"}, inplace=True)
        driver_points["Points"] = 0.0
        
        return driver_points.sort_values(by="Driver").reset_index(drop=True)
        
    standings_response = ergast.get_driver_standings(season=Season, round=current_round - 1)
    
    if hasattr(standings_response, 'content'):
        standings = standings_response.content[0]
    else:
        standings = standings_response
    
    driver_points = standings[["driverCode", "points"]].copy()
    driver_points.rename(columns={"driverCode": "Driver", "points": "Points"}, inplace=True)
    
    driver_points = driver_points.sort_values(by="Points", ascending=False).reset_index(drop=True)
    
    return driver_points

def get_constructor_points_before_race(Season, race_name):
    event = fastf1.get_event(Season, race_name)
    current_round = event.RoundNumber
    
    ergast = Ergast()
    
    if current_round == 1:
        constructors = ergast.get_constructor_info(season=Season, round=1)
        
        constructor_points = constructors[["constructorId"]].copy()
        constructor_points.rename(columns={"constructorId": "Constructor"}, inplace=True)
        constructor_points["Points"] = 0.0
        
        return constructor_points.sort_values(by="Constructor").reset_index(drop=True)
        
    standings_response = ergast.get_constructor_standings(season=Season, round=current_round - 1)
    
    if hasattr(standings_response, 'content'):
        standings = standings_response.content[0]
    else:
        standings = standings_response
    
    constructor_points = standings[["constructorId", "points"]].copy()
    constructor_points.rename(columns={"constructorId": "Constructor", "points": "Points"}, inplace=True)
    
    constructor_points = constructor_points.sort_values(by="Points", ascending=False).reset_index(drop=True)
    
    return constructor_points





Map = {
    "NOR":"McLaren",
    "PIA":"McLaren",

    "VER":"Red Bull Racing",
    "HAD":"Red Bull Racing",

    "LEC":"Ferrari",
    "HAM":"Ferrari",

    "RUS":"Mercedes",
    "ANT":"Mercedes",

    "ALO":"Aston Martin",
    "STR":"Aston Martin",

    "ALB":"Williams",
    "SAI":"Williams",

    "OCO":"Haas F1 Team",
    "BEA":"Haas F1 Team",

    "GAS":"Alpine",
    "COL":"Alpine",

    "HUL":"Audi",
    "BOR":"Audi",

    "PER":"Cadillac",
    "BOT":"Cadillac",
    
    "LAW":"Racing Bulls",
    "LIN":"Racing Bulls"  
}

Constructor_Map = {
    "mercedes":"Mercedes",
    "ferrari":"Ferrari",
    "mclaren":"McLaren",
    "red_bull":"Red Bull Racing",
    "alpine":"Alpine",
    "haas":"Haas F1 Team",
    "rb":"Racing Bulls",
    "williams":"Williams",
    "audi":"Audi",
    "cadillac":"Cadillac",
    "aston_martin":"Aston Martin"
}






year_and_race = {
    2018: 21,
    2019: 21,
    2020: 17,
    2021: 22,
    2022: 22,
    2023: 22,
    2024: 24,
    2025: 24
}




for year in range(2024,2026):
    Season = year
    Races = year_and_race[year]
    for Race in range(1,Races+1):
        event = fastf1.get_event(Season, Race)
        sessions = [
            event["Session1"],
            event["Session2"],
            event["Session3"],
            event["Session4"],
            event["Session5"]
        ]

        if "Sprint" in sessions:
            FP1 = fastf1.get_session(Season, Race, 'FP1')
            FP1.load()
            FP2 = fastf1.get_session(Season, Race, 'SQ')
            FP2.load()
            FP3 = fastf1.get_session(Season, Race, 'S')
            FP3.load()

            Qualify = fastf1.get_session(Season, Race, 'Q')
            Qualify.load()

            Result = fastf1.get_session(Season, Race, 'R')
            Result.load()

        

            print(f"Done Loading Season {Season} & Race {Race}")

            fp1_best = get_fp1_best(FP1)
            fp2_best = get_fp2_best(FP2)
            fp3_best = get_fp3_best(FP3)
            sector_time_best = get_sector_times(FP2)
            average_laptime = get_average_laptime(FP2)
            qualifying_time = get_qualifying_data(Qualify)
            starting_position = get_starting_position(Qualify)
            result = get_race_results(Result)
            df_points = get_driver_points_before_race(Season, Race)
            df_constructor_points = get_constructor_points_before_race(Season, Race)


            df_points['Constructor'] = df_points['Driver'].map(Map)
            df_constructor_points['NewConstructor'] = df_constructor_points['Constructor'].map(Constructor_Map)
            df_constructor_points.drop(columns=['Constructor'],axis=1,inplace=True)
            df_constructor_points.rename({'NewConstructor':'Constructor'},axis=1,inplace=True)
            df_points = df_points.merge(
                df_constructor_points[["Constructor","Points"]],
                on = "Constructor",
                how = "left"
            )
            df_points.rename({"Points_x":"DriversPoint","Points_y":"ConstructorsPoint"},axis=1,inplace=True)



            sessions_to_analyze = []

            

            start_round = max(1, Race - 2)

            for r in range(start_round, Race ):
                Result = fastf1.get_session(Season, r, 'R')
                Result.load()
                sessions_to_analyze.append(Result)

            driver_form = get_driver_performance_recent(sessions_to_analyze)
            constructor_form = get_constructor_performance_recent(sessions_to_analyze)

            if constructor_form.empty:
                constructor_form = pd.DataFrame({
                    "Constructor": list(set(Map.values())),
                    "ConstructorAveragePointFromLast3Races": 0
                })

            if driver_form.empty:
                driver_form = pd.DataFrame({
                    "Driver": list(Map.keys()),
                    "AveragePositionFromLast3Races": 22,
                    "AveragePointsFromLast3Races": 0
                })

        
            driver_form.iloc[:, 4:7] = driver_form.iloc[:, 4:7].fillna(0)
            driver_form.iloc[:,1:4] = driver_form.iloc[:,1:4].fillna(22)
            driver_form['AveragePositionFromLast3Races'] = driver_form.iloc[:, 1:4].mean(axis=1)
            driver_form['AveragePointsFromLast3Races'] = driver_form.iloc[:, 4:7].mean(axis=1)


            constructor_form["ConstructorAveragePointFromLast3Races"] = constructor_form.iloc[:,1:4].mean(axis=1)


            driver_form['Constructor'] = driver_form['Driver'].map(Map)

            driver_form = driver_form.merge(
                constructor_form[['Constructor','ConstructorAveragePointFromLast3Races']],
                on = 'Constructor',
                how = 'left'
            )

            final_driver_form = driver_form[['Driver','Constructor','AveragePositionFromLast3Races','AveragePointsFromLast3Races','ConstructorAveragePointFromLast3Races']]


            

            print("Data Extraction Done.")

            fp1_best.set_index("Driver",inplace=True)
            fp2_best.set_index("Driver",inplace=True)
            fp3_best.set_index("Driver",inplace=True)
            sector_time_best.set_index("Driver",inplace=True)
            average_laptime.set_index("Driver",inplace=True)
            qualifying_time.set_index("Driver",inplace=True)
            starting_position.set_index("Driver",inplace=True)
            result.set_index("Driver",inplace=True)
            final_driver_form.set_index("Driver",inplace = True)
            df_points.set_index("Driver",inplace=True)
            

            print("Setting Index Done.")

            df = final_driver_form.copy()
            df[["FP1_BestTime(s)"]] = fp1_best[["LapTime"]]
            df[["FP2_BestTime(s)"]] = fp2_best[["LapTime"]]
            df[["FP3_BestTime(s)"]] = fp3_best[["LapTime"]]
            df[["Sector1Time(s)","Sector2Time(s)","Sector3Time(s)"]] = sector_time_best[["Sector1Time","Sector2Time","Sector3Time"]]
            df[["Average_Laptime(s)"]] = average_laptime[["LapTime"]]
            df[["Qualifying_Time(s)"]] = qualifying_time[["Qualifying_Time(s)"]]
            df[["Starting_Pos"]] = starting_position[["Position"]]
            df[["Race_Result"]] = result[["Position"]]
            df[["DriverPoints","ConstructorPoints"]] = df_points[["DriversPoint","ConstructorsPoint"]]

            print("Data Transformation.")

            final_driver_form.reset_index(inplace=True)
            fp1_best.reset_index(inplace=True)
            fp2_best.reset_index(inplace=True)
            fp3_best.reset_index(inplace=True)
            sector_time_best.reset_index(inplace=True)
            average_laptime.reset_index(inplace=True)
            qualifying_time.reset_index(inplace=True)
            starting_position.reset_index(inplace=True)
            result.reset_index(inplace=True)
            df_points.reset_index(inplace=True)
            df.reset_index(inplace=True)

            print("Resetting Index Done.")


            df.to_csv(f"Experiments/Race/Data/{Season}/{Race}GP.csv",index=False)



            
            



        else:
            # For Normal Races

            
            FP1 = fastf1.get_session(Season, Race, 'FP1')
            FP1.load()
            FP2 = fastf1.get_session(Season, Race, 'FP2')
            FP2.load()
            FP3 = fastf1.get_session(Season, Race, 'FP3')
            FP3.load()

            Qualify = fastf1.get_session(Season, Race, 'Q')
            Qualify.load()

            Result = fastf1.get_session(Season, Race, 'R')
            Result.load()

        

            print(f"Done Loading Season {Season} & Race {Race}")

            fp1_best = get_fp1_best(FP1)
            fp2_best = get_fp2_best(FP2)
            fp3_best = get_fp3_best(FP3)
            sector_time_best = get_sector_times(FP2)
            average_laptime = get_average_laptime(FP2)
            qualifying_time = get_qualifying_data(Qualify)
            starting_position = get_starting_position(Qualify)
            result = get_race_results(Result)
            df_points = get_driver_points_before_race(Season, Race)
            df_constructor_points = get_constructor_points_before_race(Season, Race)


            df_points['Constructor'] = df_points['Driver'].map(Map)
            df_constructor_points['NewConstructor'] = df_constructor_points['Constructor'].map(Constructor_Map)
            df_constructor_points.drop(columns=['Constructor'],axis=1,inplace=True)
            df_constructor_points.rename({'NewConstructor':'Constructor'},axis=1,inplace=True)
            df_points = df_points.merge(
                df_constructor_points[["Constructor","Points"]],
                on = "Constructor",
                how = "left"
            )
            df_points.rename({"Points_x":"DriversPoint","Points_y":"ConstructorsPoint"},axis=1,inplace=True)



            sessions_to_analyze = []

            

            start_round = max(1, Race - 2)

            for r in range(start_round, Race ):
                Result = fastf1.get_session(Season, r, 'R')
                Result.load()
                sessions_to_analyze.append(Result)

            driver_form = get_driver_performance_recent(sessions_to_analyze)
            constructor_form = get_constructor_performance_recent(sessions_to_analyze)

            if constructor_form.empty:
                constructor_form = pd.DataFrame({
                    "Constructor": list(set(Map.values())),
                    "ConstructorAveragePointFromLast3Races": 0
                })

            if driver_form.empty:
                driver_form = pd.DataFrame({
                    "Driver": list(Map.keys()),
                    "AveragePositionFromLast3Races": 22,
                    "AveragePointsFromLast3Races": 0
                })

        
            driver_form.iloc[:, 4:7] = driver_form.iloc[:, 4:7].fillna(0)
            driver_form.iloc[:,1:4] = driver_form.iloc[:,1:4].fillna(22)
            driver_form['AveragePositionFromLast3Races'] = driver_form.iloc[:, 1:4].mean(axis=1)
            driver_form['AveragePointsFromLast3Races'] = driver_form.iloc[:, 4:7].mean(axis=1)


            constructor_form["ConstructorAveragePointFromLast3Races"] = constructor_form.iloc[:,1:4].mean(axis=1)


            driver_form['Constructor'] = driver_form['Driver'].map(Map)

            driver_form = driver_form.merge(
                constructor_form[['Constructor','ConstructorAveragePointFromLast3Races']],
                on = 'Constructor',
                how = 'left'
            )

            final_driver_form = driver_form[['Driver','Constructor','AveragePositionFromLast3Races','AveragePointsFromLast3Races','ConstructorAveragePointFromLast3Races']]


            

            print("Data Extraction Done.")

            fp1_best.set_index("Driver",inplace=True)
            fp2_best.set_index("Driver",inplace=True)
            fp3_best.set_index("Driver",inplace=True)
            sector_time_best.set_index("Driver",inplace=True)
            average_laptime.set_index("Driver",inplace=True)
            qualifying_time.set_index("Driver",inplace=True)
            starting_position.set_index("Driver",inplace=True)
            result.set_index("Driver",inplace=True)
            final_driver_form.set_index("Driver",inplace = True)
            df_points.set_index("Driver",inplace=True)
            

            print("Setting Index Done.")

            df = final_driver_form.copy()
            df[["FP1_BestTime(s)"]] = fp1_best[["LapTime"]]
            df[["FP2_BestTime(s)"]] = fp2_best[["LapTime"]]
            df[["FP3_BestTime(s)"]] = fp3_best[["LapTime"]]
            df[["Sector1Time(s)","Sector2Time(s)","Sector3Time(s)"]] = sector_time_best[["Sector1Time","Sector2Time","Sector3Time"]]
            df[["Average_Laptime(s)"]] = average_laptime[["LapTime"]]
            df[["Qualifying_Time(s)"]] = qualifying_time[["Qualifying_Time(s)"]]
            df[["Starting_Pos"]] = starting_position[["Position"]]
            df[["Race_Result"]] = result[["Position"]]
            df[["DriverPoints","ConstructorPoints"]] = df_points[["DriversPoint","ConstructorsPoint"]]

            print("Data Transformation.")

            final_driver_form.reset_index(inplace=True)
            fp1_best.reset_index(inplace=True)
            fp2_best.reset_index(inplace=True)
            fp3_best.reset_index(inplace=True)
            sector_time_best.reset_index(inplace=True)
            average_laptime.reset_index(inplace=True)
            qualifying_time.reset_index(inplace=True)
            starting_position.reset_index(inplace=True)
            result.reset_index(inplace=True)
            df_points.reset_index(inplace=True)
            df.reset_index(inplace=True)

            print("Resetting Index Done.")


            df.to_csv(f"Experiments/Race/Data/{Season}/{Race}GP.csv",index=False)



            