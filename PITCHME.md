## Django Migrations Under the Hood

### By laixintao



---?color=#ffcfdf

## Table of Contents

- 👉 What is migrations?
- How does it work?
- Pros and Cons(Compare to other sulotions)
- FAQs about django's migrations

+++

## My First Django Project...
### (Also my first Python project 😌)

- One man's job
- Including login/register/pay/notification...
- django-admin as a CMS
- It is still online! 🎉

Note:
- wroten some clumsy code, without a teacher;

+++

## There is a secrect here...

+++

## I don't know SQL!

+++

- `python manage.py makemigrations` & `python manage.py migrate` for DDL
- `python manage.py shell` for query and DML

+++

## That's Django!

> The web framework for perfectionists with deadlines.

+++

## So what is migration, exactly?

- foo
- foo
- foo

+++




---?color=#ffcfdf

## Table of Contents

- What is migrations?
- 👉 How does it work?
- Pros and Cons(Compare to other sulotions)
- FAQs about django's migrations



---?color=#ffcfdf

## Table of Contents

- What is migrations?
- How does it work?
- 👉 Pros and Cons(Compare to other sulotions)
- FAQs about django's migrations

+++

## Some Anti-SQL voice

- Defining your schema in your ORM is nuts because it ties you to one language, reduces clarity, and sometimes limits SQL features you can use
- Existing migration tools don't pull their weight
- SQL is a more general skill than ORMs and other tools should therefore mirror SQL
- Mirroring live databases to get a schema is insane because are you tunneling to prod to run your linter? Live DB shouldn't be available to developers. Source of truth should be git.
- Schema should be versioned using the same git shas as code so the logic is easy to detect if a deploy requires a migration

footnote : "<a href='https://github.com/abe-winter/automigrate#philosophy'>automigrate project</a>"

---?color=#ffcfdf

## Table of Contents

- What is migrations?
- How does it work?
- Pros and Cons(Compare to other sulotions)
- 👉 FAQs about django's migrations

---?color=#fefdca

# Thanks!
