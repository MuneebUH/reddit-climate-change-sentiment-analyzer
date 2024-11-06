# Reddit Climate Change Sentiment Analyzer

Welcome to the **Reddit Climate Change Sentiment Analyzer**! This Streamlit app leverages **VADER Sentiment Analysis** to analyze Reddit comments related to climate change. The app allows users to upload a CSV file containing Reddit comments, performs sentiment analysis, categorizes sentiments as Positive, Neutral, or Negative, and provides visual insights into the data.

---

## 🚀 Features

- **Upload CSV**: Upload a CSV file containing Reddit comments for analysis.
- **Sentiment Analysis**: Use the **VADER Sentiment Analysis** tool to classify sentiments.
- **Categorize Sentiments**: Comments are categorized into Positive, Neutral, or Negative sentiments.
- **Visualizations**: View sentiment distribution through intuitive bar charts.
- **Download Results**: After analysis, download the processed data as a CSV file.

---

## 📸 Screenshots

### 1. Upload CSV and View Introduction
This is the first step where users can upload their CSV file. The app provides an introductory overview of its functionalities.

![Screenshot 1](screenshots/screenshot1.png)

### 2. Sentiment Analysis Results
Once the file is uploaded, the app shows the sentiment analysis results for each comment, including sentiment scores and categories.

![Screenshot 2](screenshots/screenshot2.png)

### 3. Sentiment Distribution Visualization
A visualization displaying the distribution of sentiments across comments (Positive, Neutral, Negative).

![Screenshot 3](screenshots/screenshot3.png)

---

## 🛠️ Prerequisites

Before running the app, ensure you have **Python** installed, along with the following Python packages:

- `streamlit` - For building the app interface
- `pandas` - For data manipulation and analysis
- `nltk` - For sentiment analysis
- `matplotlib` - For data visualizations
- `seaborn` - For more advanced visualizations

---

## 📥 Installation

To get started, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/reddit-climate-change-sentiment-analyzer.git
    cd reddit-climate-change-sentiment-analyzer
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app**:

    ```bash
    streamlit run app.py
    ```

This will launch the app in your default web browser.

---

## 💬 Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and create a pull request.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
