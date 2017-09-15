from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from django_countries.fields import CountryField

import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'CA'
    #enter the number of participants in players_per_group. Make sure that you open one link before all the participants!
    players_per_group = 3
    num_rounds = 1
    endowment = c(10)
    number_remove_low = 1
    number_remove_high = 5
    # For choosing one treatment, go to the settings file and replace in the session configs the #-sign in front of 'treatment' and either choose 'high' or 'low'


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for player in self.get_players():
            if 'treatment' in self.session.config:
                player.treatment = self.session.config['treatment']
            else:
                player.treatment = random.choice(['high', 'low'])
            player.number_remove = Constants.number_remove_high if player.treatment == 'high' else Constants.number_remove_low



class Group(BaseGroup):
    
    no_modification_ball = models.CharField(
    	choices=["green", "red"],
    	verbose_name="Color of ball from unmodified urn",
    	doc="Color of ball from unmodified urn"
    	)

    one_modified_ball = models.CharField(
    	choices=["green", "red"],
    	verbose_name="Color of ball from urn with one ball replaced",
    	doc="Color of ball from urn with one ball replaced"
    	)

    five_modified_balls = models.CharField(
    	choices=["green", "red"],
    	verbose_name="Color of ball from urn with five balls replaced",
    	doc="Color of ball from urn with five balls replaced"
    	)


    def calculate_payoff(self):
    	for Player in self.get_players():
    		if Player.modification == "did" and Player.number_remove == "1" and self.one_modified_ball == "green":
    		    Player.ball = "green"
    		elif Player.modification == "did" and Player.number_remove == "1" and self.one_modified_ball == "red":
    		    Player.ball = "red"
    		elif Player.modification == "did" and Player.number_remove == "5" and self.five_modified_balls == "green":
    		    Player.ball = "green"
    		elif Player.modification == "did" and Player.number_remove == "5" and self.five_modified_balls == "red":
    		    Player.ball = "red"
    		elif Player.modification == "did not" and self.no_modification_ball == "green":
    		    Player.ball = "green"
    		else:
    		    Player.ball = "red"

    		if Player.modification == "did" and Player.ball == "green":
    			Player.payoff = Constants.endowment - Player.replacement_price + 10
    		elif Player.modification == "did" and Player.ball == "red":
    			Player.payoff = Constants.endowment - Player.replacement_price
    		elif Player.modification == "did not" and Player.ball == "green":
    			Player.payoff = Constants.endowment + 10
    		else:
    			Player.payoff = Constants.endowment


class Player(BasePlayer):
    expected_green_balls = models.PositiveIntegerField(
    	min=0,
    	max=10,
    	verbose_name="How many green balls do you think are in the urn?",
    	doc="participant's expectation of amount of green balls"
    	)

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

    risk = models.IntegerField(
    	min=1,
    	max=7,
    	verbose_name="Please choose on a scale from 1 to 7 how likely you are to take risk (1 means extreamly unlikely and 7 means extreamly likely).",
    	doc="participant's willingness to take risk"
    	)

    country = CountryField(
    	verbose_name="Please choose your country of birth"
    	)

    ball = models.CharField()