import os
import ConfigParser

home = os.path.expanduser('~')

config= ConfigParser.RawConfigParser()
config.optionxform = str
config.read(home + '/.config/QtProject/QtCreator.ini')
try:
    config.add_section('CppCodeStyleSettings')
    config.set('CppCodeStyleSettings','LegacyTransformed','true')
except ConfigParser.DuplicateSectionError:
    pass

config.set('CppCodeStyleSettings','CurrentPreferences','@ByteArray(codingstyle)')
with open(home + '/.config/QtProject/QtCreator.ini', 'w') as configfile:
    config.write(configfile)
