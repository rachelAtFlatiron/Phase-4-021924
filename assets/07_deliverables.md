# Auth Part Two: Deliverables

### 1. Include Bcrypt
#### 1a. `pipenv install flask-bcrypt`
#### 1b. In `app.py` import `Bcrypt` from `flask-bcrypt`
#### 1c. Pass `app` to `Bcrypt`
#### 1d. In `models.py` import `bcrypt` from `app`

<br />

---

<br />

### 2. Add a password column to `Users`
#### 2a. Add column `_password_hash` of type string
#### 2b. Add an `admin` column of type string and default set to `False`

<br />

---

<br />

### 3. Create a hybrid property `password_hash`

<br />

---

<br />

### 4. Create a password setter 
#### 4a. Create the password setter so that it takes self and a password
#### 4b. Use bcyrpt to generate the password hash with bcrypt.generate_password_hash
#### 4c. Set the _password_hash to the hashed password  

<br />

---

<br />

### 5. Create a method to authenticate a hash
#### 5a. Pass in self and password
#### 5b. Use `bcrypt`'s `check_password_hash` to verify the password against the hash in the DB with  

<br />

---

<br />

### 6. In `app.py` create a `signup` route
#### - NOTE: Removed `Users` resource and `/users` for creating users
#### 6a. Create a `Signup` resource and add it to the route `/signup`
#### 6b. Hash the given password and save it to `_password_hash`
#### 6c. Don't forget to save the `user_id` in `session`!

<br />

---

<br />

### 7. Update the `Login` resource to use a `try...except`
#### 7a. Check if user exists
#### 7b. Check if password is authentic using the `authenticate` method defined in `models.py`
#### 7c. Set `session`'s `user_id` and send a response
#### 7d. Otherwise send an error message

<br />

---

<br />

### 8. Create an error message for the user if their credentials are invalid
#### 8a. In `Auth.js` create a state `error`
#### 8b. If `formik`'s `onSubmit` throws on error, set error state with the message
#### 8c. Use conditional rendering to display the error on the form on an unsuccessful sign up/log in