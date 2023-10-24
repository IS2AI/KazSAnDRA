# dataset loader
from datasets import load_dataset

# date and time
import datetime as dt

# visualisation
import matplotlib.pyplot as plt
import seaborn as sns

# numpy and pandas
import numpy as np
import pandas as pd

# environmental variables
import os

# performance metrics
from sklearn.metrics import f1_score, classification_report, confusion_matrix, ConfusionMatrixDisplay

# gpu
import torch

# data loading utility
from torch.utils.data import DataLoader        # python iterable over dataset
from torch.utils.data import RandomSampler     # sampling elements randomly
from torch.utils.data import TensorDataset     # dataset wrapping data and target tensors

# modelling: tokenizer, model loader, trainer, early stopping
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer
from transformers import Trainer
from transformers import TrainingArguments
from transformers import EarlyStoppingCallback, IntervalStrategy

# progress bar
from tqdm import tqdm

# importing logging
from transformers.utils import logging
logging.set_verbosity_info()

print(">>> libraries imported")

##############################
########## training ##########
##############################

# specifying date and time
date_and_time = dt.datetime.today().strftime("%Y.%m.%d_%H.%M.%S")
print(">>> date and time specified")

# specifying datasets directory, task, and training set type
dataset_dir = "../dataset"
task = "pc"             # pc or sc
train_set_type = "rus"   # ros, rus, ib
print(">>> dataset directory, task, and training set type specified")
print(f">>> task is {task.upper()}")
print(f">>> train set type is {train_set_type.upper()}")

# importing train, valid, and test sets
if (task == "pc") & (train_set_type == "ib"):
    train_set_name = "01_pc_train_ib.zip"
elif (task == "pc") & (train_set_type == "ros"):
    train_set_name = "02_pc_train_ros.zip"
elif (task == "pc") & (train_set_type == "rus"):
    train_set_name = "03_pc_train_rus.zip"
elif (task == "sc") & (train_set_type == "ib"):
    train_set_name = "06_sc_train_ib.zip"
elif (task == "sc") & (train_set_type == "ros"):
    train_set_name = "07_sc_train_ros.zip"
elif (task == "sc") & (train_set_type == "rus"):
    train_set_name = "08_sc_train_rus.zip"
    
if task == "pc":
    valid_set_name = "04_pc_valid.zip"
    test_set_name = "05_pc_test.zip"
elif task == "sc":
    valid_set_name = "09_sc_valid.zip"
    test_set_name = "10_sc_test.zip"

data_files = {"train": f"{dataset_dir}/{train_set_name}", "validation": f"{dataset_dir}/{valid_set_name}", "test": f"{dataset_dir}/{test_set_name}"}
datasets = load_dataset("csv", data_files = data_files)
print(">>> train, valid, and test sets imported")

# creating list of labels
label_list = set(datasets["train"][:]["label"])

if task == "pc":
    id2label = {0: "NEGATIVE", 1: "POSITIVE"}
    label2id = {"NEGATIVE": 0, "POSITIVE": 1}
else:
    id2label = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}
    label2id = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}
print(">>> list of labels created")

# setting model hyperparameters
model_list = ["bert-base-multilingual-uncased", "xlm-roberta-base", "google/rembert", "facebook/mbart-large-50"]
model_full_name = model_list[0] # bert-base-multilingual-uncased
if "/" in model_full_name:
    model_short_name = model_full_name.split("/")[1]
else:
    model_short_name = model_full_name

batch_size = 16
epochs = 1
learning_rate = 1e-5
seed = 1
warmup_steps = 800
weight_decay = 0.001
print(f">>> {model_short_name} hyperparameters set:\n>>> batch size: {batch_size}\n>>> epochs: {epochs}\n>>> learning rate: {learning_rate}\n>>> seed: {seed}\n>>> warmup steps: {warmup_steps}\n>>> weight decay: {weight_decay}")

# creating output directory
output_dir = f"models/{date_and_time}_{model_short_name}_{task}_{train_set_type}"
os.mkdir("models")
print(">>> output directory created")

# defining performance metrics
average = "macro"

