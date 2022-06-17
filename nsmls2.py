#!/usr/bin/env python

from dataclasses import dataclass
from shutil import which
from pathlib import Path
import os
import xdg.DesktopEntry #pyxdg  https://www.freedesktop.org/wiki/Software/pyxdg/
#import xdg.IconTheme #pyxdg  https://www.freedesktop.org/wiki/Software/pyxdg/

# NOTE: the default file MUST not have a entry commented out, other then in custom_clients.
# NOTE: xdg specifications only have url for LINK entry it seems": https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html#recognized-keys
# xdg.IconTheme.getIconPath(desktopEntry.getIcon    ()

# TODO: check for multiple items

@dataclass(slots=True)
#@dataclass()
class Client:
    exec_name: str = ""
    url: str = "no_url_provided"
    info: str = ""      
    comment: str = ""  # desktopEntry.getComment()
    path: str = ""
    installed: bool = False
    desktop_entry: bool = False
    known_client: bool = True




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
            # entry.nsm_api = "!" 




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
                            #known_client.nsm_api = "!!"
                            known_client.desktop_entry = True
                            result.append(known_client)
                            break
                    if not known:
                        comment = xdg.DesktopEntry.DesktopEntry(f).getComment()
                        if not comment:
                            comment = ""
                        unknown_client = Client(exec_name=y, installed=True, known_client=False, comment=comment, desktop_entry=True)
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


# programs = set(programs) # NOTE use a key exec_name?

for __, program in enumerate(programs):
    print(f"{program.exec_name}")
    print(f"{program.url}")
    if program.info:
        print(f"{program.info}")
    elif program.comment:
        print(f"comment {program.comment}")
    print(f"{program.path}")


