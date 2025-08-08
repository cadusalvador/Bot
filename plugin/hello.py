import cs_bot
from cs_bot import MessageSession
from cs_bot.permissions import ANYONE

@cs_bot.on_prefix([""])
def saudacao(session: MessageSession):
    session.send(session.sender.email, "Waaaaall-e")
