from pyrogram import Client
from pyrogram.errors import FloodWait
from pyrogram.types import User  # Import User class
import asyncio
import time


# This code is using Pyrogram to delete all telegram contacts
# due to telegram limitations we need to add sleep after deleting 50 contact

# if you dont know how pyrogram connects to your account :
# read  https://docs.pyrogram.org/start/setup  for more information 



# Replace with your API ID and API Hash
API_ID = ""
API_HASH = ""

app = Client("Your_acount", api_id=API_ID, api_hash=API_HASH)

async def delete_all_contacts():
    async with app:
        try:
            # Fetch all contacts
            contacts = await app.get_contacts()
            print(f"Found {len(contacts)} contacts.")

            # Delete each contact
            for contact in contacts:
                try:
                    await app.delete_contacts(contact.id)
                    print(f"Deleted contact: {contact.first_name} {contact.last_name or ''} (ID: {contact.id})")
                    await asyncio.sleep(1)  # 1-second delay between deletions
                except FloodWait as e:
                    print(f"FloodWait error, sleeping for {e.value} seconds...")
                    time.sleep(e.value)  # Handle flood wait
    
                except Exception as e:
                    print(f"Error deleting contact {contact.id}: {e}")


            print("All contacts have been deleted.")
        except Exception as e:
            print(f"Error fetching or deleting contacts: {e}")

app.run(delete_all_contacts())

