from __future__ import annotations

import threading

from django.apps import AppConfig

from .receiver import start_event_hub_consumer


class EventHubConfig(AppConfig):
    name = 'django_app'

    def ready(self):
        # Start the Event Hub consumer in a separate thread
        threading.Thread(target=start_event_hub_consumer, daemon=True).start()
