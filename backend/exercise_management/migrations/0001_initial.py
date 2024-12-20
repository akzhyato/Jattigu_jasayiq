
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('duration', models.IntegerField(help_text='Duration in minutes')),
                ('intensity', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=50)),
                ('equipment_needed', models.CharField(blank=True, help_text='Equipment required (e.g., Dumbbells, Resistance Band)', max_length=100)),
                ('calories_burned_per_minute', models.DecimalField(decimal_places=2, help_text='Estimated calories burned per minute', max_digits=5)),
                ('muscle_groups', models.CharField(help_text='Target muscle groups (e.g., arms, legs, core)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, help_text='Описание плана тренировки')),
                ('duration_in_weeks', models.PositiveIntegerField(help_text='Длительность плана в неделях')),
                ('goal', models.CharField(help_text='Основная цель плана (например, потеря веса, набор мышц)', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingPlanExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sets', models.IntegerField(help_text='Количество подходов')),
                ('reps', models.IntegerField(help_text='Количество повторений в подходе')),
                ('rest_period', models.IntegerField(default=60, help_text='Время отдыха между подходами в секундах')),
                ('day', models.PositiveIntegerField(blank=True, help_text='День недели или дня плана для выполнения упражнения', null=True)),
                ('notes', models.TextField(blank=True, help_text='Дополнительные заметки для выполнения упражнения')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercise_plans', to='exercise_management.exercise')),
                ('training_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_exercises', to='exercise_management.trainingplan')),
            ],
        ),
        migrations.AddField(
            model_name='trainingplan',
            name='exercises',
            field=models.ManyToManyField(related_name='training_plans', through='exercise_management.TrainingPlanExercise', to='exercise_management.exercise'),
        ),
        migrations.AddField(
            model_name='trainingplan',
            name='level',
            field=models.ForeignKey(blank=True, help_text='Рекомендуемый уровень для этого плана', null=True, on_delete=django.db.models.deletion.SET_NULL, to='exercise_management.exerciselevel'),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='Дата, на которую запланирована тренировка')),
                ('completed', models.BooleanField(default=False, help_text='Флаг выполнения тренировки')),
                ('notes', models.TextField(blank=True, help_text='Заметки о тренировке или прогрессе')),
                ('reminder_time', models.TimeField(blank=True, help_text='Время напоминания для тренировки', null=True)),
                ('training_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='exercise_management.trainingplan')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, help_text='Описание категории упражнений')),
                ('popularity_score', models.IntegerField(default=0, help_text='Популярность категории, используется для сортировки')),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='exercise_management.exercisecategory')),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='category',
            field=models.ManyToManyField(related_name='exercises', to='exercise_management.exercisecategory'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='exercise_management.exerciselevel'),
        ),
    ]
