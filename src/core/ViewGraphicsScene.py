from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtCore import Qt


class ViewGraphicsScene(QGraphicsScene):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    def wheelEvent(self, event):
        if not event.modifiers() & Qt.ControlModifier:
            event.ignore()
            return
        
        num_pixels = event.delta()

        if num_pixels > 0 :
            self.main_window.zoom_in()
        if num_pixels < 0 :
            self.main_window.zoom_out()

        event.accept()
    
    def keyPressEvent(self, event):
        if not self.main_window.resonator.mirror_right:
            super().keyPressEvent(event)
            return
        
        pos = self.main_window.resonator.mirror_right.pos()
        x, y = pos.x(), pos.y()

        self.step = 10 # 10 pixel

        if event.key() == Qt.Key_Left:
            x -= self.step
        elif event.key() == Qt.Key_Right:
            x += self.step
        else:
            super().keyPressEvent(event)
            return

        self.main_window.resonator.mirror_right.setPos(x, y)
