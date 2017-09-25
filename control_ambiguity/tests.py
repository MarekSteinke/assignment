from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants
from otree.api import SubmissionMustFail


class PlayerBot(Bot):

    def play_round(self):
        if self.player.id_in_group ==1:
        	yield SubmissionMustFail (views.PasswordPage, {'password': "tüdelü"})
        	yield (views.PasswordPage, {'password': "spamspam"})
        else:
        	pass
        yield(views.Introduction)
        yield SubmissionMustFail(views.Choice, {'wtp_remove': 15, 'expected_green_balls': 15})
        yield (views.Choice, {'wtp_remove': 5, 'expected_green_balls': 5})
        yield(views.Information)
        if self.player.id_in_group == 1:
            yield (views.Input, {'no_modification_ball': "green", 'one_modified_ball': "green", 'five_modified_balls': "green"})
        else:
        	pass
        yield(views.Results)
        yield SubmissionMustFail(views.Demographics, {'age': -3, 'gender': "male", 'risk': 8, 'country': "AT"})
        yield SubmissionMustFail(views.Demographics, {'age': 55, 'gender': "male", 'risk': 4, 'country': "AT", 'no_student': True, 'field_of_study': "spam"})
        yield(views.Demographics, {'age': 55, 'gender': "male", 'risk': 4, 'country': "AT", 'no_student': True, 'field_of_study': ""})