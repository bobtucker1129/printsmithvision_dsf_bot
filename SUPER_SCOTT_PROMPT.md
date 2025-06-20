# SUPER_SCOTT_PROMPT.md - Master Control Document

## 🎯 **Purpose**

This document serves as the single source of truth for all project workflows, best practices, and procedures. When things get jumbled or we need to reset, this document brings everything back into harmony.

**Last Updated**: June 19, 2025  
**Version**: 1.0.0

---

## 🏗️ **PROJECT STRUCTURE STANDARDS**

### **Folder Organization (Simplified)**

```
project_name/
├── main.py                    # Main application file
├── requirements.txt           # Python dependencies
├── .env                      # Environment variables (gitignored)
├── SUPER_SCOTT_PROMPT.md     # This document (master control)
├── PROJECT_STATUS.md         # Current project status and roadmap
├── venv/                     # Virtual environment
└── db/                       # Database connections
    └── db_conn.py
```

### **Optional Folders (Only if needed)**

```
project_name/
├── config/                   # Configuration files (if complex config needed)
├── logic/                    # Business logic modules (if code gets large)
├── static/                   # Static assets (if needed)
└── templates/                # Template files (if needed)
```

### **File Naming Conventions**

- **Python files**: `snake_case.py`
- **Configuration files**: `snake_case.py` or `PascalCase.py`
- **Documentation**: `UPPER_CASE.md`
- **Backups**: `main_backup_YYYYMMDD_HHMMSS.py`

### **Documentation Hierarchy**

1. **SUPER_SCOTT_PROMPT.md** - Master control (copy to every project)
2. **PROJECT_STATUS.md** - Project-specific status and roadmap
3. **README.md** - Quick start guide (optional)
4. **Feature-specific docs** - Only for complex features

---

## 🔄 **DAILY WORKFLOW ROUTINES**

### **Start of Day**

1. **Activate virtual environment**: `source venv/bin/activate`
2. **Check app status**: `streamlit run main.py` (verify it starts)
3. **Review PROJECT_STATUS.md** (if exists) for current state
4. **Check for any pending issues** from previous session

### **End of Day**

1. **Create backup**: `cp main.py main_backup_$(date +%Y%m%d_%H%M%S).py`
2. **Update PROJECT_STATUS.md** with progress
3. **Commit changes** to version control
4. **Document any issues** or next steps
5. **Stop running processes**: `Ctrl+C` in terminal

### **Weekly Maintenance**

1. **Clean old backups** (keep last 5)
2. **Update dependencies**: `pip install -r requirements.txt --upgrade`
3. **Review and update SUPER_SCOTT_PROMPT.md** if needed
4. **Archive completed features** in documentation

---

## 💾 **BACKUP PROCEDURES**

### **Automatic Backups**

```bash
# Create timestamped backup
cp main.py main_backup_$(date +%Y%m%d_%H%M%S).py

# List recent backups
ls -la main_backup_*.py

# Clean old backups (keep last 5)
ls -t main_backup_*.py | tail -n +6 | xargs rm
```

### **Before Major Changes**

1. **Create backup** with descriptive name
2. **Test current functionality** to ensure baseline
3. **Document what you're about to change**
4. **Have rollback plan** ready

### **Recovery Procedures**

1. **Stop running app**: `Ctrl+C`
2. **Restore from backup**: `cp main_backup_YYYYMMDD_HHMMSS.py main.py`
3. **Test functionality**: `streamlit run main.py`
4. **Document what went wrong** for future reference

---

## 🧠 **MEMORY MANAGEMENT**

### **When to Reset Memory**

- **After 2-3 hours** of intensive development
- **When switching projects**
- **When confusion sets in**
- **At end of day**

### **Memory Reset Procedure**

1. **Say**: "Run SUPER_SCOTT_PROMPT.md"
2. **I will**: Read this document and restore context
3. **You will**: Provide current project status
4. **We will**: Continue from clean state

### **Context Preservation**

- **Always reference PROJECT_STATUS.md** for project-specific info
- **Keep SUPER_SCOTT_PROMPT.md** updated with new learnings
- **Document decisions** in project-specific files

---

## 🎨 **CODING STANDARDS**

### **Python Best Practices**

- **Type hints**: Use for all function parameters and returns
- **Docstrings**: Every function gets a clear description
- **Error handling**: Try/catch with specific error messages
- **Modular structure**: Break code into focused functions
- **Consistent formatting**: Use Black or similar formatter

### **Streamlit Best Practices**

- **Page config**: Set at top of every app
- **Unique keys**: For all interactive elements
- **Error handling**: User-friendly error messages
- **Loading states**: Use spinners for database operations
- **Clean UI**: Use columns, tabs, and proper spacing

### **Database Best Practices**

- **Connection management**: Always close cursors and connections
- **Parameterized queries**: Use %s placeholders
- **Error handling**: Specific database error messages
- **Transaction management**: Commit after successful operations

---

## 📋 **MILESTONE TRACKING**

### **Feature Status Codes**

