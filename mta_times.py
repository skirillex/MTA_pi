from google.transit import gtfs_realtime_pb2
from protobuf_to_dict import protobuf_to_dict
import requests
import time

# headers={"x-api-key": "769b59cf365fb57f201e379116b64829"}

api_key= "769b59cf365fb57f201e379116b64829"
feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get("http://datamine.mta.info/mta_esi.php?key=769b59cf365fb57f201e379116b64829")


feed.ParseFromString(response.content)

subway_feed = protobuf_to_dict(feed) #is a dictionary

realtime_data = subway_feed['entity'] #is a list
station_times = []

def get_traintime(data, station_id):
    for train_trip_id in data:
        if train_trip_id.get('trip_update'):
            train_schedule_update = train_trip_id["trip_update"]
            #train_id = train_trip_id["trip"] ##this gets the dictionary that holds the trip_id which has train in it
            arrival_times = train_schedule_update["stop_time_update"]
            for arrivals in arrival_times:
                if arrivals.get("stop_id") == station_id:
                    arrival_data = arrivals["arrival"]
                    time = arrival_data["time"]
                    if time != None:
                        station_times.append(time)


###may ahve to make a dictionary with train_id to time values
#the above function only gives all train times for a station, not for indiviudal train in it



get_traintime(realtime_data,"123N")
station_times.sort()
for i in station_times:
    print(i)

print("current time")
current_time = int(time.time())
print(current_time)

train_arrives_at_station = int(((station_times[2] - current_time) / 60 ))
train_arrives_at_station_next = int(((station_times[3] - current_time) / 60 ))
print("----------------------------")
print("Train arrives at station:")
print(train_arrives_at_station)
print("next train: ")
print(train_arrives_at_station_next)

#print(subway_feed)
#print(realtime_data)

#print("subway feed")
#for x in subway_feed:
#    print(x)

#print("-----------------------")
#print("realtime data")
#for x in realtime_data:
#    print(x)

#trip_update = realtime_data['trip_update']

#for x in trip_update:
#    print(x)