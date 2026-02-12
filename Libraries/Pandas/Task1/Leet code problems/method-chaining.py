import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    # check > 100
    # sort descending 
    filtered = animals.query( 'weight > 100').sort_values('weight' , ascending=False) 
    result = filtered[['name']]
    return result