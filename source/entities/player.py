class Player:

    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.direction = "right"

    def handle_input(self, command):
        """รับ Command เข้ามา และดำเนินการตามคำสั่ง"""
        if command is not None:
            command.execute(self)

    def move_left(self):
        self.x -= self.speed
        self.direction = "left"

    def move_right(self):
        self.x += self.speed
        self.direction = "right"

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed

    def jump(self):
        # Placeholder - อนาคตเพิ่ม gravity/jump logic
        self.y -= self.speed * 2

