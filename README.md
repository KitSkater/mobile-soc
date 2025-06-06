# Mobile SOC - Lifelong Security Operations Center

This repository contains the initial work-in-progress code and architecture for a **Mobile Security Operations Center (SOC)** system designed to run fully on a local machine (e.g., laptop, Raspberry Pi). 

---

## ⚠️ Warning: Work in Progress

This project is **NOT functional yet**. It is currently under active development.  
Expect incomplete code, missing features, and possible bugs.  

Use at your own risk. Contributions and feedback are welcome!

---

## Project Overview

The goal is to build a **portable, lightweight SOC** with two main parts:

1. **Local Backend Agent**  
   - Collects and analyzes logs from system and network sources  
   - Detects basic threats (e.g., SSH brute force, suspicious web activity)  
   - Stores alerts in a local database  
   - Exposes a REST API for querying alerts  

2. **Web Dashboard**  
   - Hosted on the same device  
   - Accessible via local network browser  
   - Displays real-time alerts and logs  
   - Allows filtering, search, and basic authentication  

---

## Tech Stack (Planned)

- **Backend:** Python, Flask or FastAPI  
- **Database:** SQLite  
- **Frontend:** HTML, CSS, JavaScript  
- **OS:** Linux (Ubuntu recommended)  

---

## Current Status

- Architecture planning completed  
- Backend code scaffold in progress  
- Web dashboard design upcoming  

---

## Getting Started

*Instructions will be added once the backend and frontend are functional.*

---

## Contributing

Contributions are welcome! Please open issues or pull requests.

---

## License

MIT License

---

## Contact

For questions or collaboration ideas, reach out!

