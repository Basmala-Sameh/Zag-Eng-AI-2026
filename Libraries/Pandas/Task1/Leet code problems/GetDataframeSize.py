import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    size = list(players.shape)
    return size