from libqtile.config import Group

primary_groups   = ["1", "2", "3", "4", "5", "6"]
secondary_groups = ["1b", "2b", "3b", "4b", "5b", "6b"]

# Los grupos "b" son la pareja de cada escritorio en el monitor externo
grupos = [Group(i) for i in primary_groups + secondary_groups]