from django import forms
from .models import FoodDiaryEntry


class FoodDiaryEntryForm(forms.ModelForm):
    class Meta:
        model = FoodDiaryEntry
        fields = ['food_name', 'food_image', 'calories', 'carbs', 'fats', 'fiber', 'sugar', 'protein', 'sodium', 'potassium', 'cholesterol']
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'age', 'gender', 'height', 'weight', 'enable_notifications',
            'notify_on_exceed', 'calorie_goal', 'protein_goal', 'carbs_goal', 
            'fats_goal', 'diet_type', 'food_restrictions'
        ]

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

