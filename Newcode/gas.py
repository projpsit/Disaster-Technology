import pygal
import pandas as pd
from pygal.style import Style
style1 = Style(
  background='#343a40',
  plot_background='#000000',
  foreground='#FFFFFF',
  foreground_strong='#FFFFFF',
  foreground_subtle='#FFFFFF',
  colors=('#8B8B8A', '#8B8B8A', '#E95355'))

show_list = []
df = pd.read_excel(pd.ExcelFile('gas.xlsx'))
line_chart = pygal.Line(title=u'ปริมาณก๊าสคาร์บอนไดออกไซด์ในประเทศแอฟริกาใต้', x_title='ปี ค.ศ.',y_title='metric tons', style = style1)
line_chart.x_labels = map(str, range(1960, 2014))
line_chart.add('CO2', df['gas'])
for i in range(1960,1997):
    show_list.append(None)
show_list += [0.84,0.82,0.81,0.85,0.83,0.81,0.85,0.92,0.86,0.88,0.89,0.91,0.88,0.85]
line_chart.add('CO2', show_list)
line_chart.render_to_file('gas1.svg')
