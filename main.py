from time import sleep

from graphics import *

# General TODOs:
#  Refactor all generic drawing and text methods to a graphics library layer
#   - create a generic method for rendering a full screen of text prompts
#  Start implementing game logic

def set_rectangle(window, upper_left, lower_right, color):
    r = Rectangle(upper_left, lower_right)
    r.setOutline(color)
    r.setFill(color)
    r.draw(window)


def draw_pixel(window, pixel_size, x, y, color):
    # Translate x, y to pixels based on pixel size and number of rows/columns
    # Assume 'pixels' start in the upper left as (0, 0)
    upper_left = Point(x * pixel_size, y * pixel_size)
    lower_right = upper_left.clone()
    lower_right.x += pixel_size
    lower_right.y += pixel_size
    set_rectangle(window, upper_left, lower_right, color)


def draw_horizontal_line(window, pixel_size, x, y, length, color):
    i = 0
    while i < length:
        draw_pixel(window, pixel_size, x + i, y, color)
        i += 1


def draw_vertical_line(window, pixel_size, x, y, length, color):
    i = 0
    while i < length:
        draw_pixel(window, pixel_size, x, y + i, color)
        i += 1


def draw_five_cents(window, pixel_size, x_position):
    set_rectangle(window, Point(x_position * pixel_size, 8 * pixel_size),
                  Point(36 * pixel_size, 19 * pixel_size), apple_green)
    # 5
    draw_vertical_line(window, pixel_size, 22, 11, 3, apple_pink)
    draw_vertical_line(window, pixel_size, 26, 13, 4, apple_pink)
    draw_horizontal_line(window, pixel_size, 22, 11, 5, apple_pink)
    draw_horizontal_line(window, pixel_size, 22, 13, 5, apple_pink)
    draw_horizontal_line(window, pixel_size, 22, 16, 5, apple_pink)
    # cent symbol
    draw_vertical_line(window, pixel_size, 29, 12, 4, apple_pink)
    draw_vertical_line(window, pixel_size, 31, 11, 2, apple_pink)
    draw_vertical_line(window, pixel_size, 31, 15, 2, apple_pink)
    draw_horizontal_line(window, pixel_size, 29, 12, 5, apple_pink)
    draw_horizontal_line(window, pixel_size, 29, 15, 5, apple_pink)


def draw_cup(window, pixel_size, start_x_pos, add_trailing_line):
    draw_vertical_line(window, pixel_size, start_x_pos, 9, 10, white)
    draw_horizontal_line(window, pixel_size, start_x_pos, 18, 10, white)
    draw_vertical_line(window, pixel_size, start_x_pos + 10, 9, 10, white)
    if add_trailing_line:
        draw_vertical_line(window, pixel_size, start_x_pos + 11, 9, 10, apple_green)
    set_rectangle(window, Point((start_x_pos + 1) * pixel_size, 8 * pixel_size),
                  Point((start_x_pos + 10) * pixel_size, 18 * pixel_size), apple_green)


def fill_cup(window, pixel_size):
    draw_vertical_line(window, pixel_size, 12, 7, 11, apple_lemon)
    i = 0
    while i < 8:
        draw_horizontal_line(window, pixel_size, 8, 17 - i, 9, apple_lemon)
        i = i + 1
        sleep(0.125)
    sleep(0.5)
    draw_vertical_line(window, pixel_size, 12, 7, 3, apple_green)


def animate_welcome_screen(window, pixel_size, columns, rows):
    sleep(5)
    x_position = columns
    win.autoflush = False
    while x_position >= 7:
        if x_position <= 22:
            draw_five_cents(window, pixel_size, x_position)
            draw_cup(window, pixel_size, x_position, False)
        else:
            draw_cup(window, pixel_size, x_position, True)
        win.update()
        x_position = x_position - 1
        sleep(0.125)
    win.autoflush = True
    fill_cup(window, pixel_size)
    sleep(5)


