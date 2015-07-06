
#this program returns all possible combinations when given number of scenarios
#and number of outcomes per scenario# number of scenarios (think like experiments)

combos_list = [] #to contain combinations
scenario_counter = 0
number_of_scenarios = int(raw_input("Number of Scenarios: ")) - 1
current_combo = []
for each_scenario in xrange(number_of_scenarios + 1): current_combo.append(0)
outcomes_counter = 0
number_of_outcomes = int(raw_input("Number of Possible Outcomes: ")) - 1



def add_combo(current_combo, combos_list, scenario_counter, outcomes_counter):
    current_combo[scenario_counter] = outcomes_counter
    combos_list.append(current_combo[:])
    return

def go_thru_combos(combos_list, \
                current_combo, scenario_counter, outcomes_counter, \
                number_of_scenarios, number_of_outcomes):
    if scenario_counter == number_of_scenarios: # if the program has reached the last pin
        if outcomes_counter == number_of_outcomes: #if we have reached the highest possible digit
            add_combo(current_combo, combos_list, scenario_counter, outcomes_counter)
            return
        else:
            outcomes_counter += 1
            go_thru_combos(combos_list, \
                            current_combo, scenario_counter, outcomes_counter, \
                            number_of_scenarios, number_of_outcomes)
            outcomes_counter -= 1
            add_combo(current_combo, combos_list, scenario_counter, outcomes_counter)
            return
    else: #if the program has not reached the last pin
        if outcomes_counter == number_of_outcomes: #if we have reached the highest possible digit
            scenario_counter += 1 #add one to pin counter so we move to next pin
            outcomes_counter = 0 #set digit counter to zero so we start at the bottom
            current_combo[scenario_counter] = outcomes_counter #update combo
            go_thru_combos(combos_list, \
                            current_combo, scenario_counter, outcomes_counter, \
                            number_of_scenarios, number_of_outcomes)
            return
        else: #if the program has not reached the highest possible digit
            outcomes_counter += 1 #climb the current pin
            current_combo[scenario_counter] = outcomes_counter #update combo to reflect current location
            go_thru_combos(combos_list, \
                            current_combo, scenario_counter, outcomes_counter, \
                            number_of_scenarios, number_of_outcomes)
            outcomes_counter -= 1 #take us down a digit on the same pin
            current_combo[scenario_counter] = outcomes_counter #update combo to reflect current location
            #print "here1"
            #print outcomes_counter
            #print scenario_counter
            scenario_counter += 1
            #if scenario_counter == number_of_scenarios:
            outcomes_counter = 0
            current_combo[scenario_counter] = outcomes_counter
            go_thru_combos(combos_list, \
                            current_combo, scenario_counter, outcomes_counter, \
                            number_of_scenarios, number_of_outcomes)
            #print "here2"
            #print outcomes_counter
            #print scenario_counter
            return

go_thru_combos(combos_list, \
                current_combo, scenario_counter, outcomes_counter, \
                number_of_scenarios, number_of_outcomes)
print combos_list;
print len(combos_list)
