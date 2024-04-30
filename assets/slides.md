---

title: 05_client_server

---

# Client-Server Communications

---

## `Gunicorn` and `Honcho`

- run flask AND react at same time instead of opening up two different terminals:
- `Procfile.dev` to create scripts making use of `honcho` and `gunicorn`

- `gunicorn` Python WGI HTTP server
- `honcho`: manages Procfile applications
- `Procfile`: a file that describes how to run your application even if the application is in multiple independent components 

```python

web: <Start React here>
api: <Start API here>
worker: <For job queues>

```

---

## Formik and yup
- `Formik`: npm package that makes writing React forms easier
- `yup`: npm package for object schema validation

<aside class="notes">
NOTE: Flask-WTForm and WTForms are for Python view templates
</aside>

---

## yup
You can...
- parse input values to correct types
- perform validations
- make nested schemas (blog)
## useFormik

## Formik errors
- validations run on handleChange, setFieldValue, setValues, handleSubmit and submitForm

## Displaying errors

```python
{touched.username && errors.username && <div>{errors.username}</div>}
           <Field name="email" />
```

## Formik errors

```python
{formik.touched.field && formik.errors.field ? <h3>{formik.errors.field}</h3> : ''}
```

<strong>Note:</strong> you need to have an onblur event in order for `formik.touched` to get populated 

```python
<label>Field</label>
<input
    type="number"
    name="field"
    value={formik.values.field}
    onChange={formik.handleChange}
    onBlur={formik.handleBlur}
/>
```
