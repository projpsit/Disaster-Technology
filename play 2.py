import pygal
import pandas as pd
df = pd.read_excel(pd.ExcelFile('ปริมาณอาญากรรม.xlsx'))
line_chart = pygal.Line(title=u'จำนวนประชากรที่ใช้คอมพิวเตอร์เล่นเกมส์เทียบกับปริมาณอาชญากรรม', x_title='ปี พ.ศ.',y_title='จำนวน')
line_chart.x_labels = map(str, range(2554, 2560))
line_chart.add('จำนวนคนใช้คอมเล่นเกม (x1000)', df['play'])
line_chart.add('ปริมาณอาชญากรรม', df['crime'])
line_chart.render_to_file('play2.svg')
