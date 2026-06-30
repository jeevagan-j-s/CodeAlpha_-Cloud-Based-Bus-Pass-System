# Cloud-Based Bus Pass System

## Project Description

The Cloud-Based Bus Pass System is a web application developed as part of the CodeAlpha Cloud Computing Internship. The system allows users to apply for a bus pass online and securely stores their information in a database. It helps eliminate paper-based processes, reduces the risk of pass loss, and makes bus pass management more efficient.

## Features

* Online bus pass application
* User-friendly interface
* Secure storage of passenger details
* Automatic generation of Bus Pass ID
* View bus pass details
* Database integration using SQLite
* Prevents duplicate records (optional feature)

## Technologies Used

* Python
* Flask
* SQLite
* HTML
* CSS

## Project Structure

```
CodeAlpha_BusPassSystem/
│
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   ├── index.html
│   ├── apply.html
│   └── view.html
└── static/
    └── style.css
```

## How the System Works

1. User opens the application.
2. User fills in the bus pass application form.
3. The application validates the entered details.
4. Passenger information is stored in the database.
5. A unique Bus Pass ID is generated.
6. Users can search and view their bus pass using the generated ID.

## Installation

1. Install Python.
2. Install Flask:

```
pip install flask
```

3. Run the application:

```
python app.py
```

4. Open the browser and visit:

```
http://127.0.0.1:5000
```

## Future Improvements

* User login and authentication
* QR Code enabled bus pass
* Online payment integration
* Email and SMS notifications
* Cloud database integration
* Admin dashboard

## Internship

Project completed as part of the **CodeAlpha Cloud Computing Internship**.

## Author

**Jeevagan**
