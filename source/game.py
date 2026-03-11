import pygame

from source.controller import KeyboardInputProvider, IInputProvider
from source.player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True

        # DIP: ใช้ abstraction - เปลี่ยนเป็น JoystickInputProvider ได้โดยไม่แก้ Player
        self.input_provider: IInputProvider = KeyboardInputProvider()
        self.player = Player(400, 350)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # DIP: Player รับ Command จาก input provider (ไม่รู้ว่าเป็น Keyboard หรือ Joystick)
            command = self.input_provider.get_command()
            self.player.handle_input(command)

            self.screen.fill((0, 0, 0))
            # TODO: draw player at (player.x, player.y)
            pygame.display.flip()
            self.clock.tick(60)





