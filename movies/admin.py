from django.contrib import admin
from movies.models import Movie, Genre, Rating

admin.site.site_header = 'Movie Admin'
admin.site.site_title = 'Movie Admin'
admin.site.index_title = 'Movie Admin'
# admin.site.site_url = None
# admin.site.disable_action('delete_selected')
# admin.site.disable_action('delete_selected_confirmation')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_year', 'genre')
    exclude = ('date_created',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Rating, RatingAdmin)
