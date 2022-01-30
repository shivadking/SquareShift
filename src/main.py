from utils import globals
from utils import generate_seat
from utils import allocate_seat
# input_list = [ [3,2], [4,3], [2,3], [3,4] ]
# total_seat_to_fill = 30

#Categorize and Collect - Window, Middle & Airsle seats
generate_seat.generate_available_seats(globals.input_list)

#Allocate & Display - Window, Middle & Airsle seats
for row_count in range(1,len(globals.input_list) + 1):
    for index,x in enumerate(globals.input_list):
            col = x[0]
            row = x[1]
            if row_count > row:
                for space_adjust in range(0,col):
                    value_to_print = "".rjust(2)
                    print(value_to_print, end = "   ")
                print(" ",end = "   ")
                continue
            if index == 0:  #Lef side Window execution
                allocate_seat.window_executions(index)
                allocate_seat.middle_executions(col)
                allocate_seat.airsle_executions(index,col,False)
            elif index == len(globals.input_list)-1: # Middle side execution
                allocate_seat.airsle_executions(index,col,False)
                allocate_seat.middle_executions(col)
                allocate_seat.window_executions(index)
            else:  #Right Side Window execution
                allocate_seat.airsle_executions(index,col,True)
            if index < len(globals.input_list)-1:
                print(" ",end = " | ")
    else:
        print("")