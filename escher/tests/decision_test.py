from unittest import TestCase

from autodec.decision import Decision


class TestDecision(TestCase):
    def test_simple_model(self):
        model = Decision('model', fp='C:/Users/perus/Desktop')
        model.add_variable('benefits')
        model.add_variable('costs')
        model.sample(1000)
        self.assertIsNotNone(model.last_run)
        model.set_loss('benefits - costs')
        self.assertTrue('loss' in model.last_run.columns)
