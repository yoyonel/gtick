# First Step

Pour avoir le support du fichier son pour les ticks
il faut rajouter une option avec configure (`configure.ac`):
```bash
./configure --with-sndfile
```

Variable `SampleFilename` qui semble nous intéresser pour la sauvegarde du soundfile rattaché au métronome.
Dans l'application actuellement c'est un setting lié au métronome 'global' et non au profil du métronome.
Faudrait transvaser l'attribut pour le placer également dans les profils sauvegardés.
- gtkoptions.c
- metro.c (classe principale, on dirait)

Pour les profils, on peut voir (il semblerait) ici:
- profiles.h
- profiles.c

Faut surement mettre à jour la strucutre `profile_t`

créer deux méthodes :
```c
static void profile_[set|get]_sndfile(profile_t* profile, const gchar* s)
```
(par exemple)

Et mettre à jour:
```c
static void selection_changed_cb(metro_t* metro) {...};
static int set_profile(metro_t* metro, const char* option_name, const char* option_value) {...};
static void save_profile(metro_t* metro, GtkTreeIter* iter) {...};
```

# Second Step

On a réussi à mettre en place la modification qu'on souhaitait.

Ce n'est pas encore super stable ... il semblerait avoir des segfault quand on change vite (ou trop vite) les profils avec les samplefile qui changent également

## Liens en vracs à conserver par rapport au dev.

Python - Extract folder path from file path
http://stackoverflow.com/questions/17057544/python-extract-folder-path-from-file-path

Extracting extension from filename in Python
http://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python

How can I list files with their absolute path in linux? [closed]
http://stackoverflow.com/questions/246215/how-can-i-list-files-with-their-absolute-path-in-linux

How to include python script inside a bash script
http://unix.stackexchange.com/questions/184726/how-to-include-python-script-inside-a-bash-script

How to pass variable arguments from bash script to python script
http://stackoverflow.com/questions/3955571/how-to-pass-variable-arguments-from-bash-script-to-python-script

How can I process the results of find in a bash script?
http://stackoverflow.com/questions/2087001/how-can-i-process-the-results-of-find-in-a-bash-script

Pourquoi if __name__ == '__main__' en Python ?
http://sametmax.com/pourquoi-if-__name__-__main__-en-python/

Why is my array gone after exiting loop? [duplicate]
http://stackoverflow.com/questions/13091700/why-is-my-array-gone-after-exiting-loop

Find files filtered by multiple extensions
http://superuser.com/questions/126290/find-files-filtered-by-multiple-extensions

## Scripts: Bash + Python

#### Sources

- `pybash.sh`:

```bash
#!/bin/bash

list_sndfiles=()


# (find `pwd` | grep ".wav") | {
(find `pwd` -regex ".*/.*\.\(wav\|mp3\)") | {
	while read line;
	do
		list_sndfiles+=("$line ##")
	done

	#echo ${list_sndfiles[@]}
	#echo ${#list_sndfiles[@]}

	python script_generate_profile.py ${list_sndfiles[@]}
}
```

- `script_generate_profile.py`:

```python
import os
import sys


def set_var_profile(name, value, prefix, suffix='\n'):
    """
    """
    return prefix + name + ' = ' + str(value) + suffix


def generate_options_profile(list_options, prefix, **kwargs):
    """
    """
    return "".join([
        set_var_profile(
            name_option,
            kwargs.get(name_option_in_kwargs, default_value),
            prefix
        )
        for name_option, name_option_in_kwargs, default_value in list_options
    ]
    )


def generate_profile(indice_profile, **kwargs):
    """
    """
    #
    prefix_profile = "Profile_" + str(indice_profile) + '_'
    #
    list_options = [
        ('Name', 'name', ''),
        ('Speed', 'speed', 100),
        ('Meter', 'meter', 4),
        ('Accents', 'accents', 1),
        ('SampleFilename', 'samplefilename', '')
    ]
    #
    result = generate_options_profile(list_options, prefix_profile, **kwargs)
    return result


def extract_filename(fullpath_filename):
    """
    """
    return os.path.splitext(os.path.basename(fullpath_filename))[0]


def generate_profiles_from_sndfiles(list_sndfiles):
    """
    """
    return [
        generate_profile(
            indice_profile,
            name=extract_filename(snd_filename),
            samplefilename=snd_filename
        )
        for indice_profile, snd_filename in enumerate(list_sndfiles)
    ]


if __name__ == '__main__':
    snd_filenames = sys.argv[1:]
    list_snd_filenames = filter(
        lambda s: len(s),
        " ".join(snd_filenames).split("##")
        )
    # print "\n".join(list_snd_filenames)
    #print " ".join(snd_filenames).split("##")
    #print
    print "\n".join(generate_profiles_from_sndfiles(list_snd_filenames))
```

