from drf_spectacular.utils import extend_schema, extend_schema_view

organization_summary = extend_schema_view(create=extend_schema(summary="Create a new organization"))
event_summary = extend_schema_view(
    list=extend_schema(summary="Get events list"),
    retrieve=extend_schema(summary="Get detail info about current event"),
    create=extend_schema(summary="Create a new event"),
)
