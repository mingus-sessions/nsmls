#!/usr/bin/env python

from dataclasses import dataclass
from shutil import which
from pathlib import Path
import os
import xdg.DesktopEntry #pyxdg  https://www.freedesktop.org/wiki/Software/pyxdg/
#import xdg.IconTheme #pyxdg  https://www.freedesktop.org/wiki/Software/pyxdg/

# NOTE: the default file MUST not have a entry commented out, other then in custom_clients.
# NOTE: xdg specifications only have url for LINK entry it seems": https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html#recognized-keys

# FIXME: should probably be a dictionary
@dataclass(slots=True)
#@dataclass()
class Client:
    exec_name: str = ""
    url: str = "no_url_provided"
    info: str = ""  # desktopEntry.getComment()
    comment: str = ""
    path: str = ""
    installed: bool = False
    nsm_api: str = "?"
    #nsm: bool = False
    desktop_entry: bool = False



'''
 24                         data = {
 23                             "agordejoName" : desktopEntry.getName(),
 22                             "agordejoExec" : agorExec , #to prevent 'carla-rack %u'.  This is w    hat nsm will call.
 21                             "agordejoIconPath" : xdg.IconTheme.getIconPath(desktopEntry.getIcon    ()),
 20                             "agordejoFullPath" : absExecPath, #This is only for information. ns    m calls agordejoExec #  which we can skip.
 19                             "agordejoDescription" : desktopEntry.getComment(),
 18                         }
 17                         result.append(data)
'''

# priority 1
# Custom entries for custom or unknown clients. Please report if you think they should be known.
# If on custom clients, just check if it's installed.
custom_clients = [

        Client("mixbus", "https://harrisonconsoles.com", "digital audio workstation"),
        # ("exec_name", "url", "info"),
        Client("mamba", "https://github.com/brummer10/Mamba", "virtual midi keyboard"),


        ]



green_clients = [

        Client("non-midi-mapper", "http://non.tuxfamily.org", "non-daw midi to osc mapper"),
        Client("non-mixer", "http://non.tuxfamily.org", "non-daw mixer"),
        Client("non-mixer-noui", "http://non.tuxfamily.org", "non-daw mixer"),
        Client("non-sequencer", "http://non.tuxfamily.org/", "midi sequencer"),
        Client("non-timeline", "http://non.tuxfamily.org", "non-daw audio recorder"),
        Client("nsm-proxy", "http://non.tuxfamily.org", "launch tools with no nsm or gui"),
        Client("jackpatch", "https://non.tuxfamily.org", "save jack connections"),
        Client("zynaddsubfx", "https://github.com/zynaddsubfx", "synthesizer"),  # NOTE dificult one

        ]



