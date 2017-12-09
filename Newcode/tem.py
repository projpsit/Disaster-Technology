import pygal
import pandas as pd
from pygal.style import Style
style1 = Style(
  background='#343a40',
  plot_background='#000000',
  foreground='#FFFFFF',
  foreground_strong='#FFFFFF',
  foreground_subtle='#FFFFFF',
  colors=('#FF0000', '#FF9605', '#E95355', '#E87653', '#E89B53'))

show_list=[]
df = pd.read_excel(pd.ExcelFile('Climate_Glance_1970_2016.xlsx'))
line_chart = pygal.Line(title=u'อัตราการเปลี่ยนแปลงอุณหภูมิของโลก', x_title='ปี ค.ศ.',y_title='%', style = style1)
line_chart.x_labels = map(str, range(1970, 2017))
for i in range(1970,1997):
    show_list.append(None)
show_list += [0.52,0.63,0.44,0.42,0.54,0.6,0.61,0.58,0.66,0.61,0.61,0.54,0.64,0.7]
line_chart.add('Degree celcius', df['Value'])
line_chart.add('Degree celcius', show_list)
line_chart.render_to_file('tem1.svg')
