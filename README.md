# Playwright with AgentGo

## Introduction

AgentGo provides a powerful platform for developers to seamlessly run, manage, and monitor headless browsers at scale.

Take full control of browsers and harness AgentGo's Distributed Infrastructure, Advanced Stealth Capabilities, and powerful debugging tools to enhance your automation workflows, testing environments, and AI-powered data collection.

**Get up and running in seconds** with Playwright.

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

Alternatively, we suggest using [Poetry](https://python-poetry.org/) to manage your dependencies.

```bash
poetry install
```

### 2. Create `.env` file:

```bash
cp .env.example .env
```

### 3. Get your AgentGo API Key:

- [Create an account](https://www.agentgo.dev/sign-up) or [log in to AgentGo](https://www.agentgo.dev/sign-in)
- Navigate to the Developers section and copy your API Key into the `.env` file

### 4. Run the script:

```bash
python main.py # or poetry run python main.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
