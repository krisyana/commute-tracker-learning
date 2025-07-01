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


**Happy coding! 🎉**