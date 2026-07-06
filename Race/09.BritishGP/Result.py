import pandas as pd
import fastf1

def get_race_results(Result):

    race = Result.results[["Abbreviation","Position"]]
    race.rename(columns={"Abbreviation":"Driver"},inplace=True)

    return race


season = 2026
race = 'British'

Result = fastf1.get_session(season, race, 'R')
Result.load()


result = get_race_results(Result)

result.reset_index(inplace=True, drop=True)

result.to_csv("Race/09.BritishGP/Data/Result.csv",index=False)