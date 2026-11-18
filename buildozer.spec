[app]

# (str) Title of your application
title = Flask App

# (str) Package name
package.name = flaskapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source where the app lives
source.dir = .

# (list) Source files to include (let it empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (Zorunlu alan)
version = 0.1

# (list) Application requirements
requirements = python3,kivy,flask,requests,ccxt,yfinance,openpyxl,pandas

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET
