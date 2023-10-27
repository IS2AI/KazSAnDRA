<h1 align="center">😡 KazSAnDRA 😀 </h1>

<p align="center">
  <a href="https://github.com/IS2AI/KazSAnDRA/stargazers">
    <img src="https://img.shields.io/github/stars/IS2AI/KazSAnDRA.svg?colorA=orange&colorB=orange&logo=github"
         alt="GitHub stars">
  </a>
  <a href="https://github.com/IS2AI/KazSAnDRA/issues">
    <img src="https://img.shields.io/github/issues/IS2AI/KazSAnDRA.svg"
         alt="GitHub issues">
  </a>
  <a href="https://issai.nu.edu.kz">
    <img src="https://img.shields.io/static/v1?label=ISSAI&amp;message=official site&amp;color=blue&amp"
         alt="ISSAI Official Website">
  </a> 
</p>

<p align = "center">This repository provides a <a href="https://github.com/IS2AI/KazSAnDRA/tree/main/dataset">dataset</a> and pre-trained polarity and score classification <a href="https://github.com/IS2AI/KazSAnDRA/tree/main/models">scripts</a> for the paper <br><a href = "link_to_be_added"><b>KazSAnDRA: Kazakh Sentiment Analysis Dataset of Reviews and Attitudes</b></a></p> 

## Domains ℹ️

<p align = "justify">The source data for our dataset came from four domains:</p> 

1. an online store for Android devices that offers a diverse range of applications (hereafter Appstore),
2. an online library that serves as a source of books and audiobooks in Kazakh (hereafter Bookstore)
3. digital mapping and navigation services (hereafter Mapping), 
4. online marketplaces (hereafter Market).

<table align="center">
<thead align="center">
  <tr align="center">
    <th>Domain</th>
    <th>⭐️</th>
    <th>⭐️⭐️</th>
    <th>⭐️⭐️⭐️</th>
    <th>⭐️⭐️⭐️⭐️</th>
    <th>⭐️⭐️⭐️⭐️⭐️</th>
    <th>Total</th>
  </tr>
</thead>
<tbody>
  <tr align="center">
    <td>Appstore</td>
    <td>22,547</td>
    <td>4,202</td>
    <td>5,758</td>
    <td>7,949</td>
    <td>94,617</td>
    <td>135,073</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>Bookstore</td>
    <td>686</td>
    <td>107</td>
    <td>222</td>
    <td>368</td>
    <td>4,422</td>
    <td>5,805</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>Mapping</td>
    <td>959</td>
    <td>270</td>
    <td>369</td>
    <td>525</td>
    <td>6,774</td>
    <td>8,897</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>Market</td>
    <td>1,043</td>
    <td>350</td>
    <td>913</td>
    <td>2,775</td>
    <td>25,208</td>
    <td>30,289</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td><b>Total</b></td>
    <td><b>25,235</b></td>
    <td><b>4,929</b></td>
    <td><b>7,262</b></td>
    <td><b>11,617</b></td>
    <td><b>131,021</b></td>
    <td><b>180,064</b></td>
  </tr>
</tbody>
</table>

## Review Variations 🔀

<p align = "justify">In Kazakhstan, people often switch between speaking Kazakh and Russian. There is also a trend of moving from using the <a href="https://en.wikipedia.org/wiki/Cyrillic_script">Cyrillic script</a> to the <a href="https://en.wikipedia.org/wiki/Latin_script">Latin script</a>. As a result, the Kazakh reviews in our dataset can take various forms: (a) purely Kazakh words written in the Kazakh Cyrillic script, (b) Kazakh words in the Latin script, (c) a mix of Cyrillic and Latin characters, (d) a mix of Russian and Kazakh words, or (e) entirely in Cyrillic with Russian characters instead of Kazakh ones.</p>

