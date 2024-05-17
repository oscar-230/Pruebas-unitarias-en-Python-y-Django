from django.contrib import admin
from .models import Post

# Registra el modelo Post para que pueda ser administrado desde el panel de administración
admin.site.register(Post)
