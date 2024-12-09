from fastapi import FastAPI, Request
from app.db import get_templates, insert_templates_to_db
from app.utils import determine_field_type, match_template

app = FastAPI()


async def startup_event():
    insert_templates_to_db()


@app.on_event("startup")
async def startup():
    await startup_event()


@app.post("/get_form")
async def get_form(request: Request):
    form_data = await request.form()
    data = dict(form_data)

    templates = get_templates()

    matched_template = match_template(data, templates)
    if matched_template:
        return {"template_name": matched_template["name"]}

    typed_fields = {k: determine_field_type(v) for k, v in data.items()}
    return typed_fields
