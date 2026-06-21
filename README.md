# Physics 102 CBT Exam 🎓

A web-based Computer-Based Testing (CBT) application for Physics 102, covering:
- Coulomb's Law & Electric Force
- Electric Field & Field Lines
- Gauss's Law & Applications
- Electric Potential & Potential Energy
- Electric Dipoles & Torque
- Conductors, Insulators & Semiconductors
- Electrostatic Induction & Shielding
- Continuous Charge Distributions
- Fundamental Forces of Nature
- Superposition Principle

## Features

✅ **100 Complex Questions** with detailed explanations
✅ **Shuffled Order** - Questions appear randomly each time
✅ **Instant Feedback** - Wrong answers show explanation immediately
✅ **Progress Tracking** - Real-time score display
✅ **Final Report** - Complete score, percentage, grade, and wrong answer review
✅ **Beautiful Dark UI** - Modern, responsive design

## Local Development

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/physics-102-cbt.git
cd physics-102-cbt
```

### 2. Create virtual environment
```bash
python -m venv venv
```

### 3. Activate virtual environment
**Windows:**
```bash
venv\Scripts\activate
```
**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the app
```bash
python app.py
```

Open your browser and go to `http://localhost:5000`

## Deploy to Render (Free Hosting)

### Step 1: Push to GitHub
```bash
# Initialize git (if not already)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Physics 102 CBT"

# Add remote (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/physics-102-cbt.git

# Push
git push -u origin main
```

### Step 2: Deploy on Render
1. Go to [render.com](https://render.com) and sign up (free)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure:
   - **Name:** `physics-102-cbt`
   - **Runtime:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Click **"Create Web Service"**
6. Wait for deployment (2-3 minutes)
7. Your app will be live at `https://physics-102-cbt.onrender.com`

## Project Structure

```
physics-102-cbt/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Procfile           # Render deployment config
├── .gitignore         # Git ignore rules
├── README.md          # This file
└── templates/
    ├── index.html     # Start page
    ├── question.html  # Question display
    ├── feedback.html  # Answer feedback
    └── results.html   # Final results
```

## License

MIT License - Free for educational use.
