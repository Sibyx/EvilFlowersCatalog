from typing import Optional

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from apps.core.models.entry import Entry
from apps.core.models.base import BaseModel, private_storage


class Acquisition(BaseModel):
    class Meta:
        app_label = 'core'
        db_table = 'acquisitions'
        default_permissions = ()
        verbose_name = _('Acquisition')
        verbose_name_plural = _('Acquisitions')

    class AcquisitionType(models.TextChoices):
        ACQUISITION = 'acquisition', _('acquisition')
        OPEN_ACCESS = 'open-access', _('open-access')

        def __str__(self):
            if self == self.OPEN_ACCESS:
                return 'http://opds-spec.org/acquisition/open-access'
            return 'http://opds-spec.org/acquisition'

    class AcquisitionMIME(models.TextChoices):
        PDF = 'application/pdf', _('PDF')
        EPUB = 'application/epub+zip', _('EPUB')
        MOBI = 'application/x-mobipocket-ebook', _('MOBI')

    def _upload_to_path(self, filename):
        return f"catalogs/{self.entry.catalog.url_name}/{self.entry.pk}/{filename}"

    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='acquisitions')
    relation = models.CharField(max_length=20, choices=AcquisitionType.choices, default=AcquisitionType.ACQUISITION)
    mime = models.CharField(choices=AcquisitionMIME.choices, max_length=100)
    content = models.FileField(
        upload_to=_upload_to_path, null=True, max_length=255, storage=private_storage
    )

    @property
    def url(self) -> Optional[str]:
        if not self.content:
            return None
        return f"{settings.BASE_URL}{reverse('acquisition_download', kwargs={'acquisition_id': self.pk})}"


__all__ = [
    'Acquisition'
]
