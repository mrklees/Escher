from microsoftbotframework import ReplyToActivity
from decision import Decision
import goals
import pickle
from os import listdir
from os.path import isfile, join


class BaseAction(object):
    def __init__(self):
        self.prompt = False

    def act(self, bot, message):
        pass

    def process_response(self, bot, message):
        # Define if self.prompt is True
        pass


class NeedInput(BaseAction):
    def __init__(self, name, dtype):
        self.name = str(name)
        self.dtype = dtype
        self.prompt = True

    def act(self, bot, message):
        ReplyToActivity(fill=message,
                        text=f"Please provide the {self.name}.  We're " +
                             f"expecting a {str(self.dtype)}").send()

    def test_value(self, value):
        try:
            tv = self.dtype(value)
            return type(tv) == str
        except ValueError:
            print(f"Failed to convert {value} to dtype {self.dtype}")
            return False

    def process_response(self, bot, message):
        proposed_value = message['text']
        assert self.test_value(proposed_value)
        bot.variables[self.name] = proposed_value


class Greet(BaseAction):
    def act(self, bot, message):
        # Always good to be cordial!
        ReplyToActivity(fill=message,
                        text="Hi!! Welcome to the Automated Decision Toolkit" +
                        " I am cyDecide, and I'm here to support you in in " +
                        "your decision making! Ask for help at  any time if" +
                        " needed").send()


class ProvideAssisstance(BaseAction):
    def act(self, bot, message):
        if bot.decision is None:
            ReplyToActivity(fill=message,
                            text="To get started, tell me if you would like " +
                            "a start a new decision or load an existing one") \
                            .send()

        else:
            ReplyToActivity(fill=message,
                            text="")
