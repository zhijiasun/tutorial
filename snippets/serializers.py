from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet
import snippets.models

class SnippetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Snippet
		fields = ('id','title','code','linenos','language','style')


"""
class SnippetSerializer(serializers.Serializer):
	pk = serializers.Field()
	title = serializers.CharField(required = False,max_length = 100)
	code = serializers.CharField(widget = widgets.Textarea,max_length = 100000)
	linenos = serializers.BooleanField(required=False)
	language = serializers.ChoiceField(choices=snippets.models.LANGUAGE_CHOICES,default='python')
	style = serializers.ChoiceField(choices=snippets.models.STYLE_CHOICES,default='friendly')

	def restor_object(self,attrs,instance=None):
		if instance:
			 instance.title = attrs['title']
			 instance.code = attrs['code']
			 instance.linenos = attrs['linenos']
			 instance.language = attrs['language']
			 instance.style = attrs['style']

			 return instance
		return Snippet(**attrs)

"""