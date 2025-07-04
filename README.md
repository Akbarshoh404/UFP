# Uzbekistan Freelancing Platform

The **Uzbekistan Freelancing Platform** is a Flask-based backend application designed to connect freelancers and clients in Uzbekistan. It provides features for managing users, projects, proposals, contracts, payments, messages, and admin tasks. The application uses PostgreSQL as its database and is deployable to platforms like Heroku using `gunicorn`.

## Features
- **User Management**: Register and manage freelancers, clients, and admins with roles and profiles.
- **Project Posting**: Clients can post projects with details like budget, duration, and category.
- **Proposals**: Freelancers can submit proposals for projects, including cover letters and proposed rates.
- **Contracts**: Create and manage contracts between clients and freelancers.
- **Payments**: Track payments for contracts with statuses (pending, paid, failed).
- **Messaging**: Enable communication between users via messages.
- **Admin Controls**: Admins can manage users and projects with specific permissions.
- **RESTful API**: Exposes endpoints for all functionalities, with JSON responses.

## Technologies
- **Backend**: Flask 3.0.3
- **Database**: PostgreSQL (with Flask-SQLAlchemy 3.1.1)
- **Deployment**: Gunicorn 23.0.0, Heroku-compatible
- **Other Libraries**: Flask-Cors 5.0.0, psycopg2-binary 2.9.9, python-dotenv 1.0.1, Werkzeug 3.0.4

## Project Structure
```
uzbekistan-freelancing-platform/
├── app.py                # Main Flask application
├── config.py             # Configuration settings
├── models.py             # Database models and enums
├── requirements.txt      # Python dependencies
├── Procfile              # Deployment command for Heroku
├── schema.txt            # Database schema with example JSON objects
├── routes/
│   ├── user_routes.py    # User management endpoints
│   ├── project_routes.py # Project management endpoints
│   ├── proposal_routes.py# Proposal management endpoints
│   ├── contract_routes.py# Contract management endpoints
│   ├── payment_routes.py # Payment management endpoints
│   ├── message_routes.py # Messaging endpoints
│   ├── admin_routes.py   # Admin management endpoints
├── .env                 # Environment variables (not committed)
```

## Database Schema
The application uses the following models, detailed in `schema.txt`:
- **User**: Represents freelancers, clients, or admins (e.g., `{"id": 1, "name": "John Doe", "email": "john@example.com", ...}`).
- **Project**: Projects posted by clients (e.g., `{"id": 1, "title": "E-commerce Website", "budget": 1000.0, ...}`).
- **Proposal**: Bids by freelancers (e.g., `{"id": 1, "projectId": 1, "freelancerId": 2, ...}`).
- **Contract**: Agreements between clients and freelancers (e.g., `{"id": 1, "projectId": 1, "agreedRate": 950.0, ...}`).
- **Payment**: Payments for contracts (e.g., `{"id": 1, "contractId": 1, "amount": 950.0, ...}`).
- **Message**: Messages between users (e.g., `{"id": 1, "senderId": 2, "text": "Discuss timeline", ...}`).
- **Admin**: Admin users with permissions (e.g., `{"id": 1, "email": "admin@example.com", "permissions": ["manage_users"], ...}`).

See `schema.txt` for full details, including field types, constraints, and example JSON objects.

## Setup Instructions

### Prerequisites
- Python 3.9+ (3.12 recommended)
- PostgreSQL 13+
- Git
- (Optional) Docker for containerized deployment
- (Optional) Heroku CLI for Heroku deployment

### Local Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/uzbekistan-freelancing-platform.git
   cd uzbekistan-freelancing-platform
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up PostgreSQL**:
   - Install PostgreSQL and create a database:
     ```bash
     createdb uzbek_freelancing_db
     ```
   - Create a `.env` file in the project root with:
     ```
     DATABASE_URL=postgresql://username:password@localhost:5432/uzbek_freelancing_db
     PORT=5000
     ```

5. **Run the Application**:
   ```bash
   python app.py
   ```
   The server will start at `http://localhost:5000`.

6. **Test with Gunicorn**:
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

### Docker Setup
1. **Build the Docker Image**:
   ```bash
   docker build -t uzbek-freelancing-platform .
   ```

