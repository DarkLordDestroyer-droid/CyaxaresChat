# settings.py

APP_NAME = "CyaxaresChat"
VERSION = "0.1"

# Desteklenen Lehçe ve Dil Kodları Listesi
SUPPORTED_LANGUAGES = {
    # Kürtçe Lehçeleri
    'ku_kmr': 'Kurdî (Kurmancî)',
    'ku_zza': 'Kurdî (Zazaki / Dimilî)',
    'ku_ckb': 'Kurdî (Soranî)',
    'ku_bad': 'Kurdî (Badînî)',
    'ku_gor': 'Kurdî (Goranî / Hawramî)',
    'ku_sdh': 'Kurdî (Kelhurî / Xwarag / Şêx Bizinî)',
    'ku_lek': 'Kurdî (Lekî)',
    'ku_lur': 'Kurdî (Lurî)',
    # Dünya Dilleri
    'tr': 'Türkçe',
    'en': 'English',
    'de': 'Deutsch',
    'ru': 'Русский'
}

# Varsayılan Dil (Kürtçe - Kurmancî)
DEFAULT_LANGUAGE = "ku_kmr"

# Uygulama Tema Renkleri (RGBA)
PRIMARY_COLOR = [0.15, 0.45, 0.75, 1]
BACKGROUND_COLOR = [0.95, 0.95, 0.95, 1]

# Sunucu Bağlantı Ayarları
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000
