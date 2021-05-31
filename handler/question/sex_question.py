from handler.question.base_question import BaseQuestion


class SexQuestion(BaseQuestion):
    def question(self):
        return 'Введите ваш пол (1-м, 2-ж, 0-не имеет значения)'

    def is_valid_answer(self, answer, params):
        try:
            answer = int(answer)
            return answer in [1, 2, 0]
        except ValueError:
            return False

    def get_param_name(self):
        return 'sex'
