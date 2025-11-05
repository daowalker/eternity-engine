# ✨ EternityEngine: World Simulation Vision

This document defines the **core concepts**, **structures**, and **mechanics** behind the EternityEngine simulation system. It serves as a reference point for development and a foundation for future contributors.

---

## 🧘 1. Cultivators

Each Cultivator is a dynamic entity with multiple possible development paths.

### Core Attributes:
- `name`: name of the cultivator  
- `age`: current age in years  
- `race`: biological or spiritual origin (e.g. Human, Demon, Beast, Construct)

### Cultivation Realms:
A cultivator may follow **multiple cultivation paths in parallel**, each with its own realm and progress:

```json
{
  "Body": { "tier": "Core Formation", "sublevel": "Peak", "progress": 85 },
  "Soul": { "tier": "Foundation", "sublevel": "Mid", "progress": 20 }
}
```

- Each **path** (e.g., Body, Soul, Yin-Yang, Bloodline) develops independently.
- **Breakthrough progress** is tracked per path.
- Realms have **tiers** (e.g. Foundation, Core Formation) and optional **sublevels** (e.g. Early, Mid, Peak).

### Qi Types:
Cultivators can hold different kinds of Qi at the same time:
```json
{
  "Dragon Qi": 120,
  "Nature Qi": 45
}
```

- Types include: *Dragon Qi*, *Body Qi*, *Nature Qi*, *Yin Qi*, *Chaotic Qi*, etc.
- Each type fuels different techniques and paths.

### Additional:
- `lifespan`: max years before death unless ascended  
- `techniques`: known cultivation methods or arts  
- `affiliation`: current sect or clan (optional)

---

## 🗺️ 2. World Structure

The world in EternityEngine is composed of interconnected regions, factions, and special locations. It is designed to be modular, dynamic, and rich in flavor — suitable for both simulation and narrative.

---

### 🌍 Regions

Large zones that influence cultivation, exploration, and survival.

#### Properties:
- **Qi Density**: how much Qi is available — Low / Medium / High / Chaotic
- **Qi Types**: multiple types can coexist (e.g. Fire Qi, Nature Qi, Yin Qi)
- **Danger Level**: threat level from beasts, cultivators, or corruption
- **Time Dilation** *(optional)*: time may flow faster or slower here
- **Attributes**: visual and symbolic flavor — like “foggy, moonlit, cursed ground”
- **Currency** *(optional)*: local trade tokens or sect-based currency

---

### 🏯 Factions

Factions are organized groups with power, doctrine, and influence.

#### Types:
- **Sect** – spiritual hierarchy
- **Clan** – bloodline-based power
- **School** – public cultivation institution
- **Cult** – heretical or forbidden doctrine
- **City-States / Freeholds** – autonomous strongholds

#### Features:
- Internal **hierarchy** (e.g. Disciple → Elder → Patriarch)
- Unique **doctrines**, forbidden arts
- **Reputation system**
- May control **cities** or **regions**
- May use **own currency**

---

### 🏞️ Places (Local Sites)

Specialized, smaller-scale locations:
- *Spiritual Caves*, *Forbidden Zones*, *Ancient Ruins*, *Hidden Cities*, *Mirror Realms*

> Structure will be defined during implementation — conceptually, they are key points of interest.

---

### 🪐 World Layers / Realms

The world contains many **planes of existence**, not strictly vertical.

Examples:
- **Mortal Realm**
- **Spirit World**
- **Celestial Domain**
- **Abyssal Plane**
- **Dream / Mental Realms**
- **Pocket Realms**

Connections may be spatial, conditional, or narrative (e.g. accessed only via ritual or tribulation).

---

## ⚡ 3. Realms and Breakthroughs

Cultivation is divided into **realms** — stages of power and understanding.

### Realm Structure:
- `tier`: e.g. Foundation → Core → Nascent Soul → Ascension → Immortal
- `sublevel`: e.g. Early → Mid → Peak
- `progress`: % toward breakthrough

---

### 🔄 Breakthrough Mechanics

To breakthrough, cultivators must accumulate:
- Qi
- Time
- Conditions (location, items, fate, etc.)

Outcomes:
- Success → level up
- Failure → injury, death, Qi deviation
- Deviation → corruption, altered path

---

### ☯️ Non-Linear Paths

- Cultivators may pursue **multiple paths in parallel**
- Paths can **synergize** or **conflict**
- Some breakthroughs require progress in multiple paths
- Rare combinations unlock **hybrid states**

---

## ⏳ 4. Time and Simulation

EternityEngine runs on a **tick-based loop**. Each tick simulates:

### Tick flow:
1. **Cultivator Actions** (meditate, travel, duel)
2. **World State Update** (Qi, factions, resources)
3. **Event Processing**
4. **Aging / Lifespan check**
5. **Passive Gains** (Qi, realm progress, karma)

---

### AI-Driven Behavior:
- Each entity has a **behavior profile**
- Actions can emerge from priorities + context
- Enables generational, large-scale simulations

---

## 📜 5. Events System

Events are the heartbeat of EternityEngine. They may be:

- Personal (Breakthrough, Internal Conflict)
- World-scale (Sect War, City Falls)
- Exploration (Secret Realm Opens)
- Cosmic (Heavenly Tribunal, Karmic Reversal)

Events can:
- Be chained (war → famine → rebellion)
- Emerge from world state (e.g. too much Yin Qi = beast awakening)
- Be hidden or visible
- Affect individuals, regions, or the whole world

Each event includes:
- **Trigger**, **Participants**, **Outcome logic**, **Aftermath**

---

📌 **This file is not technical documentation.**  
It is a world-building and design vision — a conceptual foundation for what EternityEngine *can* become.
