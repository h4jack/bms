from utils.provider import APIProvider

api = APIProvider(91, 7557888303, "sms", delay=2)
for i in api:
    print(i)