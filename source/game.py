import pygame
from pathlib import Path
from config import screen_width, screen_height, FPS
from source.entities.tower import Tower


try:
    from pytmx.util_pygame import load_pygame
    HAS_PYTMX = True
except ImportError:
    HAS_PYTMX = False

from source.systems.control import KeyboardInputProvider, IInputProvider
from source.entities.player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.tmx_map = None
        self.tower = Tower()  # ตรงกลางแมพ (TOWER_POS)
        self.all_sprites = pygame.sprite.Group(self.tower)
        

        if HAS_PYTMX:
            map_path = Path(__file__).resolve().parent.parent / "assets" / "map" / "map01.tmx"
            try:
                self.tmx_map = load_pygame(str(map_path))
            except Exception as e:
                print(f"Could not load map: {e}")

    def _draw_map(self):
        """วาด TMX map เป็น background"""
        if self.tmx_map is None:
            self.screen.fill((30, 30, 50))
            return
        for layer_idx in self.tmx_map.visible_tile_layers:
            layer = self.tmx_map.layers[layer_idx]
            for x, y, gid in layer.iter_data():
                if gid:
                    tile = self.tmx_map.get_tile_image_by_gid(gid)
                    if tile:
                        self.screen.blit(
                            tile,
                            (x * self.tmx_map.tilewidth, y * self.tmx_map.tileheight),
                        )

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill((0, 0, 0))
            self._draw_map()
            self.tower.update()
            self.all_sprites.draw(self.screen)
            self.tower.draw_health_bar(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)








