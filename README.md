# 🎯 VAK Quiz Mini Project (Streamlit + Python)

This is a **VAK Learning Style Quiz** mini project built using **Python** and the **Streamlit** library.

The VAK model helps identify a person’s preferred learning style:
- **Visual (V)** – learning by seeing
- **Auditory (A)** – learning by listening
- **Kinesthetic (K)** – learning by doing/practicing

---

## ✅ Project Features

- 📌 **30 MCQ Questions**
- 📝 Each question has **3 options**
- ✅ User selects answers using **radio buttons**
- 🔘 **Submit button** to finish the quiz
- 📊 Final result shows:
  - **Visual %**
  - **Auditory %**
  - **Kinesthetic %**
- 🏆 Displays the **highest learning style** based on score

---

## 🛠️ Technologies Used

- **Python**
- **Streamlit**

---

## 📌 How the Result is Calculated

At the end of the quiz, the app counts total answers for each category:

- Visual count = V  
- Auditory count = A  
- Kinesthetic count = K

percentage = (category_count / total_questions) * 100


---

## ▶️ How to Run the Project

1. Install Streamlit:

```bash
pip install streamlit

2. Use this to run in terminal:
```bash
streamlit run mini.py

✅ Output

After submitting all 30 questions, the app shows the final learning style result with average percentage.

Example:

Visual: 70%

Auditory: 20%

Kinesthetic: 10%


Then percentage is calculated like this:

