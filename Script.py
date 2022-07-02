class script(object):
    START_TXT = """<b>Hᴇʟʟᴏ {}
    
Sᴏʀʀʏ ɪ ᴏɴʟʏ ᴡᴏʀᴋ ᴏɴ <a href='https://t.me/movie_hub_main'>𝖬ᴏᴠɪᴇ 𝖧ᴜʙ</a> Gʀᴏᴜᴘ. Nᴏ ᴏᴛʜᴇʀ ᴄᴏᴍᴍᴀɴᴅ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴛʜɪs ʙᴏᴛ ᴇxᴄᴇᴘᴛ sᴛᴀʀᴛ. ᴅᴏɴ’ᴛ ᴡᴀsᴛᴇ ʏᴏᴜʀ ᴛɪᴍᴇ</b>
"""
    HELP_TXT = """<b>Hᴇʟʟᴏ {}
    
Sᴏʀʀʏ ɪ ᴏɴʟʏ ᴡᴏʀᴋ ᴏɴ <a href='https://t.me/movie_hub_main'>𝖬ᴏᴠɪᴇ 𝖧ᴜʙ</a> Gʀᴏᴜᴘ. Nᴏ ᴏᴛʜᴇʀ ᴄᴏᴍᴍᴀɴᴅ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴛʜɪs ʙᴏᴛ ᴇxᴄᴇᴘᴛ sᴛᴀʀᴛ. ᴅᴏɴ’ᴛ ᴡᴀsᴛᴇ ʏᴏᴜʀ ᴛɪᴍᴇ</b>"""
    ABOUT_TXT = """<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟
    
• ꜰᴜʟʟ ɴᴀᴍᴇ : sʜɪᴠᴀ
• ᴜꜱᴇʀɴᴀᴍᴇ : @OGGY123kph
• ᴘᴇʀᴍᴀɴᴇɴᴛ ᴅᴍ ʟɪɴᴋ : <a href='https://t.me/OGGY123kph'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>

“ Failure is an option here. If things are not failing, you are not innovating enough. ”</b>"""
    SOURCE_TXT = """<b>NOTE:</b>

- ഇപ്പൊ കിട്ടും നോക്കി ഇരുന്നോ .

<b>DEVS:</b>
- <a href=https://t.me/ss_linkz>ss ʟɪɴᴋᴢ</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and 𝕋𝔼𝕊𝕊𝔸 will respond whenever a keyword is found the message

<b>NOTE:</b>
1. BOT should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- BOT Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. 𝕋𝔼𝕊𝕊𝔸 supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/+_gaIOMP_AjM0MWNl)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of 𝕋𝔼𝕊𝕊𝔸

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """📂 ғɪʟᴇs sᴀᴠᴇᴅ: <code>{}</code>
👤 ᴜsᴇʀs: <code>{}</code>
👥 ɢʀᴏᴜᴘs: <code>{}</code>
📉 ᴏᴄᴄᴜᴘɪᴇᴅ: <code>{}</code> """
 
    LOG_TEXT_G = """📮 ᴄᴏʙʏ ʙᴏᴛ #NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """📮 ᴄᴏʙʏ ʙᴏᴛ #NewUser
ID - <code>{}</code>
Name - {}
"""
    ENGLISH_TXT = """<i>Look in Google or any internet browser's and find the right movie name and send it here for the movie / series ....\n\nIf you still do not get it. Send a message to our support Group @Coby_Support\n\nWe will try to upload if requested one is theatre print Not Get It (Theatre Print ❌️). Ott and Dvd released movies, will upload within 24 hours.</i>"""

    MALAYALAM_TXT = """<i>Google അല്ലെങ്കിൽ ഏതേലും internet browser's ഇൽ നോക്കി ശരിയായ സിനിമയുടെ പേര് കണ്ടെത്തി ഇവിടെ നൽകുക എന്നാലേ സിനിമ / സീരിയസ് കിട്ടുകയുള്ളു....\n\nഎന്നിട്ടും കിട്ടുന്നില്ല എങ്കിൽ നമ്മുടെ സപ്പോർട്ട് ഗ്രൂപ്പിൽ പറയുക @Coby_Support, 24 മണിക്കൂറിനുള്ളിൽ അഡ്മിൻ കിട്ടിയാൽ upload ചെയ്യാം..\n\nതിയേറ്ററിൽ റിലീസ് ആയ മൂവിയാണ് ചോദിച്ചതെങ്കിൽ കിട്ടില്ല (തീയേറ്റർ പ്രിന്റ് ❌️). ott Dvd റിലീസ് ആയത് ആണെങ്കിൽ തന്നിരിക്കും.</i>"""
