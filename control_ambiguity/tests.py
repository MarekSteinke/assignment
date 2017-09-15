from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield(views.Introduction)
        yield (views.Choice, {'wtp_remove': 5, 'expected_green_balls': 5})
        yield(views.Information)
        if self.player.id_in_group == 1:
            yield (views.Input, {'no_modification_ball': "green", 'one_modified_ball': "green", 'five_modified_balls': "green"})
        else:
        	pass
        yield(views.Results)
        yield(views.Demographics, {'age': 55, 'gender': "male", 'risk': 4, 'country': "AT"})