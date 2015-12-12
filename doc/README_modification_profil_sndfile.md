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
