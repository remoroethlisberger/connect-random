import argparse
from dotenv import load_dotenv, find_dotenv
import pandas as pd
import numpy as np
load_dotenv(find_dotenv())

from webexteamssdk import WebexTeamsAPI
api = WebexTeamsAPI()

# Add arguments
parser = argparse.ArgumentParser(description='Specify a file and the number of people per group')
parser.add_argument('-n', type=int, help='an integer for size of each group', required=True)
parser.add_argument('-f', dest='file', help='the CSV file with single column of email addresses', required=True)
parser.add_argument('-t', dest='test', help='do a dry run?', required=False)
# Parse args
args = parser.parse_args()

# Store in CONST VARIABLE
N = args.n
M = 5
FILENAME = args.file
SPACE_TITLE = 'Holiday Chat Room'

df = pd.read_csv(FILENAME)
df = df.sample(frac=1) # shuffle the main CSV file
groups = [df[i:i+N] for i in range(0, df.shape[0], N)]

# maybe we would like to add the possiblity to check if
# last group is smaller than M and if so, 
# merge them to the second last one
if groups[-1].shape[0] < M and df.shape[0] > N:
    groups[-2] = pd.concat([groups[-2], groups[-1]])
    groups.pop()

# for each group
for i, group in enumerate(groups, start=1):
    ROOM = api.rooms.create(SPACE_TITLE + ' #' + str(i))
    for i, row in group.iterrows():
        # assumes the first column is a valid email address
        email = row.iloc[0]
        api.memberships.create(roomId=ROOM.id, personEmail=email)