<table align="center">
  <tr align="center">
    <td></td>
    <td><b>Actual review</b></td>
    <td><b>Correct form</b></td>
    <td><b>English translation</b></td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>a</td>
    <td><i>керемет кітап<i/></td>
    <td><i>керемет кітап<i/></td>
    <td><i>a wonderful book<i/></td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>b</td>
    <td><i>keremet<i/></td>
    <td><i>керемет<i/></td>
    <td><i>wonderful<i/></td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>c</td>
    <td><i>jok кітап<i/></td>
    <td><i>кітап жоқ<i/></td>
    <td><i>no books<i/></td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>d</td>
    <td><i>Осы приложениеге көп рахмет!<i/></td>
    <td><i>Осы қолданбаға көп рақмет!<i/></td>
    <td><i>Many thanks to this app!<i/></td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>e</td>
    <td><i>Кушти!<i/></td>
    <td><i>Күшті!<i/></td>
    <td><i>Great!<i/></td>
  </tr>
</table>

## Sentiment Classification Tasks 🕵️‍♂️

<p align = "justify">We utilised KazSAnDRA for two distinct tasks:</p>

1. polarity classification (PC), involving the prediction of whether a review is positive or negative:
   - reviews with original scores of 1 or 2 were classified as negative and assigned a new score of 0,
   - reviews with original scores of 4 or 5 were classified as positive and assigned a new score of 1,
   - reviews with an original score of 3 were categorized as neutral and were excluded from the task.
2. score classification (SC), where the objective was to predict the score of a review on a scale ranging from 1 to 5.

## Data Preprocessing 🔧

<p align = "justify">During the data preprocessing stage, the following steps were undertaken:</p>

- Removal of emojis 🤓
- Lowercasing all reviews 🔠 ➙ 🔡
- Removal of punctuation marks ⁉️
- Removal of newline (\n), tab (\t), and carriage return (\r) characters ⇥ ↵
- Replacement of multiple spaces with a single space ␣
- Reduction of consecutive recurring characters to two single instances (e.g., "кееррреемееетт" to "кеерреемеетт") 🔂
- Removal of duplicate entries (i.e., reviews sharing identical text and scores) 👯‍♂️

## Data Partitioning 🧩

<p align = "justify">For the sake of maintaining consistency and facilitating reproducibility of our experimental outcomes among different research groups, we partitioned KaZSAnDRA into three distinct sets: training (train), validation (valid), and testing (test) sets, following an 80/10/10 ratio.</p>

<table align="center">
  <tr align="center">
    <td rowspan="3"><b>Task</b></td>
    <td colspan="2"><b>Train</b></td>
    <td colspan="2"><b>Valid</b></td>
    <td colspan="2"><b>Test</b></td>
    <td colspan="2"><b>Total</b></td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td><b>#</b></td>
    <td><b>%</b></td>
    <td><b>#</b></td>
    <td><b>%</b></td>
    <td><b>#</b></td>
    <td><b>%</b></td>
    <td><b>#</b></td>
    <td><b>%</b></td>
  </tr>
   <tr></tr>
  <tr align="center">
    <td>PC</td>
    <td>134,368</td>
    <td>80</td>
    <td>16,796</td>
    <td>10</td>
    <td>16,797</td>
    <td>10</td>
    <td>167,961</td>
    <td>100</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>SC</td>
    <td>140,126</td>
    <td>80</td>
    <td>17,516</td>
    <td>10</td>
    <td>17,516</td>
    <td>10</td>
    <td>175,158</td>
    <td>100</td>
  </tr>
</table>

<p align = "justify">The distribution of reviews across the three sets based on their domains and scores for the PC task:</p>

<table align="center">
<thead>
  <tr align="center">
    <th rowspan="3">Domain</th>
    <th colspan="2">Train</th>
    <th colspan="2">Valid</th>
    <th colspan="2">Test</th>
  </tr>
  <tr></tr>
  <tr align="center">
    <th>#</th>
    <th>%</th>
    <th>#</th>
    <th>%</th>
    <th>#</th>
    <th>%</th>
  </tr>
