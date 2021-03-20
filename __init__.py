from mycroft import MycroftSkill, intent_file_handler


class Exercicioinicio(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('exercicioinicio.intent')
    def handle_exercicioinicio(self, message):
        self.speak_dialog('exercicioinicio')


def create_skill():
    return Exercicioinicio()

