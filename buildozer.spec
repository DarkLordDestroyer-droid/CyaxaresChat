[app]

title = CyaxaresChat
package.name = cyaxareschat
package.domain = org.cyaxares
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 0

# Android SDK / NDK Ayarları
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_licenses = True
android.archs = arm64-v8a

# Python-for-android güncel dalı (Cython 3 çakışmasını çözer)
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
