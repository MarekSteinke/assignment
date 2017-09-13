from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def before_next_page(self):
        self.player.replacement_price_decission()


class Choice(Page):
    
    form_model = models.Player
    form_fields = ["wtp_remove"]
    def before_next_page(self):
        self.player.modification_decision()
    
    


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Information(Page):
    pass


class Results(Page):
    pass


class Demographics(Page):
    form_model = models.Player
    form_fields = ["age", "gender", "risk", "country"]


class EndPage(Page):
    pass


page_sequence = [
    Introduction,
    Choice,
    ResultsWaitPage,
    Information,
    Results,
    Demographics,
    EndPage
]