def draw_welcome_screen(window, pixel_size, columns, rows):
    set_rectangle(window, Point(0, 0), Point(pixel_size * columns, pixel_size * rows), apple_green)
    # L
    draw_vertical_line(win, pixel_size, 0, 1, 6, apple_pink)
    draw_horizontal_line(win, pixel_size, 0, 7, 4, apple_pink)
    # e
    draw_vertical_line(win, pixel_size, 5, 3, 4, apple_pink)
    draw_vertical_line(win, pixel_size, 8, 3, 2, apple_pink)
    draw_horizontal_line(win, pixel_size, 5, 3, 3, apple_pink)
    draw_horizontal_line(win, pixel_size, 5, 5, 4, apple_pink)
    draw_horizontal_line(win, pixel_size, 5, 7, 4, apple_pink)
    # m
    draw_vertical_line(win, pixel_size, 10, 3, 5, apple_pink)
    draw_vertical_line(win, pixel_size, 12, 3, 4, apple_pink)
    draw_vertical_line(win, pixel_size, 14, 3, 5, apple_pink)
    draw_horizontal_line(win, pixel_size, 10, 3, 5, apple_pink)
    # o
    draw_vertical_line(win, pixel_size, 16, 3, 5, apple_pink)
    draw_vertical_line(win, pixel_size, 19, 3, 5, apple_pink)
    draw_horizontal_line(win, pixel_size, 16, 3, 4, apple_pink)
    draw_horizontal_line(win, pixel_size, 16, 7, 4, apple_pink)
    # n
    draw_vertical_line(win, pixel_size, 21, 3, 5, apple_pink)
    draw_vertical_line(win, pixel_size, 24, 3, 5, apple_pink)
    draw_horizontal_line(win, pixel_size, 21, 3, 4, apple_pink)
    # a
    draw_vertical_line(win, pixel_size, 26, 5, 3, apple_pink)
    draw_vertical_line(win, pixel_size, 29, 3, 5, apple_pink)
    draw_horizontal_line(win, pixel_size, 26, 3, 4, apple_pink)
    draw_horizontal_line(win, pixel_size, 26, 5, 4, apple_pink)
    draw_horizontal_line(win, pixel_size, 26, 7, 4, apple_pink)
    # d
    draw_vertical_line(win, pixel_size, 31, 3, 5, apple_pink)
    draw_vertical_line(win, pixel_size, 34, 1, 7, apple_pink)
    draw_horizontal_line(win, pixel_size, 31, 3, 4, apple_pink)
    draw_horizontal_line(win, pixel_size, 31, 7, 4, apple_pink)
    # e
    draw_vertical_line(win, pixel_size, 36, 3, 4, apple_pink)
    draw_vertical_line(win, pixel_size, 39, 3, 2, apple_pink)
    draw_horizontal_line(win, pixel_size, 36, 3, 3, apple_pink)
    draw_horizontal_line(win, pixel_size, 36, 5, 4, apple_pink)
    draw_horizontal_line(win, pixel_size, 36, 7, 4, apple_pink)
    # S
    draw_vertical_line(win, pixel_size, 8, 10, 4, apple_pink)
    draw_vertical_line(win, pixel_size, 12, 13, 4, apple_pink)
    draw_horizontal_line(win, pixel_size, 8, 10, 5, apple_pink)
    draw_horizontal_line(win, pixel_size, 8, 13, 5, apple_pink)
    draw_horizontal_line(win, pixel_size, 8, 16, 5, apple_pink)
    # t
    draw_vertical_line(win, pixel_size, 15, 10, 7, apple_pink)
    draw_horizontal_line(win, pixel_size, 14, 12, 3, apple_pink)
    # a
    draw_vertical_line(win, pixel_size, 18, 14, 3, apple_pink)
    draw_vertical_line(win, pixel_size, 21, 12, 5, apple_pink)
    draw_horizontal_line(win, pixel_size, 18, 12, 4, apple_pink)
    draw_horizontal_line(win, pixel_size, 18, 14, 4, apple_pink)
    draw_horizontal_line(win, pixel_size, 18, 16, 4, apple_pink)
    # n
    draw_vertical_line(win, pixel_size, 23, 12, 5, apple_pink)
    draw_vertical_line(win, pixel_size, 26, 12, 5, apple_pink)
    draw_horizontal_line(win, pixel_size, 23, 12, 4, apple_pink)
    # d
    draw_vertical_line(win, pixel_size, 28, 12, 5, apple_pink)
    draw_vertical_line(win, pixel_size, 31, 10, 7, apple_pink)
    draw_horizontal_line(win, pixel_size, 28, 12, 4, apple_pink)
    draw_horizontal_line(win, pixel_size, 28, 16, 4, apple_pink)

    text = Text(Point(pixelSize * 20, pixelSize * 22), 'COPYRIGHT 1979       APPLE COMPUTER INC.')
    text.setFace('courier')
    text.setSize(16)
    text.setTextColor('white')
    text.setStyle('bold')
    text.draw(win)

    animate_welcome_screen(window, pixel_size, columns, rows)


