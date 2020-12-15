import leather

data = [
    ('Hello', 3),
    ('How', 5,),
    ('Are', 9),
    ('You', 4)
]

chart = leather.Chart('Ordinal')
chart.add_columns(data)
chart.to_svg('examples/charts/ordinal.svg')
