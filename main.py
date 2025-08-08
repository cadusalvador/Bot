import cs_bot
from cs_bot import StartupConfig
from cs_bot.adapters import sop_bot

config = {
    "adapter": {
        "app_id": "MjcxOTUyNjU4NTM0"
        "app_secret": "y1a5ibi-uFS77hJxpVH7u8dwdG8dT8Mk"
        "signing_secret": "TbApvXoDmJ9DNqy6M3ElPQLpFfcibU8a"
    }
cs_bot.init(StartupConfig.parse_obj(config))
cs_bot.register_adapter(sop_bot.Adapter)
cs_bot.load_plugin("plugin.hello")

if __name__ == "__main__":
    cs_bot.run(host="0.0.0.0", port=8000)
