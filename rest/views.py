from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from rest.serializers import TaskViewSerializer, TaskCreateSerializer
from rest.serializers import TaskEditSerializer
from rest.models import Task


def create_edit_task(request, serializer_cls, parent=None):
    data = JSONParser().parse(request)
    serializer = serializer_cls(data=data)
    if serializer.is_valid():
        task = serializer.save()
        if parent is not None:
            task.parent = parent
            task.save()
        task_dict = model_to_dict(task, exclude='parent')
        resp_status = status.HTTP_201_CREATED \
            if isinstance(serializer_cls, TaskCreateSerializer) \
            else status.HTTP_200_OK
        return JsonResponse(task_dict, status=resp_status)

    return JsonResponse(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def task_list(request):
    """
    List all tasks, or create a new task.
    """
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskViewSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        return create_edit_task(request, serializer_cls=TaskCreateSerializer)


@csrf_exempt
@require_http_methods(['GET', 'POST', 'DELETE'])
def task_detail(request, pk):
    """
    Retrieve, update or delete a task.
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskViewSerializer(task)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        return create_edit_task(request, serializer_cls=TaskEditSerializer)

    elif request.method == 'DELETE':
        task.delete()
        return HttpResponse(status=status.HTTP_200_OK)


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def subtasks(request, pk):
    try:
        parent = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        return create_edit_task(request, serializer_cls=TaskCreateSerializer,
                                parent=parent)

    # 'GET'
    sub_tasks_serializer = TaskViewSerializer(parent.sub_tasks, many=True)
    return JsonResponse(sub_tasks_serializer.data, safe=False)
