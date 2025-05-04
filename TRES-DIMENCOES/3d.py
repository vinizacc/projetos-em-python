import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
from mpl_toolkits.mplot3d import Axes3D

# Função para limpar todas as variáveis
def clear_variables():
    global x_coords, y_coords, z_coords
    x_coords = []
    y_coords = []
    z_coords = []

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
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(left=0.25, bottom=0.3)

# Inicializa no modo 3D
build_3d()

# Exibe o gráfico
plt.show()