</thead>
<tbody>
  <tr align="center">
    <td>Appstore</td>
    <td>101,477</td>
    <td>75.52</td>
    <td>12,685</td>
    <td>75.52</td>
    <td>12,685</td>
    <td>75.52</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>Market</td>
    <td>22,561</td>
    <td>16.79</td>
    <td>2,820</td>
    <td>16.79</td>
    <td>2,820</td>
    <td>16.79</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>Mapping</td>
    <td>6,509</td>
    <td>4.84</td>
    <td>813</td>
    <td>4.84</td>
    <td>814</td>
    <td>4.85</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>Bookstore</td>
    <td>3,821</td>
    <td>2.84</td>
    <td>478</td>
    <td>2.85</td>
    <td>478</td>
    <td>2.85</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td><b>Total</b></td>
    <td><b>134,368</b></td>
    <td><b>100</b></td>
    <td><b>16,796</b></td>
    <td><b>100</b></td>
    <td><b>16,797</b></td>
    <td><b>100</b></td>
  </tr>
</tbody>
</table>

<table align="center">
<thead>
  <tr>
    <th rowspan="3">Score</th>
    <th colspan="2">Train</th>
    <th colspan="2">Valid</th>
    <th colspan="2">Test</th>
  </tr>
  <tr></tr>
  <tr align="center">
    <th>#</th>
    <th>%</th>
    <th>#</th>
    <th>%</th>
    <th>#</th>
    <th>%</th>
  </tr>
</thead>
<tbody>
  <tr align="center">
    <td>1</td>
    <td>110,417</td>
    <td>82.18</td>
    <td>13,801</td>
    <td>82.17</td>
    <td>13,804</td>
    <td>82.18</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>0</td>
    <td>23,951</td>
    <td>17.82</td>
    <td>2,995</td>
    <td>17.83</td>
    <td>2,993</td>
    <td>17.82</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td><b>Total</b></td>
    <td><b>134,368</b></td>
    <td><b>100</b></td>
    <td><b>16,796</b></td>
    <td><b>100</b></td>
    <td><b>16,797</b></td>
    <td><b>100</b></td>
  </tr>
</tbody>
</table>

<p align = "justify">The distribution of reviews across the three sets based on their domains and scores for the SC task:</p>

<table align="center">
<thead>
  <tr align="center">
    <th rowspan="3">Domain</th>
    <th colspan="2">Train</th>
    <th colspan="2">Valid</th>
    <th colspan="2">Test</th>
  </tr>
  <tr></tr>
  <tr align="center">
    <th>#</th>
    <th>%</th>
    <th>#</th>
    <th>%</th>
    <th>#</th>
    <th>%</th>
  </tr>
</thead>
<tbody>
  <tr align="center">
    <td>Appstore</td>
    <td>106,058</td>
    <td>75.69</td>
    <td>13,258</td>
    <td>75.69</td>
    <td>13,257</td>
    <td>75.69</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>Market</td>
    <td>23,278</td>
    <td>16.61</td>
    <td>2,909</td>
    <td>16.61</td>
    <td>2,910</td>
    <td>16.61</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>Mapping</td>
    <td>6,794</td>
    <td>4.85</td>
    <td>849</td>
    <td>4.85</td>
    <td>849</td>
    <td>4.85</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>Bookstore</td>
    <td>3,996</td>
    <td>2.85</td>
    <td>500</td>
    <td>2.85</td>
    <td>500</td>
    <td>2.85</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td><b>Total</b></td>
    <td><b>140,126</b></td>
    <td><b>100</b></td>
    <td><b>17,516</b></td>
    <td><b>100</b></td>
    <td><b>17,516</b></td>
    <td><b>100</b></td>
  </tr>
</tbody>
</table>

<table align="center">
<thead>
  <tr>
    <th rowspan="3">Score</th>
    <th colspan="2">Train</th>
    <th colspan="2">Valid</th>
    <th colspan="2">Test</th>
  </tr>
  <tr></tr>
  <tr align="center">
    <th>#</th>
    <th>%</th>
    <th>#</th>
    <th>%</th>
    <th>#</th>
    <th>%</th>
  </tr>
