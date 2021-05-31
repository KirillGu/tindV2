from handler.base_handler import BaseHandler


class GreetingsHandler(BaseHandler):

    def keywords(self):
        return ['Hi', 'Hello', 'ВКиндер']

    def handle_impl(self, _message):
        self.write_msg(f'Добро пожаловать в ВКиндер!\n ' \
                   f'Сервис предназначенный для романтических знакомств в соответствии с заданными параметрами ' \
                   f'(возраст, пол, город, семейное положение), с учётом геолокации.\n' \
                   f'Напишите "Старт" для начала работы')
