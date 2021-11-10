import pygame
from pygame.locals import *
import os
import agente
import math

class Supermercado:
    
    def __init__(self):
        self.OOOO0OO0OOOOO0O0 = 100
        self.OOO00O0O00000OO0 = [
            (17, 85),
            (760, 325)]
        self.O00000OO0OO0O000 = [
            [
                (475, 125),
                chr(65) + chr(110) + chr(97)],
            [
                (175, 270),
                chr(67) + chr(97) + chr(114) + chr(108) + chr(111) + chr(115)],
            [
                (365, 570),
                chr(77) + chr(97) + chr(114) + chr(105) + chr(97)]]
        self.O0000000O0O000OO = [
            [
                (730, 50),
                chr(80) + chr(97) + chr(117) + chr(108) + chr(111)],
            [
                (495, 545),
                chr(77) + chr(105) + chr(103) + chr(117) + chr(101) + chr(108)],
            [
                (425, 35),
                chr(77) + chr(97) + chr(114) + chr(105) + chr(97)],
            [
                (695, 570),
                chr(82) + chr(117) + chr(105)],
            [
                (100, 550),
                chr(80) + chr(97) + chr(117) + chr(108) + chr(97)],
            [
                (555, 40),
                chr(65) + chr(100) + chr(233) + chr(114) + chr(105) + chr(116) + chr(111)]]
        self.O00O00OO00O0O0OO = [
            [
                (630, 105),
                chr(82) + chr(105) + chr(99) + chr(97) + chr(114) + chr(100) + chr(111)],
            [
                (335, 490),
                chr(67) + chr(108) + chr(225) + chr(117) + chr(100) + chr(105) + chr(97)],
            [
                (190, 120),
                chr(69) + chr(108) + chr(115) + chr(97)],
            [
                (90, 400),
                chr(74) + chr(111) + chr(97) + chr(113) + chr(117) + chr(105) + chr(109)],
            [
                (260, 275),
                chr(70) + chr(225) + chr(98) + chr(105) + chr(111)],
            [
                (500, 470),
                chr(83) + chr(117) + chr(115) + chr(97) + chr(110) + chr(97)],
            [
                (700, 500),
                chr(77) + chr(105) + chr(99) + chr(97) + chr(101) + chr(108) + chr(97)],
            [
                (730, 240),
                chr(65) + chr(109) + chr(225) + chr(108) + chr(105) + chr(97)]]
        self.OO0OO00OO000OO00 = [
            [
                (275, 535),
                chr(99) + chr(97) + chr(105) + chr(120) + chr(97) + chr(49)],
            [
                (235, 535),
                chr(99) + chr(97) + chr(105) + chr(120) + chr(97) + chr(50)],
            [
                (195, 535),
                chr(99) + chr(97) + chr(105) + chr(120) + chr(97) + chr(51)]]
        self.OOOOO0OO00OO0OO0 = [
            [
                (285, 30),
                chr(112) + chr(97) + chr(100) + chr(97) + chr(114) + chr(105) + chr(97)],
            [
                (435, 95),
                chr(102) + chr(114) + chr(117) + chr(116) + chr(97) + chr(114) + chr(105) + chr(97)],
            [
                (760, 110),
                chr(116) + chr(97) + chr(108) + chr(104) + chr(111)],
            [
                (770, 565),
                chr(98) + chr(101) + chr(98) + chr(105) + chr(100) + chr(97) + chr(115)],
            [
                (435, 510),
                chr(104) + chr(105) + chr(103) + chr(105) + chr(101) + chr(110) + chr(101)],
            [
                (585, 490),
                chr(112) + chr(97) + chr(112) + chr(101) + chr(108) + chr(97) + chr(114) + chr(105) + chr(97)]]
        self.OO00O0OOO000OOOO = [
            [
                (210, 65),
                chr(99) + chr(97) + chr(114) + chr(114) + chr(105) + chr(110) + chr(104) + chr(111) + chr(49)],
            [
                (565, 115),
                chr(99) + chr(97) + chr(114) + chr(114) + chr(105) + chr(110) + chr(104) + chr(111) + chr(50)],
            [
                (630, 550),
                chr(99) + chr(97) + chr(114) + chr(114) + chr(105) + chr(110) + chr(104) + chr(111) + chr(51)],
            [
                (245, 235),
                chr(99) + chr(97) + chr(114) + chr(114) + chr(105) + chr(110) + chr(104) + chr(111) + chr(52)],
            [
                (60, 370),
                chr(99) + chr(97) + chr(114) + chr(114) + chr(105) + chr(110) + chr(104) + chr(111) + chr(53)],
            [
                (550, 550),
                chr(99) + chr(97) + chr(114) + chr(114) + chr(105) + chr(110) + chr(104) + chr(111) + chr(54)],
            [
                (550, 520),
                chr(99) + chr(97) + chr(114) + chr(114) + chr(105) + chr(110) + chr(104) + chr(111) + chr(55)]]
        self.OOO000OOOO000OOO = [
            'dejavusans',
            'couriernew',
            'Papyrus',
            'Comic Sans MS',
            'timesnewroman']
        self.O0O00O00OO0000OO = { }
        self.OO000OO0O000OOO0 = { }
        self.OOOO00O00OO00O0O = { }
        self.OOO0OO0O0000O00O = self.OO0000O0OO0O0OOO(chr(105) + chr(109) + chr(103) + chr(115) + chr(47) + chr(99) + chr(97) + chr(105) + chr(120) + chr(97) + chr(46) + chr(112) + chr(110) + chr(103))
        self.OOO0000O0O00OO0O = self.OO0000O0OO0O0OOO(chr(105) + chr(109) + chr(103) + chr(115) + chr(47) + chr(116) + chr(105) + chr(106) + chr(111) + chr(108) + chr(111) + chr(51) + chr(46) + chr(112) + chr(110) + chr(103))
        self.OO000OO0OO000O0O = self.OO0000O0OO0O0OOO(chr(105) + chr(109) + chr(103) + chr(115) + chr(47) + chr(99) + chr(97) + chr(114) + chr(116) + chr(46) + chr(106) + chr(112) + chr(103))
        self.O00O0O0O0OO0O00O = self.OO0000O0OO0O0OOO(chr(105) + chr(109) + chr(103) + chr(115) + chr(47) + chr(98) + chr(111) + chr(116) + chr(51) + chr(46) + chr(112) + chr(110) + chr(103))
        self.OO0O00OOO00OO0OO = self.OO0000O0OO0O0OOO(chr(105) + chr(109) + chr(103) + chr(115) + chr(47) + chr(65) + chr(49) + chr(46) + chr(112) + chr(110) + chr(103))
        self.OO00OOOO0OO0OOOO = self.OO0000O0OO0O0OOO(chr(105) + chr(109) + chr(103) + chr(115) + chr(47) + chr(67) + chr(49) + chr(46) + chr(112) + chr(110) + chr(103))
        self.O0O0O000O0O0O0O0 = self.OO0000O0OO0O0OOO(chr(105) + chr(109) + chr(103) + chr(115) + chr(47) + chr(70) + chr(49) + chr(46) + chr(112) + chr(110) + chr(103))
        self.O0O0O0O0OO0O0OO0 = self.OO0000O0OO0O0OOO(chr(105) + chr(109) + chr(103) + chr(115) + chr(47) + chr(90) + chr(46) + chr(112) + chr(110) + chr(103))
        self.O00OOO0OOOOOOO0O = self.OO0000O0OO0O0OOO(chr(105) + chr(109) + chr(103) + chr(115) + chr(47) + chr(98) + chr(97) + chr(116) + chr(101) + chr(114) + chr(105) + chr(97) + chr(46) + chr(112) + chr(110) + chr(103))
        pygame.init()
        self.O0O000O000O0OOO0 = pygame.display.set_mode((800, 600))
        pygame.display.set_caption(chr(85) + chr(66) + chr(73) + chr(32) + chr(45) + chr(45) + chr(32) + chr(73) + chr(65) + chr(32) + chr(50) + chr(48) + chr(50) + chr(49) + chr(45) + chr(50) + chr(50))
        print(chr(80) + chr(114) + chr(101) + chr(109) + chr(105) + chr(114) + chr(32) + chr(69) + chr(83) + chr(67) + chr(32) + chr(112) + chr(97) + chr(114) + chr(97) + chr(32) + chr(116) + chr(101) + chr(114) + chr(109) + chr(105) + chr(110) + chr(97) + chr(114) + chr(44) + chr(32) + chr(65) + chr(44) + chr(83) + chr(44) + chr(87) + chr(44) + chr(68) + chr(32) + chr(112) + chr(97) + chr(114) + chr(97) + chr(32) + chr(109) + chr(111) + chr(118) + chr(101) + chr(114))

    
    def OOO0O00O00O00OO0(self):
        self.O0O000O000O0OOO0.fill((255, 255, 255))
        for i in range(0, 600, 15):
            self.O0O000O000O0OOO0.blit(self.OOO0000O0O00OO0O, (0, i))
            self.O0O000O000O0OOO0.blit(self.OOO0000O0O00OO0O, (785, i))
        
        for i in range(0, 800, 15):
            self.O0O000O000O0OOO0.blit(self.OOO0000O0O00OO0O, (i, 0))
            self.O0O000O000O0OOO0.blit(self.OOO0000O0O00OO0O, (i, 585))
        
        for i in range(0, 150, 15):
            self.O0O000O000O0OOO0.blit(self.OOO0000O0O00OO0O, (150, i))
            self.O0O000O000O0OOO0.blit(self.OOO0000O0O00OO0O, (300, i))
            self.O0O000O000O0OOO0.blit(self.OOO0000O0O00OO0O, (450, i))
            self.O0O000O000O0OOO0.blit(self.OOO0000O0O00OO0O, (600, i))
        
        for i in range(450, 600, 15):
            self.O0O000O000O0OOO0.blit(self.OOO0000O0O00OO0O, (150, i))
            self.O0O000O000O0OOO0.blit(self.OOO0000O0O00OO0O, (300, i))
            self.O0O000O000O0OOO0.blit(self.OOO0000O0O00OO0O, (450, i))
            self.O0O000O000O0OOO0.blit(self.OOO0000O0O00OO0O, (600, i))
        
        for i in range(150, 300, 15):
            self.O0O000O000O0OOO0.blit(self.OOO0000O0O00OO0O, (i, 300))
        
        for i in range(450, 800, 15):
            self.O0O000O000O0OOO0.blit(self.OOO0000O0O00OO0O, (i, 300))
        
        for i in self.O00O00OO00O0O0OO:
            self.O0O000O000O0OOO0.blit(self.OO0O00OOO00OO0OO, (i[0][0] - 12, i[0][1] - 12))
        
        for i in self.O0000000O0O000OO:
            self.O0O000O000O0OOO0.blit(self.OO00OOOO0OO0OOOO, (i[0][0] - 12, i[0][1] - 12))
        
        for i in self.O00000OO0OO0O000:
            self.O0O000O000O0OOO0.blit(self.O0O0O000O0O0O0O0, (i[0][0] - 12, i[0][1] - 12))
        
        for i in self.OO0OO00OO000OO00:
            self.O0O000O000O0OOO0.blit(self.OOO0OO0O0000O00O, (i[0][0] - 12, i[0][1] - 12))
        
        for i in self.OOOOO0OO00OO0OO0:
            self.O0O000O000O0OOO0.blit(self.O0O0O0O0OO0O0OO0, (i[0][0] - 12, i[0][1] - 12))
        
        for i in self.OO00O0OOO000OOOO:
            self.O0O000O000O0OOO0.blit(self.OO000OO0OO000O0O, (i[0][0] - 12, i[0][1] - 12))
        
        for i in self.OOO00O0O00000OO0:
            self.O0O000O000O0OOO0.blit(self.O00OOO0OOOOOOO0O, i)
        

    
    def O000O000OO0OO0O0(self, fonts, size):
        available = pygame.font.get_fonts()
        choices = map((lambda x: x.lower().replace(' ', '')), fonts)
        for choice in choices:
            if choice in available:
                return pygame.font.SysFont(choice, size)
        
        return pygame.font.Font(None, size)

    
    def O0O000OOOOOO0OO0(self, O0OO000O0O0OO000, size):
        key = str(O0OO000O0O0OO000) + '|' + str(size)
        font = self.O0O00O00OO0000OO.get(key, None)
        if font == None:
            font = self.O000O000OO0OO0O0(self.OOO000OOOO000OOO, size)
            self.O0O00O00OO0000OO[key] = font
        return font

    
    def O0000OO0O0O0000O(self, text, fonts, size, color):
        key = '|'.join(map(str, (fonts, size, color, text)))
        image = self.OO000OO0O000OOO0.get(key, None)
        if image == None:
            font = self.O0O000OOOOOO0OO0(fonts, size)
            image = font.render(text, True, color)
            self.OO000OO0O000OOO0[key] = image
        return image

    
    def OO0000O0OO0O0OOO(self, path):
        image = self.OOOO00O00OO00O0O.get(path)
        if image == None:
            O0OOOOOOO00O0O0O = path.replace('/', os.sep).replace(' ', os.sep)
            image = pygame.image.load(O0OOOOOOO00O0O0O)
            self.OOOO00O00OO00O0O[path] = image
        return image

    
    def OOO0OO0OO000O0O0(self, pos):
        dt = -6
        out = []
        for i in self.O00O00OO00O0O0OO:
            if abs(pos[0] + dt - i[0][0]) + abs(pos[1] + dt - i[0][1]) < 50:
                out.append(chr(97) + chr(100) + chr(117) + chr(108) + chr(116) + chr(111) + chr(95) + i[1])
        for i in self.O0000000O0O000OO:
            if abs(pos[0] + dt - i[0][0]) + abs(pos[1] + dt - i[0][1]) < 50:
                out.append(chr(99) + chr(114) + chr(105) + chr(97) + chr(110) + chr(231) + chr(97) + chr(95) + i[1])
        for i in self.O00000OO0OO0O000:
            if abs(pos[0] + dt - i[0][0]) + abs(pos[1] + dt - i[0][1]) < 50:
                out.append(chr(102) + chr(117) + chr(110) + chr(99) + chr(105) + chr(111) + chr(110) + chr(225) + chr(114) + chr(105) + chr(111) + chr(95) + i[1])
        for i in self.OO0OO00OO000OO00:
            if abs(pos[0] + dt - i[0][0]) + abs(pos[1] + dt - i[0][1]) < 50:
                out.append(chr(99) + chr(97) + chr(105) + chr(120) + chr(97) + chr(95) + i[1])
        for i in self.OOOOO0OO00OO0OO0:
            if abs(pos[0] + dt - i[0][0]) + abs(pos[1] + dt - i[0][1]) < 50:
                out.append(chr(122) + chr(111) + chr(110) + chr(97) + chr(95) + i[1])
        for i in self.OO00O0OOO000OOOO:
            if abs(pos[0] + dt - i[0][0]) + abs(pos[1] + dt - i[0][1]) < 50:
                out.append(chr(99) + chr(97) + chr(114) + chr(114) + chr(105) + chr(110) + chr(104) + chr(111) + chr(95) + i[1])
        for i in self.OOO00O0O00000OO0:
            if abs(pos[0] + dt - i[0]) + abs(pos[1] + dt - i[1]) < 50:
                self.OOOO0OO0OOOOO0O0 = 100
        return out

    
    def O0000OOOO0000000(self):
        done = False
        O00O0OO00000OOO0 = pygame.time.Clock()
        O00OO00OOOO0OO00 = [
            False,
            False,
            False,
            False]
        OO0OO0OO00OO0000 = [
            100,
            100]
        O00O0OO00OOOO00O = ''
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == K_w:
                        O00OO00OOOO0OO00[0] = True
                    elif event.key == K_s:
                        O00OO00OOOO0OO00[1] = True
                    elif event.key == K_a:
                        O00OO00OOOO0OO00[2] = True
                    elif event.key == K_d:
                        O00OO00OOOO0OO00[3] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        O00OO00OOOO0OO00[0] = False
                    elif event.key == pygame.K_s:
                        O00OO00OOOO0OO00[1] = False
                    elif event.key == pygame.K_a:
                        O00OO00OOOO0OO00[2] = False
                    elif event.key == pygame.K_d:
                        O00OO00OOOO0OO00[3] = False
                if event.type == pygame.KEYDOWN:
                    if event.key == K_1:
                        print('1- Qual foi a pen\xc3\xbaltima pessoa do sexo feminino que viste?')
                        agente.resp1()
                        self.OOOO0OO0OOOOO0O0 -= self.OOOO0OO0OOOOO0O0 / 4000
                    elif event.key == K_2:
                        print('2- Em que tipo de zona est\xc3\xa1s agora?')
                        agente.resp2()
                        self.OOOO0OO0OOOOO0O0 -= self.OOOO0OO0OOOOO0O0 / 4123
                    elif event.key == K_3:
                        print('3- Qual o caminho para a papelaria?')
                        agente.resp3()
                        self.OOOO0OO0OOOOO0O0 -= self.OOOO0OO0OOOOO0O0 / 4000
                    elif event.key == K_4:
                        print('4- Qual a dist\xc3\xa2ncia at\xc3\xa9 ao talho?')
                        agente.resp4()
                        self.OOOO0OO0OOOOO0O0 -= self.OOOO0OO0OOOOO0O0 / 4000
                    elif event.key == K_5:
                        print('5- Quanto tempo achas que demoras a ir de onde est\xc3\xa1s at\xc3\xa9 \xc3\xa0 caixa?')
                        agente.resp5()
                        self.OOOO0OO0OOOOO0O0 -= self.OOOO0OO0OOOOO0O0 / 4000
                    elif event.key == K_6:
                        print('6- Quanto tempo achas que falta at\xc3\xa9 ficares com metade da bateria que tens agora?')
                        agente.resp6()
                        self.OOOO0OO0OOOOO0O0 -= self.OOOO0OO0OOOOO0O0 / 3333
                    elif event.key == K_7:
                        print('7- Qual \xc3\xa9 a probabilidade da pr\xc3\xb3xima pessoa a encontrares ser uma crian\xc3\xa7a?')
                        agente.resp7()
                        self.OOOO0OO0OOOOO0O0 -= self.OOOO0OO0OOOOO0O0 / 4123
                    elif event.key == K_8:
                        print('8- Qual \xc3\xa9 a probabilidade de encontrar um adulto numa zona se estiver l\xc3\xa1 uma crian\xc3\xa7a mas n\xc3\xa3o estiver l\xc3\xa1 um carrinho?')
                        agente.resp8()
                        self.OOOO0OO0OOOOO0O0 -= self.OOOO0OO0OOOOO0O0 / 4123
            
            if self.OOOO0OO0OOOOO0O0 > 1:
                if O00OO00OOOO0OO00[0] and self.O0O000O000O0OOO0.get_at((OO0OO0OO00OO0000[0] - 12, OO0OO0OO00OO0000[1] - 17)) == (255, 255, 255, 255) and self.O0O000O000O0OOO0.get_at((OO0OO0OO00OO0000[0], OO0OO0OO00OO0000[1] - 17)) == (255, 255, 255, 255) and self.O0O000O000O0OOO0.get_at((OO0OO0OO00OO0000[0] + 12, OO0OO0OO00OO0000[1] - 17)) == (255, 255, 255, 255):
                    OO0OO0OO00OO0000[1] -= 5
                    self.OOOO0OO0OOOOO0O0 -= self.OOOO0OO0OOOOO0O0 / 4000
                elif O00OO00OOOO0OO00[1] and self.O0O000O000O0OOO0.get_at((OO0OO0OO00OO0000[0] - 12, OO0OO0OO00OO0000[1] + 17)) == (255, 255, 255, 255) and self.O0O000O000O0OOO0.get_at((OO0OO0OO00OO0000[0], OO0OO0OO00OO0000[1] + 17)) == (255, 255, 255, 255) and self.O0O000O000O0OOO0.get_at((OO0OO0OO00OO0000[0] + 12, OO0OO0OO00OO0000[1] + 17)) == (255, 255, 255, 255):
                    OO0OO0OO00OO0000[1] += 5
                    self.OOOO0OO0OOOOO0O0 -= self.OOOO0OO0OOOOO0O0 / 4000
                if O00OO00OOOO0OO00[2] and self.O0O000O000O0OOO0.get_at((OO0OO0OO00OO0000[0] - 17, OO0OO0OO00OO0000[1] - 12)) == (255, 255, 255, 255) and self.O0O000O000O0OOO0.get_at((OO0OO0OO00OO0000[0] - 17, OO0OO0OO00OO0000[1])) == (255, 255, 255, 255) and self.O0O000O000O0OOO0.get_at((OO0OO0OO00OO0000[0] - 17, OO0OO0OO00OO0000[1] + 12)) == (255, 255, 255, 255):
                    OO0OO0OO00OO0000[0] -= 5
                    self.OOOO0OO0OOOOO0O0 -= self.OOOO0OO0OOOOO0O0 / 4000
                elif O00OO00OOOO0OO00[3] and self.O0O000O000O0OOO0.get_at((OO0OO0OO00OO0000[0] + 17, OO0OO0OO00OO0000[1] - 12)) == (255, 255, 255, 255) and self.O0O000O000O0OOO0.get_at((OO0OO0OO00OO0000[0] + 17, OO0OO0OO00OO0000[1])) == (255, 255, 255, 255) and self.O0O000O000O0OOO0.get_at((OO0OO0OO00OO0000[0] + 17, OO0OO0OO00OO0000[1] + 12)) == (255, 255, 255, 255):
                    OO0OO0OO00OO0000[0] += 5
                    self.OOOO0OO0OOOOO0O0 -= self.OOOO0OO0OOOOO0O0 / 4000
            self.OOO0O00O00O00OO0()
            self.O0O000O000O0OOO0.blit(self.O00O0O0O0OO0O00O, [
                OO0OO0OO00OO0000[0] - 12,
                OO0OO0OO00OO0000[1] - 12])
            text = self.O0000OO0O0O0000O(str(OO0OO0OO00OO0000), self.OOO000OOOO000OOO, 14, (0, 0, 0))
            self.O0O000O000O0OOO0.blit(text, (725, 584))
            text = self.O0000OO0O0O0000O(str(int(self.OOOO0OO0OOOOO0O0)), self.OOO000OOOO000OOO, 14, (0, 0, 0))
            self.O0O000O000O0OOO0.blit(text, (700, 584))
            if self.OOOO0OO0OOOOO0O0 > 1:
                self.OOOO0OO0OOOOO0O0 -= 0.03 * math.cos(self.OOOO0OO0OOOOO0O0 / 65)
            else:
                text = self.O0000OO0O0O0000O(chr(70) + chr(105) + chr(113) + chr(117) + chr(101) + chr(105) + chr(32) + chr(115) + chr(101) + chr(109) + chr(32) + chr(98) + chr(97) + chr(116) + chr(101) + chr(114) + chr(105) + chr(97) + chr(33) + chr(33) + chr(32) + chr(84) + chr(101) + chr(109) + chr(111) + chr(115) + chr(32) + chr(113) + chr(117) + chr(101) + chr(32) + chr(116) + chr(101) + chr(114) + chr(109) + chr(105) + chr(110) + chr(97) + chr(114) + chr(58) + chr(32) + chr(112) + chr(114) + chr(101) + chr(109) + chr(105) + chr(114) + chr(32) + chr(69) + chr(83) + chr(67), self.OOO000OOOO000OOO, 14, (0, 0, 0))
                self.O0O000O000O0OOO0.blit(text, (0, 584))
                self.OOOO0OO0OOOOO0O0 = 0
            pygame.display.flip()
            O0OO00O00O00O0O0 = self.OOO0OO0OO000O0O0(OO0OO0OO00OO0000)
            if O0OO00O00O00O0O0 != O00O0OO00OOOO00O and O0OO00O00O00O0O0 != []:
                print(O0OO00O00O00O0O0)
            O00O0OO00OOOO00O = O0OO00O00O00O0O0
            agente.work(OO0OO0OO00OO0000, self.OOOO0OO0OOOOO0O0, O0OO00O00O00O0O0)
            O00O0OO00000OOO0.tick(50)


h = Supermercado()
h.O0000OOOO0000000()
