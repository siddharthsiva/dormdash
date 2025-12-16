# DormDash 🚀

DormDash is a campus micro-delivery network built for UC San Diego students. It connects dorm residents who need quick items (food, supplies, etc.) with peers willing to fulfill requests. The platform uses gamification (XP, karma, and badges) to make delivery fun, social, and rewarding.

---

## ✨ Features

* 📦 **Request System**
  Students can post requests with item details, dorm location, urgency, and reward.

* 🏠 **Dorm Filtering**
  Browse and filter requests by dorm and completion status.

* 🎮 **Gamification**
  Earn XP and karma points for completing deliveries and helping others.

* 🏅 **Badges**
  Unlock badges like *Speed Demon* or *Campus Hero* based on performance.

* 📊 **Leaderboard**
  View top contributors ranked by XP or karma.

* 📱 **Cross-Platform Frontend**
  React Native app built with Expo, supporting both mobile and web.

* ⚡ **Scalable Backend**
  FastAPI backend with PostgreSQL, designed for performance and extensibility.

---

## 🧱 Project Structure

```
DormDash/
├── backend/                        # FastAPI backend
│   ├── app/
│   │   ├── main.py                 # FastAPI entrypoint
│   │   ├── models/                 # SQLAlchemy models
│   │   │   ├── user.py             # User model (XP, karma, dorm)
│   │   │   ├── request.py          # Request model (item, urgency, reward)
│   │   ├── routers/                # API endpoints
│   │   │   ├── users.py            # User routes (leaderboard, profile)
│   │   │   ├── requests.py         # Request routes (create, list, fulfill)
│   │   ├── services/               # Business logic engines
│   │   │   ├── xp_engine.py        # XP & karma calculation
│   │   │   ├── badge_engine.py     # Badge assignment logic
│   │   ├── schemas/                # Pydantic schemas
│   │   │   ├── user.py             # User request/response schemas
│   │   │   ├── request.py          # Request request/response schemas
│   │   ├── crud/                   # Database operations
│   │   │   ├── user.py             # User CRUD functions
│   │   │   ├── request.py          # Request CRUD functions
│   │   ├── db/
│   │   │   ├── database.py         # SQLAlchemy engine, session, Base
│   │   └── __init__.py             # Marks app as a package
│   ├── requirements.txt            # Python dependencies
│   ├── Dockerfile                  # Container config for Render
│   └── README.md                   # Backend-specific documentation
│
├── frontend/                       # React Native frontend
│   ├── assets/                     # Images, icons, fonts
│   │   └── logo.png
│   ├── components/                 # Reusable UI components
│   │   ├── RequestCard.tsx         # Displays a request
│   │   ├── UserBadge.tsx           # Displays user info + badge
│   ├── screens/                    # App screens
│   │   ├── HomeScreen.tsx          # List of requests
│   │   ├── RequestForm.tsx         # Form to create new request
│   │   ├── Leaderboard.tsx         # Leaderboard view
│   ├── services/                   # API integration
│   │   └── api.ts                  # Axios client + endpoints
│   ├── context/                    # Global state management
│   │   └── AuthContext.tsx         # Authentication context (future expansion)
│   ├── App.tsx                     # Entry point with navigation
│   ├── package.json                # NPM dependencies + scripts
│   ├── babel.config.js             # Babel config for Expo
│   ├── tsconfig.json               # TypeScript config
│   ├── .gitignore                  # Ignore node_modules, build, etc.
│   └── README.md                   # Frontend-specific documentation
│
├── README.md                       # Root project documentation
└── vercel.json                     # Vercel deployment config (frontend)
```

---

## ⚙️ Backend Setup (FastAPI)

1. **Clone the repository and navigate to the backend directory**

   ```bash
   cd backend
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set the database environment variable**

   ```bash
   export DATABASE_URL="postgres://<user>:<password>@<host>:5432/<dbname>?sslmode=require"
   ```

4. **Run the server locally**

   ```bash
   uvicorn app.main:app --reload
   ```

5. **Deploy to Render**

   * Add `DATABASE_URL` to Render environment variables
   * Deploy using the provided `Dockerfile`

---

## ⚙️ Frontend Setup (React Native + Expo)

1. **Navigate to the frontend directory**

   ```bash
   cd frontend
   ```

2. **Install dependencies**

   ```bash
   npm install
   ```

3. **Start the Expo development server**

   ```bash
   npm run start
   ```

4. **Run the app**

   * **Web:** Open [http://localhost:19006](http://localhost:19006)
   * **Mobile:** Scan the QR code using the Expo Go app

---

## 🌐 Deployment

* **Backend:** Hosted on Render (FastAPI + PostgreSQL)
* **Frontend:** Deployed on Vercel for web, Expo Go for mobile testing

---

## 🛠️ Tech Stack

* **Frontend:** React Native, Expo, React Navigation, Axios
* **Backend:** FastAPI, SQLAlchemy, PostgreSQL
* **Hosting:** Render (backend), Vercel (frontend)
* **Gamification:** XP engine, karma engine, badge engine

---

## 🚀 Roadmap

* 🔔 Real-time notifications for new requests
* 🗺️ Map-based view of requests across dorms
* 🤝 Peer-to-peer tipping system
* 🔒 Authentication and UCSD login integration

---

## 👨‍💻 Contributors

**Siddharth Sivalanka**
UC San Diego — Computer Science (Bioinformatics)
Creator of DormDash

Contributions are welcome from UCSD students and beyond.

---

## 📜 License

DormDash is released under the MIT License.
