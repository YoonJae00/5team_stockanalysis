from utils.stock_market import get_stock_history


def stock_plot(name):
    get_stock_history(name, 7)