</thead>
<tbody>
  <tr align="center">
    <td>5</td>
    <td>101,302</td>
    <td>72.29</td>
    <td>12,663</td>
    <td>72.29</td>
    <td>12,663</td>
    <td>72.29</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>1</td>
    <td>20,031</td>
    <td>14.29</td>
    <td>2,504</td>
    <td>14.30</td>
    <td>2,504</td>
    <td>14.30</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>4</td>
    <td>9,115</td>
    <td>6.50</td>
    <td>1,140</td>
    <td>6.51</td>
    <td>1,139</td>
    <td>6.50</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>3</td>
    <td>5,758</td>
    <td>4.11</td>
    <td>719</td>
    <td>4.10</td>
    <td>720</td>
    <td>4.11</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>2</td>
    <td>3,920</td>
    <td>2.80</td>
    <td>490</td>
    <td>2.80</td>
    <td>490</td>
    <td>2.80</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td><b>Total</b></td>
    <td><b>140,126</b></td>
    <td><b>100</b></td>
    <td><b>17,516</b></td>
    <td><b>100</b></td>
    <td><b>17,517</b></td>
    <td><b>100</b></td>
  </tr>
</tbody>
</table>

## Score Resampling ♻️

<p align = "justify">To address the data imbalance in our training data, we employed random oversampling (ROS) and random undersampling (RUS) techniques, aiming to balance the representation of classes by creating new samples for the smaller class to align with the count of the majority class and eliminating samples from the larger class to match the count of the minority class.</p>

<p align = "justify">The balanced training sets for the PC task:</p>

<table align = "center">
<thead>
  <tr align = "center">
    <th rowspan="3">Score</th>
    <th colspan="2">Balanced</th>
    <th rowspan="3">Imbalanced</th>
  </tr>
  <tr></tr>
  <tr align = "center">
    <th>OS</th>
    <th>US</th>
  </tr>
</thead>
<tbody>
  <tr align = "center">
    <td>0</td>
    <td>110,417</td>
    <td>23,951</td>
    <td>23,951</td>
  </tr>
   <tr></tr>
  <tr align = "center">
    <td>1</td>
    <td>110,417</td>
    <td>23,951</td>
    <td>110,417</td>
  </tr>
</tbody>
</table>

<p align = "justify">The balanced training sets for the SC task:</p>

<table  align = "center">
<thead>
  <tr>
    <th rowspan="3">Score</th>
    <th colspan="2">Balanced</th>
    <th rowspan="3">Imbalanced</th>
  </tr>
  <tr></tr>
  <tr  align = "center">
    <th>OS</th>
    <th>US</th>
  </tr>
</thead>
<tbody>
  <tr  align = "center">
    <td>1</td>
    <td>101,302</td>
    <td>3,920</td>
    <td>20,031</td>
  </tr>
  <tr></tr>
  <tr  align = "center">
    <td>2</td>
    <td>101,302</td>
    <td>3,920</td>
    <td>3,920</td>
  </tr>
  <tr></tr>
  <tr  align = "center">
    <td>3</td>
    <td>101,302</td>
    <td>3,920</td>
    <td>5,758</td>
  </tr>
  <tr></tr>
  <tr  align = "center">
    <td>4</td>
    <td>101,302</td>
    <td>3,920</td>
    <td>9,115</td>
  </tr>
  <tr></tr>
  <tr  align = "center">
    <td>5</td>
    <td>101,302</td>
    <td>3,920</td>
    <td>101,302</td>
  </tr>
</tbody>
</table>

## Dataset Structure 📁

