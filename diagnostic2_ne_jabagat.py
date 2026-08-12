def calculate_fuel(cargo_weight):
    base_ship_weight = 50000
    total_weight = base_ship_weight + cargo_weight
    return total_weight * 3

def cargo_load(cargo_weight):
    #"satellite" == 1000
    #"rover" == 2500
    #"supplies" == 500

    cargo_weight = 0

    while cargo_weight >= 0:
        cargo = (input("Input cargo to be loaded: "))
        if cargo == "satellite":
            cargo_weight + 1000 
        elif cargo == "rover":             
            cargo_weight + 2500  
        elif cargo == "supplies":
            cargo_weight + 500  
        elif cargo == "launch":
            if cargo_weight > 10000:
                print ("MAX WEIGHT REACHED") 
                print ("WILL NOT LAUNCH")
            else:
                print ("Rocket will launch.")
        else:
            print("Command not authorized for mission.")

cargo_load(any)



