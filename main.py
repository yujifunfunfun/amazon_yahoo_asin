import eel
from fetch_item_data import *


@eel.expose
def main(filter):
    fetch_item_data(filter)

eel.init("web")
eel.start("main.html",size=(600, 600))


