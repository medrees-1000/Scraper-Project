import pytest
from playwright.sync_api import Page



def test_title(page: Page):
    page.goto("/")
    
    assert page.title() == "Swag Labs"
    
    

def test_inventory(page: Page):
    page.goto("/inventory.html")
    assert page.inner_text('h3') == "Epic sadface: Username is required"