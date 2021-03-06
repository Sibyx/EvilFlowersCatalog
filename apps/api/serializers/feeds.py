from datetime import datetime
from uuid import UUID

from porcupine.base import Serializer

from apps.core.models import Feed


class FeedSerializer:
    class Base(Serializer):
        id: UUID
        catalog_id: UUID
        parent_id: UUID = None
        creator_id: UUID
        title: str
        kind: Feed.FeedKind
        url_name: str
        url: str
        content: str
        per_page: int = None
        created_at: datetime
        updated_at: datetime
