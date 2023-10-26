import pygame
# 初始化Pygame
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('普莱尔棋丨PlaierChess')

pygame.mixer.music.load('data/music.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
class ChessGame:
    def __init__(self):
        self.selected_piece = None
        self.tern = 1
        # 获取显示器信息
        display_info = pygame.display.Info()
        # 获取屏幕高度
        screen_height = display_info.current_h

        # 窗口大小
        self.window_height = screen_height - 100
        self.window_width = self.window_height * 0.91

        # 创建窗口
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))

        self.square_size = int(self.window_width * 0.1)

        # 加载棋盘图像
        self.chessboard_image = pygame.image.load('data/棋盘.png')
        self.chessboard_image = pygame.transform.scale(self.chessboard_image, (self.window_width, self.window_height))

        self.game_over_image = pygame.image.load('data/游戏结束.png')
        self.game_over_image = pygame.transform.scale(self.game_over_image, (self.window_width, self.window_height))

        self.cursor_image = pygame.image.load('data/UI/光标.png')
        self.cursor_image = pygame.transform.scale(self.cursor_image, (self.square_size - 10, self.square_size - 10))

        self.circle_image = pygame.image.load('data/UI/选中棋子.png')
        self.circle_image = pygame.transform.scale(self.circle_image, (self.square_size + 5, self.square_size + 5))

        self.start = True
        self.start_image = pygame.image.load('data/封面.png')
        self.start_image = pygame.transform.scale(self.start_image, (self.window_width, self.window_height))
        #self.screen.blit(self.start_image, (0, 0))

        self.back_image = pygame.image.load('data/UI/再次操作.png')
        self.back_image = pygame.transform.scale(self.back_image, (self.window_width * 0.065, self.window_height * 0.25))

        self.sticker = 1
        self.sticker_image = pygame.image.load('data/UI/卡图更换.png')
        self.sticker_image = pygame.transform.scale(self.sticker_image,(self.window_width * 0.065, self.window_height * 0.25))

        self.refresh_image = pygame.image.load('data/UI/刷新游戏.png')
        self.refresh_image = pygame.transform.scale(self.refresh_image,(self.window_width * 0.065, self.window_height * 0.25))

        self.restart_image = pygame.image.load('data/UI/时间回溯.png')
        self.restart_image = pygame.transform.scale(self.restart_image,(self.window_width * 0.5, self.window_height * 0.1))

        self.off_image = pygame.image.load('data/UI/退出游戏.png')
        self.off_image = pygame.transform.scale(self.off_image,(self.window_width * 0.5, self.window_height * 0.1))

        # 加载象棋棋子的图像
        # if self.sticker % 2 == 1 :
        #     self.white_king_image = pygame.image.load('data/帝国棋子/王.png')
        #     self.white_queen_image = pygame.image.load('data/帝国棋子/后.png')
        #     self.white_knight_image = pygame.image.load('data/帝国棋子/骑.png')
        #     self.white_rook_image = pygame.image.load('data/帝国棋子/堡.png')
        #     self.white_bishop_image = pygame.image.load('data/帝国棋子/圣.png')
        #     self.white_pawn_image = pygame.image.load('data/帝国棋子/兵.png')
        #     self.black_king_image = pygame.image.load('data/洛城棋子/将.png')
        #     self.black_advisor_image = pygame.image.load('data/洛城棋子/士.png')
        #     self.black_minister_image = pygame.image.load('data/洛城棋子/相.png')
        #     self.black_cavalry_image = pygame.image.load('data/洛城棋子/马.png')
        #     self.black_crossbow_image = pygame.image.load('data/洛城棋子/砲.png')
        #     self.black_rook_image = pygame.image.load('data/洛城棋子/車.png')
        #     self.black_pawn_image = pygame.image.load('data/洛城棋子/卒.png')
        #
        # elif self.sticker % 2 == 0 :
        #     self.white_king_image = pygame.image.load('data/帝国棋子/扎伊兹克.png')
        #     self.white_queen_image = pygame.image.load('data/帝国棋子/鬼面武士.png')
        #     self.white_knight_image = pygame.image.load('data/帝国棋子/帝国骑兵.png')
        #     self.white_rook_image = pygame.image.load('data/帝国棋子/堡垒.png')
        #     self.white_bishop_image = pygame.image.load('data/帝国棋子/圣职者.png')
        #     self.white_pawn_image = pygame.image.load('data/帝国棋子/帝国盾步兵.png')
        #     self.black_king_image = pygame.image.load('data/洛城棋子/洛武帝.png')
        #     self.black_advisor_image = pygame.image.load('data/洛城棋子/近卫.png')
        #     self.black_minister_image = pygame.image.load('data/洛城棋子/丞相.png')
        #     self.black_cavalry_image = pygame.image.load('data/洛城棋子/战马.png')
        #     self.black_crossbow_image = pygame.image.load('data/洛城棋子/洛城重弩.png')
        #     self.black_rook_image = pygame.image.load('data/洛城棋子/战車.png')
        #     self.black_pawn_image = pygame.image.load('data/洛城棋子/洛城兵卒.png')

        if True:
            self.white_king_image = pygame.image.load('data/帝国棋子/扎伊兹克.png')
            self.white_queen_image = pygame.image.load('data/帝国棋子/鬼面武士.png')
            self.white_knight_image = pygame.image.load('data/帝国棋子/帝国骑兵.png')
            self.white_rook_image = pygame.image.load('data/帝国棋子/堡垒.png')
            self.white_bishop_image = pygame.image.load('data/帝国棋子/圣职者.png')
            self.white_pawn_image = pygame.image.load('data/帝国棋子/帝国盾步兵.png')
            self.black_king_image = pygame.image.load('data/洛城棋子/洛武帝.png')
            self.black_advisor_image = pygame.image.load('data/洛城棋子/近卫.png')
            self.black_minister_image = pygame.image.load('data/洛城棋子/丞相.png')
            self.black_cavalry_image = pygame.image.load('data/洛城棋子/战马.png')
            self.black_crossbow_image = pygame.image.load('data/洛城棋子/洛城重弩.png')
            self.black_rook_image = pygame.image.load('data/洛城棋子/战車.png')
            self.black_pawn_image = pygame.image.load('data/洛城棋子/洛城兵卒.png')

            # self.white_king_image = pygame.image.load('data/帝国棋子/王.png')
            # self.white_queen_image = pygame.image.load('data/帝国棋子/后.png')
            # self.white_knight_image = pygame.image.load('data/帝国棋子/骑.png')
            # self.white_rook_image = pygame.image.load('data/帝国棋子/堡.png')
            # self.white_bishop_image = pygame.image.load('data/帝国棋子/圣.png')
            # self.white_pawn_image = pygame.image.load('data/帝国棋子/兵.png')
            # self.black_king_image = pygame.image.load('data/洛城棋子/将.png')
            # self.black_advisor_image = pygame.image.load('data/洛城棋子/士.png')
            # self.black_minister_image = pygame.image.load('data/洛城棋子/相.png')
            # self.black_cavalry_image = pygame.image.load('data/洛城棋子/马.png')
            # self.black_crossbow_image = pygame.image.load('data/洛城棋子/砲.png')
            # self.black_rook_image = pygame.image.load('data/洛城棋子/車.png')
            # self.black_pawn_image = pygame.image.load('data/洛城棋子/卒.png')

        # 创建象棋棋子实例，并传递图像
        self.white_king = ChessPiece('white', 'king', 1.5, 4.5, self.white_king_image, self.square_size)
        self.white_queen = ChessPiece('white', 'queen', 0.5, 4.5, self.white_queen_image, self.square_size)
        self.white_knightA = ChessPiece('white', 'knight', 1.5, 1.5, self.white_knight_image, self.square_size)
        self.white_knightB = ChessPiece('white', 'knight', 1.5, 7.5, self.white_knight_image, self.square_size)
        self.white_rookA = ChessPiece('white', 'rook', 1.5, 0.5, self.white_rook_image, self.square_size)
        self.white_rookB = ChessPiece('white', 'rook', 1.5, 8.5, self.white_rook_image, self.square_size)
        self.white_bishopA = ChessPiece('white', 'bishop', 1.5, 3.5, self.white_bishop_image, self.square_size)
        self.white_bishopB = ChessPiece('white', 'bishop', 1.5, 5.5, self.white_bishop_image, self.square_size)
        self.white_pawn1 = ChessPiece('white', 'pawn', 2.5, 0.5, self.white_pawn_image, self.square_size)
        self.white_pawn2 = ChessPiece('white', 'pawn', 2.5, 1.5, self.white_pawn_image, self.square_size)
        self.white_pawn3 = ChessPiece('white', 'pawn', 2.5, 2.5, self.white_pawn_image, self.square_size)
        self.white_pawn4 = ChessPiece('white', 'pawn', 2.5, 3.5, self.white_pawn_image, self.square_size)
        self.white_pawn5 = ChessPiece('white', 'pawn', 2.5, 4.5, self.white_pawn_image, self.square_size)
        self.white_pawn6 = ChessPiece('white', 'pawn', 2.5, 5.5, self.white_pawn_image, self.square_size)
        self.white_pawn7 = ChessPiece('white', 'pawn', 2.5, 6.5, self.white_pawn_image, self.square_size)
        self.white_pawn8 = ChessPiece('white', 'pawn', 2.5, 7.5, self.white_pawn_image, self.square_size)
        self.white_pawn9 = ChessPiece('white', 'pawn', 2.5, 8.5, self.white_pawn_image, self.square_size)
        self.black_king = ChessPiece('black', 'R_king', 9.5, 4.5, self.black_king_image, self.square_size)
        self.black_advisorA = ChessPiece('black', 'R_advisor', 9.5, 3.5, self.black_advisor_image, self.square_size)
        self.black_advisorB = ChessPiece('black', 'R_advisor', 9.5, 5.5, self.black_advisor_image, self.square_size)
        self.black_ministerA = ChessPiece('black', 'R_minister', 9.5, 2.5, self.black_minister_image, self.square_size)
        self.black_ministerB = ChessPiece('black', 'R_minister', 9.5, 6.5, self.black_minister_image, self.square_size)
        self.black_cavalryA = ChessPiece('black', 'R_cavalry', 9.5, 1.5, self.black_cavalry_image, self.square_size)
        self.black_cavalryB = ChessPiece('black', 'R_cavalry', 9.5, 7.5, self.black_cavalry_image, self.square_size)
        self.black_crossbowA = ChessPiece('black', 'R_crossbow', 7.5, 1.5, self.black_crossbow_image, self.square_size)
        self.black_crossbowB = ChessPiece('black', 'R_crossbow', 7.5, 7.5, self.black_crossbow_image, self.square_size)
        self.black_rookA = ChessPiece('black', 'R_rook', 9.5, 0.5, self.black_rook_image, self.square_size)
        self.black_rookB = ChessPiece('black', 'R_rook', 9.5, 8.5, self.black_rook_image, self.square_size)
        self.black_pawn1 = ChessPiece('black', 'R_pawn', 6.5, 0.5, self.black_pawn_image, self.square_size)
        self.black_pawn2 = ChessPiece('black', 'R_pawn', 6.5, 2.5, self.black_pawn_image, self.square_size)
        self.black_pawn3 = ChessPiece('black', 'R_pawn', 6.5, 4.5, self.black_pawn_image, self.square_size)
        self.black_pawn4 = ChessPiece('black', 'R_pawn', 6.5, 6.5, self.black_pawn_image, self.square_size)
        self.black_pawn5 = ChessPiece('black', 'R_pawn', 6.5, 8.5, self.black_pawn_image, self.square_size)

        self.all_pieces = [
            self.white_king, self.white_queen, self.white_knightA, self.white_knightB,
            self.white_rookA, self.white_rookB, self.white_bishopA, self.white_bishopB,
            self.white_pawn1, self.white_pawn2, self.white_pawn3, self.white_pawn4,
            self.white_pawn5, self.white_pawn6, self.white_pawn7, self.white_pawn8,
            self.white_pawn9, self.black_king, self.black_advisorA, self.black_advisorB,
            self.black_ministerA, self.black_ministerB, self.black_cavalryA, self.black_cavalryB,
            self.black_crossbowA, self.black_crossbowB, self.black_rookA, self.black_rookB,
            self.black_pawn1, self.black_pawn2, self.black_pawn3, self.black_pawn4, self.black_pawn5]

        self.valid_possibility = []

        # 游戏主循环
        self.running = True
    def is_mouse_click_on_piece(self, piece, mouse_x, mouse_y):
        # 判断鼠标点击是否在棋子的区域内
        piece_rect = piece.image.get_rect()
        piece_rect.topleft = (piece.col * self.square_size, piece.row * self.square_size)
        return piece_rect.collidepoint(mouse_x, mouse_y)

    def is_mouse_click_on_back(self, back_image, mouse_x, mouse_y):
        # 判断鼠标点击是否在按钮的区域内
        back_image_rect = back_image.get_rect()
        back_image_rect.topleft = (self.window_width * 0.91, 100)
        return back_image_rect.collidepoint(mouse_x, mouse_y)

    # def is_mouse_click_on_sticker(self, sticker_image, mouse_x, mouse_y):
    #     # 判断鼠标点击是否在按钮的区域内
    #     sticker_image_rect = sticker_image.get_rect()
    #     sticker_image_rect.topleft = (self.window_width * 0.91, 640)
    #     return sticker_image_rect.collidepoint(mouse_x, mouse_y)

    def is_mouse_click_on_refresh(self, refresh_image, mouse_x, mouse_y):
        # 判断鼠标点击是否在按钮的区域内
        refresh_image_rect = refresh_image.get_rect()
        refresh_image_rect.topleft = (self.window_width * 0.91, 365)
        return refresh_image_rect.collidepoint(mouse_x, mouse_y)

    def is_mouse_click_on_cursor(self, mouse_x, mouse_y):
        for coordinates in self.valid_possibility :
            x , y = coordinates
            # print(x,y)
            # print(mouse_x // self.square_size - 0.5, mouse_y // self.square_size - 0.5)
            # print(mouse_x // self.square_size - 0.5 == x and mouse_y // self.square_size - 0.5 == y)
            if mouse_x // self.square_size - 0.5 == x and mouse_y // self.square_size - 0.5 == y :
                return True

    def is_mouse_click_on_off(self, off_image, mouse_x, mouse_y):
        # 判断鼠标点击是否在按钮的区域内
        off_image_rect = off_image.get_rect()
        off_image_rect.topleft = (230, 650)
        return off_image_rect.collidepoint(mouse_x, mouse_y)

    def is_mouse_click_on_restart(self, restart_image, mouse_x, mouse_y):
        # 判断鼠标点击是否在按钮的区域内
        restart_image_rect = restart_image.get_rect()
        restart_image_rect.topleft = (230, 530)
        return restart_image_rect.collidepoint(mouse_x, mouse_y)

        #return cursor_rect.collidepoint(mouse_x, mouse_y)

    # def is_mouse_click_on_cursor(self, cursor, mouse_x, mouse_y, valid_possibility):
    #     # 判断鼠标点击是否在光标的区域内
    #     cursor_rect = cursor.image.get_rect()
    #     cursor_rect.topleft = (cursor.col * self.square_size, cursor.row * self.square_size)


    def is_valid_move(self,piece_type,piece_row,piece_col):
        if self.selected_piece == self.white_king :
            if piece_type == 'king' :
                self.screen.blit(self.circle_image, (piece_col * self.square_size + 2.5, piece_row * self.square_size - 0.6))
                possibility = [(piece_row - 1,piece_col + 1),(piece_row , piece_col + 1),
                               (piece_row + 1,piece_col + 1),(piece_row + 1,piece_col),
                               (piece_row - 1,piece_col),(piece_row - 1,piece_col - 1),
                               (piece_row ,piece_col - 1),(piece_row + 1,piece_col - 1)]
                valid_not_possibility = []
                for coordinates in possibility :
                    x , y = coordinates
                    if 10 > x > 0 and 9 > y > 0:
                        for pieces in self.all_pieces :
                            if x == pieces.row and y == pieces.col and pieces.color == 'white':
                                valid_not_possibility.append(coordinates)
                    else:
                        valid_not_possibility.append(coordinates)


                self.valid_possibility = list(set(possibility) - set(valid_not_possibility))

                for coordinates in self.valid_possibility :
                    x, y = coordinates
                    self.screen.blit(self.cursor_image, (y * self.square_size + 10, x * self.square_size + 10))
                    pygame.display.flip()

        elif self.selected_piece == self.white_queen :
            if piece_type == 'queen' :
                self.screen.blit(self.circle_image, (piece_col * self.square_size + 2.5, piece_row * self.square_size - 0.6))
                self.valid_possibility = []

                for N in range(1, 10):
                    x = piece_row - N
                    y = piece_col
                    block = False
                    if x < 0:
                        break
                    for piece in self.all_pieces:
                        if x == piece.row and y == piece.col:
                            if piece.color == 'white':
                                block = True
                                break
                            else:
                                self.valid_possibility.append((x, y))
                                block = True
                                break
                    else:
                        self.valid_possibility.append((x, y))

                    if block:
                        break

                for S in range(1, 10):
                    x = piece_row + S
                    y = piece_col
                    block = False
                    if x > 10:
                        break
                    for piece in self.all_pieces:
                        if x == piece.row and y == piece.col:
                            if piece.color == 'white':
                                block = True
                                break
                            else:
                                self.valid_possibility.append((x, y))
                                block = True
                                break
                    else:
                        self.valid_possibility.append((x, y))

                    if block:
                        break

                for W in range(1, 10):
                    x = piece_row
                    y = piece_col - W
                    block = False
                    if y < 0:
                        break
                    for piece in self.all_pieces:
                        if x == piece.row and y == piece.col:
                            if piece.color == 'white':
                                block = True
                                break
                            else:
                                self.valid_possibility.append((x, y))
                                block = True
                                break
                    else:
                        self.valid_possibility.append((x, y))

                    if block:
                        break

                for E in range(1, 10):
                    x = piece_row
                    y = piece_col + E
                    block = False
                    if y > 9:
                        break
                    for piece in self.all_pieces:
                        if x == piece.row and y == piece.col:
                            if piece.color == 'white':
                                block = True
                                break
                            else:
                                self.valid_possibility.append((x, y))
                                block = True
                                break
                    else:
                        self.valid_possibility.append((x, y))

                    if block:
                        break

                for NE in range(1, 10):
                    x = piece_row - NE
                    y = piece_col + NE
                    block = False
                    if x > 10 or x < 0 or y > 9 or y < 0 :
                        break
                    for piece in self.all_pieces:
                        if x == piece.row and y == piece.col:
                            if piece.color == 'white':
                                block = True
                                break
                            else:
                                self.valid_possibility.append((x, y))
                                block = True
                                break
                    else:
                        self.valid_possibility.append((x, y))

                    if block:
                        break

                for SE in range(1, 10):
                    x = piece_row + SE
                    y = piece_col + SE
                    block = False
                    if x > 10 or x < 0 or y > 9 or y < 0 :
                        break
                    for piece in self.all_pieces:
                        if x == piece.row and y == piece.col:
                            if piece.color == 'white':
                                block = True
                                break
                            else:
                                self.valid_possibility.append((x, y))
                                block = True
                                break
                    else:
                        self.valid_possibility.append((x, y))

                    if block:
                        break

                for NW in range(1, 10):
                    x = piece_row - NW
                    y = piece_col - NW
                    block = False
                    if x > 10 or x < 0 or y > 9 or y < 0 :
                        break
                    for piece in self.all_pieces:
                        if x == piece.row and y == piece.col:
                            if piece.color == 'white':
                                block = True
                                break
                            else:
                                self.valid_possibility.append((x, y))
                                block = True
                                break
                    else:
                        self.valid_possibility.append((x, y))

                    if block:
                        break

                for SW in range(1, 10):
                    x = piece_row + SW
                    y = piece_col - SW
                    block = False
                    if x > 10 or x < 0 or y > 9 or y < 0 :
                        break
                    for piece in self.all_pieces:
                        if x == piece.row and y == piece.col:
                            if piece.color == 'white':
                                block = True
                                break
                            else:
                                self.valid_possibility.append((x, y))
                                block = True
                                break
                    else:
                        self.valid_possibility.append((x, y))

                    if block:
                        break

                for coordinates in self.valid_possibility :
                    x, y = coordinates
                    self.screen.blit(self.cursor_image, (y * self.square_size + 10, x * self.square_size + 10))
                    pygame.display.flip()

        elif self.selected_piece == self.white_rookA or self.selected_piece == self.white_rookB :
            if piece_type == 'rook':
                self.screen.blit(self.circle_image,
                                 (piece_col * self.square_size + 2.5, piece_row * self.square_size - 0.6))
                self.valid_possibility = []

                for N in range(1, 10):
                    x = piece_row - N
                    y = piece_col
                    block = False
                    if x < 0:
                        break
                    for piece in self.all_pieces:
                        if x == piece.row and y == piece.col:
                            if piece.color == 'white':
                                block = True
                                break
                            else:
                                self.valid_possibility.append((x, y))
                                block = True
                                break
                    else:
                        self.valid_possibility.append((x, y))

                    if block:
                        break

                for S in range(1, 10):
                    x = piece_row + S
                    y = piece_col
                    block = False
                    if x > 10:
                        break
                    for piece in self.all_pieces:
                        if x == piece.row and y == piece.col:
                            if piece.color == 'white':
                                block = True
                                break
                            else:
                                self.valid_possibility.append((x, y))
                                block = True
                                break
                    else:
                        self.valid_possibility.append((x, y))

                    if block:
                        break

                for W in range(1, 10):
                    x = piece_row
                    y = piece_col - W
                    block = False
                    if y < 0:
                        break
                    for piece in self.all_pieces:
                        if x == piece.row and y == piece.col:
                            if piece.color == 'white':
                                block = True
                                break
                            else:
                                self.valid_possibility.append((x, y))
                                block = True
                                break
                    else:
                        self.valid_possibility.append((x, y))

                    if block:
                        break

                for E in range(1, 10):
                    x = piece_row
                    y = piece_col + E
                    block = False
                    if y > 9:
                        break
                    for piece in self.all_pieces:
                        if x == piece.row and y == piece.col:
                            if piece.color == 'white':
                                block = True
                                break
                            else:
                                self.valid_possibility.append((x, y))
                                block = True
                                break
                    else:
                        self.valid_possibility.append((x, y))

                    if block:
                        break

                for coordinates in self.valid_possibility :
                    x, y = coordinates
                    self.screen.blit(self.cursor_image, (y * self.square_size + 10, x * self.square_size + 10))
                    pygame.display.flip()

        elif self.selected_piece == self.white_bishopA or self.selected_piece == self.white_bishopB :
            if piece_type == 'bishop':
                self.screen.blit(self.circle_image,
                                 (piece_col * self.square_size + 2.5, piece_row * self.square_size - 0.6))
                self.valid_possibility = []

                for NE in range(1, 10):
                    x = piece_row - NE
                    y = piece_col + NE
                    block = False
                    if x > 10 or x < 0 or y > 9 or y < 0 :
                        break
                    for piece in self.all_pieces:
                        if x == piece.row and y == piece.col:
                            if piece.color == 'white':
                                block = True
                                break
                            else:
                                self.valid_possibility.append((x, y))
                                block = True
                                break
                    else:
                        self.valid_possibility.append((x, y))

                    if block:
                        break

                for SE in range(1, 10):
                    x = piece_row + SE
                    y = piece_col + SE
                    block = False
                    if x > 10 or x < 0 or y > 9 or y < 0 :
                        break
                    for piece in self.all_pieces:
                        if x == piece.row and y == piece.col:
                            if piece.color == 'white':
                                block = True
                                break
                            else:
                                self.valid_possibility.append((x, y))
                                block = True
                                break
                    else:
                        self.valid_possibility.append((x, y))

                    if block:
                        break

                for NW in range(1, 10):
                    x = piece_row - NW
                    y = piece_col - NW
                    block = False
                    if x > 10 or x < 0 or y > 9 or y < 0 :
                        break
                    for piece in self.all_pieces:
                        if x == piece.row and y == piece.col:
                            if piece.color == 'white':
                                block = True
                                break
                            else:
                                self.valid_possibility.append((x, y))
                                block = True
                                break
                    else:
                        self.valid_possibility.append((x, y))

                    if block:
                        break

                for SW in range(1, 10):
                    x = piece_row + SW
                    y = piece_col - SW
                    block = False
                    if x > 10 or x < 0 or y > 9 or y < 0 :
                        break
                    for piece in self.all_pieces:
                        if x == piece.row and y == piece.col:
                            if piece.color == 'white':
                                block = True
                                break
                            else:
                                self.valid_possibility.append((x, y))
                                block = True
                                break
                    else:
                        self.valid_possibility.append((x, y))

                    if block:
                        break

                for coordinates in self.valid_possibility:
                    x, y = coordinates
                    self.screen.blit(self.cursor_image, (y * self.square_size + 10, x * self.square_size + 10))
                    pygame.display.flip()

        elif self.selected_piece == self.white_pawn1 or self.selected_piece == self.white_pawn2 or self.selected_piece == self.white_pawn3 or self.selected_piece == self.white_pawn4 or self.selected_piece == self.white_pawn5 or self.selected_piece == self.white_pawn6 or self.selected_piece == self.white_pawn7 or self.selected_piece == self.white_pawn8 or self.selected_piece == self.white_pawn9:
            if piece_type == 'pawn' :
                #print(piece_row,piece_col)
                self.valid_possibility = []
                self.screen.blit(self.circle_image, (piece_col * self.square_size + 2.5, piece_row * self.square_size - 0.6))
                if piece_row == 2.5 :
                    possibility = [(piece_row + 2, piece_col),(piece_row + 1, piece_col)]
                    valid_not_possibility = []
                    for coordinates in possibility:
                        x, y = coordinates
                        if 10 > x > 0 and 9 > y > 0:
                            for pieces in self.all_pieces:
                                if x == pieces.row and y == pieces.col:
                                    valid_not_possibility.append(coordinates)
                        else:
                            valid_not_possibility.append(coordinates)
                        #print(coordinates)
                    self.valid_possibility = list(set(possibility) - set(valid_not_possibility))
                    # for i in self.valid_possibility :
                    #     print(i)
                else:
                    possibility = [(piece_row + 1, piece_col)]
                    valid_not_possibility = []
                    for coordinates in possibility:
                        x, y = coordinates
                        if 10 > x > 0 and 10 > y > 0:
                            for pieces in self.all_pieces:
                                if x == pieces.row and y == pieces.col:
                                    valid_not_possibility.append(coordinates)
                        else:
                            valid_not_possibility.append(coordinates)

                    self.valid_possibility = list(set(possibility) - set(valid_not_possibility))

                possibility = [(piece_row + 1, piece_col + 1), (piece_row + 1, piece_col - 1)]
                for coordinates in possibility:
                    x, y = coordinates
                    if 10 > x > 0 and 9 > y > 0:
                        for pieces in self.all_pieces:
                            if x == pieces.row and y == pieces.col and pieces.color == 'black':
                                self.valid_possibility.append(coordinates)
                    else:
                        pass

                for coordinates in self.valid_possibility:
                    x, y = coordinates
                    self.screen.blit(self.cursor_image, (y * self.square_size + 10, x * self.square_size + 10))
                    pygame.display.flip()

        elif self.selected_piece == self.white_knightA or self.selected_piece == self.white_knightB :
            if piece_type == 'knight' :
                self.screen.blit(self.circle_image, (piece_col * self.square_size + 2.5, piece_row * self.square_size - 0.6))
                possibility = [(piece_row - 2,piece_col - 1),(piece_row - 2 , piece_col + 1),
                               (piece_row - 1,piece_col - 2),(piece_row - 1,piece_col + 2),
                               (piece_row + 1,piece_col - 2),(piece_row + 1,piece_col + 2),
                               (piece_row + 2,piece_col - 1),(piece_row + 2,piece_col + 1)]
                valid_not_possibility = []
                for coordinates in possibility :
                    x , y = coordinates
                    if 10 > x > 0 and 9 > y > 0:
                        for pieces in self.all_pieces :
                            if x == pieces.row and y == pieces.col and pieces.color == 'white':
                                valid_not_possibility.append(coordinates)
                    else:
                        valid_not_possibility.append(coordinates)


                self.valid_possibility = list(set(possibility) - set(valid_not_possibility))

                for coordinates in self.valid_possibility :
                    x, y = coordinates
                    self.screen.blit(self.cursor_image, (y * self.square_size + 10, x * self.square_size + 10))
                    pygame.display.flip()

        elif self.selected_piece == self.black_king :
            if piece_type == 'R_king' :
                self.screen.blit(self.circle_image, (piece_col * self.square_size + 2.5, piece_row * self.square_size + 7.4))
                possibility = [(piece_row , piece_col + 1),  (piece_row + 1,piece_col),
                               (piece_row - 1,piece_col),(piece_row ,piece_col - 1)]
                valid_not_possibility = []
                for coordinates in possibility :
                    x , y = coordinates
                    if 10 > x > 7 and 6 > y > 3:
                        for pieces in self.all_pieces :
                            if x == pieces.row and y == pieces.col and pieces.color == 'black':
                                valid_not_possibility.append(coordinates)
                    else:
                        valid_not_possibility.append(coordinates)


                self.valid_possibility = list(set(possibility) - set(valid_not_possibility))

                if self.black_king.col == self.white_king.col :
                    for N in range(1, 10):
                        x = piece_row - N
                        y = piece_col
                        block = False
                        if x < 0:
                            break
                        for piece in self.all_pieces:
                            if x == piece.row and y == piece.col:
                                if piece.piece_type == 'king':
                                    self.valid_possibility.append((x, y))
                                    block = True
                                    break
                                else:
                                    block = True
                                    break

                        if block:
                            break

                for coordinates in self.valid_possibility :
                    x, y = coordinates
                    self.screen.blit(self.cursor_image, (y * self.square_size + 10, x * self.square_size + 10))
                    pygame.display.flip()

        elif self.selected_piece == self.black_ministerA or self.selected_piece == self.black_ministerB :
            if piece_type == 'R_minister' :
                self.screen.blit(self.circle_image, (piece_col * self.square_size + 2.5, piece_row * self.square_size + 5))
                possibility = [(piece_row - 2,piece_col + 2),(piece_row + 2, piece_col - 2),
                               (piece_row + 2,piece_col + 2),(piece_row - 2,piece_col - 2),]
                valid_not_possibility = []
                for coordinates in possibility :
                    x , y = coordinates
                    if 10 > x > 5 and 9 > y > 0:
                        for pieces in self.all_pieces :
                            if x == pieces.row and y == pieces.col and pieces.color == 'black':
                                valid_not_possibility.append(coordinates)
                    else:
                        valid_not_possibility.append(coordinates)

                for pieces in self.all_pieces:
                    if piece_row + 1 == pieces.row and piece_col + 1 == pieces.col:
                        valid_not_possibility.append((piece_row + 2 , piece_col + 2))

                    elif piece_row - 1 == pieces.row and piece_col - 1 == pieces.col:
                        valid_not_possibility.append((piece_row - 2 , piece_col - 2))

                    elif piece_row + 1 == pieces.row and piece_col - 1 == pieces.col:
                        valid_not_possibility.append((piece_row + 2 , piece_col - 2))

                    elif piece_row - 1 == pieces.row and piece_col + 1 == pieces.col:
                        valid_not_possibility.append((piece_row + 2 , piece_col + 2))

                self.valid_possibility = list(set(possibility) - set(valid_not_possibility))

                for coordinates in self.valid_possibility :
                    x, y = coordinates
                    self.screen.blit(self.cursor_image, (y * self.square_size + 10, x * self.square_size + 10))
                    pygame.display.flip()

        elif self.selected_piece == self.black_advisorA or self.selected_piece == self.black_advisorB :
            if piece_type == 'R_advisor' :
                self.screen.blit(self.circle_image, (piece_col * self.square_size + 2.5, piece_row * self.square_size + 5))
                possibility = [(piece_row - 1,piece_col + 1),(piece_row + 1, piece_col - 1),
                               (piece_row + 1,piece_col + 1),(piece_row - 1,piece_col - 1),]
                valid_not_possibility = []
                for coordinates in possibility :
                    x , y = coordinates
                    if 10 > x > 7 and 6 > y > 3:
                        for pieces in self.all_pieces :
                            if x == pieces.row and y == pieces.col and pieces.color == 'black':
                                valid_not_possibility.append(coordinates)
                    else:
                        valid_not_possibility.append(coordinates)


                self.valid_possibility = list(set(possibility) - set(valid_not_possibility))

                for coordinates in self.valid_possibility :
                    x, y = coordinates
                    self.screen.blit(self.cursor_image, (y * self.square_size + 10, x * self.square_size + 10))
                    pygame.display.flip()

        elif self.selected_piece == self.black_rookA or self.selected_piece == self.black_rookB :
            if piece_type == 'R_rook':
                self.screen.blit(self.circle_image,
                                 (piece_col * self.square_size + 2.5, piece_row * self.square_size - 0.6))
                self.valid_possibility = []

                for N in range(1, 10):
                    x = piece_row - N
                    y = piece_col
                    block = False
                    if x < 0:
                        break
                    for piece in self.all_pieces:
                        if x == piece.row and y == piece.col:
                            if piece.color == 'black':
                                block = True
                                break
                            else:
                                self.valid_possibility.append((x, y))
                                block = True
                                break
                    else:
                        self.valid_possibility.append((x, y))

                    if block:
                        break

                for S in range(1, 10):
                    x = piece_row + S
                    y = piece_col
                    block = False
                    if x > 10:
                        break
                    for piece in self.all_pieces:
                        if x == piece.row and y == piece.col:
                            if piece.color == 'black':
                                block = True
                                break
                            else:
                                self.valid_possibility.append((x, y))
                                block = True
                                break
                    else:
                        self.valid_possibility.append((x, y))

                    if block:
                        break

                for W in range(1, 10):
                    x = piece_row
                    y = piece_col - W
                    block = False
                    if y < 0:
                        break
                    for piece in self.all_pieces:
                        if x == piece.row and y == piece.col:
                            if piece.color == 'black':
                                block = True
                                break
                            else:
                                self.valid_possibility.append((x, y))
                                block = True
                                break
                    else:
                        self.valid_possibility.append((x, y))

                    if block:
                        break

                for E in range(1, 10):
                    x = piece_row
                    y = piece_col + E
                    block = False
                    if y > 9:
                        break
                    for piece in self.all_pieces:
                        if x == piece.row and y == piece.col:
                            if piece.color == 'black':
                                block = True
                                break
                            else:
                                self.valid_possibility.append((x, y))
                                block = True
                                break
                    else:
                        self.valid_possibility.append((x, y))

                    if block:
                        break

                for coordinates in self.valid_possibility :
                    x, y = coordinates
                    self.screen.blit(self.cursor_image, (y * self.square_size + 10, x * self.square_size + 10))
                    pygame.display.flip()

        elif self.selected_piece == self.black_pawn1 or self.selected_piece == self.black_pawn2 or self.selected_piece == self.black_pawn3 or self.selected_piece == self.black_pawn4 or self.selected_piece == self.black_pawn5 :
            if piece_type == 'R_pawn' :
                self.screen.blit(self.circle_image, (piece_col * self.square_size + 2.5, piece_row * self.square_size + 2))
                possibility = []
                valid_not_possibility = []
                #print(piece_row)

                if piece_row > 5 :
                    possibility = [(piece_row - 1,piece_col)]

                elif piece_row < 5 :
                    possibility = [(piece_row - 1, piece_col),(piece_row, piece_col + 1),(piece_row, piece_col - 1)]

                for coordinates in possibility :
                    x , y = coordinates
                    if 10 > x > 0 and 9 > y > 0:
                        for pieces in self.all_pieces :
                            if x == pieces.row and y == pieces.col and pieces.color == 'black':
                                valid_not_possibility.append(coordinates)
                    else:
                        valid_not_possibility.append(coordinates)


                self.valid_possibility = list(set(possibility) - set(valid_not_possibility))

                for coordinates in self.valid_possibility :
                    x, y = coordinates
                    self.screen.blit(self.cursor_image, (y * self.square_size + 10, x * self.square_size + 10))
                    pygame.display.flip()

        elif self.selected_piece == self.black_cavalryA or self.selected_piece == self.black_cavalryB :
            if piece_type == 'R_cavalry' :
                self.screen.blit(self.circle_image, (piece_col * self.square_size + 2.5, piece_row * self.square_size - 0.6))
                possibility = [(piece_row - 2,piece_col - 1),(piece_row - 2 , piece_col + 1),
                               (piece_row - 1,piece_col - 2),(piece_row - 1,piece_col + 2),
                               (piece_row + 1,piece_col - 2),(piece_row + 1,piece_col + 2),
                               (piece_row + 2,piece_col - 1),(piece_row + 2,piece_col + 1)]
                valid_not_possibility = []
                for coordinates in possibility :
                    x , y = coordinates
                    if 10 > x > 0 and 10 > y > 0:
                        for pieces in self.all_pieces :
                            if x == pieces.row and y == pieces.col and pieces.color == 'black':
                                valid_not_possibility.append(coordinates)
                    else:
                        valid_not_possibility.append(coordinates)

                for pieces in self.all_pieces:
                    if piece_row + 1 == pieces.row and piece_col == pieces.col:
                        valid_not_possibility.append((piece_row + 2 , piece_col + 1))
                        valid_not_possibility.append((piece_row + 2 , piece_col - 1))

                    elif piece_row - 1 == pieces.row and piece_col == pieces.col:
                        valid_not_possibility.append((piece_row - 2 , piece_col + 1))
                        valid_not_possibility.append((piece_row - 2 , piece_col - 1))

                    elif piece_row == pieces.row and piece_col - 1 == pieces.col:
                        valid_not_possibility.append((piece_row + 1 , piece_col - 2))
                        valid_not_possibility.append((piece_row - 1 , piece_col - 2))

                    elif piece_row == pieces.row and piece_col + 1 == pieces.col:
                        valid_not_possibility.append((piece_row + 1 , piece_col + 2))
                        valid_not_possibility.append((piece_row - 1 , piece_col + 2))

                self.valid_possibility = list(set(possibility) - set(valid_not_possibility))

                for coordinates in self.valid_possibility :
                    x, y = coordinates
                    self.screen.blit(self.cursor_image, (y * self.square_size + 10, x * self.square_size + 10))
                    pygame.display.flip()

        elif self.selected_piece == self.black_crossbowA or self.selected_piece == self.black_crossbowB :
            if piece_type == 'R_crossbow':
                self.screen.blit(self.circle_image,
                                 (piece_col * self.square_size + 2.5, piece_row * self.square_size - 0.6))
                self.valid_possibility = []

                for N in range(1, 10):
                    x = piece_row - N
                    y = piece_col
                    block = False
                    if x < 0:
                        break
                    for piece in self.all_pieces:
                        if x == piece.row and y == piece.col:
                            block = True
                            break
                    else:
                        self.valid_possibility.append((x, y))

                    if block:
                        break

                R = False

                for NX in range(1, 10):
                    x = piece_row - NX
                    y = piece_col
                    block = False
                    if x < 0:
                        break
                    for piece in self.all_pieces:
                        #print(R)
                        if x == piece.row and y == piece.col and R == False:
                            #block = True
                            R = True
                            #print(x, y)
                            #break
                        elif x == piece.row and y == piece.col and R == True :
                            #print(x,y)
                            if piece.color == 'white':
                                self.valid_possibility.append((x, y))
                                print(x, y)
                                block = True
                                break
                            elif piece.color == 'black':
                                block = True
                                break
                            else:
                                pass
                                #print('Error')

                    if block:
                        break

                for S in range(1, 10):
                    x = piece_row + S
                    y = piece_col
                    block = False
                    if x > 10:
                        break
                    for piece in self.all_pieces:
                        if x == piece.row and y == piece.col:
                            block = True
                            break
                    else:
                        self.valid_possibility.append((x, y))

                    if block:
                        break

                R = False

                for SX in range(1, 10):
                    x = piece_row + SX
                    y = piece_col
                    block = False
                    if x < 0:
                        break
                    for piece in self.all_pieces:
                        # print(R)
                        if x == piece.row and y == piece.col and R == False:
                            # block = True
                            R = True
                            # print(x, y)
                            # break
                        elif x == piece.row and y == piece.col and R == True:
                            # print(x,y)
                            if piece.color == 'white':
                                self.valid_possibility.append((x, y))
                                print(x, y)
                                block = True
                                break
                            elif piece.color == 'black':
                                block = True
                                break
                            else:
                                pass
                                # print('Error')

                    if block:
                        break

                for W in range(1, 10):
                    x = piece_row
                    y = piece_col - W
                    block = False
                    if y < 0:
                        break
                    for piece in self.all_pieces:
                        if x == piece.row and y == piece.col:
                            block = True
                            break
                    else:
                        self.valid_possibility.append((x, y))

                    if block:
                        break

                R = False

                for WX in range(1, 10):
                    x = piece_row
                    y = piece_col - WX
                    block = False
                    if x < 0:
                        break
                    for piece in self.all_pieces:
                        # print(R)
                        if x == piece.row and y == piece.col and R == False:
                            # block = True
                            R = True
                            # print(x, y)
                            # break
                        elif x == piece.row and y == piece.col and R == True:
                            # print(x,y)
                            if piece.color == 'white':
                                self.valid_possibility.append((x, y))
                                print(x, y)
                                block = True
                                break
                            elif piece.color == 'black':
                                block = True
                                break
                            else:
                                pass
                                # print('Error')

                    if block:
                        break

                for E in range(1, 10):
                    x = piece_row
                    y = piece_col + E
                    block = False
                    if y > 9:
                        break
                    for piece in self.all_pieces:
                        if x == piece.row and y == piece.col:
                            block = True
                            break
                    else:
                        self.valid_possibility.append((x, y))

                    if block:
                        break

                R = False

                for EX in range(1, 10):
                    x = piece_row
                    y = piece_col + EX
                    block = False
                    if x < 0:
                        break
                    for piece in self.all_pieces:
                        # print(R)
                        if x == piece.row and y == piece.col and R == False:
                            # block = True
                            R = True
                            # print(x, y)
                            # break
                        elif x == piece.row and y == piece.col and R == True:
                            # print(x,y)
                            if piece.color == 'white':
                                self.valid_possibility.append((x, y))
                                print(x, y)
                                block = True
                                break
                            elif piece.color == 'black':
                                block = True
                                break
                            else:
                                pass
                                # print('Error')

                    if block:
                        break

                for coordinates in self.valid_possibility:
                    x, y = coordinates
                    self.screen.blit(self.cursor_image, (y * self.square_size + 10, x * self.square_size + 10))
                    pygame.display.flip()

    def remove_piece(self, row,col):
        for piece in self.all_pieces:
            if row == piece.row and col == piece.col and self.selected_piece != piece :
                self.all_pieces.remove(piece)
    def run(self):
        self.screen.blit(self.start_image, (0, 0))
        if self.start :
            pygame.display.flip()
        while self.running:
            # if self.start :
            #     self.screen.blit(self.start_image, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # if self.start :
                    #     self.start = False
                    pygame.display.flip()
                    # 检测左键点击
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    if self.is_mouse_click_on_back(self.back_image, mouse_x, mouse_y) and self.tern > 1 :
                        #print("True")
                        self.tern = self.tern - 1
                        if self.tern % 2 == 1:
                            print('已重置，现在是帝国方走棋')
                        elif self.tern % 2 == 0:
                            print('已重置，现在是洛城方走棋')
                    # if self.is_mouse_click_on_sticker(self.sticker_image, mouse_x, mouse_y):
                    #     self.sticker = self.sticker + 1
                    #     print('mouse_click_on_sticker')

                    # if self.is_mouse_click_on_sticker(self.sticker_image, mouse_x, mouse_y) and self.sticker == True:
                    #     self.white_king_image = pygame.image.load('data/帝国棋子/王.png')
                    #     self.white_queen_image = pygame.image.load('data/帝国棋子/后.png')
                    #     self.white_knight_image = pygame.image.load('data/帝国棋子/骑.png')
                    #     self.white_rook_image = pygame.image.load('data/帝国棋子/堡.png')
                    #     self.white_bishop_image = pygame.image.load('data/帝国棋子/圣.png')
                    #     self.white_pawn_image = pygame.image.load('data/帝国棋子/兵.png')
                    #     self.black_king_image = pygame.image.load('data/洛城棋子/将.png')
                    #     self.black_advisor_image = pygame.image.load('data/洛城棋子/士.png')
                    #     self.black_minister_image = pygame.image.load('data/洛城棋子/相.png')
                    #     self.black_cavalry_image = pygame.image.load('data/洛城棋子/马.png')
                    #     self.black_crossbow_image = pygame.image.load('data/洛城棋子/砲.png')
                    #     self.black_rook_image = pygame.image.load('data/洛城棋子/車.png')
                    #     self.black_pawn_image = pygame.image.load('data/洛城棋子/卒.png')
                    #
                    #     self.sticker = False
                    #     print(1)
                    #     pygame.display.flip()
                    #
                    # elif self.is_mouse_click_on_sticker(self.sticker_image, mouse_x, mouse_y) and self.sticker == False:
                    #     #print("True")
                    #     self.white_king_image = pygame.image.load('data/帝国棋子/扎伊兹克.png')
                    #     self.white_queen_image = pygame.image.load('data/帝国棋子/鬼面武士.png')
                    #     self.white_knight_image = pygame.image.load('data/帝国棋子/帝国骑兵.png')
                    #     self.white_rook_image = pygame.image.load('data/帝国棋子/堡垒.png')
                    #     self.white_bishop_image = pygame.image.load('data/帝国棋子/圣职者.png')
                    #     self.white_pawn_image = pygame.image.load('data/帝国棋子/帝国盾步兵.png')
                    #     self.black_king_image = pygame.image.load('data/洛城棋子/洛武帝.png')
                    #     self.black_advisor_image = pygame.image.load('data/洛城棋子/近卫.png')
                    #     self.black_minister_image = pygame.image.load('data/洛城棋子/丞相.png')
                    #     self.black_cavalry_image = pygame.image.load('data/洛城棋子/战马.png')
                    #     self.black_crossbow_image = pygame.image.load('data/洛城棋子/洛城重弩.png')
                    #     self.black_rook_image = pygame.image.load('data/洛城棋子/战車.png')
                    #     self.black_pawn_image = pygame.image.load('data/洛城棋子/洛城兵卒.png')
                    #
                    #     self.sticker = True
                    #     #print(self.sticker)
                    #     print(2)
                    #     pygame.display.flip()

                    if self.is_mouse_click_on_refresh(self.refresh_image, mouse_x, mouse_y):
                        print("Refreshed")
                        self.valid_possibility = []
                        self.selected_piece = None

                    if self.selected_piece != None :
                        if self.is_mouse_click_on_cursor(mouse_y, mouse_x):
                            self.remove_piece(mouse_y // self.square_size - 0.5, mouse_x // self.square_size - 0.5)
                    #if self.selected_piece == False :
                    for piece in self.all_pieces:
                        if self.tern % 2 == 1 :
                            if self.is_mouse_click_on_piece(self.white_king, mouse_x,
                                                            mouse_y) and piece == self.white_king:
                                # print('king')
                                self.selected_piece = self.white_king
                                self.is_valid_move('king', self.white_king.row, self.white_king.col)
                                break

                            elif self.is_mouse_click_on_piece(self.white_queen, mouse_x,
                                                              mouse_y) and piece == self.white_queen:
                                # print('queen')
                                self.selected_piece = self.white_queen
                                self.is_valid_move('queen', self.white_queen.row, self.white_queen.col)
                                break

                            elif self.is_mouse_click_on_piece(self.white_rookA, mouse_x,
                                                              mouse_y) and piece == self.white_rookA:
                                # print('rook')
                                self.selected_piece = self.white_rookA
                                self.is_valid_move('rook', self.white_rookA.row, self.white_rookA.col)
                                break

                            elif self.is_mouse_click_on_piece(self.white_rookB, mouse_x,
                                                              mouse_y) and piece == self.white_rookB:
                                # print('rook')
                                self.selected_piece = self.white_rookB
                                self.is_valid_move('rook', self.white_rookB.row, self.white_rookB.col)
                                break

                            elif self.is_mouse_click_on_piece(self.white_bishopA, mouse_x,
                                                              mouse_y) and piece == self.white_bishopA:
                                # print('bishop')
                                self.selected_piece = self.white_bishopA
                                self.is_valid_move('bishop', self.white_bishopA.row, self.white_bishopA.col)
                                break

                            elif self.is_mouse_click_on_piece(self.white_bishopB, mouse_x,
                                                              mouse_y) and piece == self.white_bishopB:
                                # print('bishop')
                                self.selected_piece = self.white_bishopB
                                self.is_valid_move('bishop', self.white_bishopB.row, self.white_bishopB.col)
                                break

                            elif self.is_mouse_click_on_piece(self.white_pawn1, mouse_x,
                                                              mouse_y) and piece == self.white_pawn1:
                                # print('pawn')
                                self.selected_piece = self.white_pawn1
                                self.is_valid_move('pawn', self.white_pawn1.row, self.white_pawn1.col)
                                break

                            elif self.is_mouse_click_on_piece(self.white_pawn2, mouse_x,
                                                              mouse_y) and piece == self.white_pawn2:
                                # print('pawn')
                                self.selected_piece = self.white_pawn2
                                self.is_valid_move('pawn', self.white_pawn2.row, self.white_pawn2.col)
                                break

                            elif self.is_mouse_click_on_piece(self.white_pawn3, mouse_x,
                                                              mouse_y) and piece == self.white_pawn3:
                                # print('pawn')
                                self.selected_piece = self.white_pawn3
                                self.is_valid_move('pawn', self.white_pawn3.row, self.white_pawn3.col)
                                break

                            elif self.is_mouse_click_on_piece(self.white_pawn4, mouse_x,
                                                              mouse_y) and piece == self.white_pawn4:
                                # print('pawn')
                                self.selected_piece = self.white_pawn4
                                self.is_valid_move('pawn', self.white_pawn4.row, self.white_pawn4.col)
                                break

                            elif self.is_mouse_click_on_piece(self.white_pawn5, mouse_x,
                                                              mouse_y) and piece == self.white_pawn5:
                                # print('pawn')
                                self.selected_piece = self.white_pawn5
                                self.is_valid_move('pawn', self.white_pawn5.row, self.white_pawn5.col)
                                break

                            elif self.is_mouse_click_on_piece(self.white_pawn6, mouse_x,
                                                              mouse_y) and piece == self.white_pawn6:
                                # print('pawn')
                                self.selected_piece = self.white_pawn6
                                self.is_valid_move('pawn', self.white_pawn6.row, self.white_pawn6.col)
                                break

                            elif self.is_mouse_click_on_piece(self.white_pawn7, mouse_x,
                                                              mouse_y) and piece == self.white_pawn7:
                                # print('pawn')
                                self.selected_piece = self.white_pawn7
                                self.is_valid_move('pawn', self.white_pawn7.row, self.white_pawn7.col)
                                break

                            elif self.is_mouse_click_on_piece(self.white_pawn8, mouse_x,
                                                              mouse_y) and piece == self.white_pawn8:
                                # print('pawn')
                                self.selected_piece = self.white_pawn8
                                self.is_valid_move('pawn', self.white_pawn8.row, self.white_pawn8.col)
                                break

                            elif self.is_mouse_click_on_piece(self.white_pawn9, mouse_x,
                                                              mouse_y) and piece == self.white_pawn9:
                                # print('pawn')
                                self.selected_piece = self.white_pawn9
                                self.is_valid_move('pawn', self.white_pawn9.row, self.white_pawn9.col)
                                break

                            elif self.is_mouse_click_on_piece(self.white_knightA, mouse_x,
                                                              mouse_y) and piece == self.white_knightA:
                                # print('knight')
                                self.selected_piece = self.white_knightA
                                self.is_valid_move('knight', self.white_knightA.row, self.white_knightA.col)
                                break

                            elif self.is_mouse_click_on_piece(self.white_knightB, mouse_x,
                                                              mouse_y) and piece == self.white_knightB:
                                # print('knight')
                                self.selected_piece = self.white_knightB
                                self.is_valid_move('knight', self.white_knightB.row, self.white_knightB.col)
                                break

                        elif self.tern % 2 == 0 :
                            if self.is_mouse_click_on_piece(self.black_king, mouse_x,
                                                            mouse_y) and piece == self.black_king:
                                # print('R_king')
                                self.selected_piece = self.black_king
                                self.is_valid_move('R_king', self.black_king.row, self.black_king.col)
                                break

                            elif self.is_mouse_click_on_piece(self.black_advisorA, mouse_x,
                                                            mouse_y) and piece == self.black_advisorA:
                                # print('R_advisor')
                                self.selected_piece = self.black_advisorA
                                self.is_valid_move('R_advisor', self.black_advisorA.row, self.black_advisorA.col)
                                break

                            elif self.is_mouse_click_on_piece(self.black_advisorB, mouse_x,
                                                            mouse_y) and piece == self.black_advisorB:
                                # print('R_advisor')
                                self.selected_piece = self.black_advisorB
                                self.is_valid_move('R_advisor', self.black_advisorB.row, self.black_advisorB.col)
                                break

                            elif self.is_mouse_click_on_piece(self.black_ministerA, mouse_x,
                                                            mouse_y) and piece == self.black_ministerA:
                                # print('R_minister')
                                self.selected_piece = self.black_ministerA
                                self.is_valid_move('R_minister', self.black_ministerA.row, self.black_ministerA.col)
                                break

                            elif self.is_mouse_click_on_piece(self.black_ministerB, mouse_x,
                                                            mouse_y) and piece == self.black_ministerB:
                                # print('R_minister')
                                self.selected_piece = self.black_ministerB
                                self.is_valid_move('R_minister', self.black_ministerB.row, self.black_ministerB.col)
                                break

                            elif self.is_mouse_click_on_piece(self.black_cavalryA, mouse_x,
                                                            mouse_y) and piece == self.black_cavalryA:
                                # print('R_cavalry')
                                self.selected_piece = self.black_cavalryA
                                self.is_valid_move('R_cavalry', self.black_cavalryA.row, self.black_cavalryA.col)
                                break

                            elif self.is_mouse_click_on_piece(self.black_cavalryB, mouse_x,
                                                            mouse_y) and piece == self.black_cavalryB:
                                # print('R_cavalry')
                                self.selected_piece = self.black_cavalryB
                                self.is_valid_move('R_cavalry', self.black_cavalryB.row, self.black_cavalryB.col)
                                break

                            elif self.is_mouse_click_on_piece(self.black_crossbowA, mouse_x,
                                                              mouse_y) and piece == self.black_crossbowA:
                                # print('R_crossbow')
                                self.selected_piece = self.black_crossbowA
                                self.is_valid_move('R_crossbow', self.black_crossbowA.row, self.black_crossbowA.col)
                                break

                            elif self.is_mouse_click_on_piece(self.black_crossbowB, mouse_x,
                                                              mouse_y) and piece == self.black_crossbowB:
                                # print('R_crossbow')
                                self.selected_piece = self.black_crossbowB
                                self.is_valid_move('R_crossbow', self.black_crossbowB.row, self.black_crossbowB.col)
                                break

                            elif self.is_mouse_click_on_piece(self.black_rookA, mouse_x,
                                                            mouse_y) and piece == self.black_rookA:
                                # print('R_rook')
                                self.selected_piece = self.black_rookA
                                self.is_valid_move('R_rook', self.black_rookA.row, self.black_rookA.col)
                                break

                            elif self.is_mouse_click_on_piece(self.black_rookB, mouse_x,
                                                            mouse_y) and piece == self.black_rookB:
                                # print('R_rook')
                                self.selected_piece = self.black_rookB
                                self.is_valid_move('R_rook', self.black_rookB.row, self.black_rookB.col)
                                break

                            elif self.is_mouse_click_on_piece(self.black_pawn1, mouse_x,
                                                            mouse_y) and piece == self.black_pawn1:
                                # print('R_pawn')
                                self.selected_piece = self.black_pawn1
                                self.is_valid_move('R_pawn', self.black_pawn1.row, self.black_pawn1.col)
                                break


                            elif self.is_mouse_click_on_piece(self.black_pawn2, mouse_x,
                                                            mouse_y) and piece == self.black_pawn2:
                                # print('R_pawn')
                                self.selected_piece = self.black_pawn2
                                self.is_valid_move('R_pawn', self.black_pawn2.row, self.black_pawn2.col)
                                break

                            elif self.is_mouse_click_on_piece(self.black_pawn3, mouse_x,
                                                            mouse_y) and piece == self.black_pawn3:
                                # print('R_pawn')
                                self.selected_piece = self.black_pawn3
                                self.is_valid_move('R_pawn', self.black_pawn3.row, self.black_pawn3.col)
                                break

                            elif self.is_mouse_click_on_piece(self.black_pawn4, mouse_x,
                                                            mouse_y) and piece == self.black_pawn4:
                                # print('R_pawn')
                                self.selected_piece = self.black_pawn4
                                self.is_valid_move('R_pawn', self.black_pawn4.row, self.black_pawn4.col)
                                break

                            elif self.is_mouse_click_on_piece(self.black_pawn5, mouse_x,
                                                            mouse_y) and piece == self.black_pawn5:
                                # print('R_pawn')
                                self.selected_piece = self.black_pawn5
                                self.is_valid_move('R_pawn', self.black_pawn5.row, self.black_pawn5.col)
                                break

                        else:
                            pass


                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if self.is_mouse_click_on_cursor(mouse_y, mouse_x):
                        self.selected_piece.row = mouse_y // self.square_size - 0.5
                        self.selected_piece.col = mouse_x // self.square_size - 0.5

                        #self.remove_piece(self.selected_piece.row, self.selected_piece.col)

                        self.valid_possibility = []
                        pygame.display.flip()
                        self.selected_piece = None
                        self.tern = self.tern + 1

                        # if True:
                        #     pygame.display.flip()

                # 在游戏循环中绘制棋盘
                self.screen.blit(self.chessboard_image, (0, 0))
                # self.screen.blit(self.back_image, (800, 100))
                # self.screen.blit(self.sticker_image, (800, 640))
                # self.screen.blit(self.refresh_image, (800, 365))
                self.screen.blit(self.back_image, (self.window_width * 0.91, 100))
                self.screen.blit(self.sticker_image, (self.window_width * 0.91, 640))
                self.screen.blit(self.refresh_image, (self.window_width * 0.91, 365))
                # 计算棋子应该绘制的大小，例如，设置为格子大小的一部分
                piece_size_ratio = 0.1  # 棋子大小相对于格子大小的比例
                piece_size = min(self.window_width, self.window_height) * piece_size_ratio

                # 绘制棋子，传递棋盘格子的位置
                alpha = 0
                for piece in self.all_pieces :
                    if piece == self.white_king :
                        self.white_king.draw(self.screen, piece_size)
                        alpha = alpha + 1
                    elif piece == self.white_queen :
                        self.white_queen.draw(self.screen, piece_size)
                    elif piece == self.white_knightA :
                        self.white_knightA.draw(self.screen, piece_size)
                    elif piece == self.white_knightB :
                        self.white_knightB.draw(self.screen, piece_size)
                    elif piece == self.white_rookA:
                        self.white_rookA.draw(self.screen, piece_size)
                    elif piece ==self.white_rookB:
                        self.white_rookB.draw(self.screen, piece_size)
                    elif piece ==self.white_bishopA:
                        self.white_bishopA.draw(self.screen, piece_size)
                    elif piece ==self.white_bishopB:
                        self.white_bishopB.draw(self.screen, piece_size)
                    elif piece ==self.white_pawn1:
                        self.white_pawn1.draw(self.screen, piece_size)
                    elif piece ==self.white_pawn2:
                        self.white_pawn2.draw(self.screen, piece_size)
                    elif piece ==self.white_pawn3:
                        self.white_pawn3.draw(self.screen, piece_size)
                    elif piece ==self.white_pawn4:
                        self.white_pawn4.draw(self.screen, piece_size)
                    elif piece ==self.white_pawn5:
                        self.white_pawn5.draw(self.screen, piece_size)
                    elif piece ==self.white_pawn6:
                        self.white_pawn6.draw(self.screen, piece_size)
                    elif piece ==self.white_pawn7:
                        self.white_pawn7.draw(self.screen, piece_size)
                    elif piece ==self.white_pawn8:
                        self.white_pawn8.draw(self.screen, piece_size)
                    elif piece ==self.white_pawn9:
                        self.white_pawn9.draw(self.screen, piece_size)
                    elif piece ==self.black_king:
                        self.black_king.draw(self.screen, piece_size)
                        alpha = alpha + 1
                    elif piece ==self.black_advisorA:
                        self.black_advisorA.draw(self.screen, piece_size)
                    elif piece ==self.black_advisorB:
                        self.black_advisorB.draw(self.screen, piece_size)
                    elif piece ==self.black_ministerA:
                        self.black_ministerA.draw(self.screen, piece_size)
                    elif piece ==self.black_ministerB:
                        self.black_ministerB.draw(self.screen, piece_size)
                    elif piece ==self.black_cavalryA:
                        self.black_cavalryA.draw(self.screen, piece_size)
                    elif piece ==self.black_cavalryB:
                        self.black_cavalryB.draw(self.screen, piece_size)
                    elif piece ==self.black_crossbowA:
                        self.black_crossbowA.draw(self.screen, piece_size)
                    elif piece ==self.black_crossbowB:
                        self.black_crossbowB.draw(self.screen, piece_size)
                    elif piece ==self.black_rookA:
                        self.black_rookA.draw(self.screen, piece_size)
                    elif piece ==self.black_rookB:
                        self.black_rookB.draw(self.screen, piece_size)
                    elif piece ==self.black_pawn1:
                        self.black_pawn1.draw(self.screen, piece_size)
                    elif piece ==self.black_pawn2:
                        self.black_pawn2.draw(self.screen, piece_size)
                    elif piece ==self.black_pawn3:
                        self.black_pawn3.draw(self.screen, piece_size)
                    elif piece ==self.black_pawn4:
                        self.black_pawn4.draw(self.screen, piece_size)
                    elif piece ==self.black_pawn5:
                        self.black_pawn5.draw(self.screen, piece_size)

                while alpha < 2 :
                    #self.running = False
                    check = False
                    self.screen.blit(self.game_over_image, (0, 0))
                    self.screen.blit(self.restart_image, (230, 530))
                    self.screen.blit(self.off_image, (230, 650))
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            if self.is_mouse_click_on_off :
                                #self.running = False
                                pygame.quit()

                            elif self.is_mouse_click_on_restart :
                                print(1)
                                self.all_pieces = [
                                    self.white_king, self.white_queen, self.white_knightA, self.white_knightB,
                                    self.white_rookA, self.white_rookB, self.white_bishopA, self.white_bishopB,
                                    self.white_pawn1, self.white_pawn2, self.white_pawn3, self.white_pawn4,
                                    self.white_pawn5, self.white_pawn6, self.white_pawn7, self.white_pawn8,
                                    self.white_pawn9, self.black_king, self.black_advisorA, self.black_advisorB,
                                    self.black_ministerA, self.black_ministerB, self.black_cavalryA,
                                    self.black_cavalryB,
                                    self.black_crossbowA, self.black_crossbowB, self.black_rookA, self.black_rookB,
                                    self.black_pawn1, self.black_pawn2, self.black_pawn3, self.black_pawn4,
                                    self.black_pawn5]

                                self.white_king = ChessPiece('white', 'king', 1.5, 4.5, self.white_king_image,
                                                             self.square_size)
                                self.white_queen = ChessPiece('white', 'queen', 0.5, 4.5, self.white_queen_image,
                                                              self.square_size)
                                self.white_knightA = ChessPiece('white', 'knight', 1.5, 1.5, self.white_knight_image,
                                                                self.square_size)
                                self.white_knightB = ChessPiece('white', 'knight', 1.5, 7.5, self.white_knight_image,
                                                                self.square_size)
                                self.white_rookA = ChessPiece('white', 'rook', 1.5, 0.5, self.white_rook_image,
                                                              self.square_size)
                                self.white_rookB = ChessPiece('white', 'rook', 1.5, 8.5, self.white_rook_image,
                                                              self.square_size)
                                self.white_bishopA = ChessPiece('white', 'bishop', 1.5, 3.5, self.white_bishop_image,
                                                                self.square_size)
                                self.white_bishopB = ChessPiece('white', 'bishop', 1.5, 5.5, self.white_bishop_image,
                                                                self.square_size)
                                self.white_pawn1 = ChessPiece('white', 'pawn', 2.5, 0.5, self.white_pawn_image,
                                                              self.square_size)
                                self.white_pawn2 = ChessPiece('white', 'pawn', 2.5, 1.5, self.white_pawn_image,
                                                              self.square_size)
                                self.white_pawn3 = ChessPiece('white', 'pawn', 2.5, 2.5, self.white_pawn_image,
                                                              self.square_size)
                                self.white_pawn4 = ChessPiece('white', 'pawn', 2.5, 3.5, self.white_pawn_image,
                                                              self.square_size)
                                self.white_pawn5 = ChessPiece('white', 'pawn', 2.5, 4.5, self.white_pawn_image,
                                                              self.square_size)
                                self.white_pawn6 = ChessPiece('white', 'pawn', 2.5, 5.5, self.white_pawn_image,
                                                              self.square_size)
                                self.white_pawn7 = ChessPiece('white', 'pawn', 2.5, 6.5, self.white_pawn_image,
                                                              self.square_size)
                                self.white_pawn8 = ChessPiece('white', 'pawn', 2.5, 7.5, self.white_pawn_image,
                                                              self.square_size)
                                self.white_pawn9 = ChessPiece('white', 'pawn', 2.5, 8.5, self.white_pawn_image,
                                                              self.square_size)
                                self.black_king = ChessPiece('black', 'R_king', 9.5, 4.5, self.black_king_image,
                                                             self.square_size)
                                self.black_advisorA = ChessPiece('black', 'R_advisor', 9.5, 3.5,
                                                                 self.black_advisor_image, self.square_size)
                                self.black_advisorB = ChessPiece('black', 'R_advisor', 9.5, 5.5,
                                                                 self.black_advisor_image, self.square_size)
                                self.black_ministerA = ChessPiece('black', 'R_minister', 9.5, 2.5,
                                                                  self.black_minister_image, self.square_size)
                                self.black_ministerB = ChessPiece('black', 'R_minister', 9.5, 6.5,
                                                                  self.black_minister_image, self.square_size)
                                self.black_cavalryA = ChessPiece('black', 'R_cavalry', 9.5, 1.5,
                                                                 self.black_cavalry_image, self.square_size)
                                self.black_cavalryB = ChessPiece('black', 'R_cavalry', 9.5, 7.5,
                                                                 self.black_cavalry_image, self.square_size)
                                self.black_crossbowA = ChessPiece('black', 'R_crossbow', 7.5, 1.5,
                                                                  self.black_crossbow_image, self.square_size)
                                self.black_crossbowB = ChessPiece('black', 'R_crossbow', 7.5, 7.5,
                                                                  self.black_crossbow_image, self.square_size)
                                self.black_rookA = ChessPiece('black', 'R_rook', 9.5, 0.5, self.black_rook_image,
                                                              self.square_size)
                                self.black_rookB = ChessPiece('black', 'R_rook', 9.5, 8.5, self.black_rook_image,
                                                              self.square_size)
                                self.black_pawn1 = ChessPiece('black', 'R_pawn', 6.5, 0.5, self.black_pawn_image,
                                                              self.square_size)
                                self.black_pawn2 = ChessPiece('black', 'R_pawn', 6.5, 2.5, self.black_pawn_image,
                                                              self.square_size)
                                self.black_pawn3 = ChessPiece('black', 'R_pawn', 6.5, 4.5, self.black_pawn_image,
                                                              self.square_size)
                                self.black_pawn4 = ChessPiece('black', 'R_pawn', 6.5, 6.5, self.black_pawn_image,
                                                              self.square_size)
                                self.black_pawn5 = ChessPiece('black', 'R_pawn', 6.5, 8.5, self.black_pawn_image,
                                                              self.square_size)

                                cheak =True

                            else:
                                pass

                    if check:
                        break
                # 更新屏幕
                #pygame.display.flip()

        # 退出Pygame
        pygame.quit()

class ChessPiece:
    def __init__(self, color, piece_type, row, col, image, piece_size):
        self.color = color  # 棋子颜色
        self.piece_type = piece_type  # 棋子类型
        self.row = row  # 棋子所在行
        self.col = col  # 棋子所在列

        # 缩放棋子图像以保持一致的大小
        self.image = pygame.transform.scale(image, (piece_size, piece_size))

    def draw(self, screen, square_size):
        # 绘制棋子到指定屏幕位置
        if self.image is not None:
            piece_rect = self.image.get_rect()
            piece_rect.topleft = (self.col * square_size, self.row * square_size)
            screen.blit(self.image, piece_rect)

if __name__ == "__main__":
    game = ChessGame()
    game.run()