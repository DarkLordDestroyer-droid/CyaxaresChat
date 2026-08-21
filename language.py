# language.py

TRANSLATIONS = {
    # --- KÜRTÇE LEHÇELERİ (Temel Dil Grubu) ---
    'ku_kmr': {  # Kurmancî
        'title': 'CyaxaresChat',
        'welcome': '[System] Bi xêr hatî CyaxaresChat\'ê!\n',
        'placeholder': 'Peyama xwe binivîse...',
        'send': 'Rêke',
        'you': 'Tû'
    },
    'ku_zza': {  # Zazaki (Dimilî)
        'title': 'CyaxaresChat',
        'welcome': '[System] Şima xêr amê CyaxaresChat!\n',
        'placeholder': 'Mesafe xo binuse...',
        'send': 'Ruşne',
        'you': 'Ti'
    },
    'ku_ckb': {  # Soranî
        'title': 'CyaxaresChat',
        'welcome': '[System] Be xêr bêt bo CyaxaresChat!\n',
        'placeholder': 'Peyameket binûse...',
        'send': 'Nêrdin',
        'you': 'Tô'
    },
    'ku_bad': {  # Badînî
        'title': 'CyaxaresChat',
        'welcome': '[System] Bi xêr hatî bo CyaxaresChat!\n',
        'placeholder': 'Peyama xwe binivîse...',
        'send': 'Rêke',
        'you': 'Tû'
    },
    'ku_gor': {  # Goranî (Hawramî)
        'title': 'CyaxaresChat',
        'welcome': '[System] Bi xêr amayî fer CyaxaresChat!\n',
        'placeholder': 'Peyama xo binuwîse...',
        'send': 'Kiyar',
        'you': 'To'
    },
    'ku_sdh': {  # Kelhurî / Xwarag / Şêx Bizinî
        'title': 'CyaxaresChat',
        'welcome': '[System] Xoş hatî we CyaxaresChat!\n',
        'placeholder': 'Peyam xwey binoos...',
        'send': 'Rasin',
        'you': 'To'
    },
    'ku_lek': {  # Lekî
        'title': 'CyaxaresChat',
        'welcome': '[System] Xoş hatîn er CyaxaresChat!\n',
        'placeholder': 'Peyama xo binoos...',
        'send': 'Rasnîn',
        'you': 'To'
    },
    'ku_lur': {  # Lurî
        'title': 'CyaxaresChat',
        'welcome': '[System] Xoş amaditî be CyaxaresChat!\n',
        'placeholder': 'Peyama xota bineset...',
        'send': 'Feresdan',
        'you': 'To'
    },

    # --- DÜNYA DİLLERİ ---
    'tr': {  # Türkçe
        'title': 'CyaxaresChat',
        'welcome': '[System] CyaxaresChat\'e Hoş Geldiniz!\n',
        'placeholder': 'Mesajınızı yazın...',
        'send': 'Gönder',
        'you': 'Siz'
    },
    'en': {  # İngilizce
        'title': 'CyaxaresChat',
        'welcome': '[System] Welcome to CyaxaresChat!\n',
        'placeholder': 'Type your message...',
        'send': 'Send',
        'you': 'You'
    },
    'de': {  # Almanca
        'title': 'CyaxaresChat',
        'welcome': '[System] Willkommen bei CyaxaresChat!\n',
        'placeholder': 'Nachricht schreiben...',
        'send': 'Senden',
        'you': 'Du'
    },
    'ru': {  # Rusça
        'title': 'CyaxaresChat',
        'welcome': '[System] Добро пожаловать в CyaxaresChat!\n',
        'placeholder': 'Введите сообщение...',
        'send': 'Отправить',
        'you': 'Вы'
    }
}

class LanguageManager:
    def __init__(self, current_lang='ku_kmr'):
        # Varsayılan dil grubu Kürtçe (Kurmancî)
        self.current_lang = current_lang

    def set_language(self, lang_code):
        if lang_code in TRANSLATIONS:
            self.current_lang = lang_code

    def get_text(self, key):
        return TRANSLATIONS.get(self.current_lang, TRANSLATIONS['ku_kmr']).get(key, key)
