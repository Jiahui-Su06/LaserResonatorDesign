from PySide6.QtCore import QSize, Qt, QPointF
from PySide6.QtGui import QPen, QBrush, QPainterPath, QFont, QPainter
from ui_mainwindow import Ui_MainWindow
from core import LaserBeam, ViewGraphicsScene, Ruler, LaserResonator
from PySide6.QtWidgets import (
    QMainWindow,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsItem,
    QGraphicsTextItem,
    QGraphicsPathItem,
)


class LRDWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # set default value
        self.wavelength_DSpinBox.setValue(1.046)
        self.cavity_length_DSpinBox.setValue(450.0)
        self.left_radius_DSpinBox.setValue(1000.0)
        self.right_radius_DSpinBox.setValue(1000.0)
        self.key_step_DSpinBox.setValue(20.0)
        
        self.scene = ViewGraphicsScene(self)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setRenderHint(QPainter.Antialiasing)

        wl = self.wavelength_DSpinBox.value()
        L = self.cavity_length_DSpinBox.value()
        r1 = self.left_radius_DSpinBox.value()
        r2 = self.right_radius_DSpinBox.value()

        self.resonator = LaserResonator(
            parent_scene=self.scene,
            wl=wl, L=L, r1=r1, r2=r2
        )

        # L = self.cavity_length_DSpinBox.value()
        # Ruler(parent_scene=self.scene, parent_item=self.resonator.mirror_left, cursor=L)

        self.wavelength_DSpinBox.valueChanged.connect(self.redraw_scene)
        self.cavity_length_DSpinBox.valueChanged.connect(self.redraw_scene)
        self.left_radius_DSpinBox.valueChanged.connect(self.redraw_scene)
        self.right_radius_DSpinBox.valueChanged.connect(self.redraw_scene)
    
    def zoom_in(self):
        self.graphicsView.scale(2, 2)
        # mirror_left_pos = self.resonator.mirror_left.scenePos()
        # self.resonator.x = mirror_left_pos.x() + self.resonator.thick_mirror
        # self.resonator.y = mirror_left_pos.y() + self.resonator.w_mirror

    def zoom_out(self):
        self.graphicsView.scale(0.5, 0.5)
        # mirror_left_pos = self.resonator.mirror_left.scenePos()
        # self.resonator.x = mirror_left_pos.x() + self.resonator.thick_mirror
        # self.resonator.y = mirror_left_pos.y() + self.resonator.w_mirror

    def redraw_scene(self):
        wl = self.wavelength_DSpinBox.value()
        L = self.cavity_length_DSpinBox.value()
        r1 = self.left_radius_DSpinBox.value()
        r2 = self.right_radius_DSpinBox.value()

        self.resonator.update_params(wl=wl, L=L, r1=r1, r2=r2)
        self.resonator.redraw()