#from main_script_RTB import myShare


# in this example, we will have three slots
# each slot will have 2 possible digits (a 0 or a 1)
# that is 2^3 possibilities
# need the algorithm to go through and figure out all possible combinations
possible_digits = 6 #subtract 1 if used in function
possible_tickers = 3 #subtract 1 if used in function
#setup below
combos_list = [] #to contain combinations
combo_template = [] #template for a certain combination --> exple: [0,0,0]
current_combo = [0,0,0,0,0,0,0] #may not even need to declare with all three slots
pin_counter = 0
pin_counter_highest = 6
digit_counter = 0
digit_counter_highest = 6

#create_combo

#def create_combo

def add_combo(current_combo, combos_list, pin_counter, digit_counter):
    current_combo[pin_counter] = digit_counter
    combos_list.append(current_combo[:])
    return

def go_thru_combos(possible_digits, possible_tickers, combos_list, \
                current_combo, pin_counter, digit_counter, \
                pin_counter_highest, digit_counter_highest):
    if pin_counter == pin_counter_highest: # if the program has reached the last pin
        if digit_counter == digit_counter_highest: #if we have reached the highest possible digit
            add_combo(current_combo, combos_list, pin_counter, digit_counter)
            return
        else:
            digit_counter += 1
            go_thru_combos(possible_digits, possible_tickers, combos_list, \
                            current_combo, pin_counter, digit_counter, \
                            pin_counter_highest, digit_counter_highest)
            digit_counter -= 1
            add_combo(current_combo, combos_list, pin_counter, digit_counter)
            return
    else: #if the program has not reached the last pin
        if digit_counter == digit_counter_highest: #if we have reached the highest possible digit
            pin_counter += 1 #add one to pin counter so we move to next pin
            digit_counter = 0 #set digit counter to zero so we start at the bottom
            current_combo[pin_counter] = digit_counter #update combo
            go_thru_combos(possible_digits, possible_tickers, combos_list, \
                            current_combo, pin_counter, digit_counter, \
                            pin_counter_highest, digit_counter_highest)
            return
        else: #if the program has not reached the highest possible digit
            digit_counter += 1 #climb the current pin
            current_combo[pin_counter] = digit_counter #update combo to reflect current location
            go_thru_combos(possible_digits, possible_tickers, combos_list, \
                            current_combo, pin_counter, digit_counter, \
                            pin_counter_highest, digit_counter_highest)
            digit_counter -= 1 #take us down a digit on the same pin
            current_combo[pin_counter] = digit_counter #update combo to reflect current location
            #print "here1"
            #print digit_counter
            #print pin_counter
            pin_counter += 1
            #if pin_counter == pin_counter_highest:
            digit_counter = 0
            current_combo[pin_counter] = digit_counter
            go_thru_combos(possible_digits, possible_tickers, combos_list, \
                            current_combo, pin_counter, digit_counter, \
                            pin_counter_highest, digit_counter_highest)
            #print "here2"
            #print digit_counter
            #print pin_counter
            return

go_thru_combos(possible_digits, possible_tickers, combos_list, \
                current_combo, pin_counter, digit_counter, \
                pin_counter_highest, digit_counter_highest)
print combos_list;
print len(combos_list)
