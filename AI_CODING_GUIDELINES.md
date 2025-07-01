# 🤖 AI Coding Guidelines

Best practices for using AI coding assistants like Cursor, GitHub Copilot, and ChatGPT effectively while learning Python and web development.

## 🎯 Core Principles

### 1. Use AI as a Learning Partner, Not a Crutch
- **DO**: Ask AI to explain concepts and patterns
- **DON'T**: Copy-paste code without understanding
- **PRACTICE**: Always try to implement first, then ask for help

### 2. Progressive Learning Approach
```python
# ❌ Bad: Asking AI to build entire feature
"Build a complete user authentication system with FastAPI"

# ✅ Good: Learning step by step
"Explain how password hashing works in Python"
"Show me a simple Pydantic model for user registration"
"How do I validate JWT tokens in FastAPI?"
```

## 🎨 Effective Prompt Engineering

### For Learning Python Concepts
```
Template: "I'm learning [CONCEPT]. Can you:
1. Explain [CONCEPT] in simple terms
2. Show a basic example
3. Explain what each line does
4. Give me a small exercise to practice"

Example:
"I'm learning SQLAlchemy relationships. Can you:
1. Explain one-to-many relationships in simple terms
2. Show a basic example with User and Post models
3. Explain what each line does
4. Give me a small exercise to practice"
```

### For Code Review and Improvement
```python
# When asking for code review
"Please review this Python function. Focus on:
- Code readability and Python best practices
- Potential bugs or edge cases
- Performance improvements
- How to make it more Pythonic

[YOUR CODE HERE]"
```

### For Debugging
```python
# Effective debugging prompts
"I'm getting this error: [ERROR MESSAGE]
In this code: [CODE SNIPPET]
I think the issue might be [YOUR HYPOTHESIS]
Can you help me understand what's wrong and how to fix it?"
```

## 🔧 Cursor IDE Best Practices

### 1. Context Management
```typescript
// Use clear, descriptive comments for context
// TODO: Implement user authentication middleware
// LEARNING: This function handles JWT token validation

// Add type hints for better AI suggestions
async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    # AI will better understand the context with type hints
```

### 2. Effective Use of Chat
```bash
# Good chat prompts in Cursor
"Explain this FastAPI decorator @app.post and how it works"
"What's the difference between async def and def in Python?"
"How can I improve this database query for better performance?"

# Instead of just asking for code
"Write me a complete API endpoint"
```

### 3. Code Generation Best Practices
- Use Ctrl+K for inline code generation
- Provide context in comments before generating
- Review and understand generated code before accepting
- Test generated code thoroughly

## 📚 Learning-Focused AI Usage

### Phase 1: Python Fundamentals
```python
# Ask AI to explain concepts, not write code
"What are Python type hints and why should I use them?"
"Explain the difference between sync and async functions"
"How does FastAPI automatic validation work?"

# Then practice implementing yourself
```

### Phase 2: Database Integration
```python
# Good learning prompts
"Walk me through creating a SQLAlchemy model step by step"
"Explain database relationships with a simple example"
"What are database migrations and how do they work?"

# Practice with variations
"Now help me create a similar model for [YOUR DOMAIN]"
```

### Phase 3: API Integration
```python
# Understanding-focused questions
"Explain how async HTTP requests work in Python"
"What's the difference between aiohttp and requests?"
"How should I handle API errors and retries?"

# Then implement with guidance
"I'm trying to implement [SPECIFIC FEATURE], can you guide me through the steps?"
```

## 🧪 Testing with AI

### Writing Tests
```python
# Instead of: "Write tests for this function"
# Ask: "What should I test in this function and why?"

def test_commute_calculation():
    """
    AI helped me understand I should test:
    - Valid input handling
    - Edge cases (zero duration, invalid coordinates)
    - Error conditions
    - Return value format
    """
    pass
```

### Test-Driven Development
```python
# Good approach: Ask AI to help design tests first
"I want to implement a route optimization function. 
What test cases should I consider before writing the code?"

# Then implement tests, then function
```

## 🐛 Debugging Strategies

### 1. Systematic Debugging
```python
# Provide full context to AI
"""
Error: [FULL ERROR MESSAGE]
Context: [What you were trying to do]
Code: [RELEVANT CODE SNIPPET]
Environment: [Python version, dependencies]
What I've tried: [Your debugging attempts]
"""
```

### 2. Learning from Errors
```python
# Don't just ask for fixes, ask for understanding
"This error occurs when [SITUATION]. Can you explain:
1. Why this error happens
2. How to fix it
3. How to prevent it in the future
4. What this teaches me about Python/FastAPI"
```

## 📖 Documentation and Comments

### Self-Documenting Code with AI
```python
# Ask AI to help improve your documentation
"""
Can you help me improve the documentation for this function?
Current: [YOUR CODE]
Please suggest:
- Better docstring
- Clearer variable names
- Helpful comments
- Type hints
"""
```

### Learning-Oriented Comments
```python
# Write comments that show your learning
async def get_user_commutes(user_id: int, db: Session):
    """
    LEARNING: Using dependency injection for database session
    LEARNING: async/await for non-blocking database operations
    """
    result = await db.execute(
        select(Commute).where(Commute.user_id == user_id)
    )
    return result.scalars().all()
```

## 🎯 Project-Specific Guidelines

### For This Commute Tracker Project

#### Phase-by-Phase AI Usage
```python
# Phase 1: Basic FastAPI
"Help me understand how FastAPI routing works"
"Explain Pydantic models with a commute tracking example"

# Phase 2: Database
"Guide me through setting up SQLAlchemy with FastAPI"
"How do I handle database sessions properly?"

# Phase 3: External APIs
"Best practices for integrating Google Maps API"
"How to handle API errors gracefully"

# Phase 4: Data Analysis
"Introduction to Pandas for commute data analysis"
"How to create meaningful insights from time-series data"
```

## 🚫 What NOT to Do

### Avoid These AI Usage Patterns
- ❌ Copying large code blocks without understanding
- ❌ Asking AI to complete entire features
- ❌ Not testing AI-generated code
- ❌ Using AI to bypass learning fundamentals
- ❌ Not asking follow-up questions when confused

### Instead, Do This
- ✅ Ask for explanations and examples
- ✅ Request step-by-step guidance
- ✅ Seek help with specific problems
- ✅ Use AI to validate your understanding
- ✅ Ask for code review and improvement suggestions

## 📊 Track Your Learning

### Keep a Learning Journal
```markdown
## Date: 2024-XX-XX
### What I Learned Today
- [Concept/skill learned]
- [How AI helped in the learning process]
- [What I implemented myself]

### Questions I Asked AI
- [Question 1 and what I learned from the answer]
- [Question 2 and follow-up insights]

### Code I Wrote
- [Brief description of code written]
- [What worked well]
- [What I need to improve]

### Tomorrow's Goals
- [Specific learning objectives]
- [How I plan to use AI to support learning]
```

## 🎓 Remember

AI is a powerful learning tool when used correctly. The goal is to:
1. **Understand** the concepts deeply
2. **Practice** implementing solutions
3. **Learn** from AI guidance
4. **Build** real skills that transfer beyond this project

---

Use AI to accelerate your learning, not replace it! 🚀