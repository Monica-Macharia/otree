from otree.api import *

doc = """
Mini Ultimatum Game
"""

class Constants(BaseConstants):
    name_in_url = 'mini_ultimatum_game'
    players_per_group = 3
    num_rounds = 1
    initial_endowment = cu(200)

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        min=0,
        max=Constants.initial_endowment,
        label="How much do you want to send to Player 2?"
    )
    punish_decision = models.BooleanField(
        label="Choose one:",
        choices=[
            [True, "Punish Player 1"],
            [False, "Not Punish Player 1"],
        ]
    )

class Player(BasePlayer):
    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoffs(self):
        if self.group.punish_decision:
            self.payoff = cu(0)
            self.group.get_player_by_id(1).payoff = cu(0)
        else:
            self.payoff = Constants.initial_endowment - self.group.sent_amount
            self.group.get_player_by_id(1).payoff = self.group.sent_amount

class Introduction(Page):
    pass

class SendMoney(Page):
    form_model = 'group'
    form_fields = ['sent_amount']

class PunishDecision(Page):
    form_model = 'group'
    form_fields = ['punish_decision']

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'

class Results(Page):
    pass

page_sequence = [Introduction, SendMoney, PunishDecision, ResultsWaitPage, Results]
