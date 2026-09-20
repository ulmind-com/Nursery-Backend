<div align="center">

# 🌿 Nursery Backend

### Premium Plant E-Commerce API · FastAPI + MongoDB + AI-Powered

[![Python](https://img.shields.io/badge/Python-3.13+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.141-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://mongodb.com)
[![UV](https://img.shields.io/badge/UV-Package_Manager-7C3AED?style=for-the-badge)](https://docs.astral.sh/uv/)
[![License](https://img.shields.io/badge/License-Private-ef4444?style=for-the-badge)]()

<br/>

<img src="https://img.shields.io/badge/🌱_Plant_Nursery-E--Commerce_Backend-16a34a?style=for-the-badge&labelColor=064e3b" alt="Plant Nursery" />

<br/><br/>

*A production-grade REST API for a premium online plant nursery — featuring AI-powered plant recommendations, intelligent customer support chatbot, real-time restock notifications, and comprehensive order management.*

</div>

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🌿 Plant Management
- Full CRUD with **PlantSpec** metadata (sunlight, watering, difficulty, soil type, temperature)
- **Size variants** — Small/Medium/Large with pot types (Ceramic, Terracotta, GraPot)
- Plant badges: 🐾 Pet Safe · 💨 Air Purifying · 💊 Medicinal · 🌸 Flowering
- Advanced filters (plant_type, sunlight, difficulty, pet_safe, air_purifying)
- Full-text search on title, description, scientific name

</td>
<td width="50%">

### 🤖 AI-Powered
- **Sage 🌿** — AI customer support + plant care assistant (Groq/Llama 3.3)
- **Smart Recommendations** — LLM re-ranker considers care compatibility, sunlight needs, and complementary plants
- Plant care advice: watering schedules, sunlight, repotting, pest control
- 30-day plant guarantee information

</td>
</tr>
<tr>
<td>

### 📦 Orders & Payments
- **Razorpay** integration (UPI, Cards, Netbanking)
- Order lifecycle management (placed → confirmed → shipped → delivered)
- Gift wrapping & messages
- PDF invoice generation
- Weight-based delivery fee calculator
- Pan-India shipping with state-based pricing

</td>
<td>

### 🔔 Smart Notifications
- **Restock waitlist** — auto-email when out-of-stock size variants return
- Push notifications via **Firebase**
- Scheduled notification system with background sweeper
- Google Business review sync

</td>
</tr>
</table>

---

## 🏗️ Architecture

```
app/
├── core/           # Config, security, JWT
├── db/             # MongoDB connection + indexes
├── models/         # Pydantic schemas
│   ├── product.py  # PlantSpec, SizeVariant, ProductCreate
│   ├── order.py    # OrderItem, Gift support
│   ├── settings.py # PlantGuarantee, NurseryConfig
│   └── ...
├── routers/        # API endpoints
│   ├── products.py # Plant CRUD + advanced filters
│   ├── orders.py   # Order management
│   ├── waitlist.py # Restock notifications
│   └── ...
└── services/       # Business logic
    ├── agent.py    # Sage 🌿 AI chat assistant
    ├── recommender.py  # LLM recommendation re-ranker
    ├── pricing.py  # Size-variant pricing engine
    └── ...
```

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.13+**
- **UV** package manager (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
- **MongoDB Atlas** account (or local MongoDB)

### Setup

```bash
# 1. Clone & install
git clone https://github.com/ulmind-com/Nursery-Backend.git
cd Nursery-Backend
uv sync

# 2. Configure environment
cp .env.example .env
# Edit .env with your MongoDB URI, Cloudinary, Razorpay & Groq keys

# 3. Run
uv run uvicorn app.main:app --reload --port 8000
```

### API Docs
Once running, visit:
- **Swagger UI** → `http://localhost:8000/docs`
- **ReDoc** → `http://localhost:8000/redoc`
- **Health Check** → `http://localhost:8000/`

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/products` | List plants with filters (plant_type, sunlight, difficulty, pet_safe, etc.) |
| `GET` | `/products/{id}` | Plant detail with computed pricing |
| `POST` | `/products` | Create plant (admin) |
| `PATCH` | `/products/{id}` | Update plant (admin, triggers restock alerts) |
| `GET` | `/categories` | Plant categories |
| `POST` | `/orders` | Place order |
| `POST` | `/auth/login` | Admin/user login |
| `POST` | `/waitlist` | Join restock waitlist |
| `POST` | `/chat/reply` | Talk to Sage 🌿 AI assistant |
| `GET` | `/recommendations/{id}` | AI-powered plant recommendations |

<details>
<summary><b>📋 Full endpoint list (20+ routes)</b></summary>

| Route Group | Endpoints |
|-------------|-----------|
| Auth | `/auth/login`, `/auth/register`, `/auth/firebase` |
| Products | CRUD + `/admin/low-stock` |
| Categories | CRUD with parent/child |
| Orders | CRUD + `/webhook/razorpay` |
| Waitlist | Join + `/admin/summary` + `/admin/{id}/resolve` |
| Combos | Plant bundles CRUD |
| Coupons | Discount code management |
| Reviews | Customer review moderation |
| Blog | Plant care articles CMS |
| Banners | Storefront banner management |
| Home Sections | Drag-and-drop layout |
| Settings | Store config + plant guarantee |
| Analytics | Revenue, orders, product stats |
| Chat | AI assistant conversations |
| Upload | Cloudinary image upload |

</details>

---

## 🗺️ Roadmap

| Phase | Feature | Status |
|-------|---------|--------|
| **v1.0** | Core plant CRUD + size variants | ✅ Done |
| **v1.0** | AI recommendations + Sage chat | ✅ Done |
| **v1.0** | Razorpay payments | ✅ Done |
| **v1.0** | Restock waitlist notifications | ✅ Done |
| **v1.1** | Plant care schedule reminders | 🔜 Planned |
| **v1.1** | Subscription / auto-repot service | 🔜 Planned |
| **v1.2** | Seasonal plant collections | 🔜 Planned |
| **v1.2** | Plant health diagnosis (AI + images) | 🔜 Planned |
| **v2.0** | Multi-vendor nursery marketplace | 📋 Backlog |
| **v2.0** | AR plant placement preview | 📋 Backlog |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Runtime** | Python 3.13 + UV |
| **Framework** | FastAPI 0.141 |
| **Database** | MongoDB Atlas (Motor async driver) |
| **Auth** | JWT + Firebase Auth + Google/Facebook OAuth |
| **Payments** | Razorpay (UPI, Cards, Netbanking) |
| **Storage** | Cloudinary (images, videos) |
| **AI** | Groq (Llama 3.3 70B) |
| **Email** | Resend (transactional) |
| **Push** | Firebase Cloud Messaging |

---

## 📝 Environment Variables

```env
# Required
MONGO_URI=mongodb+srv://...
CLOUDINARY_CLOUD_NAME=...
CLOUDINARY_API_KEY=...
CLOUDINARY_API_SECRET=...
RAZORPAY_KEY_ID=...
RAZORPAY_KEY_SECRET=...
GROQ_API_KEY=...

# Optional
JWT_SECRET=your-secret
RESEND_API_KEY=...
FIREBASE_CREDENTIALS=...
```

See [`.env.example`](.env.example) for the full list.

---

<div align="center">

**Built with 💚 for plant lovers**

*[ulmind-com](https://github.com/ulmind-com)*

</div>
