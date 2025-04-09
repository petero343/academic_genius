from django import forms
from students.models import Result, Student, Course

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ["student", "course", "marks"]  # ✅ Only marks, not grade

    def __init__(self, *args, teacher=None, **kwargs):
        super().__init__(*args, **kwargs)

        # Limit to available students
        self.fields["student"].queryset = Student.objects.all()

        if teacher:
            self.fields["course"].queryset = teacher.assigned_subjects.all()

    def clean_marks(self):
        marks = self.cleaned_data.get("marks")

        # Validate that marks is an integer between 1 and 100
        if not isinstance(marks, int):
            raise forms.ValidationError("Marks must be a whole number.")
        if marks < 1 or marks > 100:
            raise forms.ValidationError("Marks must be between 1 and 100.")

        return marks

    def clean(self):
        cleaned_data = super().clean()
        student = cleaned_data.get("student")
        course = cleaned_data.get("course")

        if student and course:
            if Result.objects.filter(student=student, course=course).exists():
                raise forms.ValidationError("This student already has a result for this subject.")

        return cleaned_data