nsm_clients = [

    Client("adljack", "https://github.com/jpcima/adljack", "opl3/opn2 synthesizer"),
    Client("ams", "http://alsamodular.sourceforge.net", "modular synthesizer"),
    Client("amsynth", "http://amsynth.github.io", "analog modelling synthesizer"),
    Client("ardour", "https://ardour.org", "digital audio workstation"),
    Client("ardour3", "https://ardour.org", "digital audio workstation"),
    Client("ardour4", "https://ardour.org", "digital audio workstation"),
    Client("ardour5", "https://ardour.org", "digital audio workstation"),
    Client("ardour6", "https://ardour.org", "digital audio workstation"),
    Client("ardour7", "https://ardour.org", "digital audio workstation"),
    Client("carla-jack-multi", "https://github.com/falkTX/Carla", "plugin host multi"),
    Client("carla-rack", "https://github.com/falkTX/Carla", "plugin host rack"),
    Client("drumkv1_jack", "https://github.com/rncbc/drumkv1", "drumkit sampler"),
    #Client("fluajho", "https://laborejo.org", "soundfont player"),
    Client("guitarix", "https://github.com/brummer10/guitarix", "virtual guitar amplifier"),
    Client("hydrogen", "https://github.com/hydrogen-music/hydrogen", "drum machine"),
    Client("jack_mixer", "https://rdio.space/jackmixer", "mixer"),
    Client("laborejo", "https://laborejo.org", "music notation midi sequencing"),
    Client("loop192", "https://github.com/jean-emmanuel/loop192", "midi looper"),
    Client("luppp", "http://openavproductions.com/luppp", "live looper"),
    Client("mamba", "https://github.com/brummer10/Mamba", "virtual midi keyboard"),
    Client("mfp", "https://github.com/bgribble/mfp", "visual composing"),
    Client("padthv1_jack", "https://github.com/rncbc/padthv1", "additive synthesizer"),
    Client("patroneo", "https://laborejo.org", "midi sequencer"),
    Client("petri-foo", "http://petri-foo.sourceforge.net", "sampler"),
    Client("qmidiarp", "http://qmidiarp.sourceforge.net", "midi arpeggiator"),
    Client("qtractor", "https://github.com/rncbc/qtractor", "digital audio workstation"),
    Client("qseq66", "https://github.com/ahlstromcj/seq66", "midi sequencer"),
    Client("radium", "http://users.notam02.no/~kjetism/radium", "tracker"),
    Client("radium_compressor", "http://users.notam02.no/~kjetism/radium", "compressor"),
    Client("samplv1_jack", "https://github.com/rncbc/samplv1", "sampler synthesizer"),
    Client("seq192", "https://github.com/jean-emmanuel/seq192", "midi sequencer"),
    Client("shuriken", "https://rock-hopper.github.io/shuriken", "beat slicer"),
    Client("synthpod_jack", "https://open-music-kontrollers.ch/lv2", "lv2 plugin container"), # FIXME
    Client("synthv1_jack", "https://github.com/rncbc/synthv1", "substractive synthesizer"),
    Client("tembro", "https://laborejo.org/tembro/", "virtual instrument samples"),
    Client("xtuner", "https://github.com/brummer10/XTuner", "instrument tuner"),
    Client("zita-at1", "https://github.com/royvegard/zita-at1", "autotuner (fork)"),
    Client("zita-rev1", "https://github.com/royvegard/zita-rev1", "reverb (fork)"),


        ]


xdg_paths = (

        Path("/usr/share/applications"),
        Path("/usr/local/share/applications"),
        #pathlib.Path(pathlib.Path.home(), ".local/share/applications"),

        )


joinedlist = custom_clients + green_clients

#print(f"{joinedlist}")

# Python code to convert into dictionary
  
#data_list = tuple_to_dataclass(joinedlist)
data_list = joinedlist


def get_path(input_list):
    for __, entry in enumerate(input_list):
        path = which(entry.exec_name)
        if path:
            entry.path = path
            entry.installed = True
            entry.nsm_api = "!" 




# os walk? First try without. os.listdir
# if files endswith *.desktop
# if desktopEntry.get("X-NSM-Exec")
# match with list and add url or description accordingly 


# xdg stuff was inspire by...
def get_entries(paths, nsm_clients):
    result = []
    known = False
    for __, basePath in enumerate(paths):
        for f in basePath.glob('**/*'):
            if f.is_file() and f.suffix == ".desktop":
                y = xdg.DesktopEntry.DesktopEntry(f).get('X-NSM-Exec')
                if y:
                    for __, known_client in enumerate(nsm_clients):
                        if y == known_client.exec_name:
                            known = True
                            #path = xdg.DesktopEntry.DesktopEntry(f).getPath()
                            #if not path:
                            #    path = ""
                            #known_client.path = path 
                            known_client.installed = True
                            known_client.nsm_api = "!!"
                            known_client.desktop_entry = True
                            result.append(known_client)
                            break
                    if not known:
                        comment = xdg.DesktopEntry.DesktopEntry(f).getComment()
                        if not comment:
                            comment = ""
                        unknown_client = Client(exec_name=y, installed=True, nsm_api="!!", comment=comment, desktop_entry=True)
                        result.append(unknown_client)
    return result




#entries = tuple(get_entries(xdg_paths))
#get_entries(xdg_paths)
#entries = []
programs = get_entries(xdg_paths, nsm_clients)

get_path(data_list)
get_path(programs)

#programs = programs + data_list

for __, client in enumerate(data_list):
    if client.installed:
        #yield client
        programs.append(client)

