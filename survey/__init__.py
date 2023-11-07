from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
   
    gender = models.StringField(
        choices=[['Kisumu', 'Kisumu'], ['Nairobi', 'Nairobi'], ['Mombasa', 'Mombasa']],
        label='What is the capital City of Kenya?',
        widget=widgets.RadioSelect,
    )
    math = models.IntegerField(label='What is 14 + 15 ?', min=29, max=29)
    crt_bat = models.IntegerField(
        label='''
        What is the population of Kenya?
        '''
    )
    


# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['gender', 'math']


class CognitiveReflectionTest(Page):
    form_model = 'player'
    form_fields = ['crt_bat']


page_sequence = [Demographics, CognitiveReflectionTest]
