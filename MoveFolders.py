import imaplib
import json

settings = json.load(open("myIMAPlogin.json", "r"))


# Connect to the IMAP server
mail = imaplib.IMAP4_SSL(settings["IMAPserver"])

# Login to the server
mail.login(settings["email"],settings["password"])

# Destination Folder name.
newFolderName = ""

# Search String. Find folders starting with:
searchString = ""


# Select the INBOX
mail.select('INBOX')

# Get a list of all the folders in the INBOX
typ, data = mail.list()

# Loop through each folder
for folder in data:
    try:
        # Get the name of the folder
        name = folder.decode('utf-8').split(' "/" ')[1]

        # Check if the folder starts with "I 1"
        if name.startswith(searchString):
            # Create "Masse Mapper" folder if it doesn't exist
            # print(mail.create('000MasseMapper'))
            mail.select(f'{newFolderName}')
            # name = name.replace('"','')
            newfolderPath = f'{newFolderName}/{name}'.replace('"','').replace(" ","")
            # print()
            try:
                # Move folder to "Masse Mapper"
                print(mail.rename(f'{name}', f"{newfolderPath}"))
            except Exception as e:
                print(e)
                print()

    except IndexError:
        # Failed to extract the folder name
        print(f"Failed to extract the name from folder: {folder}")
        continue

# Logout from the server
mail.close()
mail.logout()