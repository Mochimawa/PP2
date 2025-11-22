import pygame
import math

# ========================================================
# ДОБАВЛЕННЫЕ ИНСТРУМЕНТЫ:
# 1 – линия (старый режим)
# 2 – прямоугольник
# 3 – круг
# 4 – квадрат
# 5 – прямоугольный треугольник
# 6 – равносторонний треугольник
# 7 – ромб
# E – ластик
# ========================================================


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    tool = 1  # дефолт = линия
    draft_surface = pygame.Surface((640, 480), pygame.SRCALPHA)
    points = []

    drawing = False
    start_pos = None

    while True:

        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # ======= Смена цвета =======
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                    points = []
                elif event.key == pygame.K_b:
                    mode = 'blue'

                # ======= Смена инструмента =======
                if event.key == pygame.K_1:
                    tool = 1
                if event.key == pygame.K_2:
                    tool = 2
                if event.key == pygame.K_3:
                    tool = 3
                if event.key == pygame.K_4:
                    tool = 4
                if event.key == pygame.K_5:
                    tool = 5
                if event.key == pygame.K_6:
                    tool = 6
                if event.key == pygame.K_7:
                    tool = 7
                if event.key == pygame.K_e:
                    tool = "eraser"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    start_pos = event.pos

                    if tool == 1:  # линия
                        points.append(event.pos)

                elif event.button == 3:
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    drawing = False

                    end_pos = event.pos
                    commit_shape(screen, start_pos, end_pos, radius, mode, tool)

                    draft_surface.fill((0, 0, 0, 0))

            if event.type == pygame.MOUSEMOTION:
                if tool == 1:
                    pos = event.pos
                    points.append(pos)
                    points = points[-256:]

                if drawing and tool != 1:
                    draft_surface.fill((0, 0, 0, 0))
                    preview_shape(draft_surface, start_pos, event.pos, radius, mode, tool)

        screen.fill((0, 0, 0))

        # рисуем линию старым способом
        if tool == 1:
            for i in range(len(points) - 1):
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)

        screen.blit(draft_surface, (0, 0))
        pygame.display.flip()
        clock.tick(60)


# ========================================================
# Рисование линии (исходная функция)
# ========================================================
def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)


# ========================================================
# ФИГУРЫ — превью и окончательное рисование
# ========================================================

def preview_shape(surface, start, end, width, color, tool):
    if tool == 2:  # rectangle
        pygame.draw.rect(surface, get_color(color), rect_from_points(start, end), width=2)
    elif tool == 3:  # circle
        pygame.draw.circle(surface, get_color(color), start, distance(start, end), 2)
    elif tool == 4:  # square
        pygame.draw.rect(surface, get_color(color), square_from_points(start, end), 2)
    elif tool == 5:  # right triangle
        pygame.draw.polygon(surface, get_color(color), right_triangle(start, end), 2)
    elif tool == 6:  # equilateral triangle
        pygame.draw.polygon(surface, get_color(color), equilateral_triangle(start, end), 2)
    elif tool == 7:  # rhombus
        pygame.draw.polygon(surface, get_color(color), rhombus(start, end), 2)


def commit_shape(surface, start, end, width, color, tool):
    if tool == "eraser":
        pygame.draw.circle(surface, (0, 0, 0), start, 20)
        return

    c = get_color(color)

    if tool == 2:
        pygame.draw.rect(surface, c, rect_from_points(start, end), 2)
    elif tool == 3:
        pygame.draw.circle(surface, c, start, distance(start, end), 2)
    elif tool == 4:
        pygame.draw.rect(surface, c, square_from_points(start, end), 2)
    elif tool == 5:
        pygame.draw.polygon(surface, c, right_triangle(start, end), 2)
    elif tool == 6:
        pygame.draw.polygon(surface, c, equilateral_triangle(start, end), 2)
    elif tool == 7:
        pygame.draw.polygon(surface, c, rhombus(start, end), 2)


# ========================================================
# Геометрические функции
# ========================================================

def get_color(mode):
    if mode == "red": return (255, 0, 0)
    if mode == "green": return (0, 255, 0)
    if mode == "blue": return (0, 150, 255)
    return (255, 255, 255)


def rect_from_points(a, b):
    return pygame.Rect(min(a[0], b[0]), min(a[1], b[1]),
                       abs(a[0] - b[0]), abs(a[1] - b[1]))


def square_from_points(a, b):
    side = max(abs(a[0] - b[0]), abs(a[1] - b[1]))
    return pygame.Rect(a[0], a[1], side, side)


def distance(a, b):
    return int(math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2))


def right_triangle(a, b):
    return [a, (a[0], b[1]), b]


def equilateral_triangle(a, b):
    h = distance(a, b)
    return [
        a,
        b,
        (a[0] + (b[0] - a[0]) // 2, a[1] - h)
    ]


def rhombus(a, b):
    cx = (a[0] + b[0]) // 2
    cy = (a[1] + b[1]) // 2
    return [(cx, a[1]), (b[0], cy), (cx, b[1]), (a[0], cy)]


main()
