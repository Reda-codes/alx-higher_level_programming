#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints python list
 * @p: a pointer to a pyobj
 * Return: is a void func
 */
void print_python_list_info(PyObject *p)
{
	long int i, j, k;
	PyObject *item;

	k = PyList_Size(p);
	j = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", k);
	printf("[*] Allocated = %ld\n", j);

	for (i = 0; i < s; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);

	}
}
