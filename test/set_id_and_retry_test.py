import pytest
import allure


@pytest.mark.parametrize("test_id", [140988, 140989])
@allure.severity(allure.severity_level.NORMAL)
def test_refactored(test_id):
    allure.dynamic.id(test_id)


@allure.id(140987)
@allure.severity(allure.severity_level.CRITICAL)
def test_renamed():
    pass

@allure.severity(allure.severity_level.MINOR)
def test_new_test_with_severity():
    pass

@allure.severity(allure.severity_level.TRIVIAL)
def test_one_more_new_test_with_severity():
    pass

@allure.label("layer", "UI Tests")
def test_ui_test():
    pass


@pytest.mark.parametrize(["a", "b"], [(1, "a"), (2, "b")])
def test_parametrized(a, b):
    pass
