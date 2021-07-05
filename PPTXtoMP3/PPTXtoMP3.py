from pprint import pprint
from pathlib import Path
import zipfile
import shutil
import time
import sys
import os
import re

# My self made module for renaming files for this purpose
import file_renaming

acceptable_formats = ['.pptx', '.ppsx']
# ppt does not work.

# ===== Getting pptx file path from user and evaluating the validity of the path =====
def user_input_path():
    user_input_path.inp = input('*** Enter PowerPoint file path: ')
    if not Path(user_input_path.inp).exists():
        print('!!! Invalid path, try again later !!!')
        user_input_path()
    # time.sleep(2)
    # raise Exception('!!! Invalid path, try again later !!!')
    else:
        return Path(user_input_path.inp)

pptPath = user_input_path()

zipFilePath = str(pptPath.parent / pptPath.stem) + '-zip' + '.zip'
audio_files = str(pptPath.parent / f'{pptPath.stem}_audio_files')
finalFilePath = pptPath.parent / f'{pptPath.stem}_audio_files' / 'ppt' / 'media'
# E:\University\ترم 4\Immunology\5crp1.pptx


# ===== Making the zip file and extracting the audio files =====
def audio_extracter(inp, pptPath):
    
    # ===== Making the zip file
    # zipFilePath = pptx_path[0]+pptx_path[1]+'-zip'+'.zip'
    shutil.copy2(inp, zipFilePath)
    
    # ===== Creating a directory to extract the files to it
    try:
        os.mkdir(audio_files)
    except:
        print(f'!!! Directory {audio_files} could not be created !!!')
        time.sleep(2)
    
    # ===== Extracting audio files to the created file
    with zipfile.ZipFile(zipFilePath, 'r') as zip_file:
        # zip_file.printdir()
        for f in zip_file.namelist():
            # print(re.search(r'(\..+)', f).group(1))
            if re.search(r'(\..+)', f).group(1) in file_renaming.format_tuple:
                zip_file.extract(f, path=audio_files)


# ===== Checking if the final concatinated file is present =====
def result_check():
    if Path(f'{finalFilePath / pptPath.stem}-sound.mp3').exists():
        print('     ********************')
        print(' ******************************')
        print('*** Operation was successful. ***')
        print(' ******************************')
        print('     ********************')
        print()
        print(f'File {pptPath.stem}-sound.mp3 generated at '
            f'{finalFilePath / pptPath.stem}-sound.mp3. Enjoy!', end='\n')
    else:
        print('!!! Could not concatinate audio files into a sigle file !!!')
    time.sleep(2)


def concatinate():
    # ===== Concatinating audio files together
    concat_permission = input('Audio files extracted. Do you want them to get concatinated?(y/n)')
    if concat_permission == 'y':
        if sys.platform.startswith('linux'):
            # TODO change the format of audio files so that sox can handle them
            '''sampleAudioFile = next(f.name for f in os.scandir(finalFilePath))
            # print(sampleAudioFile)
            sampleAudioFileFormat = re.search(r'\.(.*)', sampleAudioFile).group(1)
            if sampleAudioFileFormat == 'm4a':
                os.system('for f in %s/*.m4a; do ffmpeg -i "$f" "${f/%m4a/wav}"; done' % (finalFilePath))'''
            try:
                os.system(f'sox {finalFilePath}/*.* {finalFilePath / pptPath.stem}-sound.mp3')
            except:
                print('!!! Concatination failed !!!')
                time.sleep(1)
                raise Exception('!!! Concatination failed !!!')
        elif sys.platform.startswith('win32'):
            # TODO concatinating audio files in windows.
            pass
    elif concat_permission == 'n':
        print('!!! Concatination will not be preceded !!!')
    else:
        print('Not a valid option. Try again.')
        concatinate()

def MAIN():
    if pptPath.suffix in acceptable_formats:
        audio_extracter(user_input_path.inp, pptPath)

        # ===== Moving the zip file next to audio files
        # zipFilePath = str(pptPath.parent / pptPath.stem) + '-zip' + '.zip'
        try:
            shutil.move(zipFilePath, pptPath.parent / f'{pptPath.stem}_audio_files')
        except:
            print('Destination zip file already exist.')
            # TODO delete the new zip file if the file already exists in the destination

        # ===== Renaming the extracted audio files to get ready for merging them to gether
        # Calling "file_renaming" module
        try:
            file_renaming.body(finalFilePath)
        except FileExistsError:
            print('!!! Audio files already exist !!!')
            time.sleep(2)
    
        concatinate()
    
        result_check()

    else:
        print('Your file should be a PowerPoint file.' 
              f'Current file extension is <{pptPath.suffix}>. Try again next time.')
        time.sleep(2)
        raise Exception('Your file should be a PowerPoint file.' 
              f'Current file extension is <{pptPath.suffix}>. Try again next time.')



if __name__ == '__main__':
    MAIN()