<p align = "justify">The <a href="https://github.com/IS2AI/KazSAnDRA/tree/main/dataset">dataset</a> folder contains ten ZIP files, each containing a CSV file. Files "01" to "05" are associated with PC (polarity classification), while files "06" to "10" are related to SC (score classification). To align with the enumeration used for labelling in the classifier, which starts from 0 rather than 1, labels 1-5 in the SC task were transformed into 0-4. Different training set variations are indicated by the suffixes "ib" for imbalanced data, "ros" for random oversampling, and "rus" for random undersampling. Each file includes records containing a custom review identifier (<tt>custom_id</tt>), the original review text (<tt>text</tt>), the pre-processed review text (<tt>text_cleaned</tt>), the corresponding review score (<tt>label</tt>), and the domain information (<tt>domain</tt>).

## Sentiment Classification Models 🧠

<p align = "justify">For the evaluation of KazSAnDRA, we utilised four multilingual machine learning models, all incorporating the Kazakh language and accessible through the <a href = "https://huggingface.co/">Hugging Face</a> Transformers framework:</p>

1. <a href = "https://huggingface.co/bert-base-multilingual-uncased">mBERT</a>
2. <a href = "https://huggingface.co/xlm-roberta-base">XLM-R</a>
3. <a href = "https://huggingface.co/google/rembert">RemBERT</a>
4. <a href = "https://huggingface.co/facebook/mbart-large-50">mBART-50</a>

## Experimental Setup 🔬

<p align = "justify">The models were fine-tuned using both the balanced and imbalanced training sets, while the hyperparameters were refined using the validation set. The final and most optimal models were evaluated on the test sets. The fine-tuning of the models was executed on a single A100 GPU hosted on an NVIDIA DGX A100 machine. The initial learning rate was set at 10<sup>-5</sup> the weight decay rate was set at 10<sup>-3</sup>. Early stopping was employed, executed when the F<sub>1</sub>-score exhibited no improvement for three consecutive epochs. We set the batch size to 32 (mBERT, XLM-R, RemBERT) or 16 (mBART-50) and applied 800 warm-up steps.</p>

<table align = "center">
<thead>
  <tr align = "center">
    <th rowspan="3">Model</th>
    <th colspan="3">PC</th>
    <th colspan="3">SC</th>
  </tr>
  <tr></tr>
  <tr align = "center">
    <th>ROS</th>
    <th>RUS</th>
    <th>IB</th>
    <th>ROS</th>
    <th>RUS</th>
    <th>IB</th>
  </tr>
</thead>
<tbody>
  <tr align = "center">
    <td><b>mBERT</b></td>
    <td>4</td>
    <td>7</td>
    <td>6</td>
    <td>8</td>
    <td>10</td>
    <td>11</td>
  </tr>
  <tr></tr>
  <tr align = "center">
    <td><b>XLM-R</b></td>
    <td>5</td>
    <td>7</td>
    <td>5</td>
    <td>4</td>
    <td>9</td>
    <td>16</td>
  </tr>
  <tr></tr>
  <tr align = "center">
    <td><b>RemBERT</b></td>
    <td>4</td>
    <td>5</td>
    <td>5</td>
    <td>6</td>
    <td>6</td>
    <td>9</td>
  </tr>
  <tr></tr>
  <tr align = "center">
    <td><b>mBART-50</b></td>
    <td>5</td>
    <td>7</td>
    <td>5</td>
    <td>8</td>
    <td>7</td>
    <td>5</td>
  </tr>
</tbody>
</table>
<p align = "center">Number of training epochs for models</p>

## Performance Metrics
<p align = "justify">Several conventional metrics were used to evaluate the performance of the models, including accuracy (A), precision (P), recall (R), and F<sub>1</sub>-score (F<sub>1</sub>). 
Given the imbalanced nature of the dataset, where all classes carry equal importance, we opted for macro-averaging, calculated from the arithmetic (i.e., unweighted) mean of all F<sub>1</sub>-scores per class, and thus ensuring equal treatment of all classes during the evaluation, resulting in a stronger penalty if the model performs worse on minority classes.</p>

## Fine-Tuning, Evaluating, and Predicting Models
1. Download this repository and install the required packages:

