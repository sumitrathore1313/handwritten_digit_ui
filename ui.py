from ann import get_model
model = get_model()
from kivy.app import App
# kivy.require("1.8.0")
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.widget import Widget
from kivy.graphics import Line


def predict_number(img):
    data = img.reshape(1, 784).astype('float32')
    number = model.predict(data)
    import numpy as np
    number = np.argmax(number[0])
    return str(number)

class Painter(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y), width=10)

    def on_touch_move(self, touch):
        touch.ud["line"].points += [touch.x, touch.y]


class MainScreen(Screen):
    def generate_number(self):
        number = "unknown"
        import cv2
        import os
        if os.path.exists('number.png'):
            img = cv2.imread('number.png', 0)
            img = img[120:, 160:]
            img = cv2.resize(img, (28, 28))
            number = predict_number(img)
        return number


class AnotherScreen(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("hwdr.kv")


class MainApp(App):
    def build(self):
        return presentation


if __name__ == "__main__":
    MainApp().run()
