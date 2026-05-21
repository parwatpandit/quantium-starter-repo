import pytest
from dash.testing.application_runners import import_app

def test_header_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    assert dash_duo.find_element("h1").text == "Pink Morsel Sales Visualiser"

def test_visualisation_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    assert dash_duo.find_element("#sales-chart")

def test_region_picker_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    assert dash_duo.find_element("#region-filter")
    
# how to run the test 
# pytest test_app.py