import jsonschema

from django.db import models
from django.core.exceptions import ValidationError

from alfred_core.util.regex import slug_regex


class SchemaMixin( models.Model ):
    """
    Abstract class to manage schema
    """

    SCHEMA_FIELD = '_schema'

    _name = models.CharField(
        db_column    = 'name',
        verbose_name = 'Name',
        null         = False,
        blank        = False,
        max_length   = 200 )

    _schema = models.JSONField(
        db_column    = 'schema',
        encoder      = None, 
        verbose_name = 'Schema',
        null         = False,
        blank        = False,
        default      = dict )

    _slug = models.SlugField( 
        db_column    = 'slug',
        verbose_name = "Slug",
        max_length   = 50,
        validators   = [ slug_regex ] )
    
    def get_name( self ):
        return self._name
    
    def set_name( self, value ):
        self._name = value

    def get_schema( self ):
        return self._schema

    def set_schema( self, value ):
        self._schema = value

    def get_slug( self ):
        return self._slug

    def set_slug( self, value ):
        self._slug = value

    name   = property( get_name, set_name )
    schema = property( get_schema, set_schema )
    slug   = property( get_slug, set_slug )

    class Meta:
        abstract = True

    def clean( self ):
        self._validate_schema()

    def _validate_schema( self ):
        if self._schema is not None:
            try:
                jsonschema.validate( self._schema, { "type" : "object" } )
            except Exception as e:
                raise ValidationError( str( e ) ) 

    def __str__( self ):
        return self._name