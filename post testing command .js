Invoke-WebRequest -Uri http://localhost:8081/addUser `
  -Method POST `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{"user_name": "John Doe", "user_email": "john@example.com", "user_password": "password123"}'