def compute_metrics(pred):
    labels = pred.label_ids
    # obtaining predicted class labels by finding the column index with maximum probability
    preds = pred.predictions.argmax(-1)
    # computing macro (due to label imbalance) f1 score using sklearn's f1_score function
    f1 = f1_score(labels, preds, average = average)
    return {"f1": f1}
print(f">>> {average} f1 chosen as metric")

# loading tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_full_name, use_fast = True)
print(">>> tokenizer loaded")

# creating dataset tokenization function
def tokenize_function(datasets):
    return tokenizer(datasets["text_cleaned"], padding = True, truncation = True)
print(">>> dataset tokenization function created")

# tokenizing train, valid, and test sets
tokenized_datasets = datasets.map(tokenize_function, batched = True, batch_size = None)
print(">>> train, valid, and test sets tokenized")

# loading model, specifying number of labels
model = AutoModelForSequenceClassification.from_pretrained(model_full_name, num_labels = len(label_list), id2label = id2label, label2id = label2id)
print(">>> model loaded")

# setting training arguments
training_args = TrainingArguments(
    output_dir = output_dir,
    num_train_epochs = epochs,
    learning_rate = learning_rate,
    per_device_train_batch_size = batch_size,
    per_device_eval_batch_size = batch_size,
    seed = seed,
    warmup_steps = warmup_steps,
    weight_decay = weight_decay,
    evaluation_strategy = "epoch",
    save_strategy = "epoch",
    disable_tqdm = False,
    push_to_hub = False,
    load_best_model_at_end = True,
    metric_for_best_model = "f1",
    optim = "adamw_torch",
    logging_dir = output_dir,
    logging_strategy = "epoch"
)
print(">>> training arguments set")

# instantiating trainer
trainer = Trainer(
    model = model,
    args = training_args,
    compute_metrics = compute_metrics,
    train_dataset = tokenized_datasets["train"],
    eval_dataset = tokenized_datasets["validation"],
    tokenizer = tokenizer,
    callbacks = [EarlyStoppingCallback(early_stopping_patience = 3)]
)
print(">>> trainer instantiated")

# launching training
trainer.train()
print(">>> trainer launched")

# saving model
trainer.save_model(f"{output_dir}/model")
print(">>> model saved")

##############################
######### evaluating #########
##############################
print(">>> evaluation started")

# checking cuda
torch.cuda.is_available()
print(f">>> cuda is available {torch.cuda.is_available()}")

# assigning device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(">>> device assigned")

# importing valid and test sets
valid = pd.read_csv(f"{dataset_dir}/{valid_set_name}")
test = pd.read_csv(f"{dataset_dir}/{test_set_name}")
print(">>> valid and test sets imported")

# loading model, specifying number of labels
model = AutoModelForSequenceClassification.from_pretrained(f"{output_dir}/model", num_labels = len(label_list)).to(device)
print(">>> model loaded")

# loading tokenizer
tokenizer = AutoTokenizer.from_pretrained(f"{output_dir}/model")
print(">>> tokenizer loaded")

# encoding data
encoded_data_valid = tokenizer.batch_encode_plus(
    valid["text_cleaned"].to_list(),
    add_special_tokens = True,
    return_attention_mask = True,
    truncation = True,
    padding = True,
    return_tensors = "pt"
)

encoded_data_test = tokenizer.batch_encode_plus(
    test["text_cleaned"].to_list(),
    add_special_tokens = True,
    return_attention_mask = True,
    truncation = True,
    padding = True,
    return_tensors = "pt"
)

input_ids_valid = encoded_data_valid["input_ids"]
attention_masks_valid = encoded_data_valid["attention_mask"]
labels_valid = torch.tensor(valid["label"].values)

input_ids_test = encoded_data_test["input_ids"]
attention_masks_test = encoded_data_test["attention_mask"]
labels_test = torch.tensor(test["label"].values)
print(">>> valid and test sets encoded")

# turning sets into tensors datasets
dataset_valid = TensorDataset(input_ids_valid,
                              attention_masks_valid,
                              labels_valid) 

dataset_test = TensorDataset(input_ids_test,
                              attention_masks_test,
                              labels_test)
print(">>> valid and test sets turned into tensors datasets")

# creating data loaders
dataloader_valid = DataLoader(
    dataset_valid,
    sampler = RandomSampler(dataset_valid),
    batch_size = 32
)

