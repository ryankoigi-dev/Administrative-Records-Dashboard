# 📊 Administrative Records Dashboard

## Overview

The **Administrative Records Dashboard** is a centralized web-based system designed to support efficient management, tracking, and monitoring of administrative records within an organization. The dashboard provides real-time insights into records status, movement, compliance, and performance, enabling informed decision-making and improved accountability.

The system is tailored for registries, records offices, and administrative units handling both **physical and electronic records**.

---

## Key Features

### 📁 Records Management

* Create, view, update, and archive administrative records
* Categorization by **institution, subject, department, and year**
* Unique record identifiers for easy retrieval
* Support for both **incoming and outgoing records**

### 🔄 File Movement Tracking

* Track file issuance and return
* Log requesting officer, date issued, due date, and folio number
* Automated flags for **overdue files**
* Complete audit trail of file movement history

### 📈 Dashboard Analytics

* Total records count (active, closed, archived)
* Daily, monthly, and yearly activity summaries
* Overdue files and pending actions visualization
* Department-wise and category-wise statistics

### 🔍 Search & Filtering

* Advanced search by subject, institution, reference number, or date
* Filter records by status (active, pending, overdue, archived)
* Quick access to frequently used records

### 🔐 Security & Access Control

* User authentication and role-based access (Admin, Registry Staff, Viewer)
* Activity logging for accountability
* Data protection and access restriction policies

### 📂 Document Upload & Storage

* Upload scanned copies of letters and documents
* Secure digital storage linked to each record
* Easy preview and download functionality

---

## System Architecture

The dashboard follows a **client–server architecture**:

* **Frontend:** User interface for record entry, tracking, and visualization
* **Backend:** Handles business logic, authentication, and data processing
* **Database:** Stores records metadata, users, logs, and file movement data

---

## Technologies Used *(customizable)*

* **Frontend:** HTML, CSS, JavaScript (Bootstrap / React optional)
* **Backend:** Python (Flask/Django) or PHP / Node.js
* **Database:** MySQL / PostgreSQL / SQLite
* **Authentication:** Role-based access control
* **Hosting:** Local server or cloud deployment

---

## Installation & Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/administrative-records-dashboard.git
   ```
2. Navigate to the project directory:

   ```bash
   cd administrative-records-dashboard
   ```
3. Configure the database settings in the environment file
4. Run database migrations / setup scripts
5. Start the application server
6. Access the dashboard via browser at:

   ```
   http://localhost:8000
   ```

---

## User Roles

| Role           | Permissions                                  |
| -------------- | -------------------------------------------- |
| Admin          | Full system access, user management, reports |
| Registry Staff | Record creation, updates, file tracking      |
| Viewer         | Read-only access to records and reports      |

---

## Use Cases

* Registry file tracking and accountability
* Monitoring overdue files and follow-ups
* Supporting digitization and records automation
* Enhancing transparency in administrative operations
* Compliance with records management policies

---

## Future Enhancements

* Email/SMS notifications for overdue files
* Integration with EDRMS
* Automated retention and disposal scheduling
* Advanced reporting and export (PDF/Excel)
* API integration with other MIS systems

---

## Contribution

Contributions are welcome. Fork the repository, create a feature branch, and submit a pull request for review.

---

## License

This project is developed for educational and administrative purposes. Licensing can be modified based on institutional requirements.

---

## Author

Ryan Koigi Njuguna

BSc Records Management & Information Technology

Kenyatta University
