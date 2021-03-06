import os
import pandas as pd
from torchvision.io import read_image


class DatasetFromSubset():
    def __init__(self, subset, transform=None):
        self.subset = subset
        self.transform = transform

    def __getitem__(self, index):
        image, label = self.subset[index]['image'], self.subset[index]['label']
        if self.transform:
            image = self.transform(image)
        return image, label

    def __len__(self):
        return len(self.subset)


class CustomImageDataset():
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotations_file)
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
        # print(img_path)
        image = read_image(img_path)
        label = self.img_labels.iloc[idx, 1]
        label = int(label)
        sample = {"image": image, "label": label}
        return sample
