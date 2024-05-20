from __future__ import annotations

import asyncio
import time

from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient
from django.http import JsonResponse
from rest_framework.views import APIView

EVENT_HUB_CONNECTION_STR = '<Event Hub Connection String>'
EVENT_HUB_NAME = 'django-namespace-eh-1'


class DjangoTest(APIView):
    def __init__(self):
        pass

    async def async_push(self, request):
        # Without specifying partition_id or partition_key
        # the events will be distributed to available partitions via round-robin.
        producer = EventHubProducerClient.from_connection_string(
            conn_str=EVENT_HUB_CONNECTION_STR, eventhub_name=EVENT_HUB_NAME,
        )
        async with producer:
            event_data_batch = await producer.create_batch()
            event_data_batch.add(EventData('Testing with Run'))
            await producer.send_batch(event_data_batch)
        return JsonResponse({'output': f'The Django Application ran on {time.asctime()}'})

    def get(self, request):
        # Call the async method and wait for the result
        response = asyncio.run(self.async_push(request))
        return response
