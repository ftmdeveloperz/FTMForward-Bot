from os import environ
class Config(object):
    API_ID = environ.get("API_ID", "28776072")
    API_HASH = environ.get("API_HASH", "b3a786dce1f4e7d56674b7cadfde3c9d")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7639383535:AAEJzJp5I_4bC9Qa-awU51-b3HymsAqe-wI")
    STRING_SESSION = environ.get("STRING_SESSION", "BQG3FogAvpKCr_sHq6zipsGRAxeSpmvOi81hu1E85PEgek7y3fjJojMy-xwBicFKlTqnofdGX3npg7LTvoe_VFFghxI6EXMH4IO-Nhz08RXPPG3cClzL5frhKL34fnzlT_-fTlm4GEbRYFEPf6Kvxk-1Y-QVgb85vQZOlLoGTYSFCQbdvPJ9QMIesKllbsNe05Fossb-LrD3sp9E14IR0ONr4s9NnLL91Fe3cqDeSEeWtXDM_p9QEFweAMhN-jMOBjc5k380puvvmbBW4mVAQnWE363aHusrALLAceI54_DXXK_XdnrA4vl9aigAIV-QQe9cDqw5ECx4WRTESAn3aeP2_6JovgAAAAHLnSGzAA")
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
