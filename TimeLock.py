######################################################################################
must install pytz library: pip install pytz
######################################################################################
import sys
from datetime import datetime
import hashlib
import pytz

def main():

    date_formats = [
        "%Y-%m-%d %H:%M:%S",
        "%Y/%m/%d %H:%M:%S",
        "%Y %m %d %H %M %S",
        "%Y-%m-%d",
        "%Y/%m/%d",
        "%Y %m %d"
    ]

    #check the stdin to make sure it matches the proper format
    date_input = sys.stdin.read().strip() 
    for fmt in date_formats:
        try:
            epoch = datetime.strptime(date_input, fmt)
            break
        except ValueError:
            continue
    else:
        return print("Incorrect format for date and time")

    # pytz library used for compenstating for daylight savings(requires the current timezone (America/New_York) = central
    timezone = pytz.timezone('America/New_York')
    epoch = timezone.localize(epoch)

    # Get the current time in the same time zone -> comment out datetime.now(timezone) and uncomment the region below to maunally set datetime (NO PRECEEDING ZEROS)
    current_time = datetime.now(timezone) #timezone.localize(datetime(2017, 4, 26, 15, 14, 30))

    # Find the relevant time index
    elapsed_seconds = int((current_time - epoch).total_seconds())
    elapsed_seconds = (elapsed_seconds // 60) * 60
    
    # as per the prompt the Hash is executed twice to form a compund hash
    hash_input = hashlib.md5(str(elapsed_seconds).encode()).hexdigest()
    hash_input = hashlib.md5(str(hash_input).encode()).hexdigest()
    #for testing purposes
    print(hash_input)

    #JACK put your code here

if __name__ == "__main__":
    main()

