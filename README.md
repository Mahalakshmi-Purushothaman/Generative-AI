# Generative-AI
### Introduction
Generative Artificial Intelligence (Gen AI) is a subset of Deep Learning (DL) that generates new data based on training samples. It can produce images, text, audio, and video as outputs. Unlike traditional machine learning models, Generative AI does not require labeled data due to the immense volume of input data. Instead, it processes unstructured data using Large Language Models (LLMs) for training purposes.

### Importance of Generative AI
Generative AI is crucial due to the following reasons:
 - It helps in understanding complex patterns from large datasets.
 - It enables the generation of high-quality content.
 - It facilitates the development of powerful applications with reduced effort and time.

### Large Language Models (LLM)
LLMs are advanced machine learning models that utilize deep learning algorithms to process and comprehend natural language. These models serve as the backbone of various Generative AI applications.

### Generative AI Pipeline
A Generative AI pipeline consists of sequential steps designed to build an end-to-end AI-powered system. The approach involves breaking down complex requirements into smaller, manageable sub-problems and developing a structured process to solve them.
 - Pipeline Structure
 - Data Acquisition
 - Data Preparation
 - Feature Engineering
 - Modeling
 - Evaluation
 - Deployment
 - Monitoring & Model Training
![image](https://github.com/user-attachments/assets/75609deb-b69f-4472-abdf-97c73d774466)


### 1. Data Acquisition
Data acquisition involves gathering datasets from various sources, including:
 - Structured files (CSV, TXT, PDF, DOC, XLSX)
 - Databases, internet sources, APIs, and web scraping
 - Situations where no data is available may require data collection via surveys or leveraging existing LLMs with data augmentation techniques.

### Data Augmentation
Data augmentation is the process of creating new data from existing data to enhance the diversity of the training set. This technique is categorized into multiple types:
 - Image augmentation
 - Text augmentation
 - Audio augmentation
 - Video augmentation
 - Tabular data augmentation
 - Generative Adversarial Networks (GANs)

### 2. Data Preprocessing
Data preprocessing is essential for cleaning and transforming raw data into a suitable format for model training. This includes:
 - Removing HTML tags, emojis, and performing spell checks
 - Tokenization, lemmatization, and stemming
 - Part-of-Speech (POS) tagging, parsing, and coreference resolution
 - Tokenization Types
 - Word Tokenization
 - Sentence Tokenization

### 3. Feature Engineering
Feature Engineering means converting text data to numerical data. but why it is required to convert text data to numerical data?. because our machine learning model doesn’t understand text data then we have to do feature engineering. This step is also called Feature extraction from text. I have already written a complete guide on Feature extraction techniques used in NLP. Click here. In this step, we use multiple techniques to convert text to numerical vectors.

    1. One Hot Encoder
    2. Bag Of Word(BOW)
    3. n-grams
    4. Tf-Idf
    5. Word2vec

### 4. Data Modeling
 - In the modeling step, we try to make a model based on data. here also we can use multiple approaches to build the model based on the problem statement.
 - Approaches to building model –
   - Heuristic Approach
   - Machine Learning Approach
   - Deep Learning Approach
   - Cloud API
 - Approach to select right model is based on 1. Amount of data and 2. Nature of the problem.

 - If we have very less data then we can not use ML or DL approach then we have to use the heuristic approach.
 - If we have a good amount of data then we can use a machine learning approach
 - If we have a large amount of data then we can use a deep learning approach.

### 5. Model Evaluation
The performance of a Generative AI model is assessed using:
 - Intrinsic Evaluation – Measures the model’s internal consistency and accuracy
 - Extrinsic Evaluation – Evaluates the model’s effectiveness based on real-world applications

### 6. Deployment
After evaluation, the trained model is deployed into a production environment to generate insights and content at scale. Post-deployment, continuous monitoring and periodic model retraining ensure sustained performance.
Three stages of deployment –
 - Deployment – model deploying on the cloud for users.
 - Monitoring – In the monitoring phase, we have to watch the model continuously. Here we have to create a dashboard to show evaluation metrics.
 - Update- Retrain the model on new data and again deploy.

This repository serves as a guide to understanding Generative AI, its working mechanism, and its structured approach to implementation.
