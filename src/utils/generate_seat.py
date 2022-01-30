from . import globals
last_counter = 0

def general_counter_logic(arr,row):
    global last_counter
    for x in range(0,row):
        last_counter += 1
        if last_counter > globals.total_seat_to_fill:
            break
        arr.append(last_counter)
    return last_counter

def airsle_decorator(fun):
    def airsle_logic(input_list):
        for index,x in enumerate(input_list):
            col = x[0]
            row = x[1]
            min_req_airsle_position = 2
            if index in globals.window_seats_positions:
                if col - min_req_airsle_position < 0:
                    continue
                else:
                    min_req_airsle_position = 1
            general_counter_logic(globals.all_airsle_seats,min_req_airsle_position * row)
        return fun(input_list)
    return airsle_logic

def window_decorator(fun):
    def window_logic(input_list):
        for index,x in enumerate(input_list):
            row = x[1]
            if index in globals.window_seats_positions:
                general_counter_logic(globals.all_window_seats,row)
        return fun(input_list)
    return window_logic

def middle_decorator(fun):
    def middle_logic(input_list):
        for x in input_list:
            col = x[0]
            row = x[1]
            min_req_middle_position = col - 2   
            general_counter_logic(globals.all_middle_seats,min_req_middle_position * row)
        return fun(input_list)
    return middle_logic


@airsle_decorator
@window_decorator
@middle_decorator
def generate_available_seats(input_list):
    pass