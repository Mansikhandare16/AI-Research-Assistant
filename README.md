## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Mansikhandare16/AI-Research-Assistant.git
cd AI-Research-Assistant
```

### 2. Create and activate a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install the project dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `env_template.txt` to `.env`.

Add the following API keys:

```text
GROQ_API_KEY=your_groq_api_key
SERPER_API_KEY=your_serper_api_key
```

### 5. Launch the application

```bash
streamlit run app.py
```

### 6. Open the application

Open your web browser and navigate to:

```
http://localhost:8501
```

### 7. Generate a Research Report

- Enter a research topic in the input field.
- Click **Start Research**.
- The **Research Specialist** performs web research using the SerperDev Search Tool.
- The **Data Analyst** analyzes the collected information.
- The **Content Writer** generates the final structured research report.
- View the generated report in the Streamlit interface.