```bash
git clone https://github.com/IS2AI/KazSAnDRA.git
cd KazSAnDRA/scripts
pip install -r requirements.txt
```

2. To fine-tune and evaluate a model, select the necessary arguments in finetune_evaluate.py and run:
```bash
python finetune_evaluate.py
```

3. To classify a review, select the necessary arguments and add a review in predict.py and run:
```bash
python predict.py
```

## Experiment Results
<table align = "center">
<thead>
  <tr align = "center">
    <th rowspan="5">Model</th>
    <th colspan="12">POLARITY CLASSIFICATION</th>
  </tr>
  <tr></tr>
  <tr align = "center">
    <th colspan="4">Balanced (ROS)</th>
    <th colspan="4">Balanced (RUS)</th>
    <th colspan="4">Imbalanced</th>
  </tr>
  <tr></tr>
  <tr align = "center">
    <th>A</th>
    <th>P</th>
    <th>R</th>
    <th>F1</th>
    <th>A</th>
    <th>P</th>
    <th>R</th>
    <th>F1</th>
    <th>A</th>
    <th>P</th>
    <th>R</th>
    <th>F1</th>
  </tr>
</thead>
<tbody>
  <tr align = "center">
    <td><b>mBERT</b></td>
    <td>0.84</td>
    <td>0.74</td>
    <td>0.83</td>
    <td>0.77</td>
    <td>0.85</td>
    <td>0.76</td>
    <td>0.82</td>
    <td>0.78</td>
    <td>0.89</td>
    <td>0.82</td>
    <td>0.79</td>
    <td>0.80</td>
  </tr>
  <tr></tr>
  <tr align = "center">
    <td><b>XLM-R</b></td>
    <td>0.86</td>
    <td>0.76</td>
    <td>0.83</td>
    <td>0.79</td>
    <td>0.85</td>
    <td>0.75</td>
    <td>0.83</td>
    <td>0.78</td>
    <td><b>0.89</b></td>
    <td><b>0.81</b></td>
    <td><b>0.81</b></td>
    <td><b>0.81</b></td>
  </tr>
  <tr></tr>
  <tr align = "center">
    <td><b>RemBERT</b></td>
    <td>0.88</td>
    <td>0.79</td>
    <td>0.82</td>
    <td>0.81</td>
    <td>0.87</td>
    <td>0.78</td>
    <td>0.82</td>
    <td>0.80</td>
    <td><b>0.89</b></td>
    <td><b>0.81</b></td>
    <td><b>0.82</b></td>
    <td><b>0.81</b></td>
  </tr>
  <tr></tr>
  <tr align = "center">
    <td><b>mBART50</b></td>
    <td>0.87</td>
    <td>0.77</td>
    <td>0.79</td>
    <td>0.78</td>
    <td>0.81</td>
    <td>0.72</td>
    <td>0.81</td>
    <td>0.74</td>
    <td>0.89</td>
    <td>0.82</td>
    <td>0.78</td>
    <td>0.80</td>
  </tr>
</tbody>
</table>
<p align = "center">PC results on the test sets</p>

<table align = "center">
<thead>
  <tr align = "center">
    <th rowspan="5">Model</th>
    <th colspan="12">SCORE CLASSIFICATION</th>
  </tr>
  <tr></tr>
  <tr align = "center">
    <th colspan="4">Balanced (ROS)</th>
    <th colspan="4">Balanced (RUS)</th>
    <th colspan="4">Imbalanced</th>
  </tr>
  <tr></tr>
  <tr align = "center">
    <th>A</th>
    <th>P</th>
    <th>R</th>
    <th>F1</th>
    <th>A</th>
    <th>P</th>
    <th>R</th>
    <th>F1</th>
    <th>A</th>
    <th>P</th>
    <th>R</th>
    <th>F1</th>
  </tr>
