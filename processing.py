def is_in(l, pick):
    """Return boolean list if elements of list is any of pick

    Parameters:
    ----------
    l: list
        test elements of this list

    pick: list
        return True if any of elements of pick
    """
    
    return [i in list(pick) for i in l]




def subset_one(df,category,pickup):
    """Return the subset of initial data frame for a given list of location

    Parameters:
    df: pandas data frame
        original data frame

    category: string
        name of category to filter

    pickup: list of strings
        match to select
    """

    #pickup must be a list to continue
    if not isinstance(pickup,list):
        pickup = [pickup]
        
    check = is_in(df[category], pickup)
    return df[check]




