# Extensions Setup Guide

## 🚀 **Quick Setup for Your Workflow**

### **1. Install Essential Extensions**

Open Cursor/VS Code and install these extensions:

#### **Python Development**

- **Python** (Microsoft) - Core Python support
- **Pylance** - Advanced Python language server
- **Black Formatter** - Auto-format Python code
- **Python Docstring Generator** - Auto-generate docstrings

#### **Git & Workflow**

- **GitLens** - Enhanced Git integration
- **Git Graph** - Visual Git history
- **GitHub Pull Requests** - Manage PRs in editor

#### **Productivity**

- **Material Icon Theme** - File type icons
- **Bracket Pair Colorizer** - Code readability
- **Todo Tree** - Track TODO comments
- **Bookmarks** - Bookmark important code

### **2. Configure Black Formatter**

```bash
# Install Black globally
pip install black

# Create pyproject.toml in project root
cat > pyproject.toml << EOF
[tool.black]
line-length = 88
target-version = ['py39']
include = '\.pyi?$'
EOF
```

### **3. Enable Auto-formatting**

1. Open Cursor/VS Code settings (`Cmd/Ctrl + ,`)
2. Search for "format on save"
3. Enable "Editor: Format On Save"
4. Set "Python › Formatting: Provider" to "black"

### **4. Setup Quick Deploy**

```bash
# Add to your shell profile (.zshrc or .bashrc)
echo 'alias quick-deploy="git add . && git commit -m \"Auto-deploy $(date)\" && git push origin main"' >> ~/.zshrc
source ~/.zshrc
```

### **5. Create Project Notes Structure**

```bash
# Create notes files in your project
touch NOTES.md SNIPPETS.md IDEAS.md TROUBLESHOOTING.md
```

### **6. Enable Settings Sync**

1. Open Command Palette (`Cmd/Ctrl + Shift + P`)
2. Search for "Settings Sync: Turn On"
3. Sign in with GitHub/Microsoft account
4. Choose what to sync (extensions, settings, keybindings)

## 🎯 **Workflow Improvements**

### **Daily Workflow**

1. **Start**: `source venv/bin/activate && streamlit run main.py`
2. **Code**: Write code (auto-formatted on save)
3. **Deploy**: `quick-deploy` (pushes to Git, auto-deploys to Streamlit Cloud)
4. **Notes**: Add to `NOTES.md` for important decisions

### **Cross-Computer Setup**

1. **Install same extensions** on all computers
2. **Enable Settings Sync** for consistent experience
3. **Use SSH keys** for Git authentication
4. **Store projects in Google Drive** for easy access

### **Code Snippets**

Create custom snippets for repeated code:

1. Open Command Palette
2. Search for "Preferences: Configure User Snippets"
3. Select "python.json"
4. Add your custom snippets

## 📝 **Quick Reference**

### **Keyboard Shortcuts**

- **Format Code**: `Shift + Alt + F`
- **Command Palette**: `Cmd/Ctrl + Shift + P`
- **Toggle Terminal**: `Ctrl + `` (backtick)
- **Quick Deploy**: `quick-deploy` (terminal command)

### **Useful Commands**

```bash
# Check formatting
black --check .

# Format all files
black .

# Quick deploy
quick-deploy

# Search notes
grep -r "TODO" . --include="*.md"
```

### **Extension Settings**

```json
{
	"python.formatting.provider": "black",
	"python.formatting.blackArgs": ["--line-length=88"],
	"editor.formatOnSave": true,
	"files.autoSave": "onFocusChange"
}
```

## 🎉 **Benefits You'll Get**

### **Immediate Improvements**

- ✅ **Auto-formatted code** on every save
- ✅ **One-command deployment** to Streamlit Cloud
- ✅ **Cross-computer sync** of settings and extensions
- ✅ **Better code navigation** with enhanced Git integration
- ✅ **Quick notes and snippets** for repeated code

### **Long-term Benefits**

- ✅ **Consistent code style** across all projects
- ✅ **Faster development** with snippets and automation
- ✅ **Better collaboration** with enhanced Git tools
- ✅ **Reduced context switching** with integrated tools

---

**Next Steps**: Install these extensions and try the workflow. You'll be amazed at how much faster and cleaner your development process becomes! 🚀
