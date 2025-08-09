import cs_bot
from cs_bot import MessageSession
from cs_bot.permissions import ANYONE

@cs_bot.on_prefix(["hello"], permission=ANYONE)
def hello(session: MessageSession):
    logger.info(f"receive message: {session.message)
    session.send(session.sender.email, session.message.content.lstrip("Waaaaall-e"))
