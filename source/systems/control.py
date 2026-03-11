
from abc import ABC, abstractmethod

import pygame


# ============ Abstraction Layer (High-level) ============

class ICommand(ABC):
    @abstractmethod
    def execute(self, actor) -> None:
        pass


class IInputProvider(ABC):
    @abstractmethod
    def get_command(self) -> ICommand | None:
        pass


# ============ Concrete Commands ============

class MoveLeftCommand(ICommand):
    def execute(self, actor) -> None:
        if hasattr(actor, 'move_left'):
            actor.move_left()


class MoveRightCommand(ICommand):
    def execute(self, actor) -> None:
        if hasattr(actor, 'move_right'):
            actor.move_right()


class MoveUpCommand(ICommand):
    def execute(self, actor) -> None:
        if hasattr(actor, 'move_up'):
            actor.move_up()


class MoveDownCommand(ICommand):
    def execute(self, actor) -> None:
        if hasattr(actor, 'move_down'):
            actor.move_down()


class JumpCommand(ICommand):
    def execute(self, actor) -> None:
        if hasattr(actor, 'jump'):
            actor.jump()


# ============ Low-level: Keyboard Implementation ============

class KeyboardInputProvider(IInputProvider):
    """อ่าน input จาก Keyboard - อนาคตสามารถเพิ่ม JoystickInputProvider ได้"""
    
    def __init__(self):
        self._key_bindings = {
            pygame.K_LEFT: MoveLeftCommand(),
            pygame.K_a: MoveLeftCommand(),
            pygame.K_RIGHT: MoveRightCommand(),
            pygame.K_d: MoveRightCommand(),
            pygame.K_UP: MoveUpCommand(),
            pygame.K_w: MoveUpCommand(),
            pygame.K_DOWN: MoveDownCommand(),
            pygame.K_s: MoveDownCommand(),
            pygame.K_SPACE: JumpCommand(),
        }
    
    def get_command(self) -> ICommand | None:
        """Priority: แป้นแรกที่กดจะถูก return (space > direction > wasd)"""
        keys = pygame.key.get_pressed()
        
        # Space มีความสำคัญสูงสุด
        if keys[pygame.K_SPACE]:
            return JumpCommand()
        
        # Arrow keys / WASD
        for key, command in self._key_bindings.items():
            if key != pygame.K_SPACE and keys[key]:
                return command
        
        return None


# ============ Future: Joystick Implementation (ตัวอย่าง DIP benefit) ============
# สามารถเพิ่มได้โดยไม่แก้ Player เลย
#
# class JoystickInputProvider(IInputProvider):
#     def __init__(self, joystick_id: int = 0):
#         self.joystick = pygame.joystick.Joystick(joystick_id)
#
#     def get_command(self) -> ICommand | None:
#         # Map joystick axis/buttons to same Commands
#         ...
