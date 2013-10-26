import colander

from deform.widget import TextAreaWidget


class GreetingSchema(colander.MappingSchema):
    name = colander.SchemaNode(colander.String(),
                               validator=colander.Length(max=255))
    content = colander.SchemaNode(colander.String(),
                                  widget=TextAreaWidget())
