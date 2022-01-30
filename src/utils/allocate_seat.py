from utils.globals import *

def print_seat_allocations_logic(counter,count,arr,isMiddleCallRequired = False,col = 0):
    while count > 0:
        counter += 1
        try:
            value_to_print = str(arr[counter])
        except:
            value_to_print = ""
        value_to_print = value_to_print.rjust(2)
        print(value_to_print, end = " | ")
        if isMiddleCallRequired:
            middle_executions(col)
            isMiddleCallRequired = False
        count -= 1
    return counter

def window_executions(index):
    global my_last_counter_window
    if index in window_seats_positions:
        my_last_counter_window = print_seat_allocations_logic(my_last_counter_window,1,all_window_seats)
    
def middle_executions(col):
    global my_last_counter_middle
    min_req_middle_position = col - 2
    my_last_counter_middle = print_seat_allocations_logic(my_last_counter_middle,min_req_middle_position,all_middle_seats)
    
def airsle_executions(index,col,isMiddleCallRequired):
    global my_last_counter_ersle
    min_req_airsle_position = 2
    if index in window_seats_positions:
        min_req_airsle_position = 1
    my_last_counter_ersle = print_seat_allocations_logic(my_last_counter_ersle,min_req_airsle_position,all_airsle_seats,isMiddleCallRequired,col)