# ============== SELWYN TICKETING SYSTEM ==============
# Student Name: 
# Student ID : 
# =============================================================

from datetime import date,datetime,timedelta


# ==================  ALTERNATIVE DATA SET  ===================
# When we mark your assessment, we will use a dataset with the same structure, but with
# different data (e.g., different tour names and dates, and different customers).
# 
# Try renaming this file to 'atl_data.py' and check that your code still works  --

events = {
    # 
    "August Extravaganza": {
           # age restriction is the integer age limit for attendings the event, ticket purchasers must be at least this old
           "age_restriction":0,
           "event_date":date(2025,8,1),
           "capacity":2000,
            "tickets_sold":13,
            "customers":[(2316,3),(2023,2),(764,7),(765,1)]},
    "Make Noise": {"age_restriction":18,
            "event_date": date(2025,4,19),
            "capacity":1000,
            "tickets_sold":1,
            "customers":[(2343,1)]},
    "Quest 24": {
           # age restriction is the integer age limit for attendings the event, ticket purchasers must be at least this old
           "age_restriction":0,
           "event_date":date(2024,9,2),
           "capacity":500,
            "tickets_sold":10,
            "customers":[(1291,6),(1186,2),(2316,2)]},
    "Private Art Launch 25": {
           # age restriction is the integer age limit for attendings the event, ticket purchasers must be at least this old
           "age_restriction":18,
           "event_date":date(2025,7,21),
           "capacity":10,
            "tickets_sold":10,
            "customers":[(764,1),(765,1),(2023,4),(2316,4)]},
}

# [id, first_name, family_name, birthdate ,email address]
customers = [ 
	[2316, 'Kate', 'McArthur', date(1956,7,15), 'K_McArthur94@gmail.com'],
	[2023, 'Jack', 'Hopere', date(1966,9,1), 'jack.hopere@kiwi.nz'],
	[2343, 'Chloe', 'Charles', date(1994,1,25), 'chloe@charles.nz'],
	[1863, 'Xue', 'Liu', date(1992,9,30), 'xuelulu18@gmail.com'],
	[1186, 'Sam', 'Liu', date(1989,2,10), 'sammiebro@xmail.com'],
	[1801, 'Xuhong', 'Liu', date(2010,3,15), 'redfishy99@xao123.com'],
	[1291, 'Satish', 'Patel', date(1984,7,15), 'financialsolutions2016@gmail.com'],
    [1924, 'Parveen', 'Patel', date(1988,9,24), 'p.patel.1438@gtel.com'],
    [1925, 'Rashid', 'Patel', date(2006,12,24), 'skaterpro993@gtel.com'],
    [2222, 'Rishi', 'Patel', date(2021,1,3), 'p.patel.1438@gtel.com'],
    [764, 'Cyril', 'Wright', date(1939,9,19), 'cmwright@xtra.co.nz'],
    [765, 'Mabel', 'Wright', date(1941,9,20), 'cmwright@xtra.co.nz']
]

def unique_id():
    """
    This will return the next available ID as a new integer value
    that is one higher than the current maximum ID number in the list."""
    
    return max(list(zip(*customers))[0]) + 1


def display_formatted_row(row, format_str):
    """
    row is a list or tuple containing the items in a single row.
    format_str uses the following format, with one set of curly braces {} for each column:
       eg, "{: <10}" determines the width of each column, padded with spaces (10 spaces in this example)
       <, ^ and > determine the alignment of the text: < (left aligned), ^ (centre aligned), > (right aligned)
    The following example is for 3 columns of output: left-aligned 5 characters wide; centred 10 characters; right-aligned 15 characters:
        format_str = "{: <5}  {: ^10}  {: >15}"
    Make sure the column is wider than the heading text and the widest entry in that column,
        otherwise the columns won't align correctly.
    You can also pad with something other than a space and put characters between the columns, 
        eg, this pads with full stops '.' and separates the columns with the pipe character '|' :
           format_str = "{:.<5} | {:.^10} | {:.>15}"
    """
    # Convert a tuple to a list, to allow updating of values
    if type(row) == tuple: 
        row = list(row)
    # Loop through each item in the row, changing to "" (empty string) if value is None and converting all other values to string
    #   (Extra info:  enumerate() places a loop counter value in index to allow updating of the correct item in row)
    for index,item in enumerate(row):
        if item is None:      # Removes any None values from the row_list, which would cause the print(*row_list) to fail
            row[index] = ""       
        else:    
            row[index] = str(item)
    # Apply the formatting in format_str to all items in row
    print(format_str.format(*row))

