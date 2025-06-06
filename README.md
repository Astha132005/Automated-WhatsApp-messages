# 📱 Automated WhatsApp Messages

A Python script to send automated WhatsApp messages at a scheduled time using [`pywhatkit`](https://pypi.org/project/pywhatkit/). Perfect for sending reminders, greetings, or alerts without manual effort.

---

## 🛠 Features

* ⏰ Schedule messages to be sent at a specific time
* 💬 Sends messages directly to a WhatsApp contact or number
* ✅ Simple and beginner-friendly
* 🧪 Great for learning automation with Python

---

## 💻 Requirements

Make sure you have Python 3 installed. Then install the required library:

```bash
pip install pywhatkit
```

---

## 🧾 How It Works

1. `pywhatkit.sendwhatmsg()` is used to schedule the message.
2. WhatsApp Web opens automatically in your browser.
3. The script waits until the specified time.
4. The message is typed and sent to the specified number.

---

## 📝 Sample Code

```python
import pywhatkit

try:
    pywhatkit.sendwhatmsg("+91xxxxxxxxxxx", "Hello, I'm ASTHA. Nice to meet you.", 15, 30)
    print("Message Scheduled Successfully!")

except:
    print("An Unexpected Error Occurred!")
```

🕒 In the example above, a message will be sent at **3:30 PM** to the specified number.

---

## 🚀 How to Run the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Automated-WhatsApp-messages.git
cd Automated-WhatsApp-messages
```

### 2. Install Dependencies

```bash
pip install pywhatkit
```

### 3. Open the Code in Your Editor

Use any code editor (like VS Code, PyCharm, or Sublime Text) to open the folder.

Example with VS Code:

```bash
code .
```

### 4. Edit the Script

Open the `.py` file and replace:

* `+91xxxxxxxxxxx` with the recipient’s phone number (including country code)
* `"Your Message Here"` with your desired message
* `hour` and `minute` parameters with the scheduled time (24-hour format)

### 5. Run the Script

```bash
python script_name.py
```

The browser will open WhatsApp Web, so make sure you're logged in.

---

## ⚠️ Notes

* Ensure a stable internet connection.
* You must stay logged in to WhatsApp Web.
* Keep the tab active until the message is sent.

---

## 🧠 Use Cases

* Morning greetings
* Event reminders
* Alerts for important updates

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---
