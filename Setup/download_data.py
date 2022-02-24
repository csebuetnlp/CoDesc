import os
import gdown 

# go to data folder where we will keep the data
os.chdir('data/')


print('Starting download...')

gdown.download("https://drive.google.com/uc?id=14t7fYsW0a09mfBmFJhjsZv-3obnLnNmS&export=download&confirm=t", "CoDesc.7z", quiet=False)
print("CoDesc.7z downloaded")
os.system("7z x CoDesc.7z")

gdown.download("https://drive.google.com/uc?id=1z1ISkUkNC-ZStMivdU2poXAoh9OjooQw&export=download&confirm=t", "csn_preprocessed_data.7z", quiet=False)
print("csn_preprocessed_data.7z downloaded")
os.system("7z x csn_preprocessed_data.7z")

gdown.download("https://drive.google.com/uc?id=1NKHb_mCH345NXcMFUBw5SxOgki8N5wsO&export=download&confirm=t", "csn_preprocessed_data_balanced_partition.7z", quiet=False)
print("csn_preprocessed_data_balanced_partition.7z downloaded")
os.system("7z x csn_preprocessed_data_balanced_partition.7z")

gdown.download("https://drive.google.com/uc?id=1bjAkUMBTXs42lXjrDycqdVJYSrDkmirB&export=download&confirm=t", "ncs_preprocessed_data.7z", quiet=False) 
print("ncs_preprocessed_data.7z downloaded")
os.system("7z x ncs_preprocessed_data.7z")

gdown.download("https://drive.google.com/uc?id=1cRBRNPQ9eAaSchABoUa5ng_woWR6P3P_&export=download&confirm=t", "original_data.7z", quiet=False) 
print("original_data.7z downloaded")
os.system("7z x original_data.7z")


# go back to previous folder
os.chdir('..')



