from dataclasses import dataclass


@dataclass(slots=True)
class Client:
    exec_name: str = ""
    url: str = ""
    info: str = ""


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
custom_clients = [

        # ("exec_name", "url", "info"),

        ]



# priority 2
# Green clients, which certainly have nsm support, but lack proper *.desktop file and/ or lack active development.
# (Black)star clients.
green_clients = [

        ("non-midi-mapper", "http://non.tuxfamily.org", "non-daw midi to osc mapper"),
        ("non-mixer", "http://non.tuxfamily.org", "non-daw mixer"),
        ("non-mixer-noui", "http://non.tuxfamily.org", "non-daw mixer"),
        ("non-sequencer", "http://non.tuxfamily.org/", "midi sequencer"),
        ("non-timeline", "http://non.tuxfamily.org", "non-daw audio recorder"),
        ("nsm-proxy", "http://non.tuxfamily.org", "launch tools with no nsm or gui"),
        ("jackpatch", "https://non.tuxfamily.org", "save jack connections"),
        #("drumkv1_jack", "https://github.com/rncbc/drumkv1", "drumkit sampler"),
        #("samplv1_jack", "https://github.com/rncbc/samplv1", "sampler synthesizer"),
        #("padthv1_jack", "https://github.com/rncbc/padthv1", "additive synthesizer"),
        #("synthv1_jack", "https://github.com/rncbc/synthv1", "substractive synthesizer"),
        #("ardour", "https://ardour.org", "digital audio workstation"),
        #("zynaddsubfx", "https://github.com/zynaddsubfx", "synthesizer"),
        #("synthpod_jack", "https://open-music-kontrollers.ch/lv2", "lv2 plugin container"), # FIXME




        ]


#Client(*tuple)

# NOTE: a dictionary always works, you don't need python 3.10.

# Orange clients, known to have implemented nsm support, we check for *.desktop file entry.
# Check for "carla-rack " in Exec? With a space? And X-NSM-Capable=true
# There is also X-NSM-Exec=carla-rack

# check for X-NSM-Exec and check if it's on the blocking list.
# Add url when it's on the known list.

# set to prevent duplicates

# priority 3

nsm_clients = [

    ("adljack", "https://github.com/jpcima/adljack", "opl3/opn2 synthesizer"),
    ("ams", "http://alsamodular.sourceforge.net", "modular synthesizer"),
    ("amsynth", "http://amsynth.github.io", "analog modelling synthesizer"),
    ("ardour", "https://ardour.org", "digital audio workstation"),
    # ("ardour5", "https://ardour.org", "digital audio workstation"),
    # ("ardour6", "https://ardour.org", "digital audio workstation"),
    # ("ardour7", "https://ardour.org", "digital audio workstation"),
    ("carla-jack-multi", "https://github.com/falkTX/Carla", "plugin host multi"),
    #carla-patchbay https://kx.studio/Clientlications:Carla jack patchbay
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
    #("mixbus", "https://harrisonconsoles.com", "digital audio workstation"),
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
    ("tembro", "https://laborejo.org/tembro/", "virtal instrument samples"),
    ("xtuner", "https://github.com/brummer10/XTuner", "instrument tuner"),
    #(zita-at1, https://github.com/royvegard/zita-at1, autotuner (unofficial)),
    #(zita-rev1, https://github.com/royvegard/zita-rev1, reverb (unofficial)),
    #("zynaddsubfx", "https://github.com/zynaddsubfx", "synthesizer"),

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




