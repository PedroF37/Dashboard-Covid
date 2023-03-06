# -------------------------------------------------------------------------- #
# IMPORTAÇÕES


# tkinter
from tkinter import Tk, Frame, Label
from tkinter.ttk import Style, Treeview, Separator, Scrollbar

# matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# views
from views import *


# -------------------------------------------------------------------------- #
# CONSTANTES


# Cores
COLOR1 = '#feffff'  # Branco
COLOR2 = '#3a3a4d'  # Fundo
COLOR3 = '#403d3d'  # Letra
COLOR4 = '#6f9fbd'  # Azul

COLORS_BAR = [
    '#665191', '#a05195', '#d45087',
    '#f95d6a', '#ff7c43', '#ffa600'
]

COLORS_PIE = [
    '#5588bb', '#66bbbb', '#aa6644',
    '#99bb55', '#ee9944', '#444466'
]


# -------------------------------------------------------------------------- #
# JANELA


window = Tk()
window.title('')
window.resizable(0, 0)
window.geometry('1100x550')


style = Style(window)
style.theme_use('clam')


# -------------------------------------------------------------------------- #
# FRAMES


title_frame = Frame(
    window, width=1100, height=50,
    pady=0, padx=0, bg=COLOR1
)
title_frame.grid(row=0, column=0)

Separator(
    window, orient='horizontal'
).grid(
    row=1, columnspan=1, ipadx=550
)

parent_frame = Frame(
    window, width=1100, height=500,
    pady=10, padx=10, bg=COLOR2
)
parent_frame.grid(row=2, column=0, sticky='nw')


# -------------------------------------------------------------------------- #
# CONFIGURANDO TITLE_FRAME


title_label = Label(
    title_frame, text='Dashboard de COVID-19',
    font=('Roboto 20 bold'), anchor='nw',
    bg=COLOR1, fg=COLOR3
)
title_label.place(x=5, y=20)


# -------------------------------------------------------------------------- #
# CONFIGURANDO PARENT_FRAME


# Total de Casos
total_cases_frame = Frame(
    parent_frame, width=178,
    height=70, bg=COLOR1
)
total_cases_frame.place(x=0, y=0)

line_label = Label(
    total_cases_frame, text='', width=2,
    height=10, pady=0, padx=0,
    font=('Roboto 1 bold'), anchor='nw',
    bg=COLOR4, fg=COLOR3
)
line_label.place(x=0, y=0)

total_cases_label = Label(
    total_cases_frame, text='Total de Casos',
    height=1, pady=0, padx=0,
    font=('Roboto 10 bold'), anchor='center',
    bg=COLOR1, fg=COLOR3
)
total_cases_label.place(x=10, y=5)

number_cases_label = Label(
    total_cases_frame, text=f"{totals[1]['Casos']:,.0f}",
    height=1, pady=0, padx=0,
    font=('Roboto 16'), anchor='center',
    bg=COLOR1, fg=COLOR3
)
number_cases_label.place(x=20, y=35)


# Total de Recuperados
total_recovered_frame = Frame(
    parent_frame, width=178,
    height=70, bg=COLOR1
)
total_recovered_frame.place(x=188, y=0)

line_label = Label(
    total_recovered_frame, text='', width=2,
    height=10, pady=0, padx=0,
    font=('Roboto 1 bold'), anchor='nw',
    bg=COLOR4, fg=COLOR3
)
line_label.place(x=0, y=0)

total_recovered_label = Label(
    total_recovered_frame, text='Total de Recuperados',
    height=1, pady=0, padx=0,
    font=('Roboto 10 bold'), anchor='center',
    bg=COLOR1, fg=COLOR3
)
total_recovered_label.place(x=10, y=5)

number_recovered_label = Label(
    total_recovered_frame, text=f"{totals[1]['Recuperados']:,.0f}",
    height=1, pady=0, padx=0,
    font=('Roboto 16'), anchor='center',
    bg=COLOR1, fg=COLOR3
)
number_recovered_label.place(x=20, y=35)


# Total de Mortos
total_deaths_frame = Frame(
    parent_frame, width=178,
    height=70, bg=COLOR1
)
total_deaths_frame.place(x=376, y=0)

line_label = Label(
    total_deaths_frame, text='', width=2,
    height=10, pady=0, padx=0,
    font=('Roboto 1 bold'), anchor='nw',
    bg=COLOR4, fg=COLOR3
)
line_label.place(x=0, y=0)

total_deaths_label = Label(
    total_deaths_frame, text='Total de Mortes',
    height=1, pady=0, padx=0,
    font=('Roboto 10 bold'), anchor='center',
    bg=COLOR1, fg=COLOR3
)
total_deaths_label.place(x=10, y=5)

number_deaths_label = Label(
    total_deaths_frame, text=f"{totals[1]['Mortes']:,.0f}",
    height=1, pady=0, padx=0,
    font=('Roboto 16'), anchor='center',
    bg=COLOR1, fg=COLOR3
)
number_deaths_label.place(x=20, y=35)


# --- GRÁFICO BARRA --- #


# Top de 5 Países mais afetados
top_five_frame = Frame(
    parent_frame, width=200,
    height=500, bg=COLOR1
)
top_five_frame.place(x=560, y=0)

# Valores para gráfico
countries = [item[0] for item in top_countries]
values_list = [item[1] for item in top_countries]

# Container do gráfico e os eixos
figure = plt.Figure(figsize=(8.7, 3), dpi=60)
ax = figure.add_subplot(111)

