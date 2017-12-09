import pygal
import pandas as pd
from pygal.style import Style
style1 = Style(
  background='#343a40',
  plot_background='#000000',
  foreground='#FFFFFF',
  foreground_strong='#FFFFFF',
  foreground_subtle='#FFFFFF',
  colors=('#FFFFFF', '#B7B5B2', '#E95355'))

df = pd.read_excel(pd.ExcelFile('RHINO_2000_2014.xlsx'))
line_chart = pygal.Line(title=u'ปริมาณแรดที่ถูกล่า', x_title='ปี ค.ศ.',y_title='จำนวน', style = style1, fill = True)
line_chart.x_labels = map(str, range(2011, 2015))
line_chart.add('ปริมาณแรดที่ถูกล่า', [448, 668, 1004, 1215])
line_chart.render_to_file('pochx2.svg')
