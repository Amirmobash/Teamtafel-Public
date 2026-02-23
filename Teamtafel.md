**Teamtafel** is a powerful WPF-based workforce management dashboard for planning shifts, tracking absences, managing tasks, and generating reports — all in a clean, modern interface. Designed for small to medium teams, it supports multi-device workflows via a shared JSON data folder.

## 🚀 Features
- **Employee Management** – Add, edit, delete employees, assign roles, and optionally add photos.
- **Shift Planning** – Morning/evening shifts with configurable capacity, drag‑and‑drop assignment, shift swapping, and clearing.
- **Absence Tracking** – Categorize absences (vacation, sick leave, etc.), view daily absence lists, and prevent absent employees from being assigned shifts.
- **Task Management** – Create tasks, track status (Pending / In Progress / Completed), assign employees, and add progress notes.
- **Reporting** – Generate daily/weekly/monthly reports with printable previews.
- **Sync & Shared Data** – All data stored as JSON in a configurable folder; sync manager detects external changes and reloads safely.

## 🛠 Tech Stack
- **.NET (WPF)** – `net8.0-windows`
- **C#**
- **Newtonsoft.Json** – for JSON serialization
- **Microsoft.Extensions.Logging**

## 📁 Project Structure
- `ManagementApp` – Core UI for employees, shifts, absences, tasks, reports, and settings.
- `DisplayApp` – Insight layer with AI recommendations, dashboards, and visual summaries.
- `Shared` – Common models, services, JSON helpers, date utilities, and sync logic.

## 💾 Data Storage
All data is saved as JSON files in a user‑configurable directory (default: `Data`). Point the app to a shared network folder to enable seamless multi‑device usage.

## 🏁 Getting Started
1. Clone the repo:  
   `git clone https://github.com/amirmobash/Teamtafel.git`
2. Open the solution in Visual Studio 2022+.
3. Build and run.

---

**🔍 Find me on GitHub:**  
[github.com/amirmobash](https://github.com/amirmobash)

---

### Hashtags
#WPF #CSharp #DotNet #WorkforceManagement #ShiftPlanning #EmployeeScheduling #AbsenceTracking #TaskManagement #Reporting #OpenSource #SmallBusiness #TeamProductivity #DesktopApp #JSON #Sync #GitHub #AmirMobasheraghdam #Teamtafel
