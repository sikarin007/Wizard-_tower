import pygame
from pathlib import Path

from config import (
    TOWER_POS,
    TOWER_FRAME_WIDTH,
    TOWER_FRAME_HEIGHT,
    TOWER_INIT_FRAMES,
    TOWER_IDLE_FRAMES,
    TOWER_HEALTH,
    TOWER_HEALTH_BAR_LENGTH,
    TOWER_HEALTH_RATIO,
    TOWER_FRAME_DELAY,
)


class Tower(pygame.sprite.Sprite):
    """Tower Sprite Slicing: init (6 frames) → idle (8 frames)
    แต่ละเฟรมมีขนาด 64x128 พิกเซล"""

    def __init__(self, x=None, y=None):
        super().__init__()
        self.x = x if x is not None else TOWER_POS[0]
        self.y = y if y is not None else TOWER_POS[1]

        sheet_path = Path(__file__).resolve().parent.parent.parent / "assets" / "game" / "spritetower" / "Tower-Sheet.png"
        self._sheet = pygame.image.load(str(sheet_path)).convert_alpha()

        # Slice init: row 0, 6 frames (64x128 px each) - โปร่งใส เพื่อไม่ bleed จากเฟรมอื่น
        self._init_frames = [
            self._copy_frame(i * TOWER_FRAME_WIDTH, 0)
            for i in range(TOWER_INIT_FRAMES)
        ]
        # Slice idle: row 1, 8 frames (64x128 px each)
        self._idle_frames = [
            self._copy_frame(i * TOWER_FRAME_WIDTH, TOWER_FRAME_HEIGHT)
            for i in range(TOWER_IDLE_FRAMES)
        ]

        self.state = "init"
        self.frame_index = 0
        self.frame_timer = 0
        self.frame_delay = TOWER_FRAME_DELAY

        self.image = self._init_frames[0]
        # ใช้ center anchor + คง rect ตลอด (ไม่แก้ใน update)
        self.rect = pygame.Rect(0, 0, TOWER_FRAME_WIDTH, TOWER_FRAME_HEIGHT)
        self.rect.center = (self.x, self.y)

        self.max_health = TOWER_HEALTH
        self.current_health = TOWER_HEALTH
        self.health_bar_length = TOWER_HEALTH_BAR_LENGTH
        self.health_ratio = TOWER_HEALTH_RATIO

    def _copy_frame(self, x: int, y: int):
        """ตัดเฟรมและจัดให้จุดศูนย์กลาง tower ตรงกันทุกเฟรม (ป้องกันการเลื่อน)"""
        raw = pygame.Surface((TOWER_FRAME_WIDTH, TOWER_FRAME_HEIGHT), pygame.SRCALPHA)
        raw.blit(self._sheet, (0, 0), (x, y, TOWER_FRAME_WIDTH, TOWER_FRAME_HEIGHT))
        try:
            rects = pygame.mask.from_surface(raw).get_bounding_rects()
            if rects:
                bounds = rects[0].copy()
                for r in rects[1:]:
                    bounds.union_ip(r)
                # จัดให้ center ของ tower อยู่ที่ (32, 64) เหมือนกันทุกเฟรม
                target_cx = TOWER_FRAME_WIDTH // 2
                target_cy = TOWER_FRAME_HEIGHT // 2
                offset_x = target_cx - bounds.centerx
                offset_y = target_cy - bounds.centery
                out = pygame.Surface((TOWER_FRAME_WIDTH, TOWER_FRAME_HEIGHT), pygame.SRCALPHA)
                out.blit(raw, (offset_x, offset_y))
                return out
        except Exception:
            pass
        return raw

    def update(self):
        self.frame_timer += 1
        if self.frame_timer < self.frame_delay:
            return
        self.frame_timer = 0

        if self.state == "init":
            self.frame_index += 1
            if self.frame_index >= TOWER_INIT_FRAMES:
                self.frame_index = 0
                self.state = "idle"
        elif self.state == "idle":
            self.frame_index = (self.frame_index + 1) % TOWER_IDLE_FRAMES

        if self.state == "init":
            self.image = self._init_frames[self.frame_index]
        else:
            self.image = self._idle_frames[self.frame_index]
        # ไม่แก้ rect - คงที่ตั้งแต่ __init__ ป้องกันการเลื่อน

    def draw_health_bar(self, screen):
        if self.current_health <= 0:
            return
        bar_width = self.current_health / self.health_ratio
        health_bar_rect = pygame.Rect(self.rect.left, self.rect.top - 15, bar_width, 8)
        transition_bar_rect = pygame.Rect(self.rect.left, self.rect.top - 15, self.health_bar_length, 8)
        pygame.draw.rect(screen, (60, 60, 60), transition_bar_rect)
        pygame.draw.rect(screen, (0, 255, 0), health_bar_rect)
