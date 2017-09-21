from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def before_next_page(self):
        self.player.replacement_price_decission()


class Choice(Page):
    
    form_model = models.Player
    form_fields = ["wtp_remove", "expected_green_balls"]
    def before_next_page(self):
        self.player.modification_decision()
    
    


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Information(Page):
    pass


class Input(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1
    form_model = models.Group
    form_fields = ["no_modification_ball", "one_modified_ball", "five_modified_balls"]



class WaitForInput(WaitPage):
    def after_all_players_arrive(self):
        self.group.calculate_payoff()


class Results(Page):
        pass
        


class Demographics(Page):
    form_model = models.Player
    form_fields = ["age", "gender", "risk", "country", "field_of_study", "no_student"]

    def error_message(self, answer):
        if answer["no_student"] == "Non-student" and answer["field_of_study"] != None:
            return "Please don't fill in a field of study if you are a non-student"
        


class EndPage(Page):
    pass


page_sequence = [
    Introduction,
    Choice,
    ResultsWaitPage,
    Information,
    Input,
    WaitForInput,
    Results,
    Demographics,
    EndPage
]
