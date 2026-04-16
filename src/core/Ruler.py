from core import ViewGraphicsScene
from core.pixel_scaler import pixel_scaler
from PySide6.QtGui import QPen
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsTextItem


class Ruler:
    def __init__(
        self,
        parent_scene: ViewGraphicsScene,
        parent_item: QGraphicsRectItem,
        # length: float = 500, # auto select length
        # step: int = 50,    # must be 5 * N (N is postive integer)
        # sub_step: int = 10,
        cursor: float = 225.0,
        x: float = 50.0,
        y: float = 300.0
    ):
        # scale length and select step, sub_step
        self.cursor = cursor
        self.steper()
        num_step = int(cursor//self.step) + 1
        self.length = num_step * self.step
        self.length, scale = pixel_scaler(self.length)
        self.cursor *= scale
        self.step *= scale
        self.sub_step *= scale

        self.x = x
        self.y = y

        black_pen = QPen(Qt.black)
        black_pen.setWidth(2)

        scale_line = parent_scene.addLine(
            0 + self.x, 0 + self.y,
            self.length + self.x, 0 + self.y,
            black_pen
        )
        scale_line.setParentItem(parent_item)

        l_step = 10
        l_sub_step = 5

        mark = [None,] * (num_step + 1)
        for i in range(num_step + 1):
            mark[i] = parent_scene.addLine(
                0 + self.step*i + self.x, 0 + self.y,
                0 + self.step*i + self.x, 0 + l_step + self.y,
                black_pen
            )
            mark[i].setParentItem(parent_item)
        
        mark_sub = [None,] * int(num_step*self.step/self.sub_step + 1)
        for i in range(int(num_step*self.step/self.sub_step + 1)):
            mark_sub[i] = parent_scene.addLine(
                0 + self.sub_step*i + self.x, 0 + self.y,
                0 + self.sub_step*i + self.x, 0 + l_sub_step + self.y,
                black_pen
            )
            mark_sub[i].setParentItem(parent_item)

        l_cursor = 20

        cursor_begin = parent_scene.addLine(
            0 + self.x, 0 + self.y,
            0 + self.x, self.y - l_cursor,
            black_pen
        )
        cursor_begin.setParentItem(parent_item)

        cursor_end = parent_scene.addLine(
            self.cursor + self.x, 0 + self.y,
            self.cursor + self.x, self.y - l_cursor,
            black_pen
        )
        cursor_end.setParentItem(parent_item)

        cursor_num = QGraphicsTextItem(f"{cursor}")
        cursor_num.setDefaultTextColor(Qt.black)
        cursor_num.setPos(self.x+5, self.y-25)
        parent_scene.addItem(cursor_num)
        cursor_num.setParentItem(parent_item)

    
    def steper(self):
        if self.cursor > 500:
            self.step = 100
            self.sub_step = 10
        elif 250 < self.cursor <= 500:
            self.step = 50
            self.sub_step = 5
        elif 50 < self.cursor <= 250:
            self.step = 10
            self.sub_step = 1
        else:
            self.step = 5
            self.sub_step = 0.5
        




