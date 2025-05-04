import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox

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
    ax.set_xlim(-500, 500)  # Define os limites do eixo X
    ax.set_ylim(-500, 500)  # Define os limites do eixo Y
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_title('Plano Cartesiano 2D')

 # Adiciona uma linha passando pela origem (0, 0)
    ax.plot([500, 0], [0, 0], color='black', linestyle='-', linewidth=0.8)
    ax.legend(loc='upper left')  # Adiciona uma legenda para a linha

    ax.plot([-500, 0], [0, 0], color='black', linestyle='-', linewidth=0.8)  # Linha horizontal
    ax.legend(loc='upper left')  # Adiciona uma legenda para a linha

    ax.plot([0, 0], [-500, 500], color='black', linestyle='-', linewidth=0.8)  # Linha vertical
    ax.legend(loc='upper left')  # Adiciona uma legenda para a linha
    
    ax.scatter(0, 0, color='red', s=25, label='Origem (0, 0)')  # Adiciona o ponto na origem
    
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
        ax.plot(x_coords, y_coords, color='red', linestyle='-', linewidth=2)
        for x, y in zip(x_coords, y_coords):
            ax.text(x, y, f'({x},{y})', size=10, zorder=1)
        fig.canvas.draw_idle()
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números válidos.")

# Inicializa o gráfico
fig = plt.figure(figsize=(15, 12), facecolor='black')  # Tamanho da figura
fig.patch.set_facecolor('lightgray')  # Cor de fundo da figura
ax = fig.add_subplot(111)
plt.subplots_adjust(left=0.25, bottom=0.3)

# Inicializa no modo 2D
build_2d()

# Exibe o gráfico
plt.show()
