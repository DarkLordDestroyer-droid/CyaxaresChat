from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from language import LanguageManager
from settings import DEFAULT_LANGUAGE, APP_NAME

class CyaxaresChatApp(App):
    def build(self):
        self.title = APP_NAME
        self.lang_mgr = LanguageManager(current_lang=DEFAULT_LANGUAGE)
        
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.scroll_view = ScrollView()
        self.chat_history = Label(
            text=self.lang_mgr.get_text('welcome'),
            size_hint_y=None,
            markup=True
        )
        self.chat_history.bind(texture_size=self.chat_history.setter('size'))
        self.scroll_view.add_widget(self.chat_history)
        
        input_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=5)
        
        self.message_input = TextInput(
            hint_text=self.lang_mgr.get_text('placeholder'),
            multiline=False
        )
        self.message_input.bind(on_text_validate=self.send_message)
        
        send_button = Button(
            text=self.lang_mgr.get_text('send'),
            size_hint_x=None,
            width=100
        )
        send_button.bind(on_press=self.send_message)
        
        input_layout.add_widget(self.message_input)
        input_layout.add_widget(send_button)
        
        main_layout.add_widget(self.scroll_view)
        main_layout.add_widget(input_layout)
        
        return main_layout

    def send_message(self, instance):
        text = self.message_input.text.strip()
        if text:
            you_text = self.lang_mgr.get_text('you')
            self.chat_history.text += f"[b]{you_text}:[/b] {text}\n"
            self.message_input.text = ''
            self.scroll_view.scroll_y = 0

if __name__ == '__main__':
    CyaxaresChatApp().run()
