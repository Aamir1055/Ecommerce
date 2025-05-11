# Ecommerce
Ecommerce Backend
🛒 Django E-Commerce API
This project is a backend RESTful API for an e-commerce platform built with Django, Django REST Framework, and MySQL (via XAMPP). It supports buyers and sellers, allowing user registration, product management, order placement, and role-based access.

📁 Project Structure
bash
Copy
Edit
ecommerce_site/
├── ecommerce_site/      # Django project settings
├── store/               # Main app (models, views, serializers, urls)
├── manage.py
└── requirements.txt
🚀 Features
✅ Core Functionality
User Registration (as buyer or seller)

Login with JWT (via SimpleJWT)

Add Product (Only seller)

List Products (All users)

Create Order (Only buyer)

View Orders

Buyer: own orders

Seller: orders for their products

Order Details with Items

✨ Extra Features (Bonus)
✅ Pagination on product list

✅ Filtering products by price and searching by name

✅ Input validation (price, stock)

✅ Permissions (Only sellers can add products)

🧪 API Endpoints (Key Routes)
Method	Endpoint	Description
POST	/api/register/	Register as buyer or seller
POST	/api/token/	Get access + refresh JWT tokens
POST	/api/products/add/	Add new product (Seller only)
GET	/api/products/	List all products (filterable)
POST	/api/orders/create/	Create order (Buyer only)
GET	/api/orders/	View orders (role-based)
GET	/api/orders/<id>/	Order details with items
