from django.db import models
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailsnippets.models import register_snippet
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel


class SubgenreClass(ClusterableModel):

    title = models.CharField(
        max_length=255,
        help_text="Be as esoteric as you'd like. This displays on the genre "
        "page as a list to end users")

    @property
    def subgenre_url(self):
        return self.slug

    panels = [
        FieldPanel('title')
    ]

    # Even though there's no admin screen for subgenres we still need to return
    # the title for it to populate the inlinepanel on the album screen
    def __str__(self):
        return self.title

        class Meta:
            verbose_name = "Subgenre"
            verbose_name_plural = "Subgenres"


# This, calls _all_ of the fields from the model above and builds a one way
# relationship. The inline panel that's placed within the genre class will
# populate the SubgenreClass fields
class SubGenreRelationship(Orderable, SubgenreClass):
        subgenre_in_editor = ParentalKey(
            'GenreClass', related_name='sub_genre_relationship')


class GenreClass(ClusterableModel):
    """
    You've gotta define a genre right
    """

    title = models.CharField(
        "The genre",
        max_length=254,
        help_text='The genre. Something high level e.g. pop, metal, punk etc'
        )

    slug = models.SlugField(
        allow_unicode=True,
        max_length=255,
        help_text="The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/",
    )
    # Title
    # On a generic model you can use whatever field names you'd like. Initially
    # this was called 'subgenre_name' but was changed to 'title' since Wagtail
    # has out of the box JS that will convert anything put in a title field in
    # to the slug field
    #
    # SlugField
    # We need to use a SlugField because we need the slug to be unique

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Album cover image'
    )

    genre_description = RichTextField(blank=True, help_text='A description of the genre')

    @property
    # https://docs.python.org/3/library/functions.html#property
    def url(self):
        return '/genres/' + self.slug

    panels = [
        # The content panels are displaying the components of content we defined
        # in the StandardPage class above. If you add something to the class and
        # want it to appear for the editor you have to define it here too
        # A full list of the panel types you can use is at
        # http://docs.wagtail.io/en/latest/reference/pages/panels.html
        # If you add a different type of panel ensure you've imported it from
        # wagtail.wagtailadmin.edit_handlers in the `From` statements at the top
        # of the model
        FieldPanel('title'),
        FieldPanel('slug'),
        ImageChooserPanel('image'),
        FieldPanel('genre_description'),
        InlinePanel(
            'sub_genre_relationship',
            label="Subgenre",
            help_text="Note: this subgenres will populate the sub-genre snippet",
            min_num=1)
    ]

    def __str__(self):
        # We're returning the string that populates the snippets screen.
        # Obvs whatever field you choose will come through as plain text
        # Use __unicode__ if you're still using Python 2.7
        return self.title

    @property
    def description(self):
        # Descriptions aren't mandatory so make if fail silently
        try:
            return self.genre_description
        except:
            return ''

    class Meta:
        ordering = ['title']
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def genre(self):
        return self.GenreClass.all()

    # Defining all of the subgenre relationships
    # This allows us to get the title, slug etc in the
    # template view.
    def subgenres(self):
        return self.sub_genre_relationship.all()

    # This is for the model admin view
    def subgenre_list(obj):
        subgenres = ', '.join([
            n.title for n in obj.sub_genre_relationship.all()
        ])
        return subgenres
        # We can get to title of the SubgenreClass clusterable model through the
        # parental key of SubGenreRelationship because we're passing through
        # SubgenreClass as a parameter to that model (I think...)

    def get_context(self, request):
        context = super(GenreClass, self).get_context(request)

        # Add extra variables and return the updated context
        # context['artists'] = artist.objects.child_of(self).live()
        return context
