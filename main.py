from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class CyaxaresChatApp(App):
    def build(self):
        self.title = 'CyaxaresChat'
        
        # Ana Düzen (Dikey)
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Mesajların Görüneceği Alan (Kaydırılabilir)
        self.scroll_view = ScrollView()
        self.chat_history = Label(
            text="[System] CyaxaresChat'e Hoş Geldiniz!\n",
            size_hint_y=None,
            markup=True
        )
        self.chat_history.bind(texture_size=self.chat_history.setter('size'))
        self.scroll_view.add_widget(self.chat_history)
        
        # Alt Kısım: Girdi Kutusu ve Gönder Butonu (Yatay)
        input_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=5)
        
        self.message_input = TextInput(
            hint_text='Mesajınızı yazın...',
            multiline=False
        )
        self.message_input.bind(on_text_validate=self.send_message)
        
        send_button = Button(
            text='Gönder',
            size_hint_x=None,
            width=100
        )
        send_button.bind(on_press=self.send_message)
        
        input_layout.add_widget(self.message_input)
        input_layout.add_widget(send_button)
        
        # Bileşenleri Ana Düzene Ekleme
        main_layout.add_widget(self.scroll_view)
        main_layout.add_widget(input_layout)
        
        return main_layout

    def send_message(self, instance):
        text = self.message_input.text.strip()
        if text:
            self.chat_history.text += f"[b]Siz:[/b] {text}\n"
            self.message_input.text = ''
            # En son mesaja otomatik kaydır
            self.scroll_view.scroll_y = 0

if __name__ == '__main__':
    CyaxaresChatApp().run()
