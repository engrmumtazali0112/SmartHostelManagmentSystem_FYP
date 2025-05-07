from django import forms
from .models import MessMembership, MessAttendance
from django import forms

from django import forms
from .models import ShowcaseNotice, Student

# Add this to your hostel/forms.py file
from django import forms
from .models import ShowcaseNotice

# ==========================
# ShowCashes Notices Form
# ==========================

# forms.py
from django import forms
from .models import ShowcaseNotice, Student
from django_select2.forms import ModelSelect2MultipleWidget
# forms.py

from django import forms
from .models import ShowcaseNotice

# forms.py

from django import forms
from .models import ShowcaseNotice
from django.contrib.auth.models import User

class ShowcaseNoticeForm(forms.ModelForm):
    class Meta:
        model = ShowcaseNotice
        fields = ['title', 'description', 'notice_type', 'fine_amount', 'due_date', 'students']
        widgets = {
            'students': forms.SelectMultiple(attrs={'class': 'select2', 'style': 'width: 100%;'}),
        }
  
# ==========================
# Mess Membership Form
# ==========================

class MessMembershipForm(forms.ModelForm):
    class Meta:
        model = MessMembership
        fields = ['start_date', 'end_date']  # Fields that will be included in the form

    # Customize the widget to use date input for better UI
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

# ==========================
# Mess Attendance Form
# ==========================

class MessAttendanceForm(forms.ModelForm):
    class Meta:
        model = MessAttendance
        fields = ['is_present']  # Only the attendance status is needed for the form

