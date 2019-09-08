## Django Migrations Under the Hood

### By laixintao

---

## 关于我

- 《捕蛇者说》FM(@laike9m @Manjusaka @Adam)
- 《Python并行编程》翻译（还没完成）
- pingtop, git-ext, dnot-kernel, etc.
- 从2016年开始写 Python (Django1.8)

+++

## 第一个 Django 项目

- 一个人完成开发、部署、前后端；
- 包括注册登录、活动发布、报名付款，通知；
- 仍在线上运行（3年）；

+++

## 但是...
### 其实我不会SQL...

+++

- `python manage.py makemigrations` & `python manage.py migrate` for DDL
- `python manage.py shell` for query and DML

+++

## 这就是 Django ！

> The web framework for perfectionists with deadlines.

---?color=#ffcfdf

## Table of Contents

- 👉 What is migrations?
- How does it work?
- Pros and Cons(Compare to other sulotions)
- FAQs about django's migrations

+++


+++

## So what is migration, exactly?

- foo
- foo
- foo



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

+++

> Exactly this, I tend to write plain SQL nowadays since you eventually have to work around some ORM specific problems in the end. 

-- https://lobste.rs/s/ihqxej/orms_are_backwards#c_0x76xn

## Table of Contents

- What is migrations?
- How does it work?
- Pros and Cons(Compare to other sulotions)
- 👉 FAQs about django's migrations

---?color=#fefdca

# Thanks!
