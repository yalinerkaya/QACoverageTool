import analisys
import pandas as pd

test = ((1, "f", "new", "new", "a"),
        (2, "f", "trade", "pfilled", "s"),
        (3, "f", "cancel", "canceled", "d"),
        (1, "s", "new", "new", "f"),
        (2, "s", "trade", "filled", "f"),
        (1, "t", "new", "new", "r"),
        (2, "t", "amend", "new", "d"),
        (3, "t", "cancel", "canceled", "a"),
        (1, "d", "new", "new", "r"),
        (2, "d", "amend", "reject", "d"),
        (3, "d", "amend", "new", "a"),
        (4, "d", "cancel", "canceled", "a"),
        (1, "r", "new", "new", "a"),
        (2, "r", "trade", "pfilled", "s"),
        (3, "r", "cancel", "canceled", "d"),)

df = pd.DataFrame(test, columns=["seq", "ord", "trans", "state", "test"])