# Grafico de barra horizontal
ax.barh(countries, values_list, align='center', color=COLORS_BAR)
ax.set_alpha(0.3)

# Configura os labels individuais das barras.
c = 0
for i in ax.patches:
    # get_width (esquerda/direita), get_y (cima/baixo)
    ax.text(
        i.get_width() + .3, i.get_y() + .50,
        str(values_list[c]), fontsize=12,
        verticalalignment='center', fontstyle='italic',
        weight='bold', color='dimgrey'
    )

    c += 1

# Formata os eixos do gráfico
ax.patch.set_facecolor('#FFFFFF')
ax.spines['bottom'].set_color('#CCCCCC')
ax.spines['bottom'].set_linewidth(1)
ax.spines['right'].set_linewidth(0)
ax.spines['top'].set_linewidth(0)
ax.spines['left'].set_color('#CCCCCC')
ax.spines['left'].set_linewidth(1)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')
ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(False)
ax.xaxis.grid(False)


graph_title_label = Label(
    top_five_frame, text='Top 5 Países mais afetados',
    height=1, pady=5, padx=0, anchor='nw',
    font=('Roboto 10 bold'), bg=COLOR1, fg=COLOR3
)
graph_title_label.grid(
    row=0, column=0, padx=20,
    pady=0, sticky='nsew'
)

top_five_canvas = FigureCanvasTkAgg(figure, top_five_frame)
top_five_canvas.get_tk_widget().grid(
    row=1, column=0,
    sticky='nsew', columnspan=2
)


# --- TABELA --- #

country_frame = Frame(parent_frame, width=700, height=500, bg=COLOR1)
country_frame.place(x=0, y=80)

# Estiliza a tabela
table_style = Style()
table_style.element_create('Custom.Treeheading.border', 'from', 'default')
table_style.layout('Custom.Treeview.Heading', [
    ('Custom.Treeheading.cell', {'sticky': 'nsew'}),
    ('Custom.Treeheading.border', {'sticky': 'nsew', 'children': [
        ('Custom.Treeheading.padding', {'sticky': 'nsew', 'children': [
            ('Custom.Treeheading.image', {'side': 'right', 'sticky': ''}),
            ('Custom.Treeheading.text', {'sticky': 'we'})
        ]})
    ]}),
])

table_style.configure(
    'Custom.Treeview.Heading', background='#494d4a',
    foreground='white', relief='raised'
)

table_style.map(
    'Custom.Treeview.Heading', relief=[
        ('active', 'groove'),
        ('pressed', 'sunken')
    ],
    background=[('selected', '#494d4a')]
)

# Cabeçalho da tabela
table_header = [
    'País', 'Confirmados',
    'Recuperados', 'Mortes',
    'Data'
]

tree = Treeview(
    country_frame, selectmode='extended',
    style='Custom.Treeview', height=18,
    columns=table_header, show='headings'
)

# Barra de rolagem vertical
vsb = Scrollbar(
    country_frame, orient='vertical',
    command=tree.yview
)

# Barra de rolagem horizontal
hsb = Scrollbar(
    country_frame, orient='horizontal',
    command=tree.xview
)

tree.configure(
    yscrollcommand=vsb.set,
    xscrollcommand=hsb.set
)

# Posicionamento
tree.grid(row=1, column=0, sticky='nsew')
vsb.grid(row=1, column=1, sticky='ns')
hsb.grid(row=2, column=0, sticky='ew')
country_frame.grid_rowconfigure(0, weight=2)

# Posicionamento do cabeçalho e dos dados
hd = ['nw', 'ne', 'ne', 'ne', 'center', 'center', 'center']
h = [140, 100, 100, 100, 91]
n = 0

for column in table_header:
    tree.heading(column, text=column, anchor='center')
    tree.column(column, width=h[n], anchor=hd[n])
    n += 1


# Coloca dados na tabela
[tree.insert('', 'end', values=item) for item in country_list]


# --- GRÁFICO PIE --- #


# Continentes
continent_frame = Frame(
    parent_frame, width=700,
    height=500, bg=COLOR1
)
continent_frame.place(x=562, y=220)


figure = plt.Figure(figsize=(8.65, 3.9), dpi=60)
ax = figure.add_subplot(111)

wedges, texts = ax.pie(
    values_continent_list, wedgeprops=dict(width=0.2),
    colors=COLORS_PIE, shadow=True, startangle=-90
)

bbox_props = dict(boxstyle='square, pad=0.3', fc='w', ec='k', lw=0.72)
kw = dict(
    arrowprops=dict(arrowstyle='-'),
    bbox=bbox_props, zorder=0, va='center'
)


# Não vou nem fingir que sei o que este código faz!!
# Tudo copy/paste!!
for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1) / 2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(
        names_continent_list[i], xy=(x, y),
        xytext=(1.35 * np.sign(x), 1.4 * y),
        horizontalalignment=horizontalalignment, **kw
    )


pie_title_label = Label(
    continent_frame, text='Continentes mais afetados',
    height=1, pady=5, padx=0, anchor='nw',
    font=('Roboto 10 bold'), bg=COLOR1, fg=COLOR3
)
pie_title_label.grid(
    row=0, column=0, padx=20,
    pady=0, sticky='nsew'
)

continent_canvas = FigureCanvasTkAgg(figure, continent_frame)
continent_canvas.get_tk_widget().grid(
    row=1, column=0,
    sticky='nsew', columnspan=2
)

# -------------------------------------------------------------------------- #
# LOOP


window.mainloop()


# -------------------------------------------------------------------------- #
