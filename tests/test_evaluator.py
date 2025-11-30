from agents.evaluator import Evaluator
def test_evaluator_instantiation():
    ev = Evaluator(config={'recent_window_days':7,'baseline_window_days':28})
    assert ev is not None
