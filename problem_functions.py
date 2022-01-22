
def MaximizeRevenue_function(listOfVariables):
    '''
        Returns the price of some item which maximizes the revenue based off the demand.
    '''

    #Unpack from given variable list
    base_itemprice      = listOfVariables[0];
    delta_itemprice     = listOfVariables[1];
    base_personcount    = listOfVariables[2];
    delta_personcount   = listOfVariables[3];

    #From Calculations
    #X denotes the amount of dollar increases
    x = (delta_itemprice*base_personcount - base_itemprice*delta_personcount) / (2*delta_itemprice*delta_personcount)

    #Debug
    #print("Increases Found: " + str(x))

    #Calculate max Item price
    maxRevenueItemPrice = base_itemprice + x*delta_itemprice;

    #Return Value
    return maxRevenueItemPrice;