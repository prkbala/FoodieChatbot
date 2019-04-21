from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-613530136404-602615234659-614037528997-95186e09fda2ba57f12b4f16a2e31bd6', #app verification token
							'xoxb-613530136404-607784380305-sg5QzREJGhtVkWhXii6btYQ4', # bot verification token
							'W7nPmxNi43uDlOjDKSZWx7xw', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))