from telethon.sync import TelegramClient, functions
import asyncio

# Replace with your own API ID and Hash from my.telegram.org
API_ID = "API_ID"  # Example: 123456
API_HASH = "API_HASH"  # Example: 'abcd1234efgh5678ijkl'
PHONE_NUMBER = "PHONE_NUMBER"  # Example: +1234567890

# Save session to avoid OTP every time
SESSION_NAME = "telegram_session"

async def search_public_channels(query):
    async with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
        await client.start(PHONE_NUMBER)

        # Search for public channels
        result = await client(functions.contacts.SearchRequest(
            q=query, limit=10  # Searches for top 10 matching channels
        ))

        # Extract channel names
        channels = [chat.title for chat in result.chats if getattr(chat, "megagroup", False) == False]

        # Save to file
        with open("output.txt", "w", encoding="utf-8") as file:
            for channel in channels:
                file.write(channel + "\n")

        print(f"Found {len(channels)} public channels. Data saved in output.txt")

# Run the async function
query = input("Enter the Telegram channel keyword: ")
asyncio.run(search_public_channels(query))
