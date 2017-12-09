import pygal
import pandas as pd
from pygal.style import Style
style1 = Style(
  background='#343a40',
  plot_background='#000000',
  foreground='#FFFFFF',
  foreground_strong='#FFFFFF',
  foreground_subtle='#FFFFFF',
  colors=('#39ff14', '#8B8B8A', '#E95355'))

df = pd.read_excel(pd.ExcelFile('for2.xlsx'))
line_chart = pygal.Line(title=u'พื้นที่ป่าในแอฟริกา', x_title='ปี ค.ศ.',y_title='ha', style = style1, fill = True)
line_chart.x_labels = map(str, [1990,2000,2005,2010])
line_chart.add('ปริมาณป่า', df['for'])
line_chart.render_to_file('for2.svg')
