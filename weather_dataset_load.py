import kagglehub
import os

# Download latest version
path = kagglehub.dataset_download("jehanbhathena/weather-dataset")
# Unpack dataset
dataset_path = os.path.join(path, "dataset")

# Move to repo Data folder
!mv {dataset_path} ../Data
# Rename folder
!mv ../Data/dataset ../Data/Weather_Dataset

# Add/commit/push weather dataset to git in batches

weather_dataset_path = "../Data/Weather_Dataset"
class_directories = os.listdir(weather_dataset_path)
for class_directory in class_directories:
    print(f"Adding class directory: {class_directory}")
    !git add {weather_dataset_path}/{class_directory}
    !git commit -m "Added {class_directory} class directory"
    !git push origin main


