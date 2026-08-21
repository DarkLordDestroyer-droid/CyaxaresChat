[app]

# Application information
title = CyaxaresChat
package.name = cyaxareschat
package.domain = org.test

# Source code location
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Version
version = 0.1

# Application requirements
requirements = python3,kivy==2.3.0

# Orientation & Display
orientation = portrait
fullscreen = 0

# Android specific configurations
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_licenses = True
android.archs = arm64-v8a, armeabi-v7a

# Permissions
android.permissions = INTERNET, NETWORK_STATE

[buildozer]
log_level = 2
warn_on_root = 1
