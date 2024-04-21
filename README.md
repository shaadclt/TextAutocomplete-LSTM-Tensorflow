# Text Autocomplete with TensorFlow LSTM
Text Autocomplete with TensorFlow LSTM is a project that demonstrates how to build a simple text autocomplete system using TensorFlow and LSTM (Long Short-Term Memory) networks. This project utilizes a dataset of frequently asked questions (FAQs) about Metridash, an all-in-one content creation platform, to train the LSTM model to predict the next word given a sequence of words.

## Project Overview
This project consists of the following components:

- Data Preparation: The FAQs about Metridash are used as the dataset for training the LSTM model. The text is tokenized and preprocessed to create input sequences and corresponding output labels.
- Model Training: A Sequential model is built using TensorFlow and Keras. The model architecture includes an Embedding layer, followed by two LSTM layers, and a Dense layer with softmax activation.
- Model Evaluation: The model is trained on the input sequences and evaluated using categorical cross-entropy loss and accuracy metrics.
- Text Autocomplete: Once the model is trained, it can be used to generate text predictions. Given a starting phrase "Metridash uses", the model predicts the next word iteratively to autocomplete the phrase.

## Getting Started
To run this project, follow these steps:

1. Clone the Repository:
```bash
git clone https://github.com/shaadclt/TextAutocomplete-LSTM-Tensorflow.git
```

2. Open the Jupyter Notebook:
Open the **autocomplete_lstm_tensorflow.ipynb** notebook in Jupyter Notebook or JupyterLab

3. Run the Notebook Cells:
Execute each cell in the notebook sequentially to preprocess the data, train the LSTM model, and save the trained model.

4. Autocomplete Text:
After training the model, execute the cells related to text autocomplete to generate predictions based on the input phrase.

## Contributing
Contributions to this project are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