- ✅ **Complete**: Feature is working and tested
- 🔄 **In Progress**: Currently being developed
- ⏸️ **On Hold**: Temporarily paused
- 📝 **Planned**: On roadmap but not started
- 🐛 **Bug**: Known issue to fix

### **Documentation Requirements**

- **PROJECT_STATUS.md**: Overall project status
- **Feature-specific docs**: For complex features
- **API documentation**: For database interactions
- **Setup guides**: For new team members

---

## 🛠️ **REFACTORING PRACTICES**

### **When to Refactor**

- **Code duplication** appears
- **Functions become too long** (>50 lines)
- **Complex nested logic** develops
- **Performance issues** arise
- **Maintainability** becomes difficult

### **Refactoring Process**

1. **Create backup** before starting
2. **Identify the problem** clearly
3. **Plan the solution** before coding
4. **Make small, incremental changes**
5. **Test after each change**
6. **Update documentation**

### **Code Organization**

- **Single responsibility**: Each function does one thing
- **Separation of concerns**: UI, logic, and data layers
- **Dependency injection**: Pass dependencies as parameters
- **Configuration externalization**: Use .env files

---

## 🔧 **FAVORITE EXTENSIONS & TOOLS**

### **Python Development (Essential)**

- **Python** (Microsoft): Core Python support and IntelliSense
- **Pylance**: Advanced Python language server with type checking
- **Black Formatter**: Auto-format Python code to PEP 8 standards on save
- **Python Docstring Generator**: Auto-generates docstrings for functions
- **Python Indent**: Smart indentation for Python
- **Python Test Explorer**: Run and debug tests

### **Code Quality & Formatting**

- **Black Formatter**: Automatic Python code formatting
- **isort**: Import statement sorting
- **flake8**: Linting and style checking
- **Code Spell Checker**: Catches typos in code and comments
- **Error Lens**: Shows errors and warnings inline

### **Git & Version Control**

- **GitLens**: Enhanced Git integration with blame, history, and more
- **Git Graph**: Visual Git history and branch management
- **GitHub Pull Requests**: Manage PRs directly in editor
- **GitHub Repositories**: Clone and manage repos easily
- **Git History**: View file history and compare changes

### **Productivity & Navigation**

- **Auto Rename Tag**: Automatically rename HTML/XML tags
- **Bracket Pair Colorizer**: Color-code matching brackets
- **Material Icon Theme**: Beautiful file type icons
- **Path Intellisense**: Auto-complete file paths
- **Todo Tree**: Highlight and track TODO comments
- **Bookmarks**: Bookmark important code sections

### **Multi-Computer Workflow**

### **Quick Setup for New Computers**

**For this specific project**: See `QUICK_SETUP.md` for a 5-minute setup guide.

### **Google Drive + Git + Streamlit Cloud Setup**

1. **Store projects in Google Drive** for easy access
2. **Use Git for version control** and collaboration
3. **Deploy to Streamlit Cloud** for testing and sharing

### **Quick Deploy Script**

```bash
# Add to your shell profile (.zshrc or .bashrc)
alias quick-deploy='git add . && git commit -m "Auto-deploy $(date)" && git push origin main'
```

### **Workflow Commands**

```bash
# Start new session
source venv/bin/activate
streamlit run main.py

# Quick save and deploy
quick-deploy

# Check status
git status
streamlit --version
```

### **Cross-Computer Sync**

- **Settings Sync**: Enable in VS Code/Cursor
- **Git credentials**: Use SSH keys or credential manager
- **Environment files**: Keep `.env` in Google Drive (secure)
- **Requirements**: Always update `requirements.txt` after new packages

---

## 📝 **SCRATCH PAD & CODE SNIPPETS**

### **Built-in Cursor Features**

- **Snippets**: Create custom code snippets for repeated code
- **Notebooks**: Use `.ipynb` files for notes and testing
- **Markdown files**: Create `NOTES.md` in each project

### **Snippet Examples**

```json
// Python function snippet
{
	"def with type hints": {
		"prefix": "deftype",
		"body": [
			"def ${1:function_name}(${2:param}: ${3:str}) -> ${4:None}:",
			"    \"\"\"${5:Function description}.\"\"\"",
			"    ${6:pass}"
		]
	}
}
```

### **Project Notes Structure**

```
project_name/
├── NOTES.md                    # General project notes
├── SNIPPETS.md                 # Code snippets for this project
├── IDEAS.md                    # Future feature ideas
└── TROUBLESHOOTING.md          # Project-specific issues
```

### **Quick Notes Commands**

```bash
# Create quick note
echo "# $(date): Quick Note" >> NOTES.md

# Search notes
grep -r "TODO" . --include="*.md"
```

---

## 🎨 **AUTOMATED CODE FORMATTING**

### **Black Configuration**

Create `pyproject.toml` in project root:

```toml
[tool.black]
line-length = 88
target-version = ['py39']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | build
  | dist
)/
'''
```

### **Auto-format on Save**

1. Install Black: `pip install black`
2. Install Black Formatter extension
3. Enable "Format on Save" in settings
4. Set Black as default Python formatter

