#!/usr/bin/env python

from pathlib import Path
from libnsmls.nsmls_dataclass import Client

  
# USER CONFIG 


# Custom user entries. This overrides the global blocked_clients list. We need the executable name, with quotes and a comma.
# For a description and url, the entry should be listed in the list nsm_clients. 

user_star_clients = [

        # example1,
        # example2,

        ]


# Blocked clients by the user.

user_blocked_clients = [

        # "example1",
        # "example2",

         ]


# END USER CONFIG


# List with clients which are known to have NSM support. They'll be listed if they have a xdg *.desktop file with a 'X-NSM-Exec' key.
# Normally a user should only add a item to the list, when a custom client in user_star_clients needs a description and a url.

nsm_clients = [
        
        Client("adljack", "opl3/opn2 synthesizer", "https://github.com/jpcima/adljack"),
        Client("ADLplug", "FM Chip Synthesizer", "https://github.com/jpcima/ADLplug"),
        Client("ams", "modular synthesizer", "http://alsamodular.sourceforge.net"),
        Client("amsynth", "analog modelling synthesizer", "http://amsynth.github.io"),
        Client("ardour6", "digital audio workstation", "https://ardour.org"),
        Client("ardour7", "digital audio workstation", "https://ardour.org"),
        Client("carla-jack-multi", "plugin host multi", "https://github.com/falkTX/Carla"),
        Client("carla-jack-single", "plugin host single", "https://github.com/falkTX/Carla"),
        Client("carla-patchbay", "patchbay", "https://github.com/falkTX/Carla"),
        Client("carla-rack", "plugin host rack", "https://github.com/falkTX/Carla"),
        Client("drumkv1_jack", "drumkit sampler", "https://github.com/rncbc/drumkv1"),
        Client("fluajho", "soundfont player", "https://laborejo.org"),
        Client("guitarix", "guitar amplifier", "https://github.com/brummer10/guitarix"),
        Client("hydrogen", "drum machine", "https://github.com/hydrogen-music/hydrogen"),
        Client("jackpatch", "save jack connections", "https://non.tuxfamily.org"),
        Client("jack_mixer", "mixer", "https://rdio.space/jackmixer"),
        Client("laborejo", "music notation midi sequencing", "https://laborejo.org"),
        Client("loop192", "midi looper", "https://github.com/jean-emmanuel/loop192"),
        Client("luppp", "live looper", "http://openavproductions.com/luppp"),
        Client("mamba", "virtual midi keyboard", "https://github.com/brummer10/Mamba"),
        Client("mixbus", "digital audio workstation", "https://harrisonconsoles.com"),  # FIXME
        Client("mfp", "visual composing", "https://github.com/bgribble/mfp"),
        Client("non-midi-mapper", "non-daw midi to osc mapper", "http://non.tuxfamily.org"),
        Client("non-mixer", "non-daw mixer", "http://non.tuxfamily.org"),
        Client("non-mixer-noui", "non-daw mixer", "http://non.tuxfamily.org"),
        Client("non-sequencer", "midi sequencer", "http://non.tuxfamily.org/"),
        Client("non-timeline", "non-daw audio recorder", "http://non.tuxfamily.org"),
        Client("nsm-proxy", "launch tools without nsm or gui", "http://non.tuxfamily.org"),
        Client("padthv1_jack", "additive synthesizer", "https://github.com/rncbc/padthv1"),
        Client("patroneo", "midi sequencer", "https://laborejo.org"),
        Client("petri-foo", "sampler", "http://petri-foo.sourceforge.net"),
        Client("qmidiarp", "midi arpeggiator", "http://qmidiarp.sourceforge.net"),
        Client("qtractor", "digital audio workstation", "https://github.com/rncbc/qtractor"),
        Client("qseq66", "midi sequencer", "https://github.com/ahlstromcj/seq66"),
        Client("radium", "tracker", "http://users.notam02.no/~kjetism/radium"),
        Client("radium_compressor", "compressor", "http://users.notam02.no/~kjetism/radium"),
        Client("samplv1_jack", "sampler synthesizer", "https://github.com/rncbc/samplv1"),
        Client("seq192", "midi sequencer", "https://github.com/jean-emmanuel/seq192"),
        Client("shuriken", "beat slicer", "https://rock-hopper.github.io/shuriken"),
        Client("synthpod_jack", "lv2 plugin container", "https://open-music-kontrollers.ch/lv2"),
        Client("synthv1_jack", "substractive synthesizer", "https://github.com/rncbc/synthv1"),
        Client("tap192", "virtual sampler", "https://github.com/PlagiatBros/tap192"),
        Client("tembro", "virtual instrument samples", "https://laborejo.org"),
        Client("vico", "midi sequencer (obsolete)", "https://laborejo.org"),
        Client("xtuner", "instrument tuner", "https://github.com/brummer10/XTuner"),
        Client("zita-at1", "autotune (nsm patch)", "https://github.com/royvegard/zita-at1"),
        Client("zita-rev1", "reverb (nsm patch)", "https://github.com/royvegard/zita-rev1"),
        Client("zynaddsubfx", "synthesizer", "https://github.com/zynaddsubfx"),

        ]


# List with (black)star clients that do have nsm support with 99% certainty, but don't have a (proper) desktop file and/ or are not maintained actively at the moment. 
# They're added to the list if they're installed. This list should be short. 

nsm_star_clients = [

        "non-midi-mapper",
        "non-mixer",
        "non-sequencer",
        "non-timeline",
        "nsm-proxy",
        "zynaddsubfx",
        "jackpatch",

        ]



# Normally you wouldn't edit this list, unless you know what you're doing.
blocked_clients = [

        # We block tools which are designed to use in Agordejo. 
        "agordejo.bin",
        "agordejo", 
        "nsm-data",          

        # We block tools which are designed to use in RaySession.
        "ray_control",
        "ray-jack_checker_daemon",
        "ray-pulse2jack",
        "ray-daemon",
        "ray-jack_config_script",
        "raysession",
        "ray_git",
        "ray-proxy",
        "ray-jackpatch",

        ]


# Normally you wouldn't edit this list, unless you know what you're doing.
xdg_paths = (

        Path("/usr/share/applications"),
        Path("/usr/local/share/applications"),
        Path(Path.home(), ".local/share/applications"), # $XDG_DATA_HOME/applications/

        )
