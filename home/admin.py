from django.contrib import admin



from home.models import Student,Lecturer,Library,Book,Section,Teacher

# Register your models here.

#admin.site.register(Student)
#admin.site.register(Lecturer)
#admin.site.register(Library)
#admin.site.register(Book)
#admin.site.register(Section)
#admin.site.register(Teacher)

@admin.register(Book)
class BookSAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ('student_name','id')
    list_filter=('student_name','department')
    fields=('student_name','department')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass        

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    pass