'''
for __, xdg_item in enumerate(entries):
    for __, client in enumerate(datat_list):
        if xdg_item = client:
            client.url 

'''


# programs = set(programs) # NOTE use a key exec_name?

for __, program in enumerate(programs):
    print(f"{program.exec_name}")
    print(f"{program.url}")
    if program.info:
        print(f"{program.info}")
    elif program.comment:
        print(f"comment {program.comment}")
    print(f"{program.path}")

#    for __, entry in enumerate(xdg_paths):
        # if ... entry.nsm_api = "!!"
        # installed = True
#        yield desktopEntry.get("X-NSM-Exec")

# https://pyxdg.readthedocs.io/_/downloads/en/latest/pdf/
# Axdg.DesktopEntry.DesktopEntry(filename=None
#findTryExec()
#Looks in the PATH for the executable given in the TryExec field.
#Returns the full path to the executable if it is found, None if not. Raises NoKeyError if TryExec is not
#present.
#New in version 0.26.

#Convenience methods to get the values of specific fields. If the field is missing, these will simply return an
#empty or zero value. There are similar methods for deprecated and KDE specific keys, but these are not
#listed here


"""
# If it's installed, we take it
for __, list_ in enumerate(dataclassses):
    if which(list_.name):
        yield list_


# nsm_clients
# convert to dataclass, now we can compare to the name? to set the url.
for __, entry_tuple in enumerate(new_list):
    yield Client(*entry_tuple)


get desktopentries:
    get X-NSM-Exec
        yield that thing


# compare with our list of dataclasses.name
if they match and not on blocking list_:
    add a url (and change description)


# sort and set
        


# print


#Client(*tuple)

# NOTE: a dictionary always works, you don't need python 3.10.

# Orange clients, known to have implemented nsm support, we check for *.desktop file entry.
# Check for "carla-rack " in Exec? With a space? And X-NSM-Capable=true
# There is also X-NSM-Exec=carla-rack

# check for X-NSM-Exec and check if it's on the blocking list.
# Add url when it's on the known list (and description?).

# set to prevent duplicates

# priority 3

nsm_clients = [

    ("adljack", "https://github.com/jpcima/adljack", "opl3/opn2 synthesizer"),
    ("ams", "http://alsamodular.sourceforge.net", "modular synthesizer"),
    ("amsynth", "http://amsynth.github.io", "analog modelling synthesizer"),
    ("ardour", "https://ardour.org", "digital audio workstation"),
    ("ardour3", "https://ardour.org", "digital audio workstation"),
    ("ardour4", "https://ardour.org", "digital audio workstation"),
    ("ardour5", "https://ardour.org", "digital audio workstation"),
    ("ardour6", "https://ardour.org", "digital audio workstation"),
    ("ardour7", "https://ardour.org", "digital audio workstation"),
    ("carla-jack-multi", "https://github.com/falkTX/Carla", "plugin host multi"),
    ("carla-rack", "https://github.com/falkTX/Carla", "plugin host rack"),
    ("drumkv1_jack", "https://github.com/rncbc/drumkv1", "drumkit sampler"),
    ("fluajho", "https://laborejo.org", "soundfont player"),
    ("guitarix", "https://github.com/brummer10/guitarix", "virtual guitar amplifier"),
    ("hydrogen", "https://github.com/hydrogen-music/hydrogen", "drum machine"),
    ("jack_mixer", "https://rdio.space/jackmixer", "mixer"),
    ("laborejo", "https://laborejo.org", "music notation midi sequencing"),
    ("loop192", "https://github.com/jean-emmanuel/loop192", "midi looper"),
    ("luppp", "http://openavproductions.com/luppp", "live looper"),
    ("mamba", "https://github.com/brummer10/Mamba", "virtual midi keyboard"),
    ("mfp", "https://github.com/bgribble/mfp", "visual composing"),
    ("padthv1_jack", "https://github.com/rncbc/padthv1", "additive synthesizer)",
    ("patroneo", "https://laborejo.org", "midi sequencer"),
    ("petri-foo", "http://petri-foo.sourceforge.net", "sampler"),
    ("qmidiarp", "http://qmidiarp.sourceforge.net", "midi arpeggiator"),
    ("qtractor", "https://github.com/rncbc/qtractor", "digital audio workstation"),
    ("qseq66", "https://github.com/ahlstromcj/seq66", "midi sequencer"),
    ("radium", "http://users.notam02.no/~kjetism/radium", "tracker"),
    ("radium_compressor", "http://users.notam02.no/~kjetism/radium", "compressor"),
    ("samplv1_jack", "https://github.com/rncbc/samplv1", "sampler synthesizer"),
    ("seq192", "https://github.com/jean-emmanuel/seq192", "midi sequencer"),
    ("shuriken", "https://rock-hopper.github.io/shuriken", "beat slicer"),
    ("synthpod_jack", "https://open-music-kontrollers.ch/lv2", "lv2 plugin container"), # FIXME
    ("synthv1_jack", "https://github.com/rncbc/synthv1", "substractive synthesizer"),
    ("tembro", "https://laborejo.org/tembro/", "virtual instrument samples"),
    ("xtuner", "https://github.com/brummer10/XTuner", "instrument tuner"),
    ("zita-at1", "https://github.com/royvegard/zita-at1", "autotuner (fork)"),
    ("zita-rev1", "https://github.com/royvegard/zita-rev1", "reverb (fork)"),


        ]

'''
zynaddsubfx-alsa.desktop
zynaddsubfx-jack.desktop
zynaddsubfx-jack-multi.desktop
zynaddsubfx-oss.desktop
'''

# NOTE: maybe we don't need this. This is only for search all list.
# Normally you wouldn't edit this.
blocked_clients = (

        # "non-midi-mapper", 
        # "non-mixer-noui"
        #carla-patchbay https://kx.studio/Clientlications:Carla jack patchbay

        "nsmd", 
        "non-daw", 
        "carla", 
        "agordejo", 
        "adljack", 
        "agordejo.bin",
        # We block raysession specific tools to keep things simple.
        "ray_control",
        "ray-jack_checker_daemon",
        "ray-pulse2jack",
        "ray-daemon",
        "ray-jack_config_script",
        "raysession",
        "ray_git",
        "ray-proxy",
        "ray-jackpatch",
        # We block Agordejo specific tools to keep things simple.
        "nsm-data",          
        )


'''
self.blackList = set(("nsmd", "non-daw", "carla", "agordejo", "adljack", "agordejo.bin", "non-midi-mapper", "non-mixer-noui")) #only programs that have to do with audio and music. There i    s another general blacklist that speeds up discovery
  1         self.whiteList = set(("thisdoesnotexisttest", "patroneo", "vico", "tembro", "laborejo",
  2                     "fluajho", "carla-rack", "carla-patchbay", "carla-jack-multi", "carla-jack-single",
  3                      "ardour5", "ardour6", "nsm-data", "jackpatch", "nsm-proxy", "ADLplug", "ams",
  4                     "drumkv1_jack", "synthv1_jack", "samplv1_jack", "padthv1_jack",
  5                     "luppp", "non-mixer", "non-timeline", "non-sequencer",
  6                     "OPNplug", "qmidiarp", "qtractor", "zynaddsubfx", "jack_mixer",
  7                     "hydrogen", "mfp", "shuriken", "guitarix", "radium",
  8                     "ray-proxy", "ray-jackpatch", "amsynth", "mamba", "qseq66", "synthpod", "tap192",
  9                     )) #shortcut list and programs not found by buildCache_grepExecutablePaths because they are just shellscripts and do not contain /nsm/server/announce.
 10         self.userWhitelist = () #added dynamically by api.systemProgramsSetWhitelist add to morePrograms. highest priority
 11         self.userBlacklist = () #added dynamically by api.systemProgramsSetBlacklist as blacklist. highest priority
 12         self.programs = [] #main data structure of this file. list of dicts. guaranteed keys: agordejoExec, name, agordejoFullPath. And probably others, like description and version.
 13         self.nsmExecutables = set() #set of executables for fast membership, if a GUI wants to know if they are available. Needs to be build "manually" with self.programs. no auto-property for a
    list. at least we don't want to do the work.
 14         self.unfilteredExecutables = None #in build()
'''
"""