#### Résultats

- Structure du répertoire contenant les fichiers audios (wav) des métronomes qu'on souhaite transférer dans gtick (via la nouvelle gestion des profiles):

```bash
$ tree -q
.
├── ch
│   └── ch.wav
├── cowbells
│   ├── hiclick.wav
│   └── loclick.wav
├── gtick.profiles
├── Metronome
│   ├── Ping Hi.wav
│   └── Ping Low.wav
├── Metronome(1)
│   ├── Metronome_hi.wav
│   └── Metronome_low.wav
├── metronome High and Low
│   ├── Mtronome H.wav
│   └── Mtronome L.wav
├── metronomes
│   ├── ch.wav
│   ├── Clave.wav
│   ├── Click.wav
│   ├── CLK_BAQ1.wav
│   ├── CLK_BAQ2.wav
│   ├── CLK_LOGIC1.wav
│   ├── CLK_LOGIC2.wav
│   ├── CLK_MARCA.wav
│   ├── Fine.Metronome 1.wav
│   ├── Fine.Metronome 2.wav
│   ├── fx_click.wav
│   ├── fx_clic.wav
│   ├── hiclave hi res.wav
│   ├── hiclave.wav
│   ├── hi_click loud.wav
│   ├── hi_click.wav
│   ├── higherss.wav
│   ├── Kristal.wav
│   ├── loudclick hi res.wav
│   ├── loudclick.wav
│   ├── lowclave hi res.wav
│   ├── lowclave.wav
│   ├── low_click loud.wav
│   ├── low_click.wav
│   ├── Ping-Hi.wav
│   ├── Ping-Low.wav
│   ├── Rim Shot.wav
│   ├── rim.wav
│   ├── samp9 - Metronom1.wav
│   ├── samp9 - Metronom2.wav
│   ├── softclick hi res.wav
│   ├── softclick.wav
│   ├── ss.wav
│   └── Tambourine.wav
├── metronome sounds
│   ├── 1.wav
│   └── 2.wav
├── pybash.sh
├── script_generate_profile.py
├── SeikoSQ50
│   ├── High Seiko SQ50.wav
│   └── Low Seiko SQ50.wav
├── Sticks (wav)
│   ├── 4c#.wav
│   └── 4d.wav
├── tree.txt
├── Urei Click
│   ├── Click-16-44.wav
│   ├── Click-16-48.wav
│   ├── Click-24-44.wav
│   └── Click-24-48.wav
└── zargon_click_1
    └── Click1.wav

11 directories, 58 files
```

- résultat de la génération de profiles par rapport à cette structure de données:

```bash
$ ./pybash.sh
Profile_0_Name = 1
Profile_0_Speed = 100
Profile_0_Meter = 4
Profile_0_Accents = 1
Profile_0_SampleFilename = /home/atty/Music/__TEMPOS__/__METRONOMES__/metronome sounds/1.wav

Profile_1_Name = 2
Profile_1_Speed = 100
Profile_1_Meter = 4
Profile_1_Accents = 1
Profile_1_SampleFilename =  /home/atty/Music/__TEMPOS__/__METRONOMES__/metronome sounds/2.wav

...

Profile_52_Name = Ping Hi
Profile_52_Speed = 100
Profile_52_Meter = 4
Profile_52_Accents = 1
Profile_52_SampleFilename =  /home/atty/Music/__TEMPOS__/__METRONOMES__/Metronome/Ping Hi.wav

Profile_53_Name = Ping Low
Profile_53_Speed = 100
Profile_53_Meter = 4
Profile_53_Accents = 1
Profile_53_SampleFilename =  /home/atty/Music/__TEMPOS__/__METRONOMES__/Metronome/Ping Low.wav
```