### **Pre-commit Hooks**

```bash
# Install pre-commit
pip install pre-commit

# Create .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black
  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
```

---

## 🔄 **WORKFLOW AUTOMATION**

### **VS Code/Cursor Tasks**

Create `.vscode/tasks.json`:

```json
{
	"version": "2.0.0",
	"tasks": [
		{
			"label": "Deploy to Streamlit",
			"type": "shell",
			"command": "git add . && git commit -m 'Auto-deploy' && git push origin main",
			"group": "build"
		},
		{
			"label": "Format Code",
			"type": "shell",
			"command": "black .",
			"group": "build"
		}
	]
}
```

### **Keyboard Shortcuts**

- **Format Document**: `Shift + Alt + F`
- **Quick Deploy**: `Ctrl + Shift + P` → "Tasks: Run Task" → "Deploy to Streamlit"
- **Toggle Terminal**: `Ctrl + `` (backtick)
- **Command Palette**: `Ctrl + Shift + P`

---

## 📊 **PROJECT ORGANIZATION WITH EXTENSIONS**

### **File Explorer Enhancements**

- **Material Icon Theme**: Visual file type identification
- **Bookmarks**: Quick access to important files
- **File Utils**: Bulk file operations

### **Code Navigation**

- **Bracket Pair Colorizer**: Visual code structure
- **Indent Rainbow**: Visual indentation levels
- **Highlight Line**: Highlight current line

### **Collaboration Tools**

- **Live Share**: Real-time collaboration
- **GitLens**: Enhanced Git integration
- **GitHub Pull Requests**: Manage PRs in editor

---

## 🚨 **TROUBLESHOOTING GUIDE**

### **Common Issues & Solutions**

#### **Import Errors**

```bash
# Check virtual environment
which python
# Should show: /path/to/project/venv/bin/python

# Reinstall dependencies
pip install -r requirements.txt
```

#### **Database Connection Issues**

```bash
# Check .env file exists
ls -la .env

# Test connection manually
python -c "from db.db_conn import get_connection; print(get_connection())"
```

#### **Streamlit Issues**

```bash
# Kill existing processes
pkill -f streamlit

# Start on different port
streamlit run main.py --server.port 8502
```

#### **Memory/Context Issues**

- **Say**: "Run SUPER_SCOTT_PROMPT.md"
- **Provide**: Current project status
- **Continue**: From clean state

---

## 📈 **PROJECT LIFECYCLE**

### **New Project Setup**

1. **Create project folder**
2. **Copy SUPER_SCOTT_PROMPT.md** to project
3. **Initialize virtual environment**
4. **Create basic structure**
5. **Set up database connection**
6. **Create initial README.md**

### **Feature Development**

1. **Plan the feature** (requirements, design)
2. **Create backup** before starting
3. **Implement incrementally**
4. **Test thoroughly**
5. **Update documentation**
6. **Deploy/commit changes**

### **Project Maintenance**

1. **Regular backups**
2. **Dependency updates**
3. **Code cleanup**
4. **Documentation updates**
5. **Performance monitoring**

---

## 🎯 **COMMUNICATION PROTOCOLS**

### **When Things Get Confusing**

1. **Stop and say**: "Run SUPER_SCOTT_PROMPT.md"
2. **I will**: Read this document and restore context
3. **You will**: Provide current situation
4. **We will**: Continue from clean state

### **When Adding New Procedures**

1. **Test the procedure** thoroughly
2. **Add to SUPER_SCOTT_PROMPT.md**
3. **Update version number**
4. **Document in project-specific files**

### **When Switching Projects**

1. **Complete current work** (backup, commit)
2. **Say**: "Run SUPER_SCOTT_PROMPT.md"
3. **Provide**: New project context
4. **Continue**: With clean state

---

## 📝 **DOCUMENTATION STANDARDS**

### **Required Documents**

- **SUPER_SCOTT_PROMPT.md**: This document (master control)
- **PROJECT_STATUS.md**: Current project status and roadmap
- **requirements.txt**: Python dependencies
- **.env**: Environment variables (gitignored)

### **Optional Documents**

- **README.md**: Project overview and quick start
- **API_DOCS.md**: Database schema and API documentation
- **TROUBLESHOOTING.md**: Project-specific issues

### **Document Maintenance**

- **Update when adding features**
- **Review weekly for accuracy**
- **Archive outdated information**
- **Keep single source of truth**

---

## 🎉 **SUCCESS METRICS**

### **Project Health Indicators**

- ✅ **App starts without errors**
- ✅ **All features working**
- ✅ **Documentation current**
- ✅ **Backups recent**
- ✅ **Code clean and organized**

### **Development Efficiency**

- ✅ **No import/export cycles**
- ✅ **Consistent code style**
- ✅ **Clear project structure**
- ✅ **Easy to onboard new team members**
- ✅ **Quick problem resolution**

---

**Remember**: This document is your master control. When in doubt, say "Run SUPER_SCOTT_PROMPT.md" and I'll bring everything back into harmony! 🎯