dataloader_test = DataLoader(
    dataset_test,
    sampler = RandomSampler(dataset_test),
    batch_size = 32
)
print(">>> data loaders created")


# creating evaluate function
def evaluate(dataloader_valid):

    model.eval()
    
    loss_valid_total = 0
    predictions, true_vals = [], []
    
    for batch in tqdm(dataloader_valid):
        
        batch = tuple(b.to(device) for b in batch)
        
        inputs = {'input_ids':      batch[0],
                  'attention_mask': batch[1],
                  'labels':         batch[2],
                 }

        with torch.no_grad():        
            outputs = model(**inputs)
            
        loss = outputs[0]
        logits = outputs[1]
        loss_valid_total += loss.item()

        logits = logits.detach().cpu().numpy()
        label_ids = inputs['labels'].cpu().numpy()
        predictions.append(logits)
        true_vals.append(label_ids)
    
    loss_valid_avg = loss_valid_total / len(dataloader_valid) 
    
    predictions = np.concatenate(predictions, axis = 0)
    true_vals = np.concatenate(true_vals, axis = 0)
            
    return loss_valid_avg, predictions, true_vals
print(">>> evaluate function created")

data_loaders = [dataloader_valid, dataloader_test]
for count, data_loader in enumerate(data_loaders, start = 1):
    
    # evaluating on sets
    if count == 1:
        current_set = "valid"
    else:
        current_set = "test"
    print(f">>> {current_set} set evaluation launched")
        
    loss, predictions, labels = evaluate(data_loader)
    predictions_flat = np.argmax(predictions, axis = 1).flatten()
    labels_flat = labels.flatten()
    
    # displaying classication precision, recall, f1, support for sets
    if task == "pc":
        report = classification_report(labels_flat, predictions_flat, output_dict = True)
    else:
        report = classification_report(labels_flat, predictions_flat, output_dict = True, target_names = [1, 2, 3, 4, 5])
    
    with open(f"{output_dir}/{current_set}_report.txt", "wt") as file:
        df_string = pd.DataFrame(report).transpose().to_string()
        file.write(df_string)
        print(f">>> classification report for {current_set} set saved")
    
    # displaying confusion matrix for sets
    fig, ax = plt.subplots(dpi = 100)
    cm = confusion_matrix(labels_flat, predictions_flat)
    
    sns.heatmap(cm, fmt = 'd', annot = True, square = True,
            cmap = 'gray_r', vmin = 0, vmax = 0,  # set all to white
            linewidths = 0.7, linecolor = 'k',  # draw black grid lines
            cbar = False)                     # disable colorbar
    
    # re-enable outer spines
    sns.despine(left = False, right = False, top = False, bottom = False)

    ax.set(xlabel = 'Predicted', ylabel = 'Actual')
    ax.xaxis.set_ticks_position('top') 
    ax.tick_params(labelbottom = False, labeltop = True, direction = "in")
    ax.set_title(task.upper(), pad = 20, fontweight = "bold");

    if task == "pc":
        ax.set_xticklabels([0, 1])
        ax.set_yticklabels([0, 1])
    else:
        ax.set_xticklabels([1, 2, 3, 4, 5])
        ax.set_yticklabels([1, 2, 3, 4, 5])
    
    plt.savefig(f"{output_dir}/{current_set}_cm.png")
    print(f">>> confusion matrix figure for {current_set} set saved")
    
    if task == "pc":
        data = {'actual': labels_flat, 'predicted': predictions_flat}
    else:
        actual = list(map(lambda x: id2label[x] if x in id2label else x, labels_flat))
        predicted = list(map(lambda x: id2label[x] if x in id2label else x, predictions_flat))
        data = {'actual': actual, 'predicted': predicted}

    df = pd.DataFrame(data)
    confusion_matrix = pd.crosstab(df['actual'], df['predicted'], rownames = ['Actual'], colnames = ['Predicted'])
    confusion_matrix.to_csv(f"{output_dir}/{current_set}_cm.csv", sep = "\t")
    
    # performance metrics should be re-imported or else DataFrame object is not iterable error appears
    from sklearn.metrics import f1_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
    print(f">>> confusion matrix for {current_set} set saved")