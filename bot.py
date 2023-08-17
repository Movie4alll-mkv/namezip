import pyrogram
import zipfile

# Define the bot's commands
commands = {
    "zip": "Download the file to be zipped",
    "zipped": "Zip the sent file",
    "zipped <filename>": "Zip the sent file with custom filename",
    "thumb": "Add thumbnail to the zipped file",
    "stop": "Cancel a process",
}

# Get the bot's token, api id, api hash, and owner id
bot_token = "YOUR_BOT_TOKEN"
api_id = "YOUR_API_ID"
api_hash = "YOUR_API_HASH"
owner_id = "YOUR_OWNER_ID"

# Create the bot
bot = pyrogram.Client(
    "FileZipBot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token,
    owner_id=owner_id,
)


@bot.on_message(filters=filters.command(commands.keys()))
async def handle_command(message):
    # Get the command
    command = message.command[0]

    # Handle the command
    if command == "zip":
        # Download the file to be zipped
        await message.reply("Downloading file...")
        file_path = await message.download_media()

    elif command == "zipped":
        # Zip the sent file
        await message.reply("Zipping file...")
        with zipfile.ZipFile(file_path, "w") as zip_file:
            zip_file.write(file_path)

        # Upload the zipped file
        await message.reply_document(file_path)

    elif command == "zipped <filename>":
        # Zip the sent file with custom filename
        await message.reply("Zipping file with custom filename...")
        with zipfile.ZipFile(file_path, "w") as zip_file:
            zip_file.write(file_path, filename=message.text.split(" ")[1])

        # Upload the zipped file
        await message.reply_document(file_path)

    elif command == "thumb":
        # Add thumbnail to the zipped file
        await message.reply("Adding thumbnail...")
        thumbnail_path = await message.download_media()

        # Zip the file with thumbnail
        with zipfile.ZipFile(file_path, "w") as zip_file:
            zip_file.write(file_path)
            zip_file.write(thumbnail_path, "thumbnail.jpg")

        # Upload the zipped file
        await message.reply_document(file_path)

    elif command == "stop":
        # Cancel a process
        await message.reply("Canceling process...")


bot.run()