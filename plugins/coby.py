from pyrogram import Client, filters

@Client.on_message(filters.command('source'))
async def source(bot, update):
    await update.reply_photo('https://telegra.ph/file/e175384031bd8081ffd2b.jpg')