</thead>
<tbody>
  <tr align = "center">
    <td><b>mBERT</b></td>
    <td>0.67</td>
    <td>0.34</td>
    <td>0.36</td>
    <td>0.35</td>
    <td>0.63</td>
    <td>0.35</td>
    <td>0.39</td>
    <td>0.36</td>
    <td>0.77</td>
    <td>0.44</td>
    <td>0.36</td>
    <td>0.37</td>
  </tr>
  <tr></tr>
  <tr align = "center">
    <td><b>XLM-R</b></td>
    <td>0.58</td>
    <td>0.36</td>
    <td>0.42</td>
    <td>0.36</td>
    <td>0.66</td>
    <td>0.36</td>
    <td>0.41</td>
    <td>0.37</td>
    <td><b>0.77</b></td>
    <td><b>0.42</b></td>
    <td><b>0.37</b></td>
    <td><b>0.39</b></td>
  </tr>
  <tr></tr>
  <tr align = "center">
    <td><b>RemBERT</b></td>
    <td>0.73</td>
    <td>0.37</td>
    <td>0.36</td>
    <td>0.36</td>
    <td>0.62</td>
    <td>0.35</td>
    <td>0.40</td>
    <td>0.35</td>
    <td><b>0.76</b></td>
    <td><b>0.41</b></td>
    <td><b>0.38</b></td>
    <td><b>0.39</b></td>
  </tr>
  <tr></tr>
  <tr align = "center">
    <td><b>mBART50</b></td>
    <td>0.74</td>
    <td>0.36</td>
    <td>0.34</td>
    <td>0.35</td>
    <td>0.55</td>
    <td>0.36</td>
    <td>0.41</td>
    <td>0.34</td>
    <td>0.77</td>
    <td>0.42</td>
    <td>0.37</td>
    <td>0.38</td>
  </tr>
</tbody>
</table>
<p align = "center">SC results on the test sets</p>

<table align = "center">
<thead>
  <tr align = "center">
    <th colspan="4"><b>POLARITY CLASSIFICATION</b></th>
  </tr>
</thead>
<tbody>
  <tr align = "center">
    <td><b>predicted &#8594;</b><br><b>actual &#8595;</b></td>
    <td><b>0</td>
    <td><b>1</td>
    <td><b>Total</b></td>
  </tr>
  <tr></tr>
  <tr align = "center">
    <td><b>0</b></td>
    <td>2,155</td>
    <td>838</td>
    <td>2,993</td>
  </tr>
  <tr></tr>
  <tr align = "center">
    <td><b>1</b></td>
    <td>1,036</td>
    <td>12,768</td>
    <td>13,804</td>
  </tr>
</tbody>
</table>
<p align = "center">RemBERT PC results</p>

<table align = "center">
<thead>
  <tr align = "center">
    <th colspan="7"><b>SCORE CLASSIFICATION</b></th>
  </tr>
</thead>
<tbody>
  <tr align = "center">
    <td><b>predicted &#8594;</b><br><b>actual &#8595;</b></td>
    <td><b>1</b></td>
    <td><b>2</b></td>
    <td><b>3</b></td>
    <td><b>4</b></td>
    <td><b>5</b></td>
    <td><b>Total</td>
  </tr>
  <tr></tr>
  <tr align = "center">
    <td><b>1</b></td>
    <td>1,379</td>
    <td>145</td>
    <td>132</td>
    <td>64</td>
    <td>784</td>
    <td>2,504</td>
  </tr>
  <tr></tr>
  <tr align = "center">
    <td><b>2</b></td>
    <td>182</td>
    <td>55</td>
    <td>56</td>
    <td>25</td>
    <td>172</td>
    <td>490</td>
  </tr>
  <tr></tr>
  <tr align = "center">
    <td><b>3</b></td>
    <td>173</td>
    <td>54</td>
    <td>118</td>
    <td>65</td>
    <td>310</td>
    <td>720</td>
  </tr>
  <tr></tr>
  <tr align = "center">
    <td><b>4</b></td>
    <td>110</td>
    <td>39</td>
    <td>90</td>
    <td>169</td>
    <td>731</td>
    <td>1,139</td>
  </tr>
  <tr></tr>
  <tr align = "center">
    <td><b>5</b></td>
    <td>564</td>
    <td>59</td>
    <td>165</td>
    <td>297</td>
    <td>11,578</td>
    <td>12,663</td>
  </tr>
