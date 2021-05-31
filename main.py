from vk_bot import VkBot
from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType
from sqlalchemy import orm
import sqlalchemy
from model.base import Base, user_to_candidate, Photo, User, Candidate


GROUP_TOKEN = ''
DSN = ''

vk = VkApi(token=GROUP_TOKEN)
long_poll = VkLongPoll(vk)

db_engine = sqlalchemy.create_engine(DSN, echo=True)
Base.metadata.create_all(db_engine)
DBSession = orm.sessionmaker(bind=db_engine)

with DBSession() as db_session:
    with db_session.begin():
        active_bots = {}

def main():
    def get_bot(user_id):
        if user_id not in active_bots:
            active_bots[user_id] = VkBot(user_id, vk, db_session)
        return active_bots[user_id]

    for event in long_poll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            bot = get_bot(event.user_id)
            bot.handle_new_message(event.text)

if __name__ == "__main__":
    main()
