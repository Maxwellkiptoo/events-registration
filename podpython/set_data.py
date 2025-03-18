# ============== SELWYN EVENT TICKETING SYSTEM ==============
# Student Name: 
# Student ID : 
# =============================================================


# * * * * * * * * * ======= WARNING ======= * * * * * * * * * * * 
# * * * Do not add any functions or variables to this file. * * *  
# * * *    It will be deleted and replaced for marking.     * * *
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

from datetime import date,datetime,timedelta



events = {
    # 
    "Brick Show 25": {
           # age restriction is the integer age limit for attendings the event, ticket purchasers must be at least this old
           "age_restriction":0,
           "event_date":date(2025,7,5),
           "capacity":2000,
            "tickets_sold":18,
            "customers":[(923,2),(810,4),(924,3),(786,9)]},
    "Selwyn Sounds 25": {"age_restriction":18,
            "event_date": date(2025,3,1),
            "capacity":1000,
            "tickets_sold":5,
            "customers":[(816,5)]},
    "Brick Show 24": {
           # age restriction is the integer age limit for attendings the event, ticket purchasers must be at least this old
           "age_restriction":0,
           "event_date":date(2024,7,13),
           "capacity":2000,
            "tickets_sold":18,
            "customers":[(816,2),(810,5),(786,3),(924,8)]},
    "Secret Music 25": {
           # age restriction is the integer age limit for attendings the event, ticket purchasers must be at least this old
           "age_restriction":18,
           "event_date":date(2025,7,21),
           "capacity":10,
            "tickets_sold":10,
            "customers":[(923,2),(786,4),(121,4)]},
}


# [id, first_name, family_name, birthdate ,email address]
customers = [ 
	[816, 'Simon', 'Charles', date(1952,7,15), 'simon@charles.nz'],
	[923, 'Simone', 'Charles', date(1987,9,1), 'simone.charles@kiwi.nz'],
	[343, 'Charlie', 'Charles', date(1954,1,25), 'charlie@charles.nz'],
	[810, 'Kate', 'McArthur', date(1972,9,30), 'K_McArthur94@gmail.com'],
	[786, 'Jack', 'Hopere', date(1980,2,10), 'Jack643@gmail.com'],
	[801, 'Chloe', 'Mathewson', date(1980,3,15), 'Chloe572@gmail.com'],
	[121, 'Kate', 'McLeod', date(1952,7,15), 'KMcLeod112@gmail.com'],
    [924, 'Samantha', 'Charles', date(2013,7,24), 'simone.charles@kiwi.nz']
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

