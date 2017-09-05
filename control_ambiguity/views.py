from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class Choice(Page):
	form_model = models.Player
	form_fields = ["wtp_remove"]

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Introduction,
    Choice,
    ResultsWaitPage,
    Results
]
