import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

BLOCK_SIZE = 20

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

snake = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]

# ========================================================
# ЗАДАЧА 1: Случайное производство пищи с разным весом
# ЗАДАЧА 2: Пища исчезает со временем (таймер)
# ========================================================

food_weight = random.randint(1, 5)     # вес еды
FOOD_TIMER_MAX = 300                   # 5 секунд при 60 FPS
food_timer = FOOD_TIMER_MAX            # таймер исчезновения

food = (
    random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
    random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
)

UP = (0, -BLOCK_SIZE)
DOWN = (0, BLOCK_SIZE)
LEFT = (-BLOCK_SIZE, 0)
RIGHT = (BLOCK_SIZE, 0)

direction = RIGHT
score = 0
level = 1
speed = 10

clock = pygame.time.Clock()


def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))


def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))


def check_border_collision(snake_head):
    return (snake_head[0] < 0 or snake_head[0] >= SCREEN_WIDTH or
            snake_head[1] < 0 or snake_head[1] >= SCREEN_HEIGHT)


def check_self_collision(snake):
    return len(snake) != len(set(snake))


def generate_food_position(snake):
    """Генерация еды с разным весом и таймером"""
    global food_weight, food_timer
    while True:
        food_position = (
            random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
            random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        )
        if food_position not in snake:
            food_weight = random.randint(1, 5)    # ЗАДАЧА 1: случайный вес еды
            food_timer = FOOD_TIMER_MAX           # сброс таймера
            return food_position


while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != DOWN:
        direction = UP
    elif keys[pygame.K_DOWN] and direction != UP:
        direction = DOWN
    elif keys[pygame.K_LEFT] and direction != RIGHT:
        direction = LEFT
    elif keys[pygame.K_RIGHT] and direction != LEFT:
        direction = RIGHT

    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)

    # Проверка столкновений
    if check_border_collision(new_head) or check_self_collision(snake):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    # =====================================================
    # ЗАДАЧА 2: еда исчезает со временем
    # =====================================================
    food_timer -= 1
    if food_timer <= 0:
        food = generate_food_position(snake)

    # =====================================================
    # ЗАДАЧА 1: учёт веса еды
    # =====================================================
    if new_head == food:
        score += food_weight  # добавляем вес еды
        if score % 3 == 0:
            level += 1
            speed += 2
        food = generate_food_position(snake)
    else:
        snake.pop()

    draw_snake(snake)
    draw_food(food)

    font = pygame.font.Font(None, 30)
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    weight_text = font.render(f"Food weight: {food_weight}", True, WHITE)
    timer_text = font.render(f"Timer: {food_timer // 60}", True, WHITE)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 30))
    screen.blit(weight_text, (10, 50))
    screen.blit(timer_text, (10, 70))

    pygame.display.update()
    clock.tick(speed)
