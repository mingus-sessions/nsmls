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
# TODO: check if installed, for all of them.


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



# CONFIG 


# Blocking clients is normally done by just commenting them out, with a '#'. There is also a general default blocked_clients list, but normally you wouldn't edit it.

# Custom entries for custom or unknown clients. Please report if you think they should be known.
custom_clients = [

        #Client("mixbus", "https://harrisonconsoles.com", "digital audio workstation"),
        # ("exec_name", "url", "info"),
        Client("mamba", "https://github.com/brummer10/Mamba", "virtual midi keyboard"),


        ]


# List with clients that do have nsm support with 99% certainty, but don't have a (proper) desktop file and/ or are not maintained actively at the moment. 
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


# List with clients which are known to have NSM support and should have a proper *.desktop file. If not, report it to the developer and add the client to your custom_clients list, after you've
# commented it out in this list in meantime.
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
    Client("fluajho", "https://laborejo.org", "soundfont player"),
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


# Normally you wouldn't edit this list, unless you know what you're doing.
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
        # We block raysession specific tools to keep things simple and clean.
        "ray_control",
        "ray-jack_checker_daemon",
        "ray-pulse2jack",
        "ray-daemon",
        "ray-jack_config_script",
        "raysession",
        "ray_git",
        "ray-proxy",
        "ray-jackpatch",
        # We block Agordejo specific tools to keep things simple and clean.
        "nsm-data",          
        )



xdg_paths = (

        Path("/usr/share/applications"),
        Path("/usr/local/share/applications"),
        Path(Path.home(), ".local/share/applications"),

        )


joinedlist = custom_clients + green_clients


data_list = joinedlist  # FIXME


def get_path(input_list):
    for __, entry in enumerate(input_list):
        path = which(entry.exec_name)
        if path:
            entry.path = path
            entry.installed = True


# xdg stuff was inspire by...
def get_entries(paths, nsm_clients, blocked_client):
    result = []
    known = False
    for __, basePath in enumerate(paths):
        for file in basePath.glob('**/*'):
            if file.is_file() and file.suffix == ".desktop":
                found = xdg.DesktopEntry.DesktopEntry(file).get('X-NSM-Exec')
                if found and not in blocked_clients
                    for __, known_client in enumerate(nsm_clients):
                        if found == known_client.exec_name:
                            known = True
                            known_client.installed = True
                            known_client.desktop_entry = True
                            result.append(known_client)
                            break
                    if not known:
                        comment = xdg.DesktopEntry.DesktopEntry(file).getComment()
                        if not comment:
                            comment = ""
                        unknown_client = Client(exec_name=found, installed=True, known_client=False, comment=comment, desktop_entry=True)
                        result.append(unknown_client)
    return result


programs = get_entries(xdg_paths, nsm_clients, blocked_clients)


get_path(data_list)
get_path(programs)


for __, client in enumerate(data_list):
    if client.installed:
        programs.append(client)


for __, program in enumerate(programs):
    print(f"{program.exec_name}")
    #print(f"{program.url}")
    #if program.info:
    #    print(f"{program.info}")
    #elif program.comment:
    #    print(f"comment {program.comment}")
    #print(f"{program.path}")


