# 🚗 Commute Tracker Learning Project

> **Learning Journey**: Master Python FastAPI + React TypeScript through building a practical commute tracking application

A comprehensive, hands-on learning project designed to teach modern web development while building something you'll actually use! This project focuses on learning **Python FastAPI** for backend development with a **React TypeScript** frontend.

## 🎯 What You'll Learn

### Backend Skills (Python FastAPI)
- ✅ **FastAPI Fundamentals** - Modern async web framework
- ✅ **SQLAlchemy & PostgreSQL** - Database operations and ORM
- ✅ **Pydantic** - Data validation and serialization
- ✅ **Async Programming** - Modern Python concurrency patterns
- ✅ **API Integration** - Google Maps APIs for real-world data
- ✅ **Authentication & Security** - JWT tokens and password hashing
- ✅ **Testing** - pytest for reliable code
- ✅ **Data Analysis** - Pandas/NumPy for commute insights

### Frontend Skills (React TypeScript)
- ✅ **Modern React** - Hooks, Context, and patterns
- ✅ **TypeScript** - Type safety and better development
- ✅ **API Integration** - Connecting to FastAPI backend
- ✅ **Google Maps** - Interactive mapping features
- ✅ **State Management** - React Query for server state
- ✅ **UI Components** - Modern, responsive design

### DevOps & Tools
- ✅ **Docker** - Containerization for consistent development
- ✅ **PostgreSQL** - Production-grade database
- ✅ **Redis** - Caching and performance
- ✅ **Git** - Version control best practices

## 🚀 Quick Start (2025 Edition)

### Prerequisites
```bash
# Required software
- Python 3.11+ 
- Node.js 20+
- Docker Desktop 4.20+
- Git 2.40+
- Code editor (VS Code recommended with Cursor)
```

### 1. Clone & Setup
```bash
# Clone the repository
git clone https://github.com/krisyana/commute-tracker-learning.git
cd commute-tracker-learning

# Copy environment template
cp .env.example .env

# Edit .env file with your Google Maps API key
# Get key from: https://console.cloud.google.com/apis/credentials
```

### 2. Get Google Maps API Key
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable these APIs:
   - Maps JavaScript API
   - Directions API
   - Geocoding API
4. Create credentials (API Key)
5. Add your API key to `.env` file

### 3. Start Development Environment
```bash
# Start all services (this might take a few minutes first time)
docker-compose up -d

# Check if everything is running
docker-compose ps

# View logs if needed
docker-compose logs -f backend
```

### 4. Access Your Application
- 🌐 **Frontend**: http://localhost:3000
- 🚀 **Backend API**: http://localhost:8000
- 📚 **API Docs**: http://localhost:8000/docs (Interactive Swagger UI)
- 🗄️ **Database Admin**: http://localhost:5050 (pgAdmin - optional)

## 📚 Learning Path (8-Week Journey)

### Week 1-2: Python & FastAPI Fundamentals
```python
# Your first endpoint
@app.get("/")
async def hello_world():
    return {"message": "Hello, Commute Tracker!"}
```

**Learning Goals:**
- [ ] Set up development environment
- [ ] Create basic FastAPI application
- [ ] Learn Pydantic models for data validation
- [ ] Implement first CRUD endpoints
- [ ] Understand async/await patterns

