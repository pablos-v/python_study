import ui
import logic

def launch():
    str = ui.inp()
    res = logic.solve(str)
    # logging
    ui.output(res)