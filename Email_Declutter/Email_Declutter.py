# Decluttering an Email Project: Start-7/13/25

import imaplib
import email
from dotenv import load_dotenv
import os
from datetime import datetime

#################################################
####
#### Loads email credentials to connect to gmail. 
####
#################################################

load_dotenv() # Loads in .env file for secure email and password so credentials are not leaked on the internet

EMAIL = os.getenv("EMAIL") # email credentials
PASSWORD = os.getenv("PASSWORD") # password credentials

# Check Statement
print(f"EMAIL={EMAIL}, PASSWORD={'set' if PASSWORD else 'not set'}")

# Connects to server
IMAP_SERVER = 'imap.gmail.com'
mail = imaplib.IMAP4_SSL(IMAP_SERVER)
mail.login(EMAIL, PASSWORD)
mail.select("inbox")

#################################################
####
#### Loads the amount of emails.  
####
#################################################

status, messages = mail.search(None, 'ALL')
if status == "OK":
    email_ids = messages[0].split()
    print(f"Total emails: {len(email_ids)}")
else:
    print("Failed to retrieve emails.")

#################################################
####
#### Asks Users what path or intent they want with their inbox.  
####
#################################################

path = int(input("How would you like to declutter your inbox today? Choose an option:\n"
               "1 - Minor Cleaning (delete old/spam emails)\n"
               "2 - Sort/Organize by sender/subject\n"
               "3 - Intensive Decluttering (remove duplicates, unsubscribe)\n"
               "4 - Generate Inbox Summary\n"
               "Enter the number of your choice: "))

# Depending on what choice is the 4 segemnts of my code.

#################################################
####
#### 1 - Minor Cleaning (delete old/spam emails)  
####
#################################################
# Going to get some keywords and specific addresses

if path == 1:
    
    # Info Gaining for more filters and specifics
    print('\nGreat, since you chose "Minor Cleaning", we are going to need a bit more info.')
    
    # Old emails
    old_emails = input("Do you want to clear old emails? Y or N?\n")

    if (old_emails == "Y") or (old_emails == "y"):
        
        # Range
        print("How long ago would you want the old emails to range?")
        start_date = input("Start Date - (MM/DD/YYYY)\n")
        end_date = input("End Date - (MM/DD/YYYY)\n")
        
        # Selected range 
        print(f"You have the selected the start date [{start_date}] & end date of [{end_date}].")
        confirmation = input("Is this correct? Y or N?\n")

        if (confirmation == "Y") or (confirmation == "y"):

            # Gets number of emails from range given
            def convert_to_imap_date(date_str):
                dt = datetime.strptime(date_str, "%m/%d/%Y")
                return dt.strftime("%d-%b-%Y")

            # converts to IMAP friendly format
            imap_start = convert_to_imap_date(start_date)
            imap_end = convert_to_imap_date(end_date)

            status, filtered = mail.search(None, f'SINCE {imap_start}', f'BEFORE {imap_end}')
            
            if status == "OK":
                filtered_ids = filtered[0].split()
                print(f"\nFound {len(filtered_ids)} emails between {start_date} and {end_date}.")
            else:
                print("Couldn't search emails in the given range.")

            # Ask for keywords to protect important emails
            print("\nTo avoid deleting anything important, let's look for keywords to keep.")
            print("Examples: 'invoice', 'receipt', 'project', 'grades', etc.")
            
            while True:
                keywords = input("Enter keywords to protect (comma-separated) (Type 'stop' when you're done):\n").lower()

                if keywords.strip() == "stop":
                    break
                
                # Split input by commas, strip whitespace, and add to the list
                new_keywords = [k.strip() for k in keywords.split(',') if k.strip()]
                keywords.extend(new_keywords)

            print(f"\nEmails containing these keywords will be excluded: {keywords}")



    else:
        print("Let's move on then.")            
                
                
                
                
                 