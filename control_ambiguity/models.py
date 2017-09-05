from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'CA'
    players_per_group = None
    num_rounds = 1
    endowment = c(10)
    number_remove_low= 1
    number_remove_high = 5


class Subsession(BaseSubsession):

     def before_session_starts(self):
        self.replacement_decision()

     def replacement_decision(self):
         for player in self.get_players():
            player.number_remove = random.choice([Constants.number_remove_low, Constants.number_remove_high])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    number_remove = models.CharField()
    
    wtp_remove = models.CurrencyField(
    	min=0,
    	max=10,
    	#choices=currency_range(c(0.00), c(10.00), c(0.1)),
    	widget=widgets.SliderInput(attrs={'step': '0.1'}),
    	verbose_name="Which price would you pay to remove ??? balls?",
    	doc="player_wtp_to_remove_balls"
    	)