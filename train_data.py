# Import Library
from facenet_pytorch import MTCNN, InceptionResnetV1
from torchvision import datasets
from torch.utils.data import DataLoader
import torch
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#initializing MTCNN and InceptionResnetV1
mtcnn0 = MTCNN(image_size=240, margin=0, keep_all=False, min_face_size=40) #keep_all = False
mtcnn = MTCNN(image_size=240, margin=0, keep_all=True, min_face_size=40) #keep_all = True
resnet = InceptionResnetV1(pretrained = 'vggface2').eval()

# Read data from folder
dataset = datasets.ImageFolder('data wajah')  # photos folder path
idx_to_class = {i: c for c, i in dataset.class_to_idx.items()}  # accessing names of peoples from folder names

def collate_fn(x):
    return x[0]

loader = DataLoader(dataset, collate_fn=collate_fn)

face_list = []  # List of cropped faces from photos folder
name_list = []  # list of names corrospoing to cropped photos
embedding_list = []  # list of embeding matrix after conversion from cropped faces to embedding matrix using resnet

engine.say("TRAIN DATA IS PROCESS")
engine.runAndWait()
for img, idx in loader:
    face, prob = mtcnn0(img, return_prob=True)
    if face is not None and prob > 0.92:
        emb = resnet(face.unsqueeze(0))
        embedding_list.append(emb.detach())
        name_list.append(idx_to_class[idx])

# save data
data = [embedding_list, name_list]
torch.save(data, 'data.pt')  # saving data.pt file

engine.say("Training is Success!")
engine.runAndWait()