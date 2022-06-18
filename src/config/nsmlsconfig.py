#!/usr/bin/env python

from dataclasses import dataclass
from pathlib import Path


#@dataclass(slots=True)
@dataclass()
class Client:
    exec_name: str = ""
    url: str = ""
    info: str = ""      
    path: str = ""
    installed: bool = False
    listed: str = ""
    known: bool = False
    desktop_file: bool = False



# USER CONFIG 


# Custom entries for custom or unknown clients. Please report if you think they should be known. This overrides global blocking.
user_clients = [
    
        # Client("example1", "https://github.com/", "my info"),
        # Client("example2", "", ""),
        # Client("example3"),
        Client("fluajho")


        ]


# Blocked clients by the user. NOTE: Syntax is different. We just need the executable name, with quotes and a comma.
user_blocked_clients = (

        # "example",
        # "example1",

         )


# END USER CONFIG




# List with clients which are known to have NSM support and should have a proper *.desktop file. If not, report it to the developer and add the client to your custom_clients list.
# Normally a user shouldn't edit this.

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
    Client("carla-jack-single", "https://github.com/falkTX/Carla", "plugin host single"),
    Client("carla-patchbay", "https://github.com/falkTX/Carla", "patchbay"),
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


# List with clients that do have nsm support with 99% certainty, but don't have a (proper) desktop file and/ or are not maintained actively at the moment. They're added to the list if they're installed. Normally you wouldn't edit this.
nsm_star_clients = [

        Client("non-midi-mapper", "http://non.tuxfamily.org", "non-daw midi to osc mapper"),
        Client("non-mixer", "http://non.tuxfamily.org", "non-daw mixer"),
        Client("non-mixer-noui", "http://non.tuxfamily.org", "non-daw mixer"),
        Client("non-sequencer", "http://non.tuxfamily.org/", "midi sequencer"),
        Client("non-timeline", "http://non.tuxfamily.org", "non-daw audio recorder"),
        Client("nsm-proxy", "http://non.tuxfamily.org", "launch tools with no nsm or gui"),
        Client("jackpatch", "https://non.tuxfamily.org", "save jack connections"),
        Client("zynaddsubfx", "https://github.com/zynaddsubfx", "synthesizer"),  # NOTE dificult one

        ]



# Normally you wouldn't edit this list, unless you know what you're doing.
blocked_clients = (

        "nsmd",
        "non-daw", 
        "carla", 
        "adljack", 
        # We block tools which are designed to use in raysession.
        "ray_control",
        "ray-jack_checker_daemon",
        "ray-pulse2jack",
        "ray-daemon",
        "ray-jack_config_script",
        "raysession",
        "ray_git",
        "ray-proxy",
        "ray-jackpatch",
        # We block tools which are designed to use in Agordejo. 
        "agordejo.bin",
        "agordejo", 
        "nsm-data",          
        )


# Normally you wouldn't edit this list, unless you know what you're doing.
xdg_paths = (

        Path("/usr/share/applications"),
        Path("/usr/local/share/applications"),
        Path(Path.home(), ".local/share/applications"),

        )
