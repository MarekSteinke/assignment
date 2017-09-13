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
    number_remove_low = 1
    number_remove_high = 5
    #Use next line for choosing one treatment
    #number_remove = ???


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for player in self.get_players():
            if 'treatment' in self.session.config:
                player.treatment = self.session.config['treatment']
            else:
                player.treatment = random.choice(['high', 'low'])
            player.number_remove = Constants.number_remove_high if player.treatment == 'high' else Constants.number_remove_low



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    number_remove = models.CharField()

    wtp_remove = models.CurrencyField(
    	min=0,
    	max=10,
    	#alternative code: choices=currency_range(c(0.00), c(10.00), c(0.1)),
    	widget=widgets.SliderInput(attrs={'step': '0.1'}),
    	verbose_name="Which price would you pay to remove the balls?",
    	doc="player's wtp to remove the balls"
    	)

    replacement_price = models.CurrencyField()

    def replacement_price_decission(self):
        self.replacement_price = random.randint(0, 10)


    modification = models.CharField()

    def modification_decision(self):
        if self.wtp_remove >= self.replacement_price:
            self.modification = "did"
        else:
            self.modification = "did not"

    gender = models.CharField(
        choices=["female", "male", "other"],
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="What is your gender?",
        doc="participant's gender"
        )

    age = models.PositiveIntegerField(
    	verbose_name="How old are you?",
    	doc="participant's gender"
    )

    #def calculate_payoff(self):
    	#if self.modification == "did" and self.ball == "green":
    		#self.payoff = Constants.endowment - self.replacement_price + 10
    	#elif self.modification == "did" and self.ball == "red":
    		#self.payoff = Constants.endowment - self.replacement_price
    	#elif self.modification == "did not" and self.ball == "green":
    		#self.payoff = Constants.endowment + 10
    	#else:
    		#self.payoff = Constants.endowment