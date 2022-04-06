import os.path as op

from schemacode import render, schema, utils

if __name__ == "__main__":
    # Load the schema path
    schemapath = utils.get_schema_path()
    schema_obj = schema.load_schema(schemapath)
    glossary_text = render.make_glossary_myst(schema_obj)
    glossary_file = op.join(op.abspath(op.dirname(op.dirname(op.dirname(op.dirname(__file__))))), "src/99-appendices/14-glossary.md")

    with open(glossary_file, "w") as fo:
        fo.write(glossary_text)
