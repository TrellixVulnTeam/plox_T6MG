import os

class Var(object):
    APP_ID = int(os.environ.get("APP_ID", 18622297))
    # 6 is a placeholder
    API_HASH = os.environ.get("API_HASH", "27e6993af0786f66f96599db6cd10bcc")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzoBu1HBcg1iJSTctkrkIJCFvC7K5jVDL6oMDM-3CbP6mclKkfNkfdwGf0a-tJpe_aI3-7_LKu786KkXHFNK-XJeDxStCTLPdKesz8RzpG4KOudgOTJcBP5tVZPeMUO-v_4cBR3zdGpyUhr7bLWiekzi5intfMEKj37LNZaMdMk6IheUcNCXIU9_GkCY29Ht23JRUq2Gcl1QziYoF8fMqnzxv1ybuX5SRvDupcDPbtltczrBQPT9yYDmrDAPZrSxVLXy4jMjf1gaDF6_SWMLoUiDMMYpQrwhtA1YBCp5Tm1DxAJDsrbLNsAVw-svL-Aqaoouzgq1SXZXi7xYmrRKOOZzGv8=")
    DB_URI = os.environ.get("DATABASE_URL", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./userbot/DOWNLOADS/")
    LOGGER = True
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    # Here for later purposes
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "1511373882").split())
    # Google Drive ()
    CHROME_BIN = os.environ.get("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
    CHROME_DRIVER = os.environ.get(
        "CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver"
    )
    WHITELIST_USERS = set(int(x) for x in os.environ.get("WHITELIST_USERS", "").split())
    BLACKLIST_USERS = set(int(x) for x in os.environ.get("BLACKLIST_USERS", "").split())
    DEVLOPERS = set(int(x) for x in os.environ.get("DEVLOPERS", "").split())
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "").split())
    EMOJI = os.environ.get("EMOJI", "📨")
    SUPPORT_USERS = set(int(x) for x in os.environ.get("SUPPORT_USERS", "").split())
    PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL", -1001726870449)) 
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    #dont Kang this 
    botnickname = os.environ.get("BOT_NICK_NAME", None)
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", 5039520811:AAHnjUTBahKcc0uKKFjOHnQA5wtgp1GD-z4)
    TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", @SuperBotestvps_bot)
    DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", None)
    PM_PERMIT_GROUP_ID = os.environ.get("PM_PERMIT_GROUP_ID", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    if AUTH_TOKEN_DATA != None:
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
        t_file = open(TEMP_DOWNLOAD_DIRECTORY+"auth_token.txt","w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    PRIVATE_GROUP_ID = os.environ.get("PRIVATE_GROUP_ID", -1001726870449)
    if PRIVATE_GROUP_ID != None:
        try:
            PRIVATE_GROUP_ID = int(PRIVATE_GROUP_ID)
        except ValueError:
            raise ValueError("Invalid Private Group ID. Make sure your ID is starts with -100 and make sure that it is only numbers.")


class Development(Var):
    LOGGER = True
    # Here for later purposes
