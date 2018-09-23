# financeapp

## Workflow Reminder

1. activate virtual environment:

```bash
source venv/bin/activate 
```

2. set FLASK_APP path variable
```bash
export FLASK_APP=finance.py
```

When creating new table in db model, 

3. create migration file
```bash
flask db migrate -m "posts table"
```

4. apply migration to database 
```bash
flask db upgrade
```