**Resources:**
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Python Async Programming](https://realpython.com/async-io-python/)

### Week 3-4: Database Integration
```python
# Your first model
class Commute(Base):
    __tablename__ = "commutes"
    id = Column(Integer, primary_key=True)
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    departure_time = Column(DateTime)
```

**Learning Goals:**
- [ ] SQLAlchemy models and relationships
- [ ] Database migrations with Alembic
- [ ] CRUD operations with async sessions
- [ ] Query optimization basics

### Week 5-6: External API Integration
```python
# Google Maps integration
async def calculate_route(origin: str, destination: str):
    async with aiohttp.ClientSession() as session:
        # Your first external API call!
        pass
```

**Learning Goals:**
- [ ] HTTP clients with aiohttp
- [ ] Google Maps API integration
- [ ] Error handling and retries
- [ ] API response caching

### Week 7-8: Data Analysis & Optimization
```python
# Analyze your commute patterns
import pandas as pd

def analyze_commute_patterns(user_commutes):
    df = pd.DataFrame(user_commutes)
    return df.groupby('hour')['duration'].mean()
```

**Learning Goals:**
- [ ] Pandas for data analysis
- [ ] Statistical insights from commute data
- [ ] Route optimization algorithms
- [ ] Data visualization

## 🛠️ Development Commands

```bash
# Start/stop services
docker-compose up -d          # Start in background
docker-compose down           # Stop all services
docker-compose restart backend # Restart specific service

# Development commands
docker-compose exec backend python -m pytest    # Run backend tests
docker-compose exec frontend npm test           # Run frontend tests
docker-compose exec backend black .             # Format Python code
docker-compose exec frontend npm run lint       # Lint frontend code

# Database operations
docker-compose exec backend alembic upgrade head # Run migrations
docker-compose exec db psql -U user commute_tracker # Access database

# View logs
docker-compose logs -f backend   # Backend logs
docker-compose logs -f frontend  # Frontend logs
docker-compose logs -f db        # Database logs
```

## 📁 Project Structure

```
commute-tracker-learning/
├── 📄 README.md                    # You are here!
├── 📄 LEARNING_LOG.md             # Track your daily progress
├── 📄 AI_CODING_GUIDELINES.md     # Best practices for AI-assisted coding
├── 🐳 docker-compose.yml          # Development environment
├── 📁 apps/
│   ├── 📁 backend/                # FastAPI Python application
│   │   ├── 📄 main.py            # Application entry point
│   │   ├── 📁 app/               # Main application code
│   │   ├── 📁 tests/             # Backend tests
│   │   └── 📄 requirements.txt   # Python dependencies
│   └── 📁 frontend/              # React TypeScript application
│       ├── 📁 src/               # Frontend source code
│       ├── 📄 package.json       # Node.js dependencies
│       └── 📄 vite.config.ts     # Build configuration
├── 📁 shared/                     # Shared code and types
├── 📁 docs/                       # Learning documentation
├── 📁 scripts/                    # Utility scripts
└── 📁 data/                       # Sample data
```

## 🤖 AI-Assisted Learning

This project is designed to work excellently with AI coding assistants like:
- **Cursor IDE** - AI-powered code editor
- **GitHub Copilot** - AI pair programmer
- **ChatGPT/Claude** - For explanations and debugging

📖 **Read [AI_CODING_GUIDELINES.md](./AI_CODING_GUIDELINES.md)** for best practices on learning with AI tools.

## 🏆 Learning Milestones

### Beginner (Week 1-2)
- [ ] ✅ Environment setup complete
- [ ] 🐍 First Python FastAPI endpoint working
- [ ] 📊 Understanding Pydantic models
- [ ] 🗄️ Database connection established

### Intermediate (Week 3-4)
- [ ] 🔄 CRUD operations implemented
- [ ] 🧪 First tests written and passing
- [ ] 🗺️ Google Maps integration working
- [ ] 🌐 Frontend talking to backend

### Advanced (Week 5-8)
- [ ] 📈 Data analysis features complete
- [ ] 🚀 Async patterns mastered
- [ ] 🔐 Authentication implemented
- [ ] 📱 Responsive UI completed

## 🌍 Real-World Application

This isn't just a learning project - you're building something useful!

**Features you'll implement:**
- 📍 Track daily commute routes and times
- 📊 Analyze patterns and optimize departure times
- 🚗 Compare different route options
- 📈 Visualize commute data over time
- 🎯 Get smart suggestions for better commuting

## 🆘 Getting Help

### Stuck? Here's how to get help:

1. **Check the logs**:
   ```bash
   docker-compose logs backend
   ```

2. **Common issues**:
   - Port already in use: `sudo lsof -i :8000` then kill the process
   - Docker issues: `docker-compose down && docker-compose up --build`
   - Database connection: Check your `.env` file settings

3. **Learning resources**:
   - 📚 [FastAPI Documentation](https://fastapi.tiangolo.com/)
   - 🐍 [Python.org Tutorial](https://docs.python.org/3/tutorial/)
   - ⚛️ [React Documentation](https://react.dev/)

4. **Community**:
   - Stack Overflow with `fastapi` tag
   - Reddit: r/FastAPI, r/Python, r/reactjs

## 📝 Daily Learning Log

Keep track of your progress in [LEARNING_LOG.md](./LEARNING_LOG.md)

Example daily entry:
```markdown
### Day 1: July 1, 2025
**Time Spent**: 2 hours
**Focus**: Setting up development environment

**What I learned**:
- Docker basics and container orchestration
- FastAPI application structure
- Environment variable management

**Challenges**:
- Docker port conflicts (solved by changing ports)
- Understanding async/await syntax

**Tomorrow's goals**:
- Create first Pydantic model
- Implement basic CRUD endpoint
```

## 🎉 What's Next?

Once you complete this learning project, you'll have:

- ✅ **Portfolio project** to show employers
- ✅ **Modern Python skills** (FastAPI, async, data analysis)
- ✅ **Full-stack capabilities** (backend + frontend)
- ✅ **DevOps knowledge** (Docker, databases)
- ✅ **Real-world experience** with external APIs

**Career paths this prepares you for:**
- Backend Python Developer
- Full-Stack Developer
- Data Engineer
- DevOps Engineer
- API Developer

## 📜 License

This project is for educational purposes. Feel free to use it for learning and share with others who want to learn!

---

**Happy Learning!** 🎓 

*Built with ❤️ for learning Python FastAPI + React TypeScript in 2025*

---

### 🏃‍♂️ Ready to Start?

1. Make sure Docker is running
2. Run `docker-compose up -d`
3. Open http://localhost:3000
4. Start coding and learning!

**Need help?** Check out the [LEARNING_LOG.md](./LEARNING_LOG.md) and [AI_CODING_GUIDELINES.md](./AI_CODING_GUIDELINES.md) for guidance.

# 🚀 Terminal Setup & Aliases Guide

A comprehensive guide to the enhanced terminal setup with useful aliases and productivity tools.

## 📋 Table of Contents

- [Terminal Setup](#terminal-setup)
- [Autocomplete Features](#autocomplete-features)
- [Useful Aliases](#useful-aliases)
- [Python Development](#python-development)
- [Git Workflow](#git-workflow)
- [Docker Commands](#docker-commands)
- [System Utilities](#system-utilities)
- [Development Servers](#development-servers)
- [Quick Reference](#quick-reference)

## 🛠️ Terminal Setup

### Installed Components
- **Shell**: Zsh with Oh My Zsh
- **Theme**: Powerlevel10k
- **Autocomplete**: Enhanced with multiple plugins
- **Syntax Highlighting**: Real-time command validation

### Plugins Installed
```bash
plugins=(
  git
  zsh-autosuggestions
  zsh-syntax-highlighting
  zsh-completions
  docker
  docker-compose
  npm
  node
  python
  pip
  vscode
  history
  sudo
  web-search
)
```

## ✨ Autocomplete Features

### Auto-suggestions
- **Real-time suggestions** based on command history
- **Accept suggestion**: Press `→` (right arrow) or `Ctrl+E`
- **Partial completion**: Type part of a command and press `Tab`

### Enhanced Tab Completion
- **Menu selection**: Use arrow keys to navigate completions
- **Fuzzy matching**: Works with typos and partial matches
- **Case-insensitive**: Commands work regardless of case

### History Search
- **Incremental search**: `Ctrl+R` to search command history
- **Arrow key search**: Up/down arrows search through history

## 🎯 Useful Aliases

### 📁 Directory Navigation
| Alias | Command | Description |
|-------|---------|-------------|
| `..` | `cd ..` | Go up one directory |
| `...` | `cd ../..` | Go up two directories |
| `....` | `cd ../../..` | Go up three directories |
| `~` | `cd ~` | Go to home directory |
| `-` | `cd -` | Go to previous directory |
| `dev` | `cd ~/projects` | Go to projects directory |
| `home` | `cd ~` | Go to home directory |

### 📋 File Operations
| Alias | Command | Description |
|-------|---------|-------------|
| `ll` | `ls -la` | Detailed file listing |
| `la` | `ls -A` | Show hidden files |
| `l` | `ls -CF` | Compact listing |
| `lsd` | `ls -la \| grep '^d'` | List directories only |
| `lsf` | `ls -la \| grep '^-'` | List files only |
| `cp` | `cp -i` | Interactive copy |
| `mv` | `mv -i` | Interactive move |
| `rm` | `rm -i` | Interactive remove |
| `mkdir` | `mkdir -p` | Create directories recursively |

### 🐍 Python Development
| Alias | Command | Description |
|-------|---------|-------------|
| `python` | `python3` | Use Python 3 |
| `pip` | `pip3` | Use pip3 |
| `py` | `python3` | Short for Python 3 |
| `py3` | `python3` | Python 3 |
| `venv` | `python3 -m venv` | Create virtual environment |
| `activate` | `source venv/bin/activate` | Activate virtual environment |

### 🔧 Git Workflow
| Alias | Command | Description |
|-------|---------|-------------|
| `g` | `git` | Git command |
| `ga` | `git add` | Add files |
| `gc` | `git commit` | Commit changes |
| `gp` | `git push` | Push to remote |
| `gl` | `git pull` | Pull from remote |
| `gs` | `git status` | Show status |
| `gd` | `git diff` | Show differences |
| `gco` | `git checkout` | Checkout branch |
| `gcb` | `git checkout -b` | Create and checkout branch |
| `gb` | `git branch` | List branches |
| `glog` | `git log --oneline --graph --decorate` | Pretty git log |
| `gst` | `git stash` | Stash changes |
| `gstp` | `git stash pop` | Pop stash |
| `gac` | `git add . && git commit -m` | Add all and commit |
| `gacp` | `git add . && git commit -m && git push` | Add, commit, and push |
| `gundo` | `git reset --soft HEAD~1` | Undo last commit |
| `gclean` | `git clean -fd` | Clean untracked files |

### 🐳 Docker Commands
| Alias | Command | Description |
|-------|---------|-------------|
| `d` | `docker` | Docker command |
| `dc` | `docker-compose` | Docker Compose |
| `dps` | `docker ps` | List running containers |
| `dpsa` | `docker ps -a` | List all containers |
| `di` | `docker images` | List images |
| `dex` | `docker exec -it` | Execute in container |
| `dlog` | `docker logs` | Show container logs |
| `dcup` | `docker-compose up` | Start services |
| `dcdown` | `docker-compose down` | Stop services |
| `dcbuild` | `docker-compose build` | Build services |
| `dcrestart` | `docker-compose restart` | Restart services |
| `dclogs` | `docker-compose logs -f` | Follow logs |

### ⚡ Quick Commands
| Alias | Command | Description |
|-------|---------|-------------|
| `c` | `clear` | Clear screen |
| `h` | `history` | Show command history |
| `j` | `jobs -l` | List background jobs |
| `k` | `kill -9` | Force kill process |
| `q` | `exit` | Exit terminal |
| `reload` | `source ~/.zshrc` | Reload configuration |
| `refresh` | `source ~/.zshrc` | Reload configuration |

### 🌐 System Utilities
| Alias | Command | Description |
|-------|---------|-------------|
| `myip` | `curl -s https://ipinfo.io/ip` | Show your IP address |
| `weather` | `curl -s wttr.in` | Show weather |
| `speedtest` | Speed test command | Test internet speed |
| `update` | `sudo apt update && sudo apt upgrade -y` | Update system |
| `cleanup` | `sudo apt autoremove && sudo apt autoclean` | Clean packages |
| `ports` | `netstat -tulanp` | Show open ports |
| `ping` | `ping -c 5` | Ping with 5 packets |
| `pingg` | `ping google.com` | Ping Google |

### 📊 System Monitoring
| Alias | Command | Description |
|-------|---------|-------------|
| `top` | `htop` | Better process viewer |
| `mem` | `free -h` | Memory usage |
| `disk` | `df -h` | Disk usage |
| `cpu` | `lscpu \| grep 'Model name'` | CPU information |
| `psg` | `ps aux \| grep` | Search processes |
| `meminfo` | `free -h` | Memory information |
| `cpuinfo` | `lscpu` | CPU information |
| `diskusage` | `df -h` | Disk usage |

### 🌐 Development Servers
| Alias | Command | Description |
|-------|---------|-------------|
| `serve` | `python3 -m http.server 8000` | Python server on 8000 |
| `serve-3000` | `python3 -m http.server 3000` | Python server on 3000 |
| `serve-8080` | `python3 -m http.server 8080` | Python server on 8080 |
| `serve-9000` | `python3 -m http.server 9000` | Python server on 9000 |
| `serve-php` | `php -S localhost:8000` | PHP server |
| `serve-node` | `npx serve .` | Node.js server |
| `serve-python` | `python3 -m http.server` | Python server |
| `serve-ruby` | `ruby -run -e httpd . -p 8000` | Ruby server |

### 📦 Package Management
| Alias | Command | Description |
|-------|---------|-------------|
| `install` | `sudo apt install` | Install packages |
| `remove` | `sudo apt remove` | Remove packages |
| `search` | `apt search` | Search packages |
| `show` | `apt show` | Show package info |

### 🔧 Configuration Files
| Alias | Command | Description |
|-------|---------|-------------|
| `zshconfig` | `code ~/.zshrc` | Edit zsh config |
| `ohmyzsh` | `code ~/.oh-my-zsh` | Edit Oh My Zsh |
| `bashconfig` | `code ~/.bashrc` | Edit bash config |
| `vimconfig` | `code ~/.vimrc` | Edit vim config |
| `gitconfig` | `code ~/.gitconfig` | Edit git config |

### 📅 Utility Functions
| Alias | Command | Description |
|-------|---------|-------------|
| `now` | `date +'%Y-%m-%d %H:%M:%S'` | Current date/time |
| `today` | `date +'%Y-%m-%d'` | Today's date |
| `week` | `date +%V` | Current week number |
| `month` | `date +%B` | Current month |
| `path` | `echo $PATH \| tr ':' '\n'` | Show PATH variable |

### 🛡️ Safety Aliases
| Alias | Command | Description |
|-------|---------|-------------|
| `rm` | `rm -i` | Interactive remove |
| `cp` | `cp -i` | Interactive copy |
| `mv` | `mv -i` | Interactive move |
| `ln` | `ln -i` | Interactive link |

### 🎨 Color and Formatting
| Alias | Command | Description |
|-------|---------|-------------|
| `grep` | `grep --color=auto` | Colored grep |
| `egrep` | `egrep --color=auto` | Colored egrep |
| `fgrep` | `fgrep --color=auto` | Colored fgrep |

## 🚀 Quick Reference

### Most Used Commands
```bash
# Navigation
ll          # List files with details
..          # Go up one directory
dev         # Go to projects directory

# Git workflow
gs          # Git status
ga .        # Add all files
gc -m "message"  # Commit with message
gp          # Push changes
glog        # Pretty git log

# Python development
python      # Use Python 3
pip         # Use pip3
venv        # Create virtual environment
serve       # Start Python server

# System
c           # Clear screen
myip        # Check IP address
weather     # Check weather
update      # Update system

# Docker
dps         # List containers
dcup        # Start services
dcdown      # Stop services
```

### File Operations
```bash
# Safe operations (ask before overwriting)
cp file1 file2    # Interactive copy
mv file1 file2    # Interactive move
rm file           # Interactive remove

# Quick listings
ll                # Detailed listing
lsd               # Directories only
lsf               # Files only
```

### Development Workflow
```bash
# Start a new project
mkdir myproject
cd myproject
venv venv
activate
pip install package_name

# Git workflow
git init
ga .
gc -m "Initial commit"
gp origin main

# Start development server
serve             # Python server on 8000
serve-3000        # Python server on 3000
```

## 📝 Notes

- All aliases are automatically loaded when you start a new terminal
- Use `alias` command to see all available aliases
- Use `reload` or `refresh` to reload configuration after changes
- The setup includes syntax highlighting and auto-suggestions
- Commands are case-insensitive and support fuzzy matching

## 🔧 Customization

To add your own aliases, edit the `.zshrc` file:
```bash
zshconfig    # Opens .zshrc in VS Code
```

Or add them directly:
```bash
echo 'alias myalias="my command"' >> ~/.zshrc
reload
```

---

**Happy coding! 🎉**