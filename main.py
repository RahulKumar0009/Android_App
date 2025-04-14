from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from camera4kivy import Preview


class CameraApp(App):
    def build(self):
        self.camera_id = 0  # Start with the back camera (ID 0)

        layout = BoxLayout(orientation='vertical')

        # Preview widget (initialize without setting camera_id directly)
        self.camera = Preview(size_hint=(1, 0.8))
        layout.add_widget(self.camera)

        # Button to capture an image
        capture_button = Button(text='Take Picture', size_hint=(1, 0.1))
        capture_button.bind(on_press=self.capture_image)
        layout.add_widget(capture_button)

        # Button to toggle the camera
        toggle_button = Button(text='Switch Camera', size_hint=(1, 0.1))
        toggle_button.bind(on_press=self.toggle_camera)
        layout.add_widget(toggle_button)

        return layout

    def capture_image(self, instance):
        self.camera.capture_photo()  # Capture an image

    def toggle_camera(self, instance):
        # Switch between front (ID 1) and back (ID 0) cameras
        self.camera_id = "1" if self.camera_id == "0" else "0"  # Convert to string

        self.camera.disconnect_camera()  # Disconnect the current camera
        self.camera.connect_camera(camera_id=self.camera_id)  # Reconnect with the new camera

if __name__ == '__main__':
    CameraApp().run()