import json
input_list = json.loads(input("Enter the Input 2D Array : "))
total_seat_to_fill = int(input("Enter the Total seat to fill : "))

all_airsle_seats = list()
all_window_seats = list()
all_middle_seats = list()

window_seats_positions = [0,len(input_list) - 1]
max_len = len(input_list)

my_last_counter_window = -1
my_last_counter_middle = -1
my_last_counter_ersle = -1