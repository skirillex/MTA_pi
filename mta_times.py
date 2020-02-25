from google.transit import gtfs_realtime_pb2
from protobuf_to_dict import protobuf_to_dict
import requests
import time


api_key= open("api_key").readline() # Imports API key from a file called api_key. key is given from the MTA dev site


def get_train(station):
    # pulls realtime feed from the MTA
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get(f"http://datamine.mta.info/mta_esi.php?key={api_key}")
    feed.ParseFromString(response.content)

    subway_feed = protobuf_to_dict(feed) # returns a dictionary (with nested lists and dictionaries) that the rest of the code works from

    realtime_data = subway_feed['entity'] # returns a list

    stations = {"72nd North" : "123N", "72nd South" : "123S", "66th South" : "124S"}

    station_times = []
    route_id_list = []
    times_dict = {}

    def get_traintime(data, station_id):
        nonlocal station_times
        nonlocal route_id_list
        for train_trip_id in data:
            if train_trip_id.get('trip_update'):
                train_schedule_update = train_trip_id["trip_update"]
                train_id = train_schedule_update["trip"]
                arrival_times = train_schedule_update["stop_time_update"]

                for arrivals in arrival_times:
                    if arrivals.get("stop_id") == station_id:  # make lists if stop_id matches station id

                        arrival_data = arrivals["arrival"]
                        time = arrival_data["time"]  # this appends train times to list
                        if time != None:
                            station_times.append(time)

                        route_id = train_id[
                            "route_id"]  # this appends train id's in the same order as train times on a separate list
                        if route_id != None:
                            route_id_list.append(route_id)

    get_traintime(realtime_data,stations.get(station)) # default is "72nd North"

    # this loop creates a dictionary with train times associated with train IDs (1, 2 or 3 train)
    for i in station_times:
        # Debug
        #print(i)
        for k in route_id_list:
            times_dict[i] = k
            # Debug
            #print(k)
            route_id_list.remove(k)
            break


    station_times.sort()

    # Debug
    print(str(times_dict))
    #print(route_id_list)
    #print(station_times)
    print("current time")
    current_time = int(time.time()) # current epoch time to compare to trains (which are also in epoch time)
    #print(current_time)
    return print_trains(station_times, current_time, times_dict)

# prints train information in terminal while also returning lists for the gui logic
def print_trains(station_times, current_time, times_dict):
    print(times_dict)
    trains_list = []
    times_list = []
    n = 4
    #for i in range(0,n):
    i = 0
    while i < n:
        if int(((station_times[i] - current_time) / 60)) > -1:
            print("------------------------")
            print(f"{times_dict.get(station_times[i])} Train") # this prints the train ID with respect to the time it departs
            trains_list.append(times_dict.get(station_times[i]))
            print(" ")
            print(f"{int(((station_times[i] - current_time) / 60 ))} Minutes") # this prints the train's departure time
            times_list.append(int(((station_times[i] - current_time) / 60 )))
            print("------------------------")
        else:
            n += 1
        i += 1

    print(trains_list)
    print(times_list)
    return trains_list, times_list
# Debug
print(get_train("72nd South"))