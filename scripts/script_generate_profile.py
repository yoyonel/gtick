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
