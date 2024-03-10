import typing

from core.celery import app
from events import serializers


@app.task
def save_event_with_delay(serializer_data: typing.Dict) -> None:
    serializer = serializers.EventSerializer(data=serializer_data)
    serializer.is_valid()
    serializer.save()
