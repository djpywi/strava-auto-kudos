from KudosBot import StravaKudos
from decouple import config

# Login every 3-4 hours and hits the Button
KEEP_GOING = config("KEEP_GOING", default=True, cast=bool)

kudos = StravaKudos()

if KEEP_GOING:
    while KEEP_GOING:
        kudos.dothework()
        kudos.deep_sleep()
else:
    kudos.dothework()
