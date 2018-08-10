from distutils.core import setup

import py2exe
import sys
import os

# If run without args, build executables
if len(sys.argv) == 1:
    sys.argv.append("py2exe")

class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        # for the versioninfo resources
        self.version = "1.0.0"
        self.company_name = "ManiSoft"
        self.copyright = "GPL"
        self.name = "Prayer Caller Hex Generator"

manifest_template = '''
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
<assemblyIdentity
    version="5.0.0.0"
    processorArchitecture="x86"
    name="%(prog)s"
    type="win32"
/>
<description>%(prog)s Program</description>
<dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.Windows.Common-Controls"
            version="6.0.0.0"
            processorArchitecture="X86"
            publicKeyToken="6595b64144ccf1df"
            language="*"
        />
    </dependentAssembly>
</dependency>
</assembly>
'''

RT_MANIFEST = 24

excludes = []
includes = []
dll_excludes = ['msvcp90.dll']

options = {
    "excludes": excludes,
    "includes": includes,
    "dll_excludes": dll_excludes
}

setup(
    # The first three parameters are not required, if at least a
    # 'version' is given, then a versioninfo resource is built from
    # them and added to the executables.
    version = "1.0.0",
    description = "Prayer Caller Hex Generator",
    name = "Prayer Caller Hex Generator",

    # targets to build
    windows = [{ 
            "script" : "PrayerEditorApp.py",
            #"icon_resources": [(1, "icon.ico")],
            "other_resources" : [
                (RT_MANIFEST, 1, manifest_template % dict(prog="PrayerVall"))
                ],
            }],
    data_files=[(".", ["./towns.db"])],


 
)