def set_standard_text(text):
    text.setFace('courier')
    text.setSize(18)
    text.setTextColor('white')
    text.setStyle('bold')


def write_text_line(window, pixel_size, line, text):
    text = Text(Point(pixel_size * 20, pixel_size * line), text)
    set_standard_text(text)
    text.draw(window)


def draw_welcome_text(window, pixel_size):
    write_text_line(window, pixel_size,  1, 'HI!  WELCOME TO LEMONSVILLE, CALIFORNIA!')
    write_text_line(window, pixel_size,  4, 'IN THIS SMALL TOWN, YOU ARE IN CHARGE OF')
    write_text_line(window, pixel_size,  6, 'RUNNING YOUR OWN LEMONADE STAND. YOU CAN')
    write_text_line(window, pixel_size,  8, 'COMPETE WITH AS MANY OTHER PEOPLE AS YOU')
    write_text_line(window, pixel_size, 10, 'WISH, BUT HOW MUCH PROFIT YOU MAKE IS UP')
    write_text_line(window, pixel_size, 12, "TO YOU (THE OTHER STANDS' SALES WILL NOT")
    write_text_line(window, pixel_size, 14, 'AFFECT YOUR BUSINESS IN ANY WAY). IF YOU')
    write_text_line(window, pixel_size, 16, "MAKE THE MOST MONEY, YOU'RE THE WINNER!!")
    write_text_line(window, pixel_size, 19, 'ARE YOU STARTING A NEW GAME? (YES OR NO)')
    write_text_line(window, pixel_size, 21, 'TYPE YOUR ANSWER AND HIT RETURN ==>     ')

    entry = Entry(Point(pixel_size * 37, pixel_size * 21), 4)
    entry.setFill(black)
    entry.setTextColor(white)
    entry.setFace('courier')
    entry.setSize(18)
    entry.setStyle('bold')
    entry.draw(window)

    while True:
        if win.isClosed():
            break
        if win.getKey() == 'Return':
            print('Return found!')
            print('Entry is:', entry.getText())
            # TODO: Take action to handle new/existing game selection
            break


if __name__ == '__main__':
    # color constants
    apple_green = color_rgb(25, 215, 0)
    apple_pink = color_rgb(255, 139, 191)
    apple_lemon = color_rgb(191, 227, 8)
    black = color_rgb(0, 0, 0)
    white = color_rgb(255, 255, 255)

    # Emulate 40-column x 25-row display
    pixelSize = 15
    width = pixelSize * 40
    height = pixelSize * 24
    win = GraphWin("Lemonade Stand", width, height)
    # Full black background to start
    set_rectangle(win, Point(0, 0), Point(width, height), black)
    # draw welcome screen over the black background
    draw_welcome_screen(win, pixelSize, 40, 20)

    # Reset black background and draw welcome text
    set_rectangle(win, Point(0, 0), Point(width, height), black)
    draw_welcome_text(win, pixelSize)

    if win.isOpen():
        while True:
            key = win.getKey()
            print(key)