2. **Run the Container**:
   ```bash
   docker run -p 5000:5000 -e DATABASE_URL=postgresql://username:password@host:5432/uzbek_freelancing_db uzbek-freelancing-platform
   ```

### Heroku Deployment
1. **Create a Heroku App**:
   ```bash
   heroku create your-app-name
   ```

2. **Add PostgreSQL**:
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

3. **Deploy the Application**:
   ```bash
   git push heroku main
   ```

4. **Set Environment Variables**:
   ```bash
   heroku config:set DATABASE_URL=$(heroku config:get DATABASE_URL)
   ```

5. **Check Logs**:
   ```bash
   heroku logs --tail
   ```

## API Endpoints
The API is RESTful and returns JSON responses. All endpoints are prefixed with their respective resource names.

### User Endpoints
- `GET /users`: List all users
- `POST /users`: Create a user (e.g., `{"name": "John Doe", "email": "john@example.com", "password": "secure123", "role": "freelancer"}`)
- `GET /users/<id>`: Get a user by ID
- `PUT /users/<id>`: Update a user (full update)
- `PATCH /users/<id>`: Update a user (partial update)
- `DELETE /users/<id>`: Delete a user

### Project Endpoints
- `GET /projects`: List all projects
- `POST /projects`: Create a project (e.g., `{"title": "E-commerce Website", "clientId": 1, "budget": 1000.0}`)
- `GET /projects/<id>`: Get a project by ID
- `PUT /projects/<id>`: Update a project
- `DELETE /projects/<id>`: Delete a project

### Proposal Endpoints
- `GET /proposals`: List all proposals
- `POST /proposals`: Create a proposal (e.g., `{"projectId": 1, "freelancerId": 2, "proposedRate": 900.0}`)
- `GET /proposals/<id>`: Get a proposal by ID
- `PUT /proposals/<id>`: Update a proposal
- `DELETE /proposals/<id>`: Delete a proposal

### Contract Endpoints
- `GET /contracts`: List all contracts
- `POST /contracts`: Create a contract (e.g., `{"proposalId": 1, "clientId": 1, "freelancerId": 2, "totalAmount": 950.0}`)
- `GET /contracts/<id>`: Get a contract by ID
- `PUT /contracts/<id>`: Update a contract
- `DELETE /contracts/<id>`: Delete a contract

### Payment Endpoints
- `GET /payments`: List all payments
- `POST /payments`: Create a payment (e.g., `{"contractId": 1, "amount": 950.0, "method": "Bank Transfer"}`)
- `GET /payments/<id>`: Get a payment by ID
- `PUT /payments/<id>`: Update a payment
- `DELETE /payments/<id>`: Delete a payment

### Message Endpoints
- `GET /messages`: List all messages
- `POST /messages`: Create a message (e.g., `{"senderId": 2, "receiverId": 1, "text": "Discuss timeline"}`)
- `GET /messages/<id>`: Get a message by ID
- `DELETE /messages/<id>`: Delete a message

### Admin Endpoints
- `GET /admins`: List all admins
- `POST /admins`: Create an admin (e.g., `{"email": "admin@example.com", "password": "admin123", "permissions": ["manage_users"]}`)
- `GET /admins/<id>`: Get an admin by ID
- `PUT /admins/<id>`: Update an admin
- `DELETE /admins/<id>`: Delete an admin

### Debug Endpoint
- `GET /routes`: List all registered API routes

## Testing the API
Use tools like Postman or `curl` to test endpoints. Example:
```bash
curl -X POST http://localhost:5000/users -H "Content-Type: application/json" -d '{"name":"John Doe","email":"john@example.com","password":"secure123","role":"freelancer"}'
```

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## Issues
If you encounter issues (e.g., import errors, deployment failures), check the following:-
- Ensure `routes/proposal_routes.py` and other route files are in the `routes/` directory.
- Verify `DATABASE_URL` is set correctly in `.env` or Heroku config.
- Check logs for detailed errors (`heroku logs --tail` or `docker logs <container>`).

Report issues on the [GitHub Issues page](https://github.com/your-username/uzbekistan-freelancing-platform/issues).

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or support, contact [your-email@example.com](mailto:your-email@example.com) or open an issue on GitHub.