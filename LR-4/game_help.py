import pygame
from constants import *


class Help():
    def __init__(self):
        font_path = ("Roboto Condensed.ttf")

        # Инициализируем шрифт
        big_font = pygame.font.Font(font_path, 40)
        self.small_font = pygame.font.Font(font_path, 24)
        text1 = big_font.render(" Меню подсказок", 1, (255, 102, 0))
        text2 = self.small_font.render(" Влево: 'a' или стрелка влево ", 1, (255, 255, 255))
        text3 = self.small_font.render(" Вправо: 'd' или стрелка вправо ", 1, (255, 255, 255))
        text4 = self.small_font.render(" Прыжок: 'w' или стрелка вверх ", 1, (255, 255, 255))
        text5 = self.small_font.render(" Выстрел: пробел ", 1, (255, 255, 255))
        text6 = self.small_font.render(" Музыка вкл/выкл: 'm', громче: 'u', тише: 'j' ", 1,
                                       (255, 255, 255))
        text7 = self.small_font.render(" Подсказка вкл/выкл (игра на паузе): 'h' ", 1,
                                       (255, 255, 255))

        img = pygame.image.load("menu.png").convert_alpha()  # Добавлен фоновый рисунок
        img = pygame.transform.scale(img, (win_width, win_height))  # Изменен размер фонового рисунка
        self.img = img

        # Получаем прямоугольник для надписи "Меню подсказок"
        text1_rect = text1.get_rect(center=(win_width / 2, win_width / 10))

        # Рассчитываем ширину самого широкого текста
        max_width = max(text.get_width() for text in [text2, text3, text4, text5, text6, text7])

        # Рассчитываем положение каждой надписи относительно центра экрана
        text_rects = [text.get_rect(topleft=(win_width / 4.1, win_height / 4 + i * 40)) for i, text in
                      enumerate([text2, text3, text4, text5, text6, text7])]

        for i, text_rect in enumerate(text_rects):
            # Создаем полупрозрачный прямоугольник вокруг надписи
            text_surface = pygame.Surface((max_width + 10, text_rect.height + 5), pygame.SRCALPHA)
            text_surface.fill((0, 0, 0, 128))  # Четвертый параметр - это альфа-канал для прозрачности
            img.blit(text_surface, (text_rect.left - 5, text_rect.top - 2))  # Размещаем прямоугольник перед надписью
            img.blit([text1, text2, text3, text4, text5, text6, text7][i + 1], text_rect.topleft)  # Размещаем надпись

        # Размещаем надпись "Меню подсказок"
        img.blit(text1, text1_rect.topleft)

        # Добавим строки для постоянной подсказки:
        self.text_points = self.small_font.render("Очков:   ", 1, (255, 255, 255))  # Изменено на белый цвет
        self.text_points_w = self.text_points.get_rect().width
        self.text_lives = self.small_font.render("Жизней:   ", 1, (255, 255, 255))  # Изменено на белый цвет
        self.text_lives_w = self.text_lives.get_rect().width
        self.text_help = self.small_font.render("Пауза/подсказка: 'h'", 1, (255, 255, 255))  # Изменено на белый цвет
        self.text_height = self.text_help.get_rect().height

    def line(self, points=0, lives=1):
        tab = 50
        img = pygame.Surface([win_width, self.text_height], pygame.SRCALPHA)
        img.blit(self.text_lives, (0, 0))
        text = self.small_font.render(str(lives), 1, (255, 255, 255))  # Изменено на белый цвет
        img.blit(text, (self.text_lives_w, 0))
        img.blit(self.text_points, (self.text_lives_w + tab, 0))
        text = self.small_font.render(str(points), 1, (255, 255, 255))  # Изменено на белый цвет
        img.blit(text, (self.text_lives_w + tab + self.text_points_w, 0))
        img.blit(self.text_help, (self.text_lives_w + tab + self.text_points_w + tab, 0))
        return img
