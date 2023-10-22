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

<p align = "center">This repository provides a dataset and pre-trained models for the paper <br><a href = "https://arxiv.org/abs/2305.15749"><b>KazSAnDRA: Kazakh Sentiment Analysis Dataset of Reviews and Attitudes</b></a></p>

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

<p align = "justify">In Kazakhstan, people often switch between speaking Kazakh and Russian. There is also a trend of moving from using the <a href="https://en.wikipedia.org/wiki/Cyrillic_script>Cyrillic</a> to the <a href="https://en.wikipedia.org/wiki/Latin_script">Latin script</a>. As a result, the Kazakh reviews in our dataset can take various forms: (a) purely Kazakh words written in the Kazakh Cyrillic script, (b) Kazakh words in the Latin script, (c) a mix of Cyrillic and Latin characters, (d) a mix of Russian and Kazakh words, or (e) entirely in Cyrillic with Russian characters instead of Kazakh ones.</p>

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
    <th rowspan="3">Source</th>
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
    <td>Play</td>
    <td>105,051</td>
    <td>76.88</td>
    <td>13,131</td>
    <td>76.88</td>
    <td>13,134</td>
    <td>76.89</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>Kaspi</td>
    <td>19,376</td>
    <td>14.18</td>
    <td>2,421</td>
    <td>14.17</td>
    <td>2,422</td>
    <td>14.18</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>2GIS</td>
    <td>3,978</td>
    <td>2.91</td>
    <td>498</td>
    <td>2.92</td>
    <td>497</td>
    <td>2.91</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>Kitap</td>
    <td>3,688</td>
    <td>2.7</td>
    <td>461</td>
    <td>2.7</td>
    <td>461</td>
    <td>2.7</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>Maps</td>
    <td>3,104</td>
    <td>2.27</td>
    <td>388</td>
    <td>2.27</td>
    <td>388</td>
    <td>2.27</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>Flip</td>
    <td>1,443</td>
    <td>1.06</td>
    <td>181</td>
    <td>1.06</td>
    <td>179</td>
    <td>1.05</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td><b>Total</b></td>
    <td><b>136,640</b></td>
    <td><b>100</b></td>
    <td><b>17,080</b></td>
    <td><b>100</b></td>
    <td><b>17,081</b></td>
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
    <td>98,363</td>
    <td>71.99</td>
    <td>12,294</td>
    <td>71.98</td>
    <td>12,297</td>
    <td>71.99</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>4</td>
    <td>19,854</td>
    <td>14.53</td>
    <td>2,481</td>
    <td>14.53</td>
    <td>2,482</td>
    <td>14.53</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>3</td>
    <td>8,880</td>
    <td>6.5</td>
    <td>1,110</td>
    <td>6.5</td>
    <td>1,110</td>
    <td>6.5</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>1</td>
    <td>5,663</td>
    <td>4.14</td>
    <td>708</td>
    <td>4.15</td>
    <td>708</td>
    <td>4.14</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td>2</td>
    <td>3,880</td>
    <td>2.84</td>
    <td>487</td>
    <td>2.85</td>
    <td>484</td>
    <td>2.83</td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td><b>Total</b></td>
    <td><b>136,640</b></td>
    <td><b>100</b></td>
    <td><b>17,080</b></td>
    <td><b>100</b></td>
    <td><b>17,081</b></td>
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
    <td>107,243</td>
    <td>23,734</td>
    <td>23,734</td>
  </tr>
   <tr></tr>
  <tr align = "center">
    <td>1</td>
    <td>107,243</td>
    <td>23,734</td>
    <td>107,243</td>
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
    <td>98,363</td>
    <td>3,880</td>
    <td>19,854</td>
  </tr>
  <tr></tr>
  <tr  align = "center">
    <td>2</td>
    <td>98,363</td>
    <td>3,880</td>
    <td>3,880</td>
  </tr>
  <tr></tr>
  <tr  align = "center">
    <td>3</td>
    <td>98,363</td>
    <td>3,880</td>
    <td>5,663</td>
  </tr>
  <tr></tr>
  <tr  align = "center">
    <td>4</td>
    <td>98,363</td>
    <td>3,880</td>
    <td>8,880</td>
  </tr>
  <tr></tr>
  <tr  align = "center">
    <td>5</td>
    <td>98,363</td>
    <td>3,880</td>
    <td>98,363</td>
  </tr>
</tbody>
</table>

## Dataset Structure 📁

<p align = "justify">The <a href="https://github.com/IS2AI/KazSAnDRA/tree/main/dataset">dataset</a> folder contains a collection of CSV files, distinguished by a two-digit prefix in their names. All the collected reviews are aggregated and stored within a unified file with the prefix "00". Additionally, the dataset includes six distinct files, numbered from "01" to "06", each explicitly annotated with the names of their respective sources, serving to indicate the origins of the reviews they contain.</p>

<p align = "justify">The dataset contains three distinct sets: the training set, validation set, and test set, denoted by the prefixes "07" to "16." Notably, the file names employ specific suffixes that warrant attention. The suffixes "pc" and "sc" pertain to the <b>P</b>olarity <b>C</b>lassification and <b>S</b>core <b>C</b>lassification tasks, respectively. The suffix "ib" designates the original <b>I</b>m<b>B</b>alanced training data. Moreover, "ros" indicates the balanced sets obtained through the <b>R</b>andom <b>O</b>ver<b>S</b>ampling technique, while "rus" signifies the balanced sets achieved through the <b>R</b>andom <b>U</b>nder<b>S</b>ampling technique.</p>

<p align = "justify">Files from 00 to 06 contain individual records, each consisting of three primary elements: the unaltered textual content of the review, the associated review score, which falls within the range of 1 to 5, and the specific source from which the review originated. These sources are identified by distinct entities such as "2gis", "flip", and others.</p>

<p align = "justify">On the other hand, files with numbering from 07 to 16 exhibit a distinct composition. With the exception of files carrying suffixes "ros" and "rus," these records encompass both the original, unprocessed text of the reviews and the preprocessed version of the review text. Furthermore, they incorporate the corresponding review score alongside the explicit origin of each review, as indicated earlier. Conversely, files labelled with "ros" and "rus" only contain the preprocessed version of the review text and its associated score.</p>

## Sentiment Classification Models 🧠

<p align = "justify">For the evaluation of KazSAnDRA, we utilised four multilingual machine learning models, all of which
incorporated the Kazakh language and are accessible through the <a href = "https://huggingface.co/">Hugging Face</a> Transformers framework:</p>

1. <a href = "https://huggingface.co/bert-base-multilingual-uncased">mBERT</a>
2. <a href = "https://huggingface.co/xlm-roberta-base">XLM-R</a>
3. <a href = "https://huggingface.co/google/rembert">RemBERT</a>
4. <a href = "https://huggingface.co/facebook/mbart-large-50">mBART-50</a>

## Acknowledgements 🙏

<p align = "justify">We express our sincere gratitude to Aizhan Seipanova, Alma Murzagulova, Almas Aitzhan, and Meiramgul Akanova, who served as moderators during the comprehensive review collection process. Their unwavering dedication, diligence, and remarkable patience significantly contributed to the successful completion of this endeavour.</p>

## Citation 🎓

<p align = "justify">We kindly urge you, if you incorporate our model into your work, to cite our paper as a gesture of recognition for its valuable contribution. The act of referencing the relevant sources not only upholds academic honesty but also ensures proper acknowledgment of the authors' efforts. Your citation in your research significantly contributes to the continuous progress and evolution of the scholarly realm. Your endorsement and acknowledgement of our endeavours are genuinely appreciated.

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
