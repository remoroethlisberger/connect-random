from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from webexteamssdk import WebexTeamsAPI
api = WebexTeamsAPI()

rooms = api.rooms.list()

for room in rooms:
    roomid = room.id
    creatorid = room.creatorId
    bot = api.people.me().id
    # check if the space is initiated by the bot
    # if so, we can send the possibly "secrete" message
    # to this space
    if bot == creatorid:
        api.messages.create(roomId=roomid, text="Super secrete message")