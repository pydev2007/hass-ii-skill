from mycroft import MycroftSkill, intent_file_handler


class HassIi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ii.hass.intent')
    def handle_ii_hass(self, message):
        self.speak_dialog('ii.hass')


def create_skill():
    return HassIi()

