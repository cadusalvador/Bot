import cs_bot
from cs_bot import MessageSession, logger
from cs_bot.adapters import sop_bot
import os

APP_ID = os.getenv("SEATALK_APP_ID")
APP_SECRET = os.getenv("SEATALK_APP_SECRET")
SIGNING_SECRET = os.getenv("SEATALK_SIGNING_SECRET")


config = {
    "adapter": {
        "app_id": APP_ID,
        "app_secret": APP_SECRET,
        "signing_secret": SIGNING_SECRET
    }
}

cs_bot.init(StartupConfig.parse_obj(config))
cs_bot.register_adapter(sop_bot.Adapter)
cs_bot.load_plugin("plugin.hello")


if __name__ == '__main__':
    cs_bot.run(host="0.0.0.0", port=int(os.getenv("PORT"))
