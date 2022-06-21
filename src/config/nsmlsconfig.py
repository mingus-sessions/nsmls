#!/usr/bjin/env python

from pathlib import Path
from src.libnsmls.nsmls_dataclass import Client

  
# USER CONFIG 


# Custom (black)star entries for own apps or apps which don't have a good xdg *.desktop file (tell the developer). 
# This overrides entries in the global blocked_clients list.
user_star_clients = [
    
        # Client("app", "description", "https://github.com/"),
        # Client("app", "description"),
        # Client("app"),
        # Client("fluajho")
        Client("ams"),
        Client("zynaddsubfx"),


        ]


# Blocked clients by the user. NOTE: Syntax is different. We just need the executable name, with quotes and a comma.
user_blocked_clients = (

        # "example",
        # "example1",
        "non-sequencer",

         )


# END USER CONFIG




# List with clients which are known to have NSM support and should have a proper *.desktop file. If not, report it to the developer and copy the Client to your user_star_clients list in meantime.
# Normally a user shouldn't edit this (other then copying a entry).

nsm_clients = [
        
        Client("adljack", "opl3/opn2 synthesizer", "https://github.com/jpcima/adljack"),
        Client("ADLplug", "FM Chip Synthesizer", "https://github.com/jpcima/ADLplug"),
        Client("ams", "modular synthesizer", "http://alsamodular.sourceforge.net"),
        Client("amsynth", "analog modelling synthesizer", "http://amsynth.github.io"),
        Client("ardour", "digital audio workstation", "https://ardour.org"),
        Client("ardour3", "digital audio workstation", "https://ardour.org"),
        Client("ardour4", "digital audio workstation", "https://ardour.org"),
        Client("ardour5", "digital audio workstation", "https://ardour.org"),
        Client("ardour6", "digital audio workstation", "https://ardour.org"),
        Client("ardour7", "digital audio workstation", "https://ardour.org"),
        Client("carla-jack-multi", "plugin host multi", "https://github.com/falkTX/Carla"),
        Client("carla-jack-single", "plugin host single", "https://github.com/falkTX/Carla"),
        Client("carla-patchbay", "patchbay", "https://github.com/falkTX/Carla"),
        Client("carla-rack", "plugin host rack", "https://github.com/falkTX/Carla"),
        Client("drumkv1_jack", "drumkit sampler", "https://github.com/rncbc/drumkv1"),
        Client("fluajho", "soundfont player", "https://laborejo.org"),
        Client("guitarix", "virtual guitar amplifier", "https://github.com/brummer10/guitarix"),
        Client("hydrogen", "drum machine", "https://github.com/hydrogen-music/hydrogen"),
        Client("jack_mixer", "mixer", "https://rdio.space/jackmixer"),
        Client("laborejo", "music notation midi sequencing", "https://laborejo.org"),
        Client("loop192", "midi looper", "https://github.com/jean-emmanuel/loop192"),
        Client("luppp", "live looper", "http://openavproductions.com/luppp"),
        Client("mamba", "virtual midi keyboard", "https://github.com/brummer10/Mamba"),
        Client("mixbus", "digital audio workstation", "https://harrisonconsoles.com"),  # FIXME
        Client("mfp", "visual composing", "https://github.com/bgribble/mfp"),
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
        Client("tap192", "midi-controlled virtual sampler", "https://github.com/PlagiatBros/tap192"),
        Client("tembro", "virtual instrument samples", "https://laborejo.org"),
        Client("vico", "midi sequencer (abandoned)", "https://laborejo.org"),
        Client("xtuner", "instrument tuner", "https://github.com/brummer10/XTuner"),
        Client("zita-at1", "autotuner (fork)", "https://github.com/royvegard/zita-at1"),
        Client("zita-rev1", "reverb (fork)", "https://github.com/royvegard/zita-rev1"),
        Client("non-midi-mapper", "non-daw midi to osc mapper", "http://non.tuxfamily.org"),
        Client("non-mixer", "non-daw mixer", "http://non.tuxfamily.org"),
        Client("non-mixer-noui", "non-daw mixer", "http://non.tuxfamily.org"),
        Client("non-sequencer", "midi sequencer", "http://non.tuxfamily.org/"),
        Client("non-timeline", "non-daw audio recorder", "http://non.tuxfamily.org"),
        Client("nsm-proxy", "launch tools with no nsm or gui", "http://non.tuxfamily.org"),
        Client("jackpatch", "save jack connections", "https://non.tuxfamily.org"),
        Client("zynaddsubfx", "synthesizer", "https://github.com/zynaddsubfx"),





        ]


# List with (black)star clients that do have nsm support with 99% certainty, but don't have a (proper) desktop file and/ or are not maintained actively at the moment. They're added to the list if they're installed. This list is short for the reason that in a ideal world, 'all' NSM clients would have a good *.desktop file with a NSM entryt . Normally you wouldn't edit this.
nsm_star_clients = (

        "non-midi-mapper",
        "non-mixer",
        "non-sequencer",
        "non-timeline",
        "nsm-proxy",
        "jackpatch",
        "zynaddsubfx",

        )



# Normally you wouldn't edit this list, unless you know what you're doing.
blocked_clients = (

        "nsmd",
        "non-daw", 
        "carla", 
        # "adljack", 
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




# DEVELOPER NOTE: for BASH a list in the following format would be easier to parse:
# zynaddsubfx https://github.com/zynaddsubfx synthesizer
# with space as delimiter, which is default in BASH.



  
