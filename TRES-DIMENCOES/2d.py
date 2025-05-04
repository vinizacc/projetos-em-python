import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox

# Limites da janela
point = 100
pointNeg = -100

# Função para limpar todas as variáveis
def clear_variables():
    global x_coords, y_coords
    x_coords = []
    y_coords = []

# Função para construir o modo 2D
def build_2d():
    global ax, text_box_x, text_box_y, button_add
    
    clear_variables()
    ax.clear()  # Limpa apenas o conteúdo do gráfico
    ax.set_xlim(pointNeg, point)  # Define os limites do eixo X
    ax.set_ylim(pointNeg, point)  # Define os limites do eixo Y
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_title('Plano Cartesiano 2D')

    # Adiciona linhas infinitas nos eixos X e Y
    ax.axhline(0, color='black', linestyle='-', linewidth=0.8)  # Linha horizontal infinita
    ax.axvline(0, color='black', linestyle='-', linewidth=0.8)  # Linha vertical infinita
    ax.legend(['Eixo X', 'Eixo Y'], loc='upper left')  # Adiciona uma legenda para os eixos
    
    # Adiciona linhas de grade (quadriculado)
    ax.set_xticks(range(pointNeg, point + 1, 100), minor=True)  # Linhas a cada 10 unidades no eixo X
    ax.set_yticks(range(pointNeg, point + 1, 100), minor=True)  # Linhas a cada 10 unidades no eixo Y
    ax.set_xticks(range(pointNeg, point + 1, 10), minor=True)  # Linhas a cada 10 unidades no eixo X
    ax.set_yticks(range(pointNeg, point + 1, 10), minor=True)  # Linhas a cada 10 unidades no eixo Y
    
    ax.grid(which='minor', color='lightgrey', linestyle='--', linewidth=0.5)  # Configura a grade
    ax.scatter(0, 0, color='red', s=40, label='Origem (0, 0)')  # Adiciona o ponto na origem
    
    # Adiciona caixas de texto para entrada de coordenadas
    axbox_x = plt.axes([0.1, 0.01, 0.2, 0.075])
    text_box_x = TextBox(axbox_x, 'X: ')

    axbox_y = plt.axes([0.4, 0.01, 0.2, 0.075])
    text_box_y = TextBox(axbox_y, 'Y: ')

    # Adiciona botão para adicionar ponto
    ax_button_add = plt.axes([0.85, 0.01, 0.1, 0.075])
    button_add = Button(ax_button_add, 'Add\nPonto')
    button_add.on_clicked(add_point_2d)

    fig.canvas.draw_idle()  # Redesenha o gráfico

# Função para adicionar ponto no modo 2D
def add_point_2d(event):
    try:
        x = float(text_box_x.text)
        y = float(text_box_y.text)
        x_coords.append(x)
        y_coords.append(y)
        ax.scatter(x_coords, y_coords, color='blue')
        for x, y in zip(x_coords, y_coords):
            ax.text(x, y, f'({x},{y})', size=10, zorder=1)
            ax.plot([0, x], [y, y], color='grey', linestyle='--', linewidth=1)
            ax.plot([x, x], [0, y], color='grey', linestyle='--', linewidth=1)
            
        fig.canvas.draw_idle()
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números válidos.")

# Função para zoom com o scroll do mouse
def zoom(event):
    base_scale = 1.1  # Scale factor for zooming
    cur_xlim = ax.get_xlim()
    cur_ylim = ax.get_ylim()

    xdata = event.xdata  # Get mouse x position
    ydata = event.ydata  # Get mouse y position

    if event.button == 'up':  # Zoom in
        scale_factor = 1 / base_scale
    elif event.button == 'down':  # Zoom out
        scale_factor = base_scale
    else:
        return

    # Adjust limits
    new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
    new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor

    relx = (cur_xlim[1] - xdata) / (cur_xlim[1] - cur_xlim[0])
    rely = (cur_ylim[1] - ydata) / (cur_ylim[1] - cur_ylim[0])

    ax.set_xlim([xdata - new_width * (1 - relx), xdata + new_width * relx])
    ax.set_ylim([ydata - new_height * (1 - rely), ydata + new_height * rely])

    fig.canvas.draw_idle()  # Redraw the canvas

# Funções para arrastar o gráfico
press_event = None

def start_pan(event):
    """Start panning when the left mouse button is pressed."""
    if event.button == 1 and event.inaxes:  # Left mouse button
        global press_event
        press_event = event  # Save the initial press event

def pan(event):
    """Pan the graph when the mouse is moved."""
    if press_event is None or event.inaxes != ax:
        return

    dx = event.xdata - press_event.xdata  # Change in x
    dy = event.ydata - press_event.ydata  # Change in y

    cur_xlim = ax.get_xlim()
    cur_ylim = ax.get_ylim()

    ax.set_xlim(cur_xlim[0] - dx, cur_xlim[1] - dx)
    ax.set_ylim(cur_ylim[0] - dy, cur_ylim[1] - dy)

    fig.canvas.draw_idle()  # Redraw the canvas

def end_pan(event):
    """End panning when the mouse button is released."""
    global press_event
    press_event = None  # Reset the press event

# Inicializa o gráfico
fig = plt.figure(figsize=(15, 12), facecolor='black')  # Tamanho da figura
fig.patch.set_facecolor('lightgray')  # Cor de fundo da figura
ax = fig.add_subplot(111)
plt.subplots_adjust(left=0.10, bottom=0.15, right=0.96, top=0.93, wspace=0.19, hspace=0.19)

# Maximiza a janela ao iniciar
manager = plt.get_current_fig_manager()
manager.window.state('zoomed')  # Maximiza a janela (funciona no Windows)

# Conecta os eventos de scroll e arrasto
fig.canvas.mpl_connect('scroll_event', zoom)
fig.canvas.mpl_connect('button_press_event', start_pan)
fig.canvas.mpl_connect('motion_notify_event', pan)
fig.canvas.mpl_connect('button_release_event', end_pan)

# Inicializa no modo 2D
build_2d()

# Exibe o gráfico
plt.show()
