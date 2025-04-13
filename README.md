# 📊 Sentylser – Sentiment Analyzer for Product Reviews

**Sentylser** is an interactive Streamlit app that performs **sentiment analysis** on product reviews using **VADER** (Valence Aware Dictionary and sEntiment Reasoner). Upload a CSV file, analyze individual product sentiments, visualize results, and download a summary of sentiment for all products.

---

## 🚀 Features

- 📁 Upload your CSV file containing product reviews
- 🎯 Select columns for product names and review texts
- 📊 Analyze sentiment (Positive, Neutral, Negative) for each review using VADER
- 🥧 Visualize sentiment distribution via a pie chart
- 🧠 Automatically detect the dominant sentiment for each product
- 💾 Download a sentiment summary CSV for all products

---

## 🧠 How It Works

1. **Upload a CSV file** with product names and review texts.
2. **Select**:
   - The column with product names
   - A product to analyze
   - The column with review text
3. **Sentiment classification** is done using VADER:
   - **Positive**: Compound score ≥ 0.5
   - **Neutral**: -0.5 < score < 0.5
   - **Negative**: Compound score ≤ -0.5
4. **Pie chart** shows sentiment breakdown for the selected product.
5. **Download** a CSV file summarizing the dominant sentiment for all products.

## Try it here: https://sentylser.streamlit.app/

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/sentylser.git
cd sentylser
