import pygal
line_chart = pygal.Line()
line_chart.title = 'จำนวนประชากรที่ใช้คอมพิวเตอร์เล่นเกมส์ อายุ 6 ปีขึ้นไป'
line_chart.x_labels = map(str, range(2554, 2560))
line_chart.add('จำนวนคน (x1000)', [1094.7691, 1261.6037, 1451.9303, 1671.1252, 1563.9080, 1308.1442])
line_chart.add('ปริมาณอาชญากรรม', [4558, 4760, 4744, 4148, 3875, 3823.6])
line_chart.render_to_png('play.png')