</tbody>
</table>
<p align = "center">RemBERT SC results</p>

<table align = "center">
<thead>
  <tr align = "center">
    <th rowspan="3">Domain</th>
    <th colspan="4">PC</th>
  </tr>
  <tr></tr>
  <tr align = "center">
    <th>A</th>
    <th>P</th>
    <th>R</th>
    <th>F1</th>
  </tr>
</thead>
<tbody>
  <tr align = "center">
    <td>Appstore</td>
    <td>0.87</td>
    <td>0.80</td>
    <td>0.81</td>
    <td>0.80</td>
  </tr>
  <tr></tr>
  <tr align = "center">
    <td>Bookstore</td>
    <td>0.86</td>
    <td>0.75</td>
    <td>0.80</td>
    <td>0.77</td>
  </tr>
  <tr></tr>
  <tr align = "center">
    <td>Mapping</td>
    <td>0.92</td>
    <td>0.84</td>
    <td>0.88</td>
    <td>0.86</td>
  </tr>
  <tr></tr>
  <tr align = "center">
    <td>Market</td>
    <td>0.97</td>
    <td>0.84</td>
    <td>0.91</td>
    <td>0.87</td>
  </tr>
</tbody>
</table>
<p align = "center">RemBERT PC results by domain</p>

<table align = "center">
<thead>
  <tr align = "center">
    <th rowspan="3">Domain</th>
    <th colspan="4">SC</th>
  </tr>
  <tr></tr>
  <tr align = "center">
    <th>A</th>
    <th>P</th>
    <th>R</th>
    <th>F1</th>
  </tr>
</thead>
<tbody>
  <tr align = "center">
    <td>Appstore</td>
    <td>0.74</td>
    <td>0.41</td>
    <td>0.37</td>
    <td>0.38</td>
  </tr>
  <tr></tr>
  <tr align = "center">
    <td>Bookstore</td>
    <td>0.73</td>
    <td>0.34</td>
    <td>0.32</td>
    <td>0.32</td>
  </tr>
  <tr></tr>
  <tr align = "center">
    <td>Mapping</td>
    <td>0.80</td>
    <td>0.42</td>
    <td>0.41</td>
    <td>0.41</td>
  </tr>
  <tr></tr>
  <tr align = "center">
    <td>Market</td>
    <td>0.82</td>
    <td>0.43</td>
    <td>0.41</td>
    <td>0.42</td>
  </tr>
</tbody>
</table>
<p align = "center">RemBERT SC results by domain</p>

## Acknowledgements 🙏

<p align = "justify">We sincerely thank Alma Murzagulova, Aizhan Seipanova, Meiramgul Akanova, Almas Aitzhan, Aigerim Boranbayeva, and Assel Kospabayeva, who acted as moderators during the review collection process. Their tireless efforts, diligence, and remarkable patience contributed significantly to the successful completion of this endeavour.</p>

## Citation 🎓

<p align = "justify">We kindly urge you, if you incorporate our model into your work, to cite our paper as a gesture of recognition for its valuable contribution. The act of referencing the relevant sources not only upholds academic honesty but also ensures proper acknowledgement of the authors' efforts. Your citation in your research significantly contributes to the continuous progress and evolution of the scholarly realm. Your endorsement and acknowledgement of our endeavours are genuinely appreciated.

```bibtex
@misc{yeshpanov2023kazsandra,
      title={KazSAnDRA: Kazakh Sentiment Analysis Dataset of Reviews and Attitudes}, 
      author={Rustem Yeshpanov and Huseyin Atakan Varol},
      year={2023},
      eprint={},
      archivePrefix={arXiv},
      primaryClass={}
}
```
