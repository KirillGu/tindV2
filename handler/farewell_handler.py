from handler.base_handler import BaseHandler


class FarewellHandler(BaseHandler):

    def keywords(self):
        return ['Пока', 'Досвидания', 'Увидимся']

    def handle_impl(self, _message):
        self.write_msg(f'Возвращайся')
