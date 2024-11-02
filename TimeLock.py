######################################################################################
#must install pytz library: pip install pytz
######################################################################################
import sys
from datetime import datetime
import hashlib
import pytz
import re

def main():
    # Check if a file path is provided as an argument
    if len(sys.argv) < 2:
        date_input = sys.stdin.read().strip()
        #print("Usage: python script.py <file_path>")
    else:
        file_path = sys.argv[1]

        # Read the content of the file
        try:
            with open(file_path, 'r') as file:
                date_input = file.read().strip()  # Strip to remove any extra whitespace or newline
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return

    #print(f"Date input received from file: {date_input}")  # Debug

    # Parse the input date in the specified format
    try:
        epoch = datetime.strptime(date_input, "%Y %m %d %H %M %S")
    except ValueError:
        print("Incorrect format for date and time")
        return

    #print(f"Parsed epoch time: {epoch}")  # Debug

    # Localize epoch and current time to the same timezone to account for DST
    timezone = pytz.timezone('America/New_York')
    epoch = timezone.localize(epoch)
    current_time = timezone.localize(datetime(2017, 4, 26, 15, 14, 30))# timezone.localize(datetime.now())
    #print(f"Current time: {current_time}")  # Debug

    # Calculate time elapsed since epoch in seconds and round down to the nearest 60-second interval
    elapsed_seconds = int((current_time - epoch).total_seconds())
    elapsed_seconds = (elapsed_seconds // 60) * 60
    #print(f"Elapsed seconds (rounded): {elapsed_seconds}")  # Debug

    # Compute the compound hash: MD5(MD5(elapsed_seconds))
    hash_input = hashlib.md5(str(elapsed_seconds).encode()).hexdigest()
    compound_hash = hashlib.md5(hash_input.encode()).hexdigest()
    #print(f"Compound hash: {compound_hash}")  # Debug

    # Extract first two letters [a-f] from left-to-right
    letters = re.findall(r'[a-f]', compound_hash)
    first_two_letters = ''.join(letters[:2]) if len(letters) >= 2 else ""

    # Extract first two digits [0-9] from right-to-left
    digits = re.findall(r'\d', compound_hash)
    first_two_digits_reversed = ''.join(digits[::-1][:2]) if len(digits) >= 2 else ""

    # Concatenate the extracted characters to form the final code
    result_code = first_two_letters + first_two_digits_reversed
    print(f"Resulting code: {result_code}")  # Final output

if __name__ == "__main__":
    main()

