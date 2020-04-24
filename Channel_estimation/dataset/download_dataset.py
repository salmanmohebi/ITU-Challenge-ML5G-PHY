'''
Download dataset for channel estimation challenge
'''
import wget

URL = 'https://nextcloud.lasseufpa.org/s/reANxekeS4dCppD/download'
TRAIN_FILE_NAME = wget.download(URL)

print(f'{TRAIN_FILE_NAME} was downloaded successfully!')

URL = 'https://nextcloud.lasseufpa.org/s/GdXnSpLCHHytPP2/download'
TEST_FILE_NAME = wget.download(URL)

print(f'{TEST_FILE_NAME} was downloaded successfully!')
