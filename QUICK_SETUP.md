# Quick Setup Guide - PrintSmith Vision DSF Bot

## 🚀 **New Computer Setup (5 minutes)**

### **1. Clone/Download Project**

```bash
# If using Git
git clone <repository-url>
cd printsmithvision_dsf_bot

# If using Google Drive
# Just navigate to the project folder
```

### **2. Set Up Python Environment**

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Mac/Linux
# or
venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt
```

### **3. Install Cursor Extensions**

Open Cursor and install these extensions (Cmd+Shift+X):

- **Python** (Microsoft)
- **Pylance**
- **Black Formatter**
- **Material Icon Theme**
- **GitLens**
- **Git Graph**

### **4. Configure Black Formatting**

1. Open Cursor settings (Cmd+,)
2. Search for "format on save"
3. Enable "Editor: Format On Save"
4. Set "Python › Formatting: Provider" to "black"

### **5. Set Up Environment Variables**

```bash
# Create .env file
cp .env.example .env  # if example exists
# or create manually with your database credentials
```

### **6. Test Everything**

```bash
# Test Black formatting
black --version

# Test app startup
streamlit run main.py
```

## ✅ **Verification Checklist**

- [ ] Virtual environment activated
- [ ] All packages installed (`pip list`)
- [ ] Black formatter working (`black --version`)
- [ ] App starts without errors (`streamlit run main.py`)
- [ ] Cursor extensions installed
- [ ] Format on save enabled
- [ ] Database connection working

## 🔧 **Current Project Tools**

### **Installed Packages**

- `streamlit` - Web app framework
- `psycopg2-binary` - PostgreSQL adapter
- `sqlalchemy` - Database ORM
- `openai` - AI integration
- `python-dotenv` - Environment management
- `black` - Code formatting
- `flake8` - Linting

### **Configuration Files**

- `pyproject.toml` - Black configuration
- `.vscode/settings.json` - Cursor workspace settings
- `requirements.txt` - Python dependencies
- `.env` - Environment variables (create from template)

### **Key Extensions**

- **Black Formatter** - Auto-format on save
- **Python/Pylance** - IntelliSense and type checking
- **GitLens** - Enhanced Git integration
- **Material Icon Theme** - File type icons

## 🚨 **Troubleshooting**

### **If Black Doesn't Auto-Format**

1. Restart Cursor
2. Check if Black Formatter extension is installed
3. Verify "Format on Save" is enabled
4. Try manual format: `Shift+Alt+F`

### **If App Won't Start**

1. Check virtual environment is activated
2. Verify all packages installed: `pip install -r requirements.txt`
3. Check `.env` file exists with correct database credentials
4. Test database connection manually

### **If Extensions Don't Work**

1. Install extensions manually in Cursor
2. Enable Settings Sync in Cursor
3. Check extension settings and permissions

## 📞 **Need Help?**

1. Check `SUPER_SCOTT_PROMPT.md` for detailed workflows
2. Review `PROJECT_STATUS.md` for current project state
3. Check `TROUBLESHOOTING.md` for known issues
4. Say "Run SUPER_SCOTT_PROMPT.md" to reset context

---

**Remember**: This project uses the master control document `SUPER_SCOTT_PROMPT.md` for all workflows and best practices! 🎯
