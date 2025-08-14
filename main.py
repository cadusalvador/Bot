import cs_bot
from cs_bot import StartupConfig
from cs_bot.adapters import sop_bot


config = {
    "adapter": {
        "app_id": "ODI1ODIyODY0NDYy",
        "app_secret": "5srPiZuFhH84GkUl2qqjRFBDuFnlQZQ4",
        "signing_secret": "4MPu_ZvbEOUIaAohr4leF09VwG2sKutB"
    }
}

cs_bot.init(StartupConfig.parse_obj(config))
cs_bot.register_adapter(sop_bot.Adapter)
cs_bot.load_plugin("plugin.hello")


if __name__ == '__main__':
    cs_bot.run(host="0.0.0.0", port=5000)
