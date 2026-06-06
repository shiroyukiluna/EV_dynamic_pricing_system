import pandas as pd
from src.config import *

def load_all_data():

    occupancy = pd.read_csv(OCCUPANCY_FILE)

    duration = pd.read_csv(DURATION_FILE)

    info = pd.read_csv(INFO_FILE)

    adj = pd.read_csv(ADJ_FILE)

    distance = pd.read_csv(DIST_FILE)


    return occupancy, duration, info, adj, distance