import os
import ConfigParser

home = os.path.expanduser('~')

config= ConfigParser.RawConfigParser()
config.optionxform = str
config.read(home + '/.config/QtProject/QtCreator.ini')

try:
    config.add_section('CppCodeStyleSettings')
except ConfigParser.DuplicateSectionError:
    pass
config.set('CppCodeStyleSettings','LegacyTransformed','true')
config.set('CppCodeStyleSettings','CurrentPreferences','@ByteArray(codingstyle)')

try:
    config.add_section('textTabPreferences')
except ConfigParser.DuplicateSectionError:
    pass
config.set('textTabPreferences','AutoSpacesForTabs','false')
config.set('textTabPreferences','IndentSize','2')
config.set('textTabPreferences','PaddingMode','1')
config.set('textTabPreferences','SpacesForTabs','true')
config.set('textTabPreferences','TabSize','2')

with open(home + '/.config/QtProject/QtCreator.ini', 'w') as configfile:
    config.write(configfile)
