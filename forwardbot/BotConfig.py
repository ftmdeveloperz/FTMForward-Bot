from os import environ
class Config(object):
    API_ID = environ.get("API_ID", "28776072")
    API_HASH = environ.get("API_HASH", "b3a786dce1f4e7d56674b7cadfde3c9d")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7639383535:AAEJzJp5I_4bC9Qa-awU51-b3HymsAqe-wI")
    STRING_SESSION = environ.get("STRING_SESSION", "BQG3FogAQenvabsdRWhN1fudvbYU9zoSi1L-2JTH1Zh7Vt9vOuw_ShtKMRAFHgMTywkuChIl2s4YT6vBkQBOq9SE5A6FXYF11bo_jTjD7-Ymffc6ydD1YCjIEp29NEpmrSa5kO9RQvhVxSmMOB4FzLWgAnFgYsCDhI2aYyZZOS94hEfzyxCCMnNR6D0e4Ki5b7GA9Bkq9vPGbDgqoOIMlX1PwI8MtE_tt-TCV2cCQl4IvkyyoZclF1LPw6Ci6KpLt8v0xikySFE1UPLIvo1ZeUpnRoVIO5Lunm2GYNEL72b7Kup2jOLZG9SMAhtCwL6lhTv7K7UAwC_5g7RGSbDpu9REV38m-AAAAAHLnSGzAA")
    SUDO_USERS = environ.get("SUDO_USERS", "6168162777 6366990600")
    COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "^/")
    HELP_MSG = """
    💢 **ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ɪɴ ᴛʜᴇ ʙᴏᴛ ᴀʀᴇ:**
    
    🔻 **Command :** /forward
    **Usage : ** Forwards messages from a channel to other.
    🔻 **Command :** /count
    **Usage : ** Returns the Total message sent using the bot.
    🔻 **Command :** /reset
    **Usage : ** Resets the message count to 0.
    🔻 **Command :** /restart
    **Usage : ** Updates and Restarts the Bot.
    🔻 **Command :** /join
    **Usage : ** Joins the channel.
    🔻 **Command :** /help
    **Usage : ** Get the help of this bot.
    🔻 **Command :** /status
    **Usage :** Check current status of Bot.
    🔻 **Command :** /uptime
    **Usage :** Check uptime of Bot.
    
    ⭕ **ʙᴏᴛ ɪs ᴄʀᴇᴀᴛᴇᴅ ʙʏ** **@ftmdeveloper**
    """
