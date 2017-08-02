import os
import re
import argparse
import sys
import logging

def rename_srt_files(path, lang):
    """Rename srt files in some path for some lang."""
    logger = logging.getLogger(__name__)
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.info("Searching files to rename in {}".format(path))
    for filename in os.listdir(path):
        lang_suffix = re.escape(r"-" + lang)
        # logger.debug(filename)
        # logger.debug(re.search(lang_suffix + r".srt$", filename))
        # print(filename)
        if re.search(lang_suffix + r".srt$", filename):
            old_filename = filename
            new_filename = re.sub(lang_suffix, "", filename)
            # logger.debug(old_filename)
            # logger.debug(new_filename)
            os.rename(os.path.join(path, old_filename), os.path.join(path, new_filename))
            logger.info("File {} was renamed to {}".format(old_filename, new_filename))

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description='Rename srt files in some path for some language.')
    arg_parser.add_argument("-p", "--path", type=str, required=True, help="The path where the srt files are to be renamed.", dest='path')
    arg_parser.add_argument("-l", "--lang", type=str, required=True, help="The language of the files to be renamed. E.g.: por", dest='lang')
    all_args = arg_parser.parse_args()
    rename_srt_files(all_args.path, all_args.lang)
