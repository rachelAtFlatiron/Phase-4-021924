---

title: '05_auth_one'

---

# Authentication

---

Authentication: verifying identity <br />
Authorization: Users' access rights

---

## Cookies

- memory IN YOUR BROWSER (client side) to track information about users
- ex. tracking ad information, keeping user logged in, seeing how many articles you've read on some site
- you can see cookies created in developer tools
- plaintext which is not secure

<aside class="notes">

- best for things not important to user security
</aside>

---

## Sessions

- `session` is a special cookie containing any information we want
- info gets encrypted and sent to client to be stored in browser
- we encrypt the information using a secret key:
```python
app.secret_key = 'BAD_SECRET_KEY'
$ python -c 'import os; print(os.urandom(16))'
```

<aside class="notes">

- The read-only sessionStorage property accesses a session Storage object for the current origin. sessionStorage is similar to localStorage; the difference is that while data in localStorage doesn't expire, data in sessionStorage is cleared when the page session ends.<br />
sessionStorage only stored for current session (deleted after closing browser), cookies can persist
- Note: `db.session()` (opening up ability to add info to database) is different than browser sessions (place to store info about user, etc.)
</aside>

---

## What We'll Be Doing

1. Signing a user up
    - creating session cookie
    - adding user to React state
2. Logging a user out
    - deleting session cookie
    - removing user from React state
3. Signing a user in
    - creating session cookie
    - adding user to React state
4. Keeping a user logged in (authenticate)
    - checking session cookie
    - adding user to React state

---

## What We'll Be Doing

- Keep a state in `App.js` that will save current user
- if `user` has an object containing a `username` no one is logged in
- Store user in sessions

1. `/login`: logs in a user by finding user in database and setting sessions
2. `/logout`: logs out a user by clearing session
3. `/authorized-session`: checks if someone is already logged in via sessions
4. `/user`: signs up new user by creating a new entry in database

---

## Signing Up

1. create a `POST` resource for `User` (`/user`)
2. on `POST`, create a new user and save to database
3. save new user in sessions and React state so user is automatically logged in

---

## Logging In

1. create a custom `POST` route so we can send a payload with user login information (`/user`) (we won't actually be adding anything to the database)
2. check if user exists in database
3. if it does, set session and React state to the user

---

## Logging Out

1. create a custom route
2. clear user information from session and React state

---

## Keeping the user logged in 

1. create custom route `/authorized-session`
2. check if there is a user stored in session
3. if there is, send to front end and update React state
