from actions import (NeedInput, CreateDecision, DecisionLoadedConfirmation,
                     LoadDecision, ListDecisions, ListDistributions)


class BaseGoal(object):
    def __init__(self):
        self.actions = []


class StartNewDecision(BaseGoal):
    def __init__(self):
        self.name = "Start New Decision"
        self.actions = [NeedInput('Decision Name', str),
                        CreateDecision(),
                        DecisionLoadedConfirmation()]


class LoadExistingDecision(BaseGoal):
    def __init__(self):
        self.name = "Load Decision"
        self.actions = [ListDecisions(),
                        NeedInput('Decision Name', str),
                        LoadDecision(),
                        DecisionLoadedConfirmation()]


class ConfigureCost(BaseGoal):
    def __init__(self):
        self.name = "Configure Costs"
        self.actions = [NeedInput('Cost Name', str),
                        ListDistributions(),
                        NeedInput('Cost Distribution', str),
                        NeedInput('Cost Lower Bound', float),
                        NeedInput('Cost Upper Bound', float),
                        AddVariable('Cost Name',
                                    'Cost Distribution',
                                    'Cost Lower Bound',
                                    'Cost Upper Bound')]


class ConfigureBenefit(BaseGoal):
    def __init__(self):
        self.name = "Configure Benefits"
        self.actions = []


class ConfigureLoss(BaseGoal):
    def __init__(self):
        self.name = "Configure Loss Fucntion"
        self.actions = []
