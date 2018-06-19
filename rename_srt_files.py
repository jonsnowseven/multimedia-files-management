import os
import re
import argparse
import sys
import logging


POSSIBLE_LANGUAGES = ['eng', 'por', 'pob']


def get_sparing_languages(lang):
    if lang == 'eng':
        return 'por'
    else:
        return 'eng'


def rename_srt_files(path, lang):
    """Rename srt files in some path for some lang."""
    logger = logging.getLogger(__name__)
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.info("Searching files to rename in '{}'".format(os.path.abspath(path)))
    for filename in os.listdir(path):
        lang_suffix = r"[-\.]" + re.escape(lang)
        current_path = os.path.join(path, filename)
        # logger.debug(current_path)
        # logger.debug(lang_suffix)
        if not os.path.isfile(current_path):
            rename_srt_files(current_path, lang)
        else:
            # logger.debug(re.search(lang_suffix + r".srt$", filename))
            # print(filename)
            if re.search(lang_suffix + r".srt$", filename):
                old_filename = filename
                new_filename = re.sub(lang_suffix, "", filename)
                logger.debug("OLD FILENAME: " + old_filename)
                logger.debug("NEW FILENAME: " + new_filename)
                old_filename_path = os.path.join(path, old_filename)
                new_filename_path = os.path.join(path, new_filename)
                if os.path.exists(new_filename_path):
                    logger.info("Filename {} already exists!".format(new_filename_path))
                    new_filename_without_conflict = new_filename_path.replace(".srt", "") + "-{}.srt".format(get_sparing_languages(lang))
                    logger.debug("New filename without conflict: {} {}".format(new_filename_path, new_filename_without_conflict))
                    os.rename(new_filename_path, new_filename_without_conflict)
                    logger.debug("Current files: {}".format(os.listdir(path)))
                    logger.info("File {} was renamed to {}".format(new_filename_path, new_filename_without_conflict))
                    os.rename(old_filename_path, new_filename_path)
                    logger.info("File {} was renamed to {}".format(old_filename, new_filename))
                else:
                    os.rename(old_filename_path, new_filename_path)
                    logger.info("File {} was renamed to {}".format(old_filename, new_filename))


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description='Rename srt files in some path for some language.')
    arg_parser.add_argument("-p", "--path", type=str, required=True, help="The path where the srt files are to be renamed.", dest='path')
    arg_parser.add_argument("-l", "--lang", type=str, required=True, help="The language of the files to be renamed. E.g.: por", dest='lang')
    all_args = arg_parser.parse_args()
    rename_srt_files(all_args.path, all_args.lang)
