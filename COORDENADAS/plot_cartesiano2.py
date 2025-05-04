import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox, Slider
from mpl_toolkits.mplot3d import Axes3D

# Inicializa o estado do programa
is_3d = False  # Começa no modo 2D

# Definir altura comum
common_y = 0.02
height = 0.07

# Função para limpar todas as variáveis
def clear_variables():
    global x_coords, y_coords, z_coords
    x_coords = []
    y_coords = []
    z_coords = []

# Função para construir o modo 2D
def build_2d():
    global ax, text_box_x, text_box_y, button_add
    
    clear_variables()
    ax.clear()  # Limpa apenas o conteúdo do gráfico
    ax.set_xlim(-10, 10)  # Define os limites do eixo X
    ax.set_ylim(-10, 10)  # Define os limites do eixo Y
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_title('Plano Cartesiano 2D')

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

# Função para construir o modo 3D
def build_3d():
    global ax, text_box_x, text_box_y, text_box_z, button_add
    
    clear_variables()
    ax.clear()  # Limpa apenas o conteúdo do gráfico
    ax = fig.add_subplot(111, projection='3d')  # Recria o gráfico como 3D
    ax.set_xlim(-10, 10)  # Define os limites do eixo X
    ax.set_ylim(-10, 10)  # Define os limites do eixo Y
    ax.set_zlim(-10, 10)  # Define os limites do eixo Z
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_zlabel('Eixo Z')
    ax.set_title('Plano Cartesiano 3D')

    # Adiciona caixas de texto para entrada de coordenadas
    axbox_x = plt.axes([0.1, 0.01, 0.2, 0.075])
    text_box_x = TextBox(axbox_x, 'X: ')
    
    axbox_y = plt.axes([0.4, 0.01, 0.2, 0.075])
    text_box_y = TextBox(axbox_y, 'Y: ')

    axbox_z = plt.axes([0.7, 0.01, 0.2, 0.075])
    text_box_z = TextBox(axbox_z, 'Z: ')

    # Adiciona botão para adicionar ponto
    ax_button_add = plt.axes([0.85, 0.01, 0.1, 0.075])
    button_add = Button(ax_button_add, 'Add\nPonto')
    button_add.on_clicked(add_point_3d)

    fig.canvas.draw_idle()  # Redesenha o gráfico

# Função para alternar entre 2D e 3D
def toggle_3d_2d(event):
    global is_3d
    is_3d = not is_3d
    if is_3d:
        build_3d()
    else:
        build_2d()

# Função para adicionar ponto no modo 2D
def add_point_2d(event):
    try:
        x = float(text_box_x.text)
        y = float(text_box_y.text)
        x_coords.append(x)
        y_coords.append(y)
        ax.scatter(x_coords, y_coords, color='blue')
        ax.plot(x_coords, y_coords, color='red', linestyle='-', linewidth=2)
        for x, y in zip(x_coords, y_coords):
            ax.text(x, y, f'({x},{y})', size=10, zorder=1)
        fig.canvas.draw_idle()
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números válidos.")

# Função para adicionar ponto no modo 3D
def add_point_3d(event):
    try:
        x = float(text_box_x.text)
        y = float(text_box_y.text)
        z = float(text_box_z.text)
        x_coords.append(x)
        y_coords.append(y)
        z_coords.append(z)
        ax.scatter(x_coords, y_coords, z_coords, color='blue')
        ax.plot(x_coords, y_coords, z_coords, color='red', linestyle='-', linewidth=2)
        for x, y, z in zip(x_coords, y_coords, z_coords):
            ax.text(x, y, z, f'({x},{y},{z})', size=10, zorder=1)
        fig.canvas.draw_idle()
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números válidos.")

# Inicializa o gráfico
fig = plt.figure(figsize=(15, 12), facecolor='black')  # Tamanho da figura
fig.patch.set_facecolor('lightgray')  # Cor de fundo da figura
ax = fig.add_subplot(111)
plt.subplots_adjust(left=0.25, bottom=0.3)

# Adiciona botão para alternar entre 2D e 3D
fig.add_subplot()
ax_button_toggle = plt.axes([0.85, 0.12, 0.1, height])
button_toggle = Button(ax_button_toggle, '2D-3D')
button_toggle.on_clicked(toggle_3d_2d)
fig.canvas.draw_idle()

# Inicializa no modo 2D
build_2d()
#
manager = plt.get_current_fig_manager()
try:
    manager.window.wm_geometry("+500+200")  # (x, y) posição da janela
except:
    pass  # Se não der, ignora (depende do sistema)
# Exibe o gráfico
plt